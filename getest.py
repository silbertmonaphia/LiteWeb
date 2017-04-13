#! /usr/bin/env python3
# encoding:utf-8

import gevent
from gevent import monkey
#monkey.patch_all()

def foo():
    print('1')
    gevent.sleep(0)
    print('2')

def bar():
    print('3')
    gevent.sleep(0)
    print('4')

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])

