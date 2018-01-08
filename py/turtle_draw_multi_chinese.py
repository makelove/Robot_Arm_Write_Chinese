# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 14:26
# @Author  : play4fun
# @File    : turtle_draw_multi_chinese.py
# @Software: PyCharm

"""
turtle_draw_multi_chinese.py:
在一行内写多个汉字
"""

import pickle
import turtle
from time import sleep
from utils import draw_rect

# 读
with open('Chinese_strokes', 'rb') as f:
    data = pickle.load(f)

turtle.screensize(100, 100, "white")
turtle.setpos(-100, 0)
turtle.down()
turtle.goto(100, 0)
turtle.up()
#
turtle.setpos(0, -100)
turtle.down()
turtle.goto(0, 100)
turtle.up()

sleep(2)
#
# sentense = '中央经济工作会议精神出炉'
# sentense = '一二手房车'
sentense = '新年快乐'
num = len(sentense)
width = 100  # 一个字的宽度 100*100
# all_width = width * num  # 总长度
# 中心点为原点


# counter = 0
for i, word in enumerate(sentense):
    # turtle.clear()
    x_pos = width * (i - num / 2)
    draw_rect(x=x_pos, y=0, width=width)

    print('----------', word)
    strokes = data[word]
    for st in strokes:
        print('--')

        turtle.goto(x_pos + st[0]['x'] / 10, -st[0]['y'] / 10)
        turtle.down()

        for po in st:
            print(x_pos + po['x'], po['y'])
            turtle.goto(x_pos + po['x'] / 10, -po['y'] / 10)
        turtle.up()
    # counter += 1
    sleep(0.5)

sleep(15)
