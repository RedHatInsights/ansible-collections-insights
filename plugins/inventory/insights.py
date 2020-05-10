from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    name: insights
    plugin_type: inventory
    short_description: insights inventory source
    requirements:
        - requests >= 1.1
    description:
        - Get inventory hosts from the cloud.redhat.com inventory service.
        - Uses a YAML configuration file that ends with ``insights.(yml|yaml)``.
    extends_documentation_fragment:
        - constructed
    options:
      plugin:
        description: the name of this plugin, it should always be set to 'redhat.insights.insights' for this plugin to recognize it as it's own.
        required: True
        choices: ['redhat.insights.insights']
      user:
        description: Red Hat username
        required: True
        env:
            - name: INSIGHTS_USER
      password:
        description: Red Hat password
        required: True
        env:
            - name: INSIGHTS_PASSWORD
      vars_prefix:
        description: prefix to apply to host variables
        default: 'insights_'
        type: str
      get_patches:
        description: Fetch patching information for each system.
        required: False
        type: bool
        default: False
'''

from ansible.plugins.inventory import BaseInventoryPlugin, to_safe_group_name, Constructable
from ansible.errors import AnsibleError
from distutils.version import LooseVersion

try:
    import requests
    if LooseVersion(requests.__version__) < LooseVersion('1.1.0'):
        raise ImportError
except ImportError:
    raise AnsibleError('This script requires python-requests 1.1 as a minimum version')


class InventoryModule(BaseInventoryPlugin, Constructable):
    ''' Host inventory parser for ansible using foreman as source. '''

    NAME = 'redhat.insights.insights'

    def get_patches(self, stale):
        url = "https://cloud.redhat.com/api/patch/v1/systems?filter[stale]=%s" % stale
        results = []

        while url: 
            response = self.session.get(url, auth=self.auth, headers=self.headers)

            if response.status_code != 200:
                raise AnsibleError("http error (%s): %s" %
                                   (response.status_code, response.text))
            elif response.status_code == 200:
                results += response.json()['data']
                next_page = response.json()['links']['next']
                if next_page:
                    url = next_page
                else:
                    url = None

        return results

    def verify_file(self, path):
        valid = False
        if super(InventoryModule, self).verify_file(path):
            if path.endswith(('insights.yaml', 'insights.yml')):
                valid = True
            else:
                self.display.vvv('Skipping due to inventory source not ending in "insights.yaml" nor "insights.yml"')
        return valid

    def parse(self, inventory, loader, path, cache=True):
        super(InventoryModule, self).parse(inventory, loader, path)
        self._read_config_data(path)

        strict = self.get_option('strict')
        get_patches = self.get_option('get_patches')
        vars_prefix = self.get_option('vars_prefix') 

        self.auth = requests.auth.HTTPBasicAuth(self.get_option('user'),
                                           self.get_option('password'))

        self.headers = {
            "Accept": "application/json"
        }

        url = "https://cloud.redhat.com/api/inventory/v1/hosts?&staleness=fresh&staleness=stale&staleness=stale_warning&staleness=unknown"


        self.session = requests.Session()
        results = []

        while url:
            response = self.session.get(url, auth=self.auth, headers=self.headers)

            if response.status_code != 200:
                raise AnsibleError("http error (%s): %s" %
                                   (response.status_code, response.text))
            elif response.status_code == 200:
                results += response.json()['results']
                total = response.json()['total']
                count = response.json()['count']
                per_page = response.json()['per_page']
                page = response.json()['page']
                if per_page * (page - 1) + count < total:
                    url = "%s?&staleness=fresh&staleness=stale&staleness=stale_warning&staleness=unknown&page=%s" % url, (page + 1)
                else:
                    url = None

        if get_patches:
            stale_patches = self.get_patches(stale=True)
            patches = self.get_patches(stale=False)
            patching_results = patches + stale_patches
            patching = {}

            for system in patching_results:
                display_name = system['attributes']['display_name']
                patching[display_name] = {}
                for attribute in system['attributes']:
                    if attribute != 'display_name':
                        patching[display_name][attribute] = system['attributes'][attribute]

        for host in results:
            host_name = self.inventory.add_host(host['display_name'])
            for item in host.keys():
                if item != 'ansible_host':
                    self.inventory.set_variable(host_name, vars_prefix + item, host[item])
                elif host[item] is None:
                    self.inventory.set_variable(host_name, item, host['fqdn'])
                else:
                    self.inventory.set_variable(host_name, item, host[item])

            if get_patches:
                if host_name in patching.keys():
                        self.inventory.set_variable(host_name, vars_prefix + 'patching', 
                                                     patching[host['display_name']])
                else:
                    self.inventory.set_variable(host_name, vars_prefix + 'patching', {'enabled': False})

            self._set_composite_vars(
                self.get_option('compose'),
                self.inventory.get_host(host_name).get_vars(), host_name,
                strict)

            self._add_host_to_composed_groups(self.get_option('groups'),
                                              dict(), host_name, strict)
            self._add_host_to_keyed_groups(self.get_option('keyed_groups'),
                                           dict(), host_name, strict)
