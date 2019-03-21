import time
import sched
from threading import Timer
from datetime import datetime


# 手动定时任务
def timer(n):
    while True:
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        time.sleep(n)


# 使用线程Timer实现定时任务
def print_time_use_timer(inc: int):
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    t = Timer(inc, print_time_use_timer, args=(inc,))
    t.start()


# 使用python自带任务调度模块实现定时任务
schedule = sched.scheduler(timefunc=time.time, delayfunc=time.sleep)


def print_time_use_sched(inc):
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    schedule.enter(inc, 0, print_time_use_sched, argument=(inc,))


def main():
    # print_time_use_timer(3)
    schedule.enter(0, 0, print_time_use_sched, argument=(3,))
    schedule.run()



if __name__ == '__main__':
    main()
