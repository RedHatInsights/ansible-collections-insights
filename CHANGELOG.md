# Insights Collection Changes

## [0.0.2]
### Added
 - get_patching option added to insights inventory plugin fetches patching data from Insights patching service.
 - vars_prefix option added to insights inventory plugin allows for customization of host var variable prefix.
 - added docs for modules and role
 - added role for Insights compliance

### Fixed
 - updated inventory endpoint url to incldue all staleness states.

### Removed
  - `ansible_host` variable no longer set by default from inventory plugin. Set `ansible_host` with compose.

## [0.0.1]
### Added
 - insights_client role for installing and registering a system to insights. Note: if migrating from previous version of role, name has changed from `insights-client` to `insights_client`.
 - insights inventory plugin for fetching dynamic inventory from Insights inventory service.
