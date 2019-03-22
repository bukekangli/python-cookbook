import os
import sys
from datetime import datetime, timedelta

from apscheduler.schedulers.blocking import BlockingScheduler

def alarm(time):
    print('Alarm! This is alarm was scheduled at %s' % time)


if __name__ == '__main__':
    sched = BlockingScheduler()
    sched.add_jobstore('redis')
    if len(sys.argv) > 1 and sys.argv[1] == '--clear':
        sched.remove_all_jobs()
    alarm_time = datetime.now() + timedelta(seconds=1)
    sched.add_job(alarm, 'date', run_date=alarm_time, args=[datetime.now()])
    sched.add_job(alarm, 'interval', seconds=1)
    print('To clear the alarms, run this example with the --clear argument.')
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        sched.start()
    except (KeyboardInterrupt, SystemExit):
        pass
