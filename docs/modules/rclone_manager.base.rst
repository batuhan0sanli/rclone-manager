Exceptions
----------
The following exception classes are defined in the module:

.. toctree::
   :maxdepth: 4

   rclone_manager.base.exceptions

Logger
-------
Logger is a singleton class that is used to log messages to a file.
Environment variables can be used to configure the logger:

- ``RCLONE_MANAGER_LOG_LEVEL``: the log level to use (default: ``INFO``)
- ``RCLONE_MANAGER_LOG_FILE``: the log file to use (default: ``rclone_manager.log``)


.. automodule:: rclone_manager.base.logger
   :members:
   :undoc-members:
   :show-inheritance:
