Examples
===========

Basic Usage
-----------

The following example shows how to use the RClone class to copy a file from
Google Drive to a local directory:

.. code-block:: python

    from rclone import RClone
    rclone = RClone()
    rclone.copy('gdrive:my-file.txt', 'local:my-file.txt')

The following example shows how to use the RClone class to copy a file from
