from rclone_manager import RClone
from time import sleep

src = './test_folder'
dst = 'gdrive:rclone_test'

rclone = RClone(src, dst).copy()

# Run rclone in background
rclone.run(wait=False)
print('Waiting for rclone to finish...')

sleep(10)

# Terminate rclone
rclone.terminate()
print('Rclone terminated')