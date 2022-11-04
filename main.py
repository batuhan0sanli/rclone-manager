from rclone_manager import RClone

src = './test_folder'
dst = 'gphotos_test:album/rclone-test-folder'

rclone = RClone(src, dst, dry_run=False).copy()
process = rclone.run(wait=True, timeout=45)
