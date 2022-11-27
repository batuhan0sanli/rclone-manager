from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

from . import task as task_module

__all__ = ['RCloneSchedule']


class RCloneSchedule:
    def __init__(self, start_cron=None, end_cron=None, blocking=True):
        self.start_cron = start_cron
        self.end_cron = end_cron

        self.scheduler = BlockingScheduler() if blocking else BackgroundScheduler()

    @property
    def start_trigger(self):
        return CronTrigger.from_crontab(self.start_cron)

    @property
    def end_trigger(self):
        return CronTrigger.from_crontab(self.end_cron)

    def schedule_start(self, task: 'task_module.RCloneTask', *args, **kwargs):
        start_trigger = {'trigger': self.start_trigger} if self.start_cron else {'next_run_time': datetime.now()}
        self.scheduler.add_job(task.job.run, args=args, kwargs={'task': task, **kwargs}, **start_trigger,
                               id=task.job.name + '_start')

        if self.end_cron:
            self.scheduler.add_job(task.job.terminate, trigger=self.end_trigger, id=task.job.name + '_end')

        self.scheduler.start()

    def __repr__(self):
        return f"Schedule({self.start_cron}, {self.end_cron})"
