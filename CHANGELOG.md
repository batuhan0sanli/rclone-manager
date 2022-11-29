# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.6.0] - 2022-11-29

### Added

- Add Docstrings to all functions and classes
- Write documentation for all functions and classes and add to ReadTheDocs
- Add environment variable to set the logging file path

### Changed

- Some refactoring of the code

## [0.5.0] - 2022-11-27

### Added

- Add RClone tests
- Add GitHub Action to run tests

## [0.4.4] - 2022-11-27

### Fixed

- Fixed RClone.cmd containing a space in the path. [#16](https://github.com/batuhan0sanli/rclone-manager/issues/16)

## [0.4.3] - 2022-11-27

### Changed

- "Jobs" module name changed to "RCloneJobs".

## [0.4.2] - 2022-11-27

### Fixes

- add apscheduler module to requirements.txt

## [0.4.1] - 2022-11-27

### Added

- Added Logging Module

### Changed

- Exception Class moved to Base Module

## [0.4.0] - 2022-11-24

### Added

- Added Schedule Module
- Added cron examples
- Added some logs

## [0.3.2] - 2022-11-11

### Added

- Added RClone Exceptions

## [0.3.1] - 2022-11-09

### Added

- Added start_time and end_time to RClone Task

### Changed

- Updated RClone Task for RClone Job

## [0.3.0] - 2022-11-09

### Added

- Add RClone Jobs
- Example of a changelog for a project that uses [Semantic Versioning](https://semver.org/).

### Changed

- RClone.run `timeout` parameter are now in the format of `wait_timeout=True` instead of `timeout=True`.

## [0.2.0] - 2022-11-07

### Added

- Branching strategy section

## [0.1.9] - 2022-11-06

### Fixed

- Fix GitHub Actions CI

## [0.1.1] - 2022-11-06

### Added

- GitHub Actions CI workflow

## [0.0.2] - 2022-11-05

### Added

- First release

[0.6.0]: https://github.com/batuhan0sanli/rclone-manager/compare/0.5.0...0.6.0

[0.5.0]: https://github.com/batuhan0sanli/rclone-manager/compare/0.4.4...0.5.0

[0.4.4]: https://github.com/batuhan0sanli/rclone-manager/compare/0.4.3...0.4.4

[0.4.3]: https://github.com/batuhan0sanli/rclone-manager/compare/0.4.2...0.4.3

[0.4.2]: https://github.com/batuhan0sanli/rclone-manager/compare/0.4.1...0.4.2

[0.4.1]: https://github.com/batuhan0sanli/rclone-manager/compare/0.4.0...0.4.1

[0.4.0]: https://github.com/batuhan0sanli/rclone-manager/compare/0.3.2...0.4.0

[0.3.2]: https://github.com/batuhan0sanli/rclone-manager/compare/0.3.1...0.3.2

[0.3.1]: https://github.com/batuhan0sanli/rclone-manager/compare/0.3.0...0.3.1

[0.3.0]: https://github.com/batuhan0sanli/rclone-manager/compare/0.2.0...0.3.0

[0.2.0]: https://github.com/batuhan0sanli/rclone-manager/compare/0.1.9...0.2.0

[0.1.9]: https://github.com/batuhan0sanli/rclone-manager/compare/0.1.1...0.1.9

[0.1.1]: https://github.com/batuhan0sanli/rclone-manager/compare/0.0.2...0.1.1

[0.0.2]: https://github.com/batuhan0sanli/rclone-manager/releases/tag/0.0.2
