# -*- coding: utf-8 -*-
# @File       : inputLogic.py
# @Author     : Yuchen Chai
# @Date       : 2020/2/8 14:23
# @Description:

from Version_1 import settings as ss

def convert(target, type, roundness = 1):
    """
    转换成需要的类型
    :param target: 需要转换的数字
    :param type: 需要转换成的类型
    :param round: 需要保留的位数
    :return:
    """
    if type == ss.variable_type.INTEGER:
        try:
            target = int(target)
        except:
            return False, ss.message.INVALID_ENTRY, None
        return True, None, target
    elif type == ss.variable_type.FLOAT:
        try:
            target = round(float(target),roundness)
        except:
            return False, ss.message.INVALID_ENTRY, None
        return True, None, target
    pass

def range_check(target, minimum = -1, maximum = -1):
    """
    根据范围检查是否在区间中
    :param target: 目标值
    :param minimum: 最小值
    :param maximum: 最大值
    :return:
    """
    if not minimum == -1:
        if target < minimum:
            return False, ss.message.INVALID_ENTRY
        pass
    if not maximum == -1:
        if target > maximum:
            return False, ss.message.INVALID_ENTRY
        pass
    return True, None

def split_data(target, sign):
    """
    根据符号，分割字符串，得到相应值
    :param target: 目标字符串
    :param sign: 符号
    :return:
    """
    value = target.split(sign)
    if len(value) == 0:
        return True, None, [None, None]
    elif len(value) == 1:
        return True, None, [value[0], None]
    elif(len(value) == 2):
        return True, None, value
    else:
        return False, ss.message.INVALID_ENTRY, [None, None]

def inputLogic(self, variableName):
    """
    根据变量种类，判断是否可以输入
    :param self: CDU类
    :param variableName: 变量类型
    :return:
    """

    msg = None
    status = True

    # 如果是消息页面
    if not self.inputLine[2] == "":
        pass
    # 如果目前进行delete
    elif self.inputLine[1] == "DELETE":
        pass
    # 如果是输入数据
    else:
        if variableName == ss.variable.PERF_COST_INDEX:
            # 转换数据
            status, msg, value = convert(self.inputLine[0], ss.variable_type.INTEGER)
            if status:
                # 检查范围
                status, msg = range_check(value, ss.variable.PERF_COST_INDEX_LOWER_LIMIT[0], ss.variable.PERF_COST_INDEX_UPPER_LIMIT[0])
                pass
            if status:
                self.dataFile.Interface_DATA_SET(ss.variable.PERF_COST_INDEX, value)
                pass
            pass

        elif variableName == ss.variable.PERF_GROSS_WEIGHT:
            status, msg, [gw, crz_cg] = split_data(self.inputLine[0], "/")

            # 验证数据
            if gw:
                status, msg, gw = convert(gw, ss.variable_type.FLOAT, 1)
                if status:
                    status, msg = range_check(gw,self.dataFile.Interface_DATA_KEYWORDS(ss.variable.PERF_FUEL),ss.variable.PERF_GROSS_WEIGHT_UPPER_LIMIT[0])
                    pass
                pass

            if crz_cg:
                status, msg, crz_cg = convert(crz_cg, ss.variable_type.FLOAT, 1)
                if status:
                    status, msg = range_check(crz_cg, ss.variable.PERF_CRUISE_CENTER_OF_GRAVITY_LOWER_LIMIT[0], ss.variable.PERF_CRUISE_CENTER_OF_GRAVITY_UPPER_LIMIT[0])
                    pass
                pass

            if status and gw:
                self.dataFile.Interface_DATA_SET(ss.variable.PERF_GROSS_WEIGHT, gw)
                self.dataFile.Interface_DATA_SET(ss.variable.PERF_ZERO_FUEL_WEIGHT, gw - self.dataFile.Interface_DATA_KEYWORDS(ss.variable.PERF_FUEL))
            if status and crz_cg:
                self.dataFile.Interface_DATA_SET(ss.variable.PERF_CRUISE_CENTER_OF_GRAVITY, crz_cg)

        # 如果有消息，消息放到列表中
        if msg:
            self.inputLine[2] = msg
            pass
        # 成功置入，清除手写板
        if status:
            self.inputLine[0] = ""


    pass