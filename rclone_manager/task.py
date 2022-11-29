import time

from . import job as job_module
from . import schedule as schedule_module
from .base import logger

__all__ = ['RCloneTask']


class RCloneTask:
    """
    This is a wrapper for the RCloneJob class. It is used to schedule jobs to run at a specific time.

    :param job: RCloneJob object
    :type job: RCloneJob
    :param schedule: RCloneSchedule object
    :type schedule: RCloneSchedule
    :param is_enabled: Enable or disable task
    :type is_enabled: bool
    :param args: Arguments to pass to RCloneJob
    :param kwargs: Keyword arguments to pass to RCloneJob
    """

    def __init__(self,
                 job: job_module.RCloneJob = None,
                 schedule: 'schedule_module.RCloneSchedule' = None,
                 is_enabled=True,
                 *args,
                 **kwargs):
        self.job = job or job_module.RCloneJob(*args, **kwargs)
        self.schedule = schedule
        self.is_enabled = is_enabled

        self.__start_time = None
        self.__end_time = None

    def run(self, *args, **kwargs):
        """
        Run the task. This will run the job and schedule the job to run again at the specified time.

        :param args: Arguments to pass to RCloneJob
        :param kwargs: Keyword arguments to pass to RCloneJob
        """
        if not self.is_enabled:
            return
        self.__start_time = time.time()
        if self.schedule:
            self.schedule.schedule_start(task=self, *args, **kwargs)
        else:
            self.job.run(task=self, *args, **kwargs)
        return self.job

    def result_handler(self, job: job_module.RCloneJob):
        """
        This is a callback function that is called when the job is finished. It will log the job stats.

        :param job: RCloneJob object
        :type job: RCloneJob
        """
        self.__end_time = time.time()
        logger.info(f"Job {job.name} finished in {self.__end_time - self.__start_time} seconds")

    @property
    def start_time(self):
        """
        Get start time of the task.

        :return: Start time
        :rtype: datetime.datetime
        """
        return self.__start_time

    @property
    def end_time(self):
        """
        Get end time of the task.

        :return: End time
        :rtype: datetime.datetime
        """
        return self.__end_time

    def __repr__(self):
        return f"Task({self.job}, name={self.job.name}, is_enabled={self.is_enabled})"

    def __str__(self):
        return str(self.job.name)

    def __eq__(self, other):
        return self.job == other.job and self.job.name == other.name and self.is_enabled == other.is_enabled

    def __hash__(self):
        return hash((self.job, self.job.name, self.is_enabled))

    def __bool__(self):
        return self.is_enabled
