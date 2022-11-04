from rclone_manager import RClone

src = './test_folder'
dst = 'gdrive:rclone_test'

RClone(src, dst).copy().run()
