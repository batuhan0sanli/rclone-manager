# RClone Manager

Define multiple tasks using rclone to sync files from one cloud storage to another.

## Features

- Define multiple tasks
- Define timeouts for each task
- Callbacks to run scripts after tasks complete
- Run tasks in parallel
- Save logs to files

## Installation

### Requirements
- [RClone](https://rclone.org/downloads/)

### Install from PyPI
```bash
pip install rclone-manager
```

## Example Usage

### Move files from Local to Google Drive

```python
from rclone_manager import RClone

src = './test_folder'
dst = 'gdrive:rclone-test-folder'

RClone(src, dst).move().run()

print('Done')

```

### Copy files but terminate whenever you want

```python
from rclone_manager.rclone import RClone

src = './test_folder'
dst = 'gdrive:rclone-test-folder'

rclone = RClone(src, dst).copy()
rclone.run(wait=False)

# Do something else

rclone.terminate()
```
