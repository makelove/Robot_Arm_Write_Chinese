# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 20:00
# @Author  : play4fun
# @File    : uArm_draw1.py
# @Software: PyCharm

"""
uArm_draw1.py:
机械臂不准确时，需要重启。
麻烦！
"""

import pickle
from time import sleep

# 输入文字，想draw哪个汉字？
word = input('想draw哪个汉字:')

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
# print('解锁电机')
# swift.set_servo_detach()
# input('设置好毛笔')
# swift.set_buzzer()
#
# print('解锁电机')
# swift.set_servo_attach()
# pos = swift.get_position()
# print('pos', pos)  # pos [98.39, 9.69, 37.51]
# pen_height = pos[2]

#
# sleep(2)
# 笔尖接触桌面
print('解锁电机')
swift.set_servo_detach()
input('笔尖接触桌面')
swift.set_buzzer()

print('锁上电机')
swift.set_servo_attach()
pos = swift.get_position()
print('pos', pos)  # pos [225.41, 16.28, 38.16]
pen_tip_height = pos[2]
center={'x':pos[0],'y':pos[1],'z':pen_tip_height+20}
#



# 修改坐标系
strokes = data[word]  # 汗
'''
[[{'x': 223.0, 'y': 131.0}, {'x': 350.0, 'y': 214.0}],
 [{'x': 125.0, 'y': 309.0}, {'x': 238.0, 'y': 416.0}],
 [{'x': 170.0, 'y': 708.0}, {'x': 315.0, 'y': 453.0}],
 [{'x': 468.0, 'y': 203.0}, {'x': 753.0, 'y': 142.0}],
 [{'x': 343.0, 'y': 403.0}, {'x': 895.0, 'y': 338.0}],
 [{'x': 588.0, 'y': 216.0}, {'x': 595.0, 'y': 817.0}]]
'''
# 中心点 x100,y0
# center = {'x': 150, 'y': 0, 'z': pen_tip_height + 20}

# swift.set_position(x=center['x'],y=center['y'],z=center['z'],wait=True)
sleep(2)

# uArm机械臂运动
swift.set_position(z=pen_tip_height + 20, wait=True)
for st in strokes:
    print('------')
    # turtle.goto(st[0]['x'] / 10, -st[0]['y'] / 10)
    # turtle.down()

    for po in st:
        print(po['x'], po['y'])
        # turtle.goto(po['x'] / 10, -po['y'] / 10)
        x = center['x'] + po['x'] / 10
        y = center['y'] + po['y'] / 10
        swift.set_position(x=x, y=y, z=pen_tip_height-3, wait=True)
        # swift.set_position(x=x, y=y, z=19, wait=True)#因为pen_tip_height每次获取position都不一样,所以只好指定坐标,自己获取
        sleep(0.5)
    # turtle.up()
    swift.set_position(z=pen_tip_height + 20, wait=True)
    sleep(0.5)

#
sleep(3)
print('重置机械臂')
swift.set_buzzer()
swift.reset(x=103,y=0,z=42,speed=1000)
# swift.reset()