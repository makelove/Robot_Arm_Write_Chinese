# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 15:28
# @Author  : play4fun
# @File    : utils.py
# @Software: PyCharm

"""
utils.py:
"""
import turtle
from time import sleep


def draw_line(x1, y1, x2, y2):
    print(x1, y1, '\t', x2, y2)
    turtle.up()
    turtle.setpos(x1, y1)
    turtle.down()
    turtle.goto(x2, y2)
    turtle.up()
    sleep(0.05)


def draw_rect(x=0, y=0, width=100):
    draw_line(x, y, x + width, y)
    draw_line(x + width, y, x + width, y - width)
    draw_line(x + width, y - width, x, y - width)
    draw_line(x, y - width, x, y, )


def test2():
    draw_rect(12, 7, width=70)
    draw_rect(12, 7, width=100)


def test1():
    draw_line(12, 3, 90, 30)


if __name__ == '__main__':
    turtle.screensize(100, 100, "white")
    test1()
    test2()
    sleep(5)
