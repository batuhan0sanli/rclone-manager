from rclone_manager import RClone

src = './test_folder'
dst = 'gdrive:rclone_test'

config = {
    'log-level': 'INFO',       # Log level DEBUG|INFO|NOTICE|ERROR (default "NOTICE")
    'log-file': 'rclone.log',  # Log everything to this file
}

flags = {
    'use-json-log',  # Use json log format
    'syslog',        # Use Syslog for logging
}

RClone(src, dst, *flags, **config).copy().run()
