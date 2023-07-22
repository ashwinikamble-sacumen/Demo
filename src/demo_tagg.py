"""Task method using tags."""
import schedule


def task(i):
    """Tags allow you to filter through all jobs and return the job objects
    for those jobs with a specific tag. To apply a tag,
    all we need to do is use the tag() function."""
    print("Execute Task:", i)


schedule.every().hour.do(task, 100).tag("hourly_task")
schedule.every().hour.do(task, 101).tag("hourly_task")
schedule.every().day.do(task, 102).tag("daily_tasks")
schedule.every().week.do(task, 103).tag("weekly_task")

hourly_tasks = schedule.get_jobs("hourly_task")
print(hourly_tasks)
