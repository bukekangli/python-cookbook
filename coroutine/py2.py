# -*- coding:utf-8 -*-
import gevent
from gevent import monkey

monkey.patch_all()
import requests


def get_body(i):
    print "start", i
    requests.get("http://cn.bing.com")
    print "end", i


tasks = [gevent.spawn(get_body, i) for i in range(3)]
gevent.joinall(tasks)
