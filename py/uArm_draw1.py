# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 20:00
# @Author  : play4fun
# @File    : uArm_draw1.py
# @Software: PyCharm

"""
uArm_draw1.py:
"""

import pickle
from time import sleep

# 读
with open('Chinese_strokes', 'rb') as f:
    data = pickle.load(f)

#
from uf.wrapper.swift_api import SwiftAPI
from uf.utils.log import *

logger_init(logging.VERBOSE)
# logger_init(logging.INFO)

print('setup swift ...')
swift = SwiftAPI()
print('sleep 2 sec ...')
sleep(2)
#

# 获取笔尖高度
print('解锁电机')
swift.set_servo_detach()
input('设置好毛笔')
swift.set_buzzer()

print('解锁电机')
swift.set_servo_attach()
pos = swift.get_position()
print('pos', pos)  # pos [98.39, 9.69, 37.51]
pen_height = pos[2]

# 输入文字，想draw哪个汉字？
word = input('想draw哪个汉字？')

# 修改坐标系
strokes = data[word]
'''
[[{'x': 223.0, 'y': 131.0}, {'x': 350.0, 'y': 214.0}],
 [{'x': 125.0, 'y': 309.0}, {'x': 238.0, 'y': 416.0}],
 [{'x': 170.0, 'y': 708.0}, {'x': 315.0, 'y': 453.0}],
 [{'x': 468.0, 'y': 203.0}, {'x': 753.0, 'y': 142.0}],
 [{'x': 343.0, 'y': 403.0}, {'x': 895.0, 'y': 338.0}],
 [{'x': 588.0, 'y': 216.0}, {'x': 595.0, 'y': 817.0}]]
'''

# uArm机械臂运动
