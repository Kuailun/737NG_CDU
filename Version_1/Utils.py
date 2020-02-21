# -*- coding: utf-8 -*-
# @File       : Utils.py
# @Author     : Yuchen Chai
# @Date       : 2020/2/10 22:42
# @Description:

import settings as ss

if ss.APPLICATION_MODE == "DEVELOPMENT":
    from Version_1 import variable
else:
    import variable

def keyRange(key, num = False, char = False, function = False, lineSelect = False):
    """
    检查是否为键盘下部的输入（0-9，A-Z等等）
    :return:
    """
    if num:
        if key == "1" or key == "2" or key == "3" or key == "4" or key == "5" or key == "6" or key == "7" or key == "8" or key == "9" or key == "0":
           return True
        pass

    if char:
        if key == "A" or key == "B" or key == "C" or key == "D" or key == "E" or key == "F" or key == "G" or key == "H" or key == "I" or key == "J" or key == "K" or key == "L" or key == "M" or key == "N" or key == "O" or key == "P" or key == "Q" or key == "R" or key == "S" or key == "T" or key == "U" or key == "V" or key == "W" or key == "X" or key == "Y" or key == "Z":
            return True
        pass

    if function:
        if key == variable.key_press_content.INIT_REF or key == variable.key_press_content.RTE or key == variable.key_press_content.CLB or key == variable.key_press_content.CRZ or key == variable.key_press_content.DES or key == variable.key_press_content.MENU or key == variable.key_press_content.LEGS or key == variable.key_press_content.DEPARR or key == variable.key_press_content.HOLD or key == variable.key_press_content.PROG or key == variable.key_press_content.N1_LIMIT or key == variable.key_press_content.FIX:
            return True
        pass

    if lineSelect:
        if key == variable.key_press_content.L1 or key == variable.key_press_content.L2 or key == variable.key_press_content.L3 or key == variable.key_press_content.L4 or key == variable.key_press_content.L5 or key == variable.key_press_content.L6 or key == variable.key_press_content.R1 or key == variable.key_press_content.R2 or key == variable.key_press_content.R3 or key == variable.key_press_content.R4 or key == variable.key_press_content.R5 or key == variable.key_press_content.R6:
            return True
    return False

def convertCoordination(value, type):
    """
    将传来的坐标数据转为标准格式的数据
    :param value: 经纬度
    :param type: 0-纬度，1-经度
    :return:
    """
    Display = ""
    Direction = ""
    Integer = 0
    Point = 0

    if type == variable.variable_coordination_type.LATITUDE:
        if value>=0:
            Direction = "N"
        else:
            Direction = "S"
            value = -value
            pass

        Integer = int(value)
        Point = str(round((value-Integer)*60,1)).ljust(2)
        Integer = str(Integer).ljust(2)

    elif type == variable.variable_coordination_type.LONGITUDE:
        if value>=0:
            Direction = "E"
        else:
            Direction = "W"
            value = -value
            pass
        Integer = int(value)
        Point = str(round((value - Integer) * 60, 1)).ljust(2)
        Integer = str(Integer).ljust(2)
    Display = "{0}{1}°{2}".format(Direction, Integer, Point)
    return Display