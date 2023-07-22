"""Python file for schedule module.s"""

import time
import schedule


def task1():
    """create job"""
    print("working on schedular")


# which takes the job object that we created,
# and removes it from the scheduler."""


def cancle_task():
    """to cancle job the cancel_job(obj) function."""
    print("cancle task")


schedule.every(2).seconds.do(cancle_task)
job = schedule.every(2).seconds.do(cancle_task)
schedule.cancel_job(job)

# schedule.clear()


schedule.every(5).seconds.do(task1)
schedule.every(5).minutes.do(task1)
schedule.every(5).hours.do(task1)
schedule.every().day.at("00:00").do(task1)

while True:
    schedule.run_pending()
    time.sleep(1)
