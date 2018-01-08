# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 19:30
# @Author  : play4fun
# @File    : 爬虫抓取笔划名称.py
# @Software: PyCharm

"""
爬虫抓取笔划名称.py:
"""

# scrapy shell https://bihua.51240.com/e4b98c__bihuachaxun/

'''
In [2]: response.xpath('//table[@width="100%"]/tr/td/text()').extract()
Out[2]:
['汉字',
 '乌 （',
 '、',
 '）',
 '\n',
 '\n',
 '\n',
 '\n',
 '读音',
 'wù',
 ' wū',
 ' ',
 '部首',
 '丿',
 '笔画数',
 '4',
 '笔画',
 '名称',
 '撇、横折钩、竖折折钩',
 '、横、']

In [3]: ex=response.xpath('//table[@width="100%"]/tr/td/text()').extract()

In [4]: ex[-2:]
Out[4]: ['撇、横折钩、竖折折钩', '、横、']

In [8]: jo='、'.join(ex[-2:])

In [9]: jo.split('、')
Out[9]: ['撇', '横折钩', '竖折折钩', '', '横', '']

In [10]: bh=[x.strip() for x in jo.split('、') if x.strip()!='']

In [11]: bh
Out[11]: ['撇', '横折钩', '竖折折钩', '横']
'''