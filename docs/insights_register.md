insights_register - This module registers the insights client
====================================
- [Synopsis](Synopsis)
- [Requirements](Requirements)
- [Parameters](Parameters)
- [Examples](Examples)

## Synopsis
This module will check the current registration status, unregister if needed, and then register the insights client (and update the display_name if needed)



## Requirements
(none)

## Parameters

<table>
<tr>
<th>Parameter</th>
<th>Choices/Defaults</th>
<th>Configuration</th>
<th>Comments</th>
</tr>
<tr>
<td><b>state</b></br>
</td>
<td><b>Choices:</b><br>
<ul>
<li>present</li>
<li>absent</li>
</ul>
<b>Default:</b><br>
present</td>
<td></td>
<td>Determines whether to register or unregister insights-client
</td>
</tr>
<tr>
<td><b>insights_name</b></br>
</td>
<td><b>Default:</b><br>
insights-client</td>
<td></td>
<td>For now, this is just 'insights-client', but it could change in the future so having it as a variable is just preparing for that
</td>
</tr>
<tr>
<td><b>display_name</b></br>
</td>
<td></td>
<td></td>
<td>This option is here to enable registering with a display_name outside of using a configuration file. Some may be used to doing it this way so I left this in as an optional parameter.
</td>
</tr>
<tr>
<td><b>force_reregister</b></br>
</td>
<td><b>Default:</b><br>
False</td>
<td></td>
<td>This option should be set to true if you wish to force a reregister of the insights-client. Note that this will remove the existing machine-id and create a new one. Only use this option if you are okay with creating a new machine-id.
</td>
</tr>
</table>

## Examples
```yaml

# Normal registration
- name: Register the insights client
  insights_register:
    state: present
  become: true

# Force a registration (for config changes, etc)
- name: Re-register the insights client
  insights_register:
    state: present
    force_reregister: true
  become: true

# Unregistration
- name: Unregister the insights client
  insights_register:
    state: absent
  become: true

```
