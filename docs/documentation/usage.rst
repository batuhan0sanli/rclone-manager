Usage
=====

Choosing the right tool
-----------------------
The following table shows the different tools and their use cases:

.. list-table:: Tool Differences
   :widths: 70 20 20 20
   :header-rows: 1

   * - Feature
     - :ref:`RClone<rclone>`
     - :ref:`RCloneJob<rclone_job>`
     - :ref:`RCloneTask<rclone_task>`
   * - Sync/Move/Copy Usage
     - Yes
     - Yes
     - Yes
   * - RClone Flags / Options
     - Yes
     - Yes
     - Yes
   * - Wait for Job Finished
     - Yes
     - No
     - No
   * - Wait for Job Finished with Timeout
     - Yes
     - No
     - No
   * - Terminate Job whenever you want
     - Yes
     - No
     - No
   * - Stats during Job execution
     - No
     - Yes
     - Yes
   * - Multiple Jobs
     - No
     - Yes
     - Yes
   * - Custom callback functions
     - No
     - Yes
     - Yes
   * - Enable/Disable defined Jobs
     - No
     - No
     - Yes
   * - Schedule Jobs
     - No
     - No
     - Yes

.. note::
    The RCloneJob is based on the RClone class. So you can use all the methods of the RClone class in
    the RCloneJob class.

.. note::
    The RCloneTask is wrapper class for the RCloneJob class. So you can use all the methods of the
    RCloneJob class in the RCloneTask class.

.. important::
    If you want use RClone on Python, you can use the RClone class. All the flags and options are
    available. But you have to handle the job execution and the termination by yourself.

    If you want use RClone on Python with a simple job execution, you can use the RCloneJob class.


Quick Start
-----------

.. toctree::
   :maxdepth: 1

   usage.quickstart

Advanced Usage
--------------

.. toctree::
   :maxdepth: 1

   usage.advanced_usage
