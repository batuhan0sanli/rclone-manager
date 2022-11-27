import time

from . import job as job_module
from . import schedule as schedule_module
from .base import logger

__all__ = ['RCloneTask']


class RCloneTask:
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
        if not self.is_enabled:
            return
        self.__start_time = time.time()
        if self.schedule:
            self.schedule.schedule_start(task=self, *args, **kwargs)
        else:
            self.job.run(task=self, *args, **kwargs)
        return self.job

    def result_handler(self, job: job_module.RCloneJob):
        self.__end_time = time.time()
        logger.info(f"Job {job.name} finished in {self.__end_time - self.__start_time} seconds")

    @property
    def start_time(self):
        return self.__start_time

    @property
    def end_time(self):
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
