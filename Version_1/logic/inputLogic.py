# -*- coding: utf-8 -*-
# @File       : inputLogic.py
# @Author     : Yuchen Chai
# @Date       : 2020/2/8 14:23
# @Description:

import settings as ss

if ss.APPLICATION_MODE == "DEVELOPMENT":
    from Version_1 import variable
else:
    import variable

def convert(target, type, roundness = 1):
    """
    转换成需要的类型
    :param target: 需要转换的数字
    :param type: 需要转换成的类型
    :param round: 需要保留的位数
    :return:
    """
    if type == variable.variable_type.INTEGER:
        try:
            target = int(target)
        except:
            return False, ss.message.INVALID_ENTRY, None
        return True, None, target
    elif type == variable.variable_type.FLOAT:
        try:
            target = round(float(target),roundness)
        except:
            return False, ss.message.INVALID_ENTRY, None
        return True, None, target
    elif type == variable.variable_type.STRING:
        return True, None, str(target)
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

def inputLogic(self, variableName,input):
    """
    根据变量种类，判断是否可以输入
    :param self: CDU类
    :param variableName: 变量类型
    :param input: 0-输入/删除数据，1-点击进入
    :return:
    """

    msg = None
    status = True

    # 如果是输入数据
    if input == variable.line_select_mode.INPUT_DELETE:
        # 设定PERF页面的COST INDEX指数
        if variableName == ss.variable.PERF_COST_INDEX:
            # 转换数据
            status, msg, value = convert(self.inputLine[0], variable.variable_type.INTEGER)
            if status:
                # 检查范围
                status, msg = range_check(value, variable.Limit_COST_INDEX.MIN, variable.Limit_COST_INDEX.MAX)
                pass
            if status:
                self.dataFile.Interface_DATA_SET(ss.variable.PERF_COST_INDEX, value)
                pass
            pass

        # 设定PERF页面的Gross Weight数目
        elif variableName == ss.variable.PERF_GROSS_WEIGHT:
            status, msg, [gw, crz_cg] = split_data(self.inputLine[0], "/")

            # 验证数据
            if gw:
                status, msg, gw = convert(gw, variable.variable_type.FLOAT, roundness=1)
                if status:
                    status, msg = range_check(gw, minimum=self.dataFile.Interface_DATA_KEYWORDS(ss.variable.PERF_FUEL), maximum=variable.Limit_GROSS_WEIGHT.MAX)
                    pass
                pass

            if crz_cg:
                status, msg, crz_cg = convert(crz_cg, variable.variable_type.FLOAT, roundness=1)
                if status:
                    status, msg = range_check(crz_cg, minimum=variable.Limit_CRUISE_CENTER_OF_GRAVITY.MIN, maximum=variable.Limit_CRUISE_CENTER_OF_GRAVITY.MAX)
                    pass
                pass

            if status and gw:
                self.dataFile.Interface_DATA_SET(ss.variable.PERF_GROSS_WEIGHT, gw)
                self.dataFile.Interface_DATA_SET(ss.variable.PERF_ZERO_FUEL_WEIGHT, gw - self.dataFile.Interface_DATA_KEYWORDS(ss.variable.PERF_FUEL))
            if status and crz_cg:
                self.dataFile.Interface_DATA_SET(ss.variable.PERF_CRUISE_CENTER_OF_GRAVITY, crz_cg)
                pass
            pass

        # 设定RTE页面的离场机场
        elif variableName == ss.variable.RTE_ORIGIN:
            # 转换数据
            status, msg, value = convert(self.inputLine[0], variable.variable_type.STRING)
            if status:
                # 检查范围
                status, msg, data = self.dataFile.Interface_ORIGIN_DEST(value)
                pass
            if status:
                self.dataFile.Interface_DATA_SET(ss.variable.RTE_ORIGIN, value)
                self.dataFile.Interface_DATA_SET(ss.variable.RTE_ORIGIN_LOCATION, data)
                self.dataFile.Interface_DEPARTURES_AIRPORT_SET(value)
                pass
            pass

        # 设定RTE页面的进场机场
        elif variableName == ss.variable.RTE_DEST:
            # 转换数据
            status, msg, value = convert(self.inputLine[0], variable.variable_type.STRING)
            if status:
                # 检查范围
                status, msg, data = self.dataFile.Interface_ORIGIN_DEST(value)
                pass
            if status:
                self.dataFile.Interface_DATA_SET(ss.variable.RTE_DEST, value)
                self.dataFile.Interface_DATA_SET(ss.variable.RTE_DEST_LOCATION, data)
                pass
            pass

        # 设定POS页面的REF AIRPORT
        elif variableName == ss.variable.POS_REF_AIRPORT:
            # 尝试删除
            if input == variable.input_line_display_mode.DELETE:
                msg = ss.message.INVALID_DELETE
            # 尝试输入
            elif input == variable.input_line_display_mode.SELFINPUT:
                status, msg, value = convert(self.inputLine[0],variable.variable_type.STRING)

                if not len(value) == 4:
                    status = False
                    msg = ss.message.INVALID_ENTRY
                # 查询机场是否存在于数据库中
                if status:
                    status, msg, data = self.dataFile.Interface_ORIGIN_DEST(value)

                # 设置该消息到数据库中
                if status:
                    self.dataFile.Interface_REF_AIRPORT_SET(value)
                else:
                    if not msg:
                        msg = ss.message.NOT_IN_DATA_BASE
                        pass
                    pass
                pass
            pass

        # 设定POS页面的REF GATE
        elif variableName == ss.variable.POS_REF_GATE:
            # 尝试删除
            if input == variable.input_line_display_mode.DELETE:
                msg = ss.message.INVALID_DELETE
            # 尝试输入
            elif input == variable.input_line_display_mode.SELFINPUT:
                ref_airport = self.dataFile.Interface_DATA_KEYWORDS(ss.variable.POS_REF_AIRPORT)

                # 该机场不存在
                if not ref_airport:
                    return

                status, msg, value = convert(self.inputLine[0], variable.variable_type.STRING)

                # 查询机场是否存在于数据库中
                if status:
                    if value in ref_airport['GATES']:
                        self.dataFile.Interface_DATA_SET(ss.variable.POS_REF_GATE, value)
                    else:
                        status = False
                        msg = ss.message.NOT_IN_DATA_BASE
                    pass
                pass
            pass

        # 设定RTE页面的Runway变量
        elif variableName == ss.variable.RTE_RUNWAY:
            # 尝试删除
            if input == variable.input_line_display_mode.DELETE:
                msg = ss.message.INVALID_DELETE
            # 尝试输入
            elif input == variable.input_line_display_mode.SELFINPUT:
                value_origin = self.dataFile.Interface_DATA_KEYWORDS(ss.variable.RTE_ORIGIN)
                value_origin_data = self.dataFile.Interface_DATA_KEYWORDS(ss.variable.DEPARR_DEP_AIRPORTS_DATA)
                # 如果没有输入ORIGIN机场，则直接跳过
                if not value_origin:
                    pass
                else:
                    value_input = self.inputLine[0]
                    if value_input[-1] == "L" or value_input[-1] == 'R':
                        value_input = str(int(value_input[0:-1])) + value_input[-1]
                        if value_input in value_origin_data['RWNS']:
                            pass
                    pass
                pass
            pass



        # 如果有消息，消息放到列表中
        if msg:
            self.insertMsg(msg)
            pass
        # 成功置入，清除手写板
        if status:
            self.resetInput()
            pass
        pass
    # 如果是点击了某个页面
    elif input == variable.line_select_mode.PAGE:
        # 如果已选定origin，则可以进入对应机场的DEP页面
        if variableName == ss.variable.DEPARR_DEP_PAGE_FLAG:
            # 清空临时的变量
            self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_SID_TEMP, None)
            self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_RUNWAY_TEMP, None)
            self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_TRANSITION_TEMP, None)
            return self.dataFile.Interface_DATA_VALID(ss.variable.RTE_ORIGIN)

        # 在DEPARTURES页面按下键的响应
        elif variableName == ss.variable.DEPARTURES_KEY_PRESSED:
            flag_sid = self.dataFile.Interface_DATA_KEYWORDS(ss.variable.DEPARTURES_SID_TEMP)
            flag_transition = self.dataFile.Interface_DATA_KEYWORDS(ss.variable.DEPARTURES_TRANSITION_TEMP)
            flag_runway = self.dataFile.Interface_DATA_KEYWORDS(ss.variable.DEPARTURES_RUNWAY_TEMP)

            value_sid = self.dataFile.Interface_DATA_KEYWORDS(ss.variable.DEPARTURES_SID)
            value_transition = self.dataFile.Interface_DATA_KEYWORDS(ss.variable.DEPARTURES_TRANSITION)
            value_runway = self.dataFile.Interface_DATA_KEYWORDS(ss.variable.DEPARTURES_RUNWAY)

            dep_data = self.dataFile.Interface_DATA_KEYWORDS(ss.variable.DEPARR_DEP_AIRPORTS_DATA)

            # 回到首页
            self.currentPageIndex = 1

            left_flag = False
            if self.key[0] == "L":
                left_flag = True
                pass
            line = int(self.key[1])
            index = (self.currentPageIndex - 1) * 5 + line

            # 全都没有选
            if (not flag_sid) and (not flag_transition) and (not flag_runway):
                # 选中SIDS
                if left_flag:
                    # 只要选了SIDS，必须重选TRANSITIONS
                    self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_TRANSITION,None)
                    self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_TRANSITION_TEMP,None)
                    if index > len(dep_data['SIDS']):
                        pass
                    else:
                        keys = list(dep_data['SIDS'].keys())
                        flag_sid = keys[index - 1]
                        self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_SID_TEMP, flag_sid)

                        # 如果在该SID下Transition为空，则抹去有关内容
                        if len(dep_data["SIDS"][flag_sid]["Transitions"]) == 0:
                            self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_TRANSITION_TEMP, None)
                            self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_TRANSITION, None)
                            pass

                        # 如果选择SID的时候，该SID在该之前选择的跑道中出现，则立即更新数据
                        if value_runway:
                            if flag_sid in dep_data['RNWS'][value_runway]['SIDS']:
                                self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_TRANSITION_TEMP, None)
                                self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_TRANSITION, None)
                                self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_SID, flag_sid)

                        pass
                    pass
                # 选中RUNWAYS
                elif not left_flag:
                    if index > len(dep_data['RNWS']):
                        pass
                    else:
                        keys = list(dep_data['RNWS'].keys())
                        flag_runway = keys[index - 1]
                        self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_RUNWAY_TEMP, flag_runway)
                        self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_RUNWAY, flag_runway)

                        # 如果在该RNWS下SIDS为空，则抹去有关内容
                        if len(dep_data["RNWS"][flag_runway]['SIDS']) == 0:
                            # 如果此时已有存储的SID，则触发msg
                            if value_sid:
                                self.insertMsg(ss.message.RUNWAY_NA_FOR_SID)

                            self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_SID_TEMP, None)
                            self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_SID, None)
                            self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_TRANSITION_TEMP, None)
                            self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_TRANSITION, None)
                            pass
                        # 如果之前选择过SID，现在重新选择Runways的时候，sid不在新的跑道中
                        if value_sid:
                            if value_sid not in dep_data['RNWS'][flag_runway]['SIDS']:
                                self.insertMsg(ss.message.RUNWAY_NA_FOR_SID)
                                self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_SID_TEMP, None)
                                self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_SID, None)
                                self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_TRANSITION_TEMP, None)
                                self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_TRANSITION, None)
                        pass
                    pass
                pass
            # 已经选择了SIDS
            elif (flag_sid) and (not flag_transition) and (not flag_runway):
                # 选左侧的
                if left_flag:
                    # 左侧的SID已经选过了
                    if index == 1:
                        pass
                    else:
                        # 超过了TRANS列表的上限
                        if (index - 2) >= len(dep_data['SIDS'][flag_sid]['Transitions']):
                            pass
                        else:
                            flag_transition = dep_data['SIDS'][flag_sid]['Transitions'][index-2]
                            self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_TRANSITION_TEMP, flag_transition)

                        pass
                    pass
                # 选右侧的RUNWAY
                elif not left_flag:
                    if index > len(dep_data['SIDS'][flag_sid]["Runways"]):
                        pass
                    else:
                        flag_runway = dep_data['SIDS'][flag_sid]["Runways"][index - 1]
                        self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_RUNWAY_TEMP, flag_runway)
                        self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_RUNWAY, flag_runway)
                        self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_SID,flag_sid)
                        pass
                    pass
            # 已经选择了RUNWAY
            elif (not flag_sid) and (not flag_transition) and (flag_runway):
                # 选左侧的
                if left_flag:
                    # 只要选了SIDS，必须重选TRANSITIONS
                    self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_TRANSITION, None)
                    self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_TRANSITION_TEMP, None)
                    if index > len(dep_data['SIDS']):
                        pass
                    else:
                        flag_sid = dep_data['RNWS'][flag_runway]["SIDS"][index-1]
                        self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_SID_TEMP, flag_sid)
                        self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_SID,flag_sid)

                        # 如果在该SID下Transition为空，则抹去有关内容
                        if len(dep_data["SIDS"][flag_sid]["Transitions"]) == 0:
                            self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_TRANSITION_TEMP, None)
                            self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_TRANSITION, None)
                        pass
                    pass
                # 右侧RUNWAYS已经选过了
                elif not left_flag:
                    pass
                pass
            elif (flag_sid) and (flag_transition) and (not flag_runway):
                # 左侧的SIDS和TRANSITION都已经选过了
                if left_flag:
                    pass
                elif not left_flag:
                    if index > len(dep_data['SIDS'][flag_sid]["Runways"]):
                        pass
                    else:
                        flag_runway = dep_data['SIDS'][flag_sid]["Runways"][index - 1]
                        self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_RUNWAY_TEMP, flag_runway)
                        self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_RUNWAY, flag_runway)
                        self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_SID_TEMP, flag_sid)
                        self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_SID, flag_sid)
                        self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_TRANSITION_TEMP, flag_transition)
                        self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_TRANSITION, flag_transition)
                        pass
                    pass
                pass
            elif (flag_sid) and (not flag_transition) and (flag_runway):
                # 选择左边的SIDS和TRANS
                if left_flag:
                    # SIDS已经选过了
                    if index == 1:
                        pass
                    # 选择TRANSITION
                    else:
                        # 超过了TRANS列表的上限
                        if (index - 2) >= len(dep_data['SIDS'][flag_sid]['Transitions']):
                            pass
                        else:
                            flag_transition = dep_data['SIDS'][flag_sid]['Transitions'][index - 2]
                            self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_TRANSITION_TEMP, flag_transition)
                            self.dataFile.Interface_DATA_SET(ss.variable.DEPARTURES_TRANSITION,flag_transition)
                        pass
                    pass
                # 右边的RUNWAY已经选过了
                elif not left_flag:
                    pass
                pass
            elif (flag_sid) and (flag_transition) and (flag_runway):
                # Do nothing
                pass
            pass
        pass
    pass