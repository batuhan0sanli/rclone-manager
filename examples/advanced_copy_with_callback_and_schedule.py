from rclone_manager import RCloneTask, RCloneJob, RCloneSchedule

src = '../rclone-test'
dst = 'gphotos_test:album/rclone_test'

start_cron = '1,3,5 * * * *'
end_cron = '2,4,6 * * * *'

callback = lambda job: print("Job Stats: ", job.stats)

job = RCloneJob(src, dst, callback=callback).copy()
schedule = RCloneSchedule(start_cron, end_cron)
task = RCloneTask(job, schedule)
task.run()
