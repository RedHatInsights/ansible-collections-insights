insights - insights inventory source
====================================
- [Synopsis](Synopsis)
- [Requirements](Requirements)
- [Parameters](Parameters)
- [Examples](Examples)

## Synopsis
- Get inventory hosts from the cloud.redhat.com inventory service.
- Uses a YAML configuration file that ends with ``insights.(yml|yaml)``.

## Requirements
- requests >= 1.1

## Parameters

<table>
<tr>
<th> Parameter </th>
<th> Choices/Defaults </th>
<th> Configuration </th>
<th> Comments </th>
</tr>
<tr>
<td><b>plugin</b></br>
<p style="color:red;font-size:75%">required</p></td>
<td><b>Choices:</b><br>
- redhat.insights.insights
</td>
<td></td>
<td> the name of this plugin, it should always be set to 'redhat.insights.insights' for this plugin to recognize it as it's own.</td>
</tr>
<tr>
<td><b>user</b></br>
<p style="color:red;font-size:75%">required</p></td>
<td></td>
<td><b>env:</b><br>
-   name: INSIGHTS_USER
</td>
<td> Red Hat username</td>
</tr>
<tr>
<td><b>password</b></br>
<p style="color:red;font-size:75%">required</p></td>
<td></td>
<td><b>env:</b><br>
-   name: INSIGHTS_PASSWORD
</td>
<td> Red Hat password</td>
</tr>
<tr>
<td><b>server</b></br>
</td>
<td><b>Default:</b><br> 
https://cloud.redhat.com</td>
<td></td>
<td> Inventory server to connect to</td>
</tr>
<tr>
<td><b>selection</b></br>
</td>
<td><b>Default:</b><br> 
fqdn</td>
<td></td>
<td> Choose what variable to use for ansible_host</td>
</tr>
<tr>
<td><b>staleness</b></br>
</td>
<td><b>Default:</b><br> 
['fresh', 'stale', 'unknown']</td>
<td></td>
<td> Choose what hosts to return, based on staleness</td>
</tr>
<tr>
<td><b>registered_with</b></br>
</td>
<td><b>Default:</b><br> 
insights</td>
<td></td>
<td> Filter out any host not registered with the specified service</td>
</tr>
<tr>
<td><b>vars_prefix</b></br>
</td>
<td><b>Default:</b><br> 
insights_</td>
<td></td>
<td> prefix to apply to host variables</td>
</tr>
<tr>
<td><b>get_patches</b></br>
</td>
<td><b>Default:</b><br> 
False</td>
<td></td>
<td> Fetch patching information for each system.</td>
</tr>
<tr>
<td><b>get_system_advisories</b></br>
</td>
<td><b>Default:</b><br> 
False</td>
<td></td>
<td> Fetch advisories information for each system. If enabled will also fetch pathching information.</td>
</tr>
<tr>
<td><b>get_system_packages</b></br>
</td>
<td><b>Default:</b><br> 
False</td>
<td></td>
<td> Fetch packages information for each system. If enabled will also fetch pathching information.</td>
</tr>
<tr>
<td><b>get_tags</b></br>
</td>
<td><b>Default:</b><br> 
False</td>
<td></td>
<td> Fetch tag data for each system.</td>
</tr>
<tr>
<td><b>filter_tags</b></br>
</td>
<td><b>Default:</b><br> 
[]</td>
<td></td>
<td> Filter hosts with given tags</td>
</tr>
</table>

## Examples
```

# basic example using environment vars for auth
plugin: redhat.insights.insights

# create groups for patching
plugin: redhat.insights.insights
get_patches: yes
groups:
  patching: insights_patching.enabled
  stale: insights_patching.stale
  bug_patch: insights_patching.rhba_count > 0
  security_patch: insights_patching.rhsa_count > 0
  enhancement_patch: insights_patching.rhea_count > 0

# filter host by tags and create groups from tags
plugin: redhat.insights.insights
get_tags: True
filter_tags:
  - insights-client/env=prod
keyed_groups:
  - key: insights_tags['insights-client']
    prefix: insights

```