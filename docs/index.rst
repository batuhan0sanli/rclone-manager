.. RClone Manager documentation master file, created by
   sphinx-quickstart on Mon Nov 28 20:46:44 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

RClone Manager Documentation
================================

RClone is a command line program to sync files and directories to and from
different cloud storage providers. RClone Manager is a Python library
for managing RClone configurations and running RClone commands.

It is designed to be used as a library, but also includes a YAML based
configuration file and a command line interface. (soon)

The process is managed by the library and can be monitored.

It allows you to manage multiple RClone configurations and run RClone
commands on them. It also allows you to run multiple RClone commands
simultaneously.

Cron jobs can be created to run and sync your files automatically. A cron job can
be created to terminate after a certain amount of time, or to run indefinitely.

Use callbacks to run your own code when a RClone command is started, finished
or fails. You can also use callbacks to run your own code when a cron job is
started, finished or fails. (soon)

All RClone commands are run in a separate process, so RClone Manager
will not hang if a command is stuck.

A minimal example of how to use RClone Manager is shown below:

.. code-block:: python

   # Import the RClone Manager library
   from rclone_manager import RClone

   # Define the source and destination
   src = './path/to/source'
   dst = 'remote:path/to/destination'

   # Copy the files from the source to the destination
   RClone(src, dst).copy().run()

.. toctree::
   :maxdepth: 2
   :caption: Documentation

   installation
   usage
   modules
   examples

.. toctree::
   :maxdepth: 1
   :caption: Contents

   changelog
   license

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
