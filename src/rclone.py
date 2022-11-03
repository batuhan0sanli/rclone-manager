import subprocess


class RClone:
    def __init__(self, src, dst, log_file='./log.json', log_level='INFO', dry_run=False):
        self.src = src
        self.dst = dst
        self.log_file = log_file
        self.log_level = log_level
        self.dry_run = dry_run
        self.process = None
        self.cmd = "rclone"

    def add_command(self, command: str):
        self.cmd = " ".join([self.cmd, command])
        return self

    def add_option(self, option, value):
        self.cmd = " ".join([self.cmd, option, value])
        return self

    def sync(self):
        self.add_command("sync")
        self._add_default_commands()
        self._add_src_dst()
        return self

    def move(self):
        self.add_command("move")
        self._add_default_commands()
        self._add_src_dst()
        return self

    def copy(self):
        self.add_command("copy")
        self._add_default_commands()
        self._add_src_dst()
        return self

    def _add_default_commands(self):
        # self.add_command("move")
        self.add_command("--use-json-log")
        self.add_option("--log-level", self.log_level)
        self.add_option("--log-file", self.log_file)
        if self.dry_run:
            self.add_command("--dry-run")
        return self

    def _add_src_dst(self):
        self.add_command(self.src)
        self.add_command(self.dst)
        return self

    def run(self, wait=True, timeout=None):
        self.process = subprocess.Popen(self.cmd.split(), stdout=subprocess.PIPE, universal_newlines=True)
        if wait:
            try:
                self.process.wait(timeout=timeout)
            except subprocess.TimeoutExpired:
                print("Process timed out")
                self.terminate()

        return self.process

    def terminate(self):
        self.process.terminate()

    def _kill(self):
        self.process.kill()

    def __str__(self):
        return self.cmd
