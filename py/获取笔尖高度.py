# -*- coding: utf-8 -*-
# @Time    : 2017/12/22 11:04
# @Author  : play4fun
# @File    : 获取笔尖高度.py
# @Software: PyCharm

"""
获取笔尖高度.py:
"""

from time import sleep

from uf.wrapper.swift_api import SwiftAPI
from uf.utils.log import *

logger_init(logging.VERBOSE)
# logger_init(logging.INFO)

print('setup swift ...')

swift = SwiftAPI()
print('sleep 2 sec ...')
sleep(2)

print('解锁电机')
swift.set_servo_detach()
input('设置好毛笔')
swift.set_buzzer()

print('解锁电机')
swift.set_servo_attach()
pos=swift.get_position()
print('pos',pos)#pos [98.39, 9.69, 37.51]

print('重置机械臂')
swift.set_buzzer()
swift.reset(x=103,
            y=0,
            z=42,
            speed=800)