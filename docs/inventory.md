insights - insights inventory source
====================================
- [Synopsis](#synopsis)
- [Requirements](#requirements)
- [Notes](#notes)
- [Parameters](#parameters)
- [Examples](#examples)

## Synopsis
- Get inventory hosts from the console.redhat.com inventory service.
- Uses a YAML configuration file that ends with ``insights.(yml|yaml)``.


## Requirements
- requests


## Notes
- A service account used to access Red Hat Insights must be in a group
with at least the `Inventory Hosts Viewer` role; in case any of the
`get_patches`, `get_system_advisories`, and `get_system_packages`
options is enabled, then also the `Patch viewer` role is required.



## Parameters

<table>
<tr>
<th>Parameter</th>
<th>Choices/Defaults</th>
<th>Configuration</th>
<th>Comments</th>
</tr>
<tr>
<td><b>plugin</b></br>
<p style="color:red;font-size:75%">required</p></td>
<td><b>Choices:</b><br>
<ul>
<li>redhat.insights.insights</li>
</ul>
</td>
<td></td>
<td>The name of this plugin, it should always be set to 'redhat.insights.insights' for this plugin to recognize it as its own.
</td>
</tr>
<tr>
<td><b>authentication</b></br>
</td>
<td><b>Choices:</b><br>
<ul>
<li>basic</li>
<li>service_account</li>
</ul>
<b>Default:</b><br>
basic</td>
<td></td>
<td>The authentication method used for the Insights Inventory server.
</td>
</tr>
<tr>
<td><b>user</b></br>
</td>
<td></td>
<td><b>env:</b><br>
-   name: INSIGHTS_USER
</td>
<td>Red Hat username; required for the 'basic' authentication method.
</td>
</tr>
<tr>
<td><b>password</b></br>
</td>
<td></td>
<td><b>env:</b><br>
-   name: INSIGHTS_PASSWORD
</td>
<td>Red Hat password; required for the 'basic' authentication method.
</td>
</tr>
<tr>
<td><b>client_id</b></br>
</td>
<td></td>
<td><b>env:</b><br>
-   name: INSIGHTS_CLIENT_ID
</td>
<td>Red Hat service account client ID; required for the 'service_account' authentication method.
</td>
</tr>
<tr>
<td><b>client_secret</b></br>
</td>
<td></td>
<td><b>env:</b><br>
-   name: INSIGHTS_CLIENT_SECRET
</td>
<td>Red Hat service account client secret; required for the 'service_account' authentication method.
</td>
</tr>
<tr>
<td><b>client_scopes</b></br>
</td>
<td><b>Default:</b><br>
['api.console']</td>
<td><b>env:</b><br>
-   name: INSIGHTS_CLIENT_SCOPES
</td>
<td>Red Hat service account client scopes; used by the 'service_account' authentication method.
</td>
</tr>
<tr>
<td><b>oidc_endpoint</b></br>
</td>
<td><b>Default:</b><br>
https://sso.redhat.com/auth/realms/redhat-external</td>
<td></td>
<td>OpenID Connect URL for 'service_account' authentication method.
</td>
</tr>
<tr>
<td><b>server</b></br>
</td>
<td><b>Default:</b><br>
https://console.redhat.com</td>
<td></td>
<td>Inventory server to connect to</td>
</tr>
<tr>
<td><b>selection</b></br>
</td>
<td><b>Default:</b><br>
fqdn</td>
<td></td>
<td>Choose what variable to use for ansible_host</td>
</tr>
<tr>
<td><b>staleness</b></br>
</td>
<td><b>Default:</b><br>
[]</td>
<td></td>
<td>Choose what hosts to return, based on staleness; an empty list means "no filtering".
</td>
</tr>
<tr>
<td><b>registered_with</b></br>
</td>
<td><b>Default:</b><br>
insights</td>
<td></td>
<td>Filter out any host not registered with the specified service</td>
</tr>
<tr>
<td><b>vars_prefix</b></br>
</td>
<td><b>Default:</b><br>
insights_</td>
<td></td>
<td>Prefix to apply to host variables</td>
</tr>
<tr>
<td><b>get_patches</b></br>
</td>
<td><b>Default:</b><br>
False</td>
<td></td>
<td>Fetch patching information for each system.</td>
</tr>
<tr>
<td><b>get_system_advisories</b></br>
</td>
<td><b>Default:</b><br>
False</td>
<td></td>
<td>Fetch advisories information for each system. If enabled will also fetch patching information.</td>
</tr>
<tr>
<td><b>get_system_packages</b></br>
</td>
<td><b>Default:</b><br>
False</td>
<td></td>
<td>Fetch packages information for each system. If enabled will also fetch patching information.</td>
</tr>
<tr>
<td><b>get_tags</b></br>
</td>
<td><b>Default:</b><br>
False</td>
<td></td>
<td>Fetch tag data for each system.</td>
</tr>
<tr>
<td><b>filter_tags</b></br>
</td>
<td><b>Default:</b><br>
[]</td>
<td></td>
<td>Filter hosts with given tags</td>
</tr>
</table>

## Examples
```yaml

# Set to use this plugin
plugin: redhat.insights.insights

# Authentication using username and password; either specify these keys,
# or set the "INSIGHTS_USER" and "INSIGHTS_PASSWORD" environment variables
user: "insights username"
password: "insights password"

# Authentication using a service account; either specify these keys, or set
# the "INSIGHTS_CLIENT_ID" and "INSIGHTS_CLIENT_SECRET" environment variables
authentication: service_account
client_id: "service account client-id"
client_secret: "service account client-secret"

# Create groups for patching
get_patches: true
groups:
  patching: insights_patching.enabled
  stale: insights_patching.stale
  bug_patch: insights_patching.rhba_count > 0
  security_patch: insights_patching.rhsa_count > 0
  enhancement_patch: insights_patching.rhea_count > 0

# Filter host by tags and create groups from tags
get_tags: true
filter_tags:
  - insights-client/env=prod
keyed_groups:
  - key: insights_tags['insights-client']
    prefix: insights

```
