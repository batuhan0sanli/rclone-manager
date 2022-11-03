import subprocess
from src.rclone import RClone

src = './test_folder'
dst = 'gphotos_test:album/rclone-test-folder'

sync = RClone(src, dst).sync()
print(sync)
