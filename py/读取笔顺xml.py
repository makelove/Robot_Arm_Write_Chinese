# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 18:46
# @Author  : play4fun
# @File    : 读取笔顺xml.py
# @Software: PyCharm

"""
读取笔顺xml.py:
"""
import sys
import xmltodict  # 转换成dict，xml太难读了。

fxml = '../handwriting-zh_CN-gb2312.xml'
'''
<dictionary name="xxx">
    <character>
        <utf8>丁</utf8>
        <strokes>
            <stroke>
                <point x="93" y="198"/>
                <point x="913" y="205"/>
            </stroke>
            <stroke>
                <point x="495" y="203"/>
                <point x="470" y="847"/>
                <point x="405" y="784"/>
            </stroke>
        </strokes>
    </character>
</dictionary>
'''

with open(fxml, 'rb') as f:
    d = xmltodict.parse(f, xml_attribs=True)

print(d.keys())
print(d['dictionary'].keys())
# odict_keys(['@name', 'character'])
print(d['dictionary']['@name'])

#
ch = d['dictionary']['character']
print(len(ch))
# 6763
print(ch[10].keys())
# odict_keys(['utf8', 'strokes'])
print(ch[10]['utf8'])
# 与
print(len(ch[10]['strokes']))
# 1
print(len(ch[10]['strokes']['stroke']))
# 3

st = ch[10]['strokes']['stroke']#边旁部首
print(len(st))
points = st[0]['point']

for point in points:#笔划
    print(point['@x'], point['@y'])

#
# sys.exit(0)


#抽取，写入字典
Chinese_strokes=dict()
for cha in d['dictionary']['character']:#[20:30]:
    print(cha['utf8'])
    key=cha['utf8'].strip()
    value=[]
    #
    sts=cha['strokes']['stroke']
    if not isinstance(sts,list):
        sts=[sts]
    for stroke in sts:
        print('---')
        stro=[]
        for point in stroke['point']:
            print(point['@x'], point['@y'])
            po={'x':float(point['@x']),'y':float(point['@y'])}
            stro.append(po)
        value.append(stro)

    #
    Chinese_strokes[key]=value


#
import pickle
#写
with open('Chinese_strokes','wb') as f:
    pickle.dump(Chinese_strokes, f)


#读
# with open('Chinese_strokes','rb') as f:
#     data = pickle.load(f)

