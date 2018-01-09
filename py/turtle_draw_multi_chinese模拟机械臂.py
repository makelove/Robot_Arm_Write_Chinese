# -*- coding: utf-8 -*-
# @Time    : 2018/1/9 09:58
# @Author  : play4fun
# @File    : turtle_draw_multi_chinese模拟机械臂.py
# @Software: PyCharm

"""
turtle_draw_multi_chinese模拟机械臂.py:
模拟机械臂的坐标
"""

import pickle
import turtle
from time import sleep
from utils import draw_rect, draw_line

# 读
with open('Chinese_strokes', 'rb') as f:
    data = pickle.load(f)

turtle.screensize(100, 100, "white")
draw_line(-100, 0, 100, 0)
draw_line(0, -100, 0, 100)

sleep(1)
#
# sentense = '中央经济工作会议精神出炉'
# sentense = '一二手房车'
sentense = '新年快乐'
num = len(sentense)
width = 100  # 一个字的宽度 100*100
# all_width = width * num  # 总长度

center = (20, 0)

# counter = 0
for i, word in enumerate(sentense):
    # turtle.clear()
    # x_pos = width * (i - num / 2)
    x_pos = 0 + center[0]
    y_pos = width * (i - num / 2 + 1) + center[1]
    # draw_rect(x=x_pos, y=0, width=width)
    draw_rect(x=x_pos, y=y_pos, width=width)

    print('----------', word)
    strokes = data[word]
    for st in strokes:  # 需要把字扭转方向，映射
        print('--')

        for p1, p2 in zip(st[0:-1], st[1:]):
            x1 = x_pos + p1['x'] / 10
            y1 = y_pos - p1['y'] / 10
            x2 = x_pos + p2['x'] / 10
            y2 = y_pos - p2['y'] / 10
            draw_line(x1, y1, x2, y2)

        # turtle.goto(y_pos - st[0]['y'] / 10, x_pos + st[0]['x'] / 10)
        # turtle.down()
        #
        # for po in st:
        #     # print(x_pos + po['x'], po['y'])
        #     xc = y_pos - po['y'] / 10
        #     yc = x_pos + po['x'] / 10
        #
        #
        #     turtle.goto(xc, yc)
        # turtle.up()
    # counter += 1
    sleep(0.1)
    # turtle.delay(500)#不行

sleep(15)
# turtle.delay(15000)
