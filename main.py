import subprocess
from src.rclone import RClone

src = './test_folder'
dst = 'gphotos_test:album/rclone-test-folder'

rclone = RClone(src, dst, dry_run=True).move().run(wait=False)
