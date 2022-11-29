import subprocess

from .base import exceptions

__all__ = ['RClone']


class RClone:
    """
    Basic rclone command line tool wrapper. This class is used to create and use rclone commands. If you want to use
    rclone as a python library, use this.

    :param src: Source path
    :param dst: Destination path
    :param args: Flags
    :param kwargs: Options & Config
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
        """
        Check if process is running.

        :return: True if process is running, False otherwise
        :rtype: bool
        """
        return self.process.poll() is None if self.process else False

    @property
    def is_started(self):
        """
        Check if process is started.

        :return: True if process is started, False otherwise
        :rtype: bool
        """
        return self.process is not None

    @property
    def cmd(self):
        """
        Get rclone command.

        :return: RClone command
        :rtype: str
        """
        if not self._method:
            raise exceptions.RCloneValueError("No method has been set")
        return " ".join(filter(None, ("rclone", self.method, self.src, self.dst, self.flags, self.options)))

    @property
    def method(self):
        """
        Get rclone method.

        :return: RClone method
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, value: str):
        """
        Set rclone method.

        :param value: RClone method
        :type value: str
        """
        if value not in {None, "sync", "move", "copy"}:
            # todo: add all methods from rclone, and move this to a constant
            raise exceptions.RCloneValueError("Invalid method")
        self._method = value

    @property
    def flags(self):
        """
        Get rclone flags.

        :return: RClone flags
        :rtype: str
        """
        return " ".join(f"--{flag}" for flag in self._flags)

    @property
    def options(self):
        """
        Get rclone options.

        :return: RClone options
        :rtype: str
        """
        return " ".join(f"--{option} {value}" for option, value in self._options.items())

    def sync(self):
        """
        Set method to sync.

        :return: self
        :rtype: RClone
        """
        self.method = "sync"
        return self

    def move(self):
        """
        Set method to move.

        :return: self
        :rtype: RClone
        """
        self.method = "move"
        return self

    def copy(self):
        """
        Set method to copy.

        :return: self
        :rtype: RClone
        """
        self.method = "copy"
        return self

    def run(self, wait=True, wait_timeout=None):
        """
        Run rclone command.

        :param wait: Wait for process to finish
        :type wait: bool
        :param wait_timeout: Timeout for process to finish
        :type wait_timeout: int
        """
        self.process = subprocess.Popen(self.cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                        universal_newlines=True)
        if wait:
            try:
                self.process.wait(timeout=wait_timeout)
            except subprocess.TimeoutExpired:
                self.terminate()

        return self.process

    def terminate(self):
        """
        Terminate process.
        """
        self.process.terminate()

    def _kill(self):
        """
        Kill process.
        """
        self.process.kill()

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)

    def __call__(self, *args, **kwargs):
        return self.run()
