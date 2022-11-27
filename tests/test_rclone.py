import unittest

from rclone_manager import RClone
from rclone_manager.base import exceptions

src = './test_folder'
dst = 'gdrive:rclone_test'


class TestRClone(unittest.TestCase):
    def test_rclone_class(self):
        rclone = RClone(src, dst)

        self.assertEqual(rclone.src, src)
        self.assertEqual(rclone.dst, dst)
        self.assertEqual(rclone.name, str(id(rclone)))
        self.assertEqual(rclone._flags, ())
        self.assertEqual(rclone._options, {})
        self.assertEqual(rclone.process, None)
        self.assertEqual(rclone._method, None)
        self.assertEqual(rclone.is_running, False)
        self.assertEqual(rclone.is_started, False)

    def test_rclone_methods(self):
        rclone = RClone(src, dst)

        self.assertEqual(rclone.method, None)
        self.assertRaises(exceptions.RCloneValueError, lambda: rclone.cmd)

        self.assertEqual(rclone.flags, "")
        self.assertEqual(rclone.options, "")

        rclone.sync()
        self.assertEqual(rclone.method, "sync")
        self.assertEqual(rclone.cmd, "rclone {method} ./test_folder gdrive:rclone_test".format(method=rclone.method))

        rclone.move()
        self.assertEqual(rclone.method, "move")
        self.assertEqual(rclone.cmd, "rclone {method} ./test_folder gdrive:rclone_test".format(method=rclone.method))

        rclone.copy()
        self.assertEqual(rclone.method, "copy")
        self.assertEqual(rclone.cmd, "rclone {method} ./test_folder gdrive:rclone_test".format(method=rclone.method))

    def test_rclone_flags(self):
        flags = {'use-json-log', 'syslog'}
        rclone = RClone(src, dst, *flags)

        rclone.sync()
        self.assertIn("--use-json-log", rclone.flags)
        self.assertIn("--syslog", rclone.flags)
        self.assertIn("--use-json-log", rclone.cmd)

    def test_rclone_options(self):
        options = {'log-level': 'INFO', 'log-file': 'rclone.log'}
        rclone = RClone(src, dst, **options)

        rclone.sync()
        self.assertIn("--log-level INFO", rclone.options)
        self.assertIn("--log-file rclone.log", rclone.options)
        self.assertIn("--log-level INFO", rclone.cmd)
        self.assertIn("--log-file rclone.log", rclone.cmd)

    def test_rclone_flags_and_options(self):
        flags = {'use-json-log', 'syslog'}
        options = {'log-level': 'INFO', 'log-file': 'rclone.log'}
        rclone = RClone(src, dst, *flags, **options)

        rclone.sync()
        self.assertIn("--use-json-log", rclone.flags)
        self.assertIn("--syslog", rclone.flags)
        self.assertIn("--log-level INFO", rclone.options)
        self.assertIn("--log-file rclone.log", rclone.options)
        self.assertIn("--use-json-log", rclone.cmd)
        self.assertIn("--syslog", rclone.cmd)
        self.assertIn("--log-level INFO", rclone.cmd)
        self.assertIn("--log-file rclone.log", rclone.cmd)
