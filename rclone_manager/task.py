from rclone_manager.rclone import RClone


class RCloneTask:
    def __init__(self, job: RClone, name=None, is_enabled=True, callback: callable = None):
        self.job = job
        self.name = name or job.name
        self.is_enabled = is_enabled
        self.callback = callback

    def run(self, *args, **kwargs):
        if not self.is_enabled:
            return
        job = self.job.run(*args, **kwargs)
        if self.callback:
            self.callback(self)
        return job

    def __repr__(self):
        return f"Task({self.job}, name={self.name}, is_enabled={self.is_enabled})"

    def __str__(self):
        return str(self.name)

    def __eq__(self, other):
        return self.job == other.job and self.name == other.name and self.is_enabled == other.is_enabled

    def __hash__(self):
        return hash((self.job, self.name, self.is_enabled))

    def __bool__(self):
        return self.is_enabled
