# -*- coding: utf-8 -*-
# @Time    : 2018/1/9 10:43
# @Author  : play4fun
# @File    : uArm_draw_多个汉字.py
# @Software: PyCharm

"""
uArm_draw_多个汉字.py:
"""

import pickle
from time import sleep

# 输入文字，想draw哪个汉字？
# word = input('想draw哪个汉字:')
# sentense = '新年快乐'
sentense = '万二三丁'
num = len(sentense)
width = 70  # uarm
# width = 100  # uarm

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

# TODO 因为swift.get_position() 返回的位置，相差很远，只好手动设置中心点
''' 
# 笔尖接触桌面
print('解锁电机')
swift.set_servo_detach()
input('笔尖接触桌面')
swift.set_buzzer()

print('锁上电机')
swift.set_servo_attach()
pos = swift.get_position()
print('pos', pos)  # pos [225.41, 16.28, 38.16]
'''
pos = [229, 0, 10]
pen_tip_height = pos[2]
center = {'x': pos[0], 'y': pos[1], 'z': pen_tip_height + 20}
#
swift.set_position(x=center['x'], y=center['y'], z=pen_tip_height + 40, wait=True)

# counter = 0
for i, word in enumerate(sentense):
    # turtle.clear()
    # x_pos = width * (i - num / 2)
    x_pos = 0 + center['x']
    y_pos = width * (i - num / 2 + 1) + center['y']
    # draw_rect(x=x_pos, y=0, width=width)
    # draw_rect(x=x_pos, y=y_pos, width=width)
    # continue

    print('----------', word)
    strokes = data[word]
    for st in strokes:  # 需要把字扭转方向，映射
        print('--')  # turtle.goto(st[0]['x'] / 10, -st[0]['y'] / 10)
        # turtle.down()

        for po in st:
            print(po['x'], po['y'])
            # turtle.goto(po['x'] / 10, -po['y'] / 10)
            x = x_pos + po['y'] / 10
            y = y_pos + po['x'] / 10 - width
            # continue
            swift.set_position(x=x, y=y, wait=True)#先移动位置
            swift.set_position(z=pen_tip_height - 1, wait=True)#再移动高度
            # swift.set_position(x=x, y=y, z=19, wait=True)#因为pen_tip_height每次获取position都不一样,所以只好指定坐标,自己获取
            sleep(0.5)
        # turtle.up()
        swift.set_position(z=pen_tip_height + 40, wait=True)
        sleep(0.5)

    # counter += 1
    sleep(0.5)
    # turtle.delay(500)#不行

#
sleep(3)
print('重置机械臂')
swift.set_buzzer()
swift.reset(x=103, y=0, z=42, speed=1000)
# swift.reset()
