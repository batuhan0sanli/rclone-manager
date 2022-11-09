from rclone_manager import RClone

src = './test_folder'
dst = 'gdrive:rclone_test'

rclone = RClone(src, dst).copy()

# Rclone terminate in 10 seconds
rclone.run(wait_timeout=10)
