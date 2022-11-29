Sync a local directory to a remote directory
--------------------------------------------

Before you start, make sure you have to rclone installed on your computer. If you don't, you can download it from here:
`<https://rclone.org/downloads/>`_

Moreover, you need to have a remote directory and make sure you have the correct credentials to access it. If you don't
have a remote directory, you can create one on Google Drive, Dropbox, OneDrive, etc. and get the credentials from there.

Once you have rclone installed and the remote directory ready, you can start syncing your local directory to the remote
directory. To do so, open a terminal and install the rclone-manager package:

.. code-block:: bash

    pip install rclone-manager

Then, import the rclone_manager module. Since this is a simple example, we will use the RClone object.

.. code-block:: python

    from rclone_manager import RClone

Now, we can define the local and remote directories. In this example, we will use the local directory "local_dir" and
the remote directory "remote:/remote_dir". If you don't know how to define the remote directory, you can check the
rclone documentation here: `<https://rclone.org/commands/rclone_sync/>`_

.. code-block:: python

    local_dir = "local_dir"
    remote_dir = "remote:/remote_dir"

Now, we can create an RClone object and sync the local directory to the remote directory.

.. code-block:: python

    rclone = RClone(local_dir, remote_dir).sync()

RClone objects have a lot of methods that you can use to sync, copy, move, etc. files. You can check the
documentation.

To start the sync process, you can use the `run()` method.

.. code-block:: python

    rclone.run()

And that's it! You can now sync your local directory to the remote directory.

Of course if you want only one line of code, you can do this:

.. code-block:: python

    RClone("local_dir", "remote:/remote_dir").sync().run()

Sync with rclone's flags
------------------------

You can also use rclone's flags. To do so, you can use the `args` parameter of the RClone object.

.. code-block:: python

    flags = {"dry-run", "verbose"}
    rclone = RClone(local_dir, remote_dir, *flags).sync().run()

Sync with Timeouts
------------------

If you want to sync your local directory to the remote directory with timeouts, you can use the `run()` command with the
`wait_timeout` parameter.

.. code-block:: python

    rclone.run(wait_timeout=60)

Now, let's say you want to sync the local directory to the remote directory every 5 minutes. You can do so by using
the RCloneScheduler object.

    from rclone_manager import RCloneScheduler

    scheduler = RCloneScheduler(local_dir, remote_dir)
    scheduler.schedule_sync(minutes=5)



.. code-block:: python

    from rclone_manager import RClone

    # Define the source and destination
    source = "/home/user/source"
    destination = "remote:/destination"

    # Create a new RClone object
    rclone = RClone(source, destination)

    # Sync the source to the destination
    rclone.sync()

    # Run the rclone command
    rclone.run()


