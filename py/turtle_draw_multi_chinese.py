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
from utils import draw_rect, draw_line

# 读
with open('Chinese_strokes', 'rb') as f:
    data = pickle.load(f)

center_point = (0, 0)
# center_point = (20, 210)  # 中心点为任意点
# turtle.setworldcoordinates(llx, lly, urx, ury)#TODO

turtle.screensize(100, 100, "white")
# turtle.setpos(-100, 0)
# turtle.down()
# turtle.goto(100, 0)
# turtle.up()
draw_line(-100 + center_point[0], 0 + center_point[1], 100 + center_point[0], 0 + center_point[1])
#
# turtle.setpos(0, -100)
# turtle.down()
# turtle.goto(0, 100)
# turtle.up()
draw_line(0 + center_point[0], -100 + center_point[1], 0 + center_point[0], 100 + center_point[1])

sleep(2)
#
# sentense = '中央经济工作会议精神出炉'
# sentense = '一二手房车'
sentense = '新年快乐'
num = len(sentense)
width = 100  # 一个字的宽度 100*100
# all_width = width * num  # 总长度



# counter = 0
for i, word in enumerate(sentense):
    # turtle.clear()
    x_pos = width * (i - num / 2) + center_point[0]
    draw_rect(x=x_pos, y=0 + center_point[1], width=width)

    print('----------', word)
    strokes = data[word]
    for st in strokes:
        print('--')

        turtle.goto(x_pos + st[0]['x'] / 10, -st[0]['y'] / 10 + center_point[1])
        turtle.down()

        for po in st:
            print(x_pos + po['x'], po['y'] + center_point[1])
            turtle.goto(x_pos + po['x'] / 10, -po['y'] / 10 + center_point[1])
        turtle.up()
    # counter += 1
    sleep(0.1)
    # turtle.delay(500)#不行

sleep(15)
# turtle.delay(15000)
