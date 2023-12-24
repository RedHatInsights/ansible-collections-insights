#!/usr/bin/python

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: insights_config
short_description: This module handles initial configuration of the insights client on install
description: >
    Supply values for various configuration options that you would like to use.
    On install this module will add those values to the insights-client.conf file prior to registering.
options:
  username:
    description: >
      Insights basic auth username. If defined this will change, set, or remove the username
      in the insights configuration. To remove a username set this value to an empty string.
    required: false
  password:
    description: >
      Insights basic auth password. If defined this will change, set, or remove the password
      in the insights configuration. To remove a password set this value to an empty string.
    required: false
  auto_config:
    description: >
      Attempt to auto-configure the network connection with Satellite or RHSM. Default is True.
    required: false
  authmethod:
    description: >
      Authentication method for the Portal (BASIC, CERT). Default is BASIC. Note: when
      auto_config is enabled, CERT will be used if RHSM or Satellite is detected.
    required: false
  display_name:
    description: >
      Custom display name to appear in the Insights web UI. Only used on machine registration.
      Blank by default.
    required: false
  insights_name:
    description: >
      For now, this is just 'insights-client', but it could change in the future so having
      it as a variable is just preparing for that.
    required: false
  proxy:
    description: >
      This set an optional proxy for the insights client to connect through if the client
      is behind a firewall or requires a proxy. Default is unspecified (none).
    required: false
 loglevel:
    description: >
      Log level the Insights client should use. Default is unspecified (none), which means
      the configuration file of the Insights client will not be touched and therefore uses
      the default configured by the Insights client itself.
    required: false
  base_url:
    description: >
      Base URL for the Insights API. Default is unspecified (none), which means the configuration
      file of the Insights client will not be touched and therefore uses the default configured
      by the Insights client itself.
    required: false
  auto_update:
    description: >
      Automatically update the dynamic configuration. Default is unspecified (none),
      which means the configuration file of the Insights client will not be touched and
      therefore uses the default configured by the Insights client itself.
    required: false
  obfuscate:
    description: >
      Obfuscate IP addresses. Default is unspecified (none), which means the
      configuration file of the Insights client will not be touched and therefore uses the
      default configured by the Insights client itself.
    required: false
  obfuscate_hostname:
    description: >
      Obfuscate hostname. Requires obfuscate=True. Default is unspecified (none),
      which means the configuration file of the Insights client will not be touched and therefore
      uses the default configured by the Insights client itself.
    required: false
  ansible_host:
    description: >
      Ansible hostname for this system as reported to the Insights API. Default is
      unspecified (none), which means the configuration file of the Insights client will not be
      touched and therefore uses the default configured by the Insights client itself.
    required: false
  cmd_timeout:
    description: >
      Timeout for commands run during collection, in seconds. Default is unspecified (none),
      which means the configuration file of the Insights client will not be
      touched and therefore uses the default configured by the Insights client itself.
    required: false
  http_timeout:
    description: >
      Timeout for HTTP calls, in seconds. Default is unspecified (none),
      which means the configuration file of the Insights client will not be
      touched and therefore uses the default configured by the Insights client itself.
    required: false
  core_collect:
    description: >
      Use insights-core as the collection source. Included for compatibility only.
      Modify only as directed. Default is unspecified (none), which means the configuration
      file of the Insights client will not be touched and therefore uses the default
      configured by the Insights client itself.
    required: false
  redaction_file:
    description: >
     Location of the redaction file for commands, files, and components. Default is
      unspecified (none), which means the configuration file of the Insights client will not
      be touched and therefore uses the default configured by the Insights client itself.
    required: false
  content_redaction_file:
    description: >
      Location of the redaction file for patterns and keywords. Default is
      unspecified (none), which means the configuration file of the Insights client will not
      be touched and therefore uses the default configured by the Insights client itself.
    required: false
  tags_file:
    description: >
      Location of the tags file for this system. Default is unspecified (none), which
      means the configuration file of the Insights client will not be touched and therefore
      uses the default configured by the Insights client itself.
    required: false

author:
    - Jason Stephens (@Jason-RH)
'''

EXAMPLES = '''
# Configure the insights client to register with RHSM and no display name;
# the insights_config module is used without parameters: this is because
# auto_config defaults to true, which in turn forces the client to try RHSM
# (or Satellite)
- name: Configure the insights client
  insights_config:
  become: true

# Configure the insights client to register with RHSM and a display name
- name: Configure the insights client
  insights_config:
    display_name: "{{ insights_display_name }}"
  become: true

# Configure the insights client to register with username and password stored
# as environment variables in the Ansible controller
- name: Configure the insights client
  insights_config:
    username: "{{ lookup('env', INSIGHTS_USER) }}"
    password: "{{ lookup('env', INSIGHTS_PASSWORD) }}"
    auto_config: "{{ auto_config }}"
    authmethod: "{{ authmethod }}"
    proxy: "{{ insights_proxy }}"
  become: true

- name: Configure the Insights client with all available options when passing variables as a role variables
  insights_config:
    username: "{{ redhat_portal_username }}"
    password: "{{ redhat_portal_password }}"
    auto_config: "{{ auto_config }}"
    authmethod: "{{ authmethod }}"
    proxy: "{{ insights_proxy }}"
    loglevel: "{{ insights_loglevel }}"
    auto_config: "{{ insights_auto_config }}"
    base_url: "{{ insights_base_url }}"
    auto_update: "{{ insights_auto_update }}"
    obfuscate: "{{ insights_obfuscate }}"
    obfuscate_hostname: "{{ insights_obfuscate_hostname }}"
    ansible_host: "{{ insights_ansible_host }}"
    cmd_timeout: "{{ insights_cmd_timeout }}"
    http_timeout: "{{ insights_http_timeout }}"
    core_collect: "{{ insights_core_collect }}"
    redaction_file: "{{ insights_redaction_file }}"
    content_redaction_file: "{{ insights_content_redaction_file }}"
    tags_file: "{{ insights_tags_file }}"
  become: true

- name: Configure the Insights client with all available options
  insights_config:
    username: John
    password: secret_P4ssW0rd.
    auto_config: true
    authmethod: CERT
    loglevel: DEBUG
    auto_config: true
    base_url: cert-api.access.redhat.com:443/r/insights
    auto_update: true
    obfuscate: true
    obfuscate_hostname: true
    ansible_host: my_host.example.com
    cmd_timeout: 120
    http_timeout: 120
    core_collect: true
'''
