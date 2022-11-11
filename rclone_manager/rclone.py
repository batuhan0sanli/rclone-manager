import subprocess
from rclone_manager.exceptions import RCloneValueError


class RClone:
    """
    This class is a wrapper for the rclone command line tool.
    """

    def __init__(self, src, dst, *args, **kwargs):
        self.src = src
        self.dst = dst
        self.name = kwargs.pop('name', str(id(self)))

        self._flags = args
        self._options = kwargs

        self.process = None
        self._method = None

        self.method = kwargs.pop('method', None)

    @property
    def is_running(self):
        return self.process.poll() is None if self.process else False

    @property
    def is_started(self):
        return self.process is not None

    @property
    def cmd(self):
        if not self._method:
            raise RCloneValueError("No method has been set")
        return " ".join(["rclone", self.method, self.src, self.dst, self.flags, self.options])

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, value: str):
        if value not in {None, "sync", "move", "copy"}:
            # todo: add all methods from rclone, and move this to a constant
            raise RCloneValueError("Invalid method")
        self._method = value

    @property
    def flags(self):
        return " ".join(f"--{flag}" for flag in self._flags)

    @property
    def options(self):
        return " ".join(f"--{option} {value}" for option, value in self._options.items())

    def sync(self):
        self.method = "sync"
        return self

    def move(self):
        self.method = "move"
        return self

    def copy(self):
        self.method = "copy"
        return self

    def run(self, wait=True, wait_timeout=None):
        self.process = subprocess.Popen(self.cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                        universal_newlines=True)
        if wait:
            try:
                self.process.wait(timeout=wait_timeout)
            except subprocess.TimeoutExpired:
                self.terminate()

        return self.process

    def terminate(self):
        self.process.terminate()

    def _kill(self):
        self.process.kill()

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)

    def __call__(self, *args, **kwargs):
        return self.run()
