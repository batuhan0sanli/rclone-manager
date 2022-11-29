from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

from . import task as task_module

__all__ = ['RCloneSchedule']


class RCloneSchedule:
    """
    It schedules a task to run at a certain time, and if an end time is specified, it will also schedule the task to
    terminate at that time. It uses APScheduler to schedule the tasks.

    :param start_cron: Cron expression for when the task should start
    :type start_cron: str
    :param end_cron: Cron expression for when the task should end
    :type end_cron: str
    :param blocking: If True, the scheduler will block the thread. If False, the scheduler will run in the background.
    :type blocking: bool
    """

    def __init__(self, start_cron=None, end_cron=None, blocking=True):
        self.start_cron = start_cron
        self.end_cron = end_cron

        self.scheduler = BlockingScheduler() if blocking else BackgroundScheduler()

    @property
    def start_trigger(self):
        """
        Get start trigger.

        :return: Start trigger object
        :rtype: CronTrigger
        """
        return CronTrigger.from_crontab(self.start_cron)

    @property
    def end_trigger(self):
        """
        Get end trigger.

        :return: End trigger object
        :rtype: CronTrigger
        """
        return CronTrigger.from_crontab(self.end_cron)

    def schedule_start(self, task: 'task_module.RCloneTask', *args, **kwargs):
        """
        Schedule the task to start at the specified time. If an end time is specified, it will also schedule the task to
        end at that time.

        :param task: RCloneTask object
        :type task: RCloneTask
        :param args: Arguments to pass to RCloneJob
        :param kwargs: Keyword arguments to pass to RCloneJob
        """
        start_trigger = {'trigger': self.start_trigger} if self.start_cron else {'next_run_time': datetime.now()}
        self.scheduler.add_job(task.job.run, args=args, kwargs={'task': task, **kwargs}, **start_trigger,
                               id=task.job.name + '_start')

        if self.end_cron:
            self.scheduler.add_job(task.job.terminate, trigger=self.end_trigger, id=task.job.name + '_end')

        self.scheduler.start()

    def __repr__(self):
        return f"Schedule({self.start_cron}, {self.end_cron})"
