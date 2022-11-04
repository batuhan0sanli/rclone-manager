from rclone_manager import RClone

src = './test_folder'
dst = 'gphotos_test:album/rclone-test-folder'

config = {
    'log-level': 'INFO',  # Log level DEBUG|INFO|NOTICE|ERROR (default "NOTICE")
}

flags = {
    'dry-run',       # Do a trial run with no permanent changes
    'use-json-log',  # Use json log format
    'syslog',        # Use Syslog for logging
}

RClone(src, dst, *flags, **config).move().run()
