import subprocess


class RClone:
    def __init__(self, src, dst, log_file='./log.json', log_level='INFO', dry_run=True):
        self.src = src
        self.dst = dst
        self.log_file = log_file
        self.log_level = log_level
        self.dry_run = dry_run
        self.cmd = None

    def sync(self):
        # todo: add copy, move, sync, etc. options
        base_cmd = "rclone move"
        use_json_log = "--use-json-log"
        log_level = "--log-level " + self.log_level
        log_file = "--log-file " + self.log_file
        dry_run = "--dry-run" if self.dry_run else ""
        self.cmd = " ".join([base_cmd, use_json_log, log_level, log_file, dry_run, self.src, self.dst])
        self._run_cmd()

    def _run_cmd(self):
        process = subprocess.Popen(self.cmd.split(), stdout=subprocess.PIPE, universal_newlines=True)
        process.stdout.close()
        return_code = process.wait()
        if return_code:
            raise subprocess.CalledProcessError
