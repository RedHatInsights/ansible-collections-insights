# Insights Collection Changes

This file contains the changes done in each version of the Insights Collection
that have any kind of impact on users, such as new & removed features, behaviour
changes, and bug fixes. Internal changes such as for CI, style/lint, and so on
are purposely not mentioned here.

## [unreleased]
### Changed
- `inventory` plugin: use the v3 API of the "patch" endpoint; the only changes
  in the results are some different properties in the `<vars_prefix>patching`
  variable set for each host

## [1.1.0]
### Changed
- There is no more a maximum supported version of Ansible for the collection,
  which now supports Ansible 2.14 and greater; the collection should generally
  work fine also with new Ansible versions, and compatibility issues will be
  fixed when noticed/reported

### Fixed
- `insights_register` module: actually make use of the `display_name` option,
  which was ignored until now
- `insights_register` module: make the `force_reregister` option work again:
  manually unregister & register again, rather than trying to use the
  `--force-reregister` option of `insights-client` which was dropped with
  insights-core 3.1.1 (December 2022)
- layout/style improvements of the Markdown documentations
- various documentation improvements & fixes

## [1.0.8]
### Fixed
- `insights_client` role: make sure `become: true` is used for all the tasks
- `insights_register` module: fix the check used to determine whether the
  system is already registered with `insights-client`
- `inventory` plugin: fix the retrieval of systems when there is a large number
  of systems in the Insights Inventory

## [1.0.7]
### Fixed
- `inventory` plugin: properly retrieve tags

## [1.0.6]
### Added
- `inventory` plugin: new `get_system_advisories` and `get_system_packages`
  options

### Fixed
- `inventory` plugin: properly retrieve patching information also for more than
  few hosts

## [1.0.5]
### Added
- `inventory` plugin: new `selection` option

## [1.0.4]
Only internal changes.

## [1.0.3]
### Added
- `inventory` plugin: new `server`, `staleness`, `registered_with` options

### Fixed
- `insights_register` module: fixed the default of the `force_reregister` option
  as `false`

## [1.0.2]
### Fixed
- Documentation fixes

## [1.0.1]
### Added
- `insights_client` role: `insights_tags` variable to deploy tags to managed
  systems
- `inventory` plugin: `get_tags` option to pull tags as variables
- `inventory` plugin: `filter_tags` option to filter hosts server side by tag
- added examples for filtering by tag and creating groups from tags

## [1.0.0]
Production Release

## [0.0.2]
### Added
- `inventory` plugin: `get_patches` option fetches patching data from Insights
  patching service
- `inventory` plugin: `vars_prefix` option allows for customization of host var
  variable prefix
- added docs for modules and role
- added role for Insights compliance

### Fixed
- update inventory endpoint URL to include all staleness states

### Removed
- `inventory` plugin: `ansible_host` variable no longer set by default
  Set `ansible_host` with compose.

## [0.0.1]
### Added
- `insights_client` role for installing and registering a system to insights
  Note: if migrating from previous version of role, name has changed from
  `insights-client` to `insights_client`
- `insights` inventory plugin for fetching dynamic inventory from Insights
  inventory service
