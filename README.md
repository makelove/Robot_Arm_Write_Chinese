# Robot_Arm_Write_Chinese
使用uArm Swift Pro写中文-毛笔字

- 参考
    - https://github.com/huzheng001/stroke-editor
        - handwriting-zh_CN-gb2312.xml
    - 汉字笔顺查询https://github.com/HeHongling/StrokeOrder
        - strokes-sqlite.db
    - 汉字笔顺练习打印
        - https://github.com/charlee/charprac

        
        
- 开发环境
    - python 3.6
    - pyuf
        - git clone https://github.com/uArm-Developer/pyuf.git
        - cd pyuf
        - python3 setup.py install
    - 机械臂：uArm Swift Pro
- 运行
    - long_0001.GCODE使用Printrun打开
    - uArm_draw1.py
    
- 总结
    - 汉字总数：6763
    - 没有边旁部首名称，TODO