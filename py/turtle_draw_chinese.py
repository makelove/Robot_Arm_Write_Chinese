# -*- coding: utf-8 -*-
# Time    : 2017/12/21 19:36
# Author  : play4fun
# File    : turtle_draw_chinese.py
# Software: PyCharm

"""
turtle_draw_chinese.py:
使用turtle库画中文
"""

import pickle
import turtle
from time import sleep

# 读
with open('Chinese_strokes', 'rb') as f:
    data = pickle.load(f)


turtle.screensize(100, 100, "white")
turtle.up()
sleep(4)
#
# sentense = '中央经济工作会议精神出炉'
sentense = '一二手房'
for word in sentense:
    turtle.clear()

    print('----------', word)
    strokes = data[word]
    for st in strokes:
        print('--')
        turtle.goto(st[0]['x'] / 10, -st[0]['y'] / 10)
        turtle.down()

        for po in st:
            print(po['x'], po['y'])
            turtle.goto(po['x'] / 10, -po['y'] / 10)
        turtle.up()
    sleep(0.5)
sleep(15)
