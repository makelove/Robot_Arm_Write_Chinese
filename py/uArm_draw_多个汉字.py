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
sentense = '新年快乐'

# 读
with open('Chinese_strokes', 'rb') as f:
    data = pickle.load(f)