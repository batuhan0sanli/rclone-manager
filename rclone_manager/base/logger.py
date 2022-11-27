import os
import logging


logger = logging.getLogger('rclone_manager')
logger.setLevel(os.environ.get('RCLONE_MANAGER_LOG_LEVEL', 'INFO'))

# create file handler which logs even debug messages
fh = logging.FileHandler('rclone_manager.log')

# create console handler with a higher log level
ch = logging.StreamHandler()

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

__all__ = ['logger']
