import time
from pytz import utc
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler




def job():
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def job2():
    print(int(time.time()))


if __name__ == '__main__':

    sched = BlockingScheduler()
    sched.add_job(job, 'interval', seconds=3)
    sched.add_job(job2, 'interval', seconds=1)
    sched.start()