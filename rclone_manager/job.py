from rclone_manager.rclone import RClone


class Job(RClone):
    def __init__(self, src, dst, *args, **kwargs):
        super().__init__(src, dst, *args, **kwargs)
