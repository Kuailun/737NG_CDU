# -*- coding: utf-8 -*-
# @File       : pageLogic.py
# @Author     : Yuchen Chai
# @Date       : 2020/2/7 9:40
# @Description:

import settings as ss

if ss.APPLICATION_MODE == "DEVELOPMENT":
    from Version_1.logic import inputLogic as il
    from Version_1 import Utils as ut
    from Version_1 import variable
else:
    import inputLogic as il
    import Utils as ut
    import variable


def pressKeyLogic(self, situation = 0):
    """
    输入栏的逻辑
    :param self:
    :param situation: 2-MSG, 1-DELETE, 0-INPUT
    :return:
    """
    if self.key == variable.key_press_content.PLUS_SUBSTRACT:
        # 自主输入模式
        if situation == variable.input_line_display_mode.SELFINPUT:
            if self.inputLine[1] == "":
                self.inputLine[1] = self.inputLine[1] + "-"
                pass
            else:
                if self.inputLine[1][-1] == "+":
                    self.inputLine[1] = self.inputLine[1][0:-1] + "-"
                elif self.inputLine[1][-1] == "-":
                    self.inputLine[1] = self.inputLine[1][0:-1] + "+"
                else:
                    self.inputLine[1] = self.inputLine[1] + "-"
                    pass
                pass
            pass
        elif situation == variable.input_line_display_mode.MESSAGE:
            self.inputLine[1] = "-"
            pass
        pass
    elif self.key == variable.key_press_content.SPACE:
        if situation == variable.input_line_display_mode.SELFINPUT:
            self.inputLine[1] = self.inputLine[1] + " "
        elif situation == variable.input_line_display_mode.MESSAGE:
            self.inputLine[1] = " "
            pass
        pass
    elif self.key == variable.key_press_content.DELETE:
        if self.inputLine[2] == "DELETE":
            self.inputLine[2] = ""
        else:
            self.inputLine[2] = "DELETE"
            pass
        pass
    elif self.key == variable.key_press_content.CLEAR:
        if situation == variable.input_line_display_mode.SELFINPUT:
            if self.inputLine[1] == "":
                pass
            else:
                self.inputLine[1] = self.inputLine[1][0:-1]
                pass
            pass
        elif situation == variable.input_line_display_mode.DELETE:
            self.inputLine[2] = ""
            pass
        elif situation == variable.input_line_display_mode.MESSAGE:
            pass
        pass
    elif self.key == variable.key_press_content.DOT:
        if situation == variable.input_line_display_mode.SELFINPUT:
            self.inputLine[1] = self.inputLine[1] + "."
        elif situation == variable.input_line_display_mode.DELETE:
            pass
        elif situation == variable.input_line_display_mode.MESSAGE:
            pass
        pass
    else:
        if situation == variable.input_line_display_mode.SELFINPUT:
            self.inputLine[1] = self.inputLine[1] + self.key
        elif situation == variable.input_line_display_mode.DELETE:
            pass
        elif situation == variable.input_line_display_mode.MESSAGE:
            pass
        pass

def pageLogic(self):
    '''
    根据当前状态，切换页面
    :param self: CDU主类
    :return:
    '''

    # 如果是按下键盘或者功能键
    if ut.keyRange(self.key, function=True):
        if self.key == variable.key_press_content.INIT_REF:
            self.currentPage = variable.page_index.POS
            self.currentPageIndex = 1
            pass
        elif self.key == variable.key_press_content.RTE:
            self.currentPage = variable.page_index.ROUTE
            self.currentPageIndex = 1
            pass
        elif self.key == variable.key_press_content.CLB:
            self.currentPage = variable.page_index.CLB
            self.currentPageIndex = 1
            pass
        elif self.key == variable.key_press_content.CRZ:
            self.currentPage = variable.page_index.CRZ
            self.currentPageIndex = 1
            pass
        elif self.key == variable.key_press_content.DES:
            self.currentPage = variable.page_index.DES
            self.currentPageIndex = 1
            pass
        elif self.key == variable.key_press_content.LEGS:
            self.currentPage = variable.page_index.LEGS
            self.currentPageIndex = 1
            pass
        elif self.key == variable.key_press_content.DEPARR:
            self.currentPage = variable.page_index.DEPARR
            self.currentPageIndex = 1
            pass
        elif self.key == variable.key_press_content.HOLD:
            self.currentPage = variable.page_index.HOLD
            self.currentPageIndex = 1
            pass
        elif self.key == variable.key_press_content.PROG:
            self.currentPage = variable.page_index.PROGRESS
            self.currentPageIndex = 1
            pass
        elif self.key == variable.key_press_content.N1_LIMIT:
            self.currentPage = variable.page_index.N1
            self.currentPageIndex = 1
            pass
        elif self.key == variable.key_press_content.FIX:
            self.currentPage = variable.page_index.FIX
            self.currentPageIndex = 1
            pass
        pass

    elif ut.keyRange(self.key,lineSelect=True) or self.key == variable.key_press_content.EXECUTE or self.key == variable.key_press_content.BRTU or self.key == variable.key_press_content.BRTD:
        # Index 索引页
        if self.currentPage == variable.page_index.INDEX:
            if self.key == variable.key_press_content.L1:
                # Ident 页面
                self.currentPage = variable.page_index.IDENT
                pass
            elif self.key == variable.key_press_content.L2:
                # POS 页面
                self.currentPage = variable.page_index.POS
                self.currentPageIndex = 1
                pass
            elif self.key == variable.key_press_content.L3:
                # PERF 页面
                self.currentPage = variable.page_index.PERF
                self.currentPageIndex = 1
                pass
            elif self.key == variable.key_press_content.L4:
                # TAKEOFF 页面
                self.currentPage = variable.page_index.TAKEOFF
                self.currentPageIndex = 1
                pass
            elif self.key == variable.key_press_content.L5:
                # APPROACH 页面
                self.currentPage = variable.page_index.APPROACH
                self.currentPageIndex = 1
                pass
            elif self.key == variable.key_press_content.L6:
                # OFFSET 页面
                self.currentPage = variable.page_index.OFFSET
                self.currentPageIndex = 1
                pass
            pass
        # Ident 页面
        elif self.currentPage == variable.page_index.IDENT:
            if self.key == variable.key_press_content.L6:
                # Index 页面
                self.currentPage = variable.page_index.INDEX
                pass
            elif self.key == variable.key_press_content.R6:
                # POS 页面
                self.currentPage = variable.page_index.POS
                self.currentPageIndex = 1
                pass
            pass
        # POS 页面
        elif self.currentPage == variable.page_index.POS:
            if self.currentPageIndex == 1:
                if self.key == variable.key_press_content.L2:
                    # 输入REF AIRPORT数据
                    il.inputLogic(self,ss.variable.POS_REF_AIRPORT,variable.input_line_display_mode.SELFINPUT)
                    pass
                elif self.key == variable.key_press_content.L3:
                    # 输入REF GATE数据
                    il.inputLogic(self,ss.variable.POS_REF_GATE, variable.input_line_display_mode.SELFINPUT)

                elif self.key == variable.key_press_content.L6:
                    # Index 页面
                    self.currentPage = variable.page_index.INDEX
                    pass
                elif self.key == variable.key_press_content.R6:
                    # POS 页面
                    self.currentPage = variable.page_index.ROUTE
                    self.currentPageIndex = 1
                    pass
                pass
            elif self.currentPageIndex == 3:
                if self.key == variable.key_press_content.L6:
                    # Index 页面
                    self.currentPage = variable.page_index.INDEX
                    pass
                pass
            pass
        # PERF 页面
        elif self.currentPage == variable.page_index.PERF:
            if self.currentPageIndex == 1:
                # GW/CRZ CG 输入框
                if self.key == variable.key_press_content.L1:
                    il.inputLogic(self, ss.variable.PERF_GROSS_WEIGHT,variable.line_select_mode.INPUT_DELETE)
                    pass
                # COST INDEX 输入框
                if self.key == variable.key_press_content.L5:
                    il.inputLogic(self, ss.variable.PERF_COST_INDEX,variable.line_select_mode.INPUT_DELETE)
                    pass
                elif self.key == variable.key_press_content.L6:
                    # Index 页面
                    self.currentPage = variable.page_index.INDEX
                    pass
                elif self.key == variable.key_press_content.R6:
                    # N1 Limit 页面
                    self.currentPage = variable.page_index.N1
                    self.currentPageIndex = 1
                    pass
                pass
            elif self.currentPageIndex == 2:
                if self.key == variable.key_press_content.L6:
                    # Index 页面
                    self.currentPage = variable.page_index.INDEX
                    pass
                elif self.key == variable.key_press_content.R6:
                    # RTA 页面
                    self.currentPage = variable.page_index.PROGRESS
                    self.currentPageIndex = 3
                    pass
                pass
            pass
        # Take Off 页面
        elif self.currentPage == variable.page_index.TAKEOFF:
            if self.currentPageIndex == 1:
                if self.key == variable.key_press_content.L6:
                    # PERF 页面
                    self.currentPage = variable.page_index.PERF
                    self.currentPageIndex = 1
                    pass
                pass
            elif self.currentPageIndex == 2:
                if self.key == variable.key_press_content.L6:
                    # PERF 页面
                    self.currentPage = variable.page_index.PERF
                    self.currentPageIndex = 1
                    pass
                pass
            pass
        # Approach 页面
        elif self.currentPage == variable.page_index.APPROACH:
            if self.currentPageIndex == 1:
                if self.key == variable.key_press_content.L6:
                    # INDEX 页面
                    self.currentPage = variable.page_index.INDEX
                    pass
                pass
        # OFFSET 页面
        elif self.currentPage == variable.page_index.OFFSET:
            pass
        # Route 页面
        elif self.currentPage == variable.page_index.ROUTE:
            # ORIGIN 输入框
            if self.key == variable.key_press_content.L1:
                il.inputLogic(self, ss.variable.RTE_ORIGIN,variable.line_select_mode.INPUT_DELETE)
                pass
            # RUNWAY 输入框
            elif self.key == variable.key_press_content.L3:
                il.inputLogic(self,ss.variable.RTE_RUNWAY, variable.line_select_mode.INPUT_DELETE)
                pass
            elif self.key == variable.key_press_content.R1:
                il.inputLogic(self,ss.variable.RTE_DEST,variable.line_select_mode.INPUT_DELETE)
            pass
        # CLB 页面
        elif self.currentPage == variable.page_index.CLB:
            pass
        # CRZ 页面
        elif self.currentPage == variable.page_index.CRZ:
            pass
        # DES 页面
        elif self.currentPage == variable.page_index.DES:
            pass
        # LEGS 页面
        elif self.currentPage == variable.page_index.LEGS:
            pass
        # DEPARR 页面
        elif self.currentPage == variable.page_index.DEPARR:
            # ORIGIN 输入框
            if self.key == variable.key_press_content.L1:
                if il.inputLogic(self, ss.variable.DEPARR_DEP_PAGE_FLAG,variable.line_select_mode.PAGE):
                    self.currentPage = variable.page_index.DEPARTURES
                    self.currentPageIndex = 1
                pass
            pass
        # HOLD 页面
        elif self.currentPage == variable.page_index.HOLD:
            pass
        # PROGRESS 页面
        elif self.currentPage == variable.page_index.PROGRESS:
            pass
        # N1 页面
        elif self.currentPage == variable.page_index.N1:
            if self.key == variable.key_press_content.L6:
                # PERF 页面
                self.currentPage = variable.page_index.PERF
                self.currentPageIndex = 1
                pass
            elif self.key == variable.key_press_content.R6:
                # TAKEOFF 页面
                self.currentPage = variable.page_index.TAKEOFF
                self.currentPageIndex = 1
                pass
            pass
        # FIX 页面
        elif self.currentPage == variable.page_index.FIX:
            pass
        # DEPARTURES 页面
        elif self.currentPage == variable.page_index.DEPARTURES:
            if self.key == variable.key_press_content.L6:
                # DEPARR 页面
                self.currentPage = variable.page_index.DEPARR
                self.currentPageIndex = 1
                pass
            elif self.key == variable.key_press_content.R6:
                # ROUTE 页面
                self.currentPage = variable.page_index.ROUTE
                self.currentPageIndex = 1
                pass
            else:
                # 按下的其他键，选择sid，trans，runways
                il.inputLogic(self,ss.variable.DEPARTURES_KEY_PRESSED,variable.line_select_mode.PAGE)
            pass
        # LOGO 页面
        elif self.currentPage == variable.page_index.LOGO:
            pass
    else:

        # 如果按下的是加减符号
        if self.key == variable.key_press_content.PLUS_SUBSTRACT:
            # 正常显示期间
            if self.inputDisplayMode == variable.input_line_display_mode.SELFINPUT:
                pressKeyLogic(self,0)
            # delete期间没作用
            elif self.inputDisplayMode == variable.input_line_display_mode.DELETE:
                pass
            # 正在显示消息
            elif self.inputDisplayMode == variable.input_line_display_mode.MESSAGE:
                pass
            pass
        # 如果按下的是空格符号
        elif self.key == variable.key_press_content.SPACE:
            # 正常显示期间
            if self.inputDisplayMode == variable.input_line_display_mode.SELFINPUT:
                pressKeyLogic(self, 0)
            # delete期间没作用
            elif self.inputDisplayMode == variable.input_line_display_mode.DELETE:
                pass
            # 正在显示消息
            elif self.inputDisplayMode == variable.input_line_display_mode.MESSAGE:
                pass
            pass
        # 如果按下的是删除符号
        elif self.key == variable.key_press_content.DELETE:
            pressKeyLogic(self)
        # 如果按下的是清除符号
        elif self.key == variable.key_press_content.CLEAR:
            # 正常显示期间
            if self.inputDisplayMode == variable.input_line_display_mode.SELFINPUT:
                pressKeyLogic(self, 0)
            # delete期间清除delete
            elif self.inputDisplayMode == variable.input_line_display_mode.DELETE:
                pressKeyLogic(self, 1)
                pass
            # 正在显示消息
            elif self.inputDisplayMode == variable.input_line_display_mode.MESSAGE:
                pressKeyLogic(self, 2)
                self.removeMsg()
                pass
            pass
        # 如果按下的是小数点符号
        elif self.key == variable.key_press_content.DOT:
            # 正常显示期间
            if self.inputDisplayMode == variable.input_line_display_mode.SELFINPUT:
                pressKeyLogic(self, 0)
            # delete期间没作用
            elif self.inputDisplayMode == variable.input_line_display_mode.DELETE:
                pass
            # 正在显示消息
            elif self.inputDisplayMode == variable.input_line_display_mode.MESSAGE:
                pass
            pass
        # 如果按下的是下一页
        elif self.key == variable.key_press_content.NEXT_PAGE:
            self.currentPageIndex = self.currentPageIndex + 1
            pass
        # 如果按下的是上一页
        elif self.key == variable.key_press_content.PREV_PAGE:
            self.currentPageIndex = self.currentPageIndex - 1
            pass
        # 其他的按键
        else:
            # 正常显示期间
            if self.inputDisplayMode == variable.input_line_display_mode.SELFINPUT:
                pressKeyLogic(self, 0)
            # delete期间没作用
            elif self.inputDisplayMode == variable.input_line_display_mode.DELETE:
                pass
            # 正在显示消息
            elif self.inputDisplayMode == variable.input_line_display_mode.MESSAGE:
                pass
            pass
        pass

    self.updateInputLine()
