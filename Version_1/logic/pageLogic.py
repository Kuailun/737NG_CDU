# -*- coding: utf-8 -*-
# @File       : pageLogic.py
# @Author     : Yuchen Chai
# @Date       : 2020/2/7 9:40
# @Description:

from Version_1 import settings as ss
from Version_1.logic import inputLogic as il

def pageLocig(self):
    '''
    根据当前状态，切换页面
    :param self: CDU主类
    :return:
    '''

    # 如果是按下键盘或者功能键
    if (
            self.key == "INIT" or
            self.key == "RTE" or
            self.key == "CLB" or
            self.key == "CRZ" or
            self.key == "DES" or
            self.key == "MENU" or
            self.key == "LEGS" or
            self.key == "DEP" or
            self.key == "HOLD" or
            self.key == "PROG" or
            self.key == "N1" or
            self.key == "FIX"
    ):
        if self.key == "INIT":
            self.currentPage = ss.pageIndex.POS
            self.currentPageIndex = 1
            pass
        elif self.key == "RTE":
            self.currentPage = ss.pageIndex.ROUTE
            self.currentPageIndex = 1
            pass
        elif self.key == "CLB":
            self.currentPage = ss.pageIndex.CLB
            self.currentPageIndex = 1
            pass
        elif self.key == "CRZ":
            self.currentPage = ss.pageIndex.CRZ
            self.currentPageIndex = 1
            pass
        elif self.key == "DES":
            self.currentPage = ss.pageIndex.DES
            self.currentPageIndex = 1
            pass
        elif self.key == "LEGS":
            self.currentPage = ss.pageIndex.LEGS
            self.currentPageIndex = 1
            pass
        elif self.key == "DEP":
            self.currentPage = ss.pageIndex.DEPARR
            self.currentPageIndex = 1
            pass
        elif self.key == "HOLD":
            self.currentPage = ss.pageIndex.HOLD
            self.currentPageIndex = 1
            pass
        elif self.key == "PROG":
            self.currentPage = ss.pageIndex.PROGRESS
            self.currentPageIndex = 1
            pass
        elif self.key == "N1":
            self.currentPage = ss.pageIndex.N1
            self.currentPageIndex = 1
            pass
        elif self.key == "FIX":
            self.currentPage = ss.pageIndex.FIX
            self.currentPageIndex = 1
            pass
        pass

    elif (
            self.key == "L1" or
            self.key == "L2" or
            self.key == "L3" or
            self.key == "L4" or
            self.key == "L5" or
            self.key == "L6" or
            self.key == "R1" or
            self.key == "R2" or
            self.key == "R3" or
            self.key == "R4" or
            self.key == "R5" or
            self.key == "R6" or
            self.key == "EXEC" or
            self.key == "BRT-" or
            self.key == "BRT+"):
        # Index 索引页
        if self.currentPage == ss.pageIndex.INDEX:
            if self.key == "L1":
                # Ident 页面
                self.currentPage = ss.pageIndex.IDENT
                pass
            elif self.key == "L2":
                # POS 页面
                self.currentPage = ss.pageIndex.POS
                self.currentPageIndex = 1
                pass
            elif self.key == "L3":
                # PERF 页面
                self.currentPage = ss.pageIndex.PERF
                self.currentPageIndex = 1
                pass
            elif self.key == "L4":
                # TAKEOFF 页面
                self.currentPage = ss.pageIndex.TAKEOFF
                self.currentPageIndex = 1
                pass
            elif self.key == "L5":
                # APPROACH 页面
                self.currentPage = ss.pageIndex.APPROACH
                self.currentPageIndex = 1
                pass
            elif self.key == "L6":
                # OFFSET 页面
                self.currentPage = ss.pageIndex.OFFSET
                self.currentPageIndex = 1
                pass
            pass
        # Ident 页面
        elif self.currentPage == ss.pageIndex.IDENT:
            if self.key == "L6":
                # Index 页面
                self.currentPage = ss.pageIndex.INDEX
                pass
            elif self.key == "R6":
                # POS 页面
                self.currentPage = ss.pageIndex.POS
                self.currentPageIndex = 1
                pass
            pass
        # POS 页面
        elif self.currentPage == ss.pageIndex.POS:
            if self.currentPageIndex == 1:
                if self.key == "L6":
                    # Index 页面
                    self.currentPage = ss.pageIndex.INDEX
                    pass
                elif self.key == "R6":
                    # POS 页面
                    self.currentPage = ss.pageIndex.ROUTE
                    self.currentPageIndex = 1
                    pass
                pass
            elif self.currentPageIndex == 3:
                if self.key == "L6":
                    # Index 页面
                    self.currentPage = ss.pageIndex.INDEX
                    pass
                pass
            pass
        # PERF 页面
        elif self.currentPage == ss.pageIndex.PERF:
            if self.currentPageIndex == 1:
                # GW/CRZ CG 输入框
                if self.key == "L1":
                    il.inputLogic(self, ss.variable.PERF_GROSS_WEIGHT)
                    pass
                # COST INDEX 输入框
                if self.key == "L5":
                    il.inputLogic(self, ss.variable.PERF_COST_INDEX)
                    pass
                elif self.key == "L6":
                    # Index 页面
                    self.currentPage = ss.pageIndex.INDEX
                    pass
                elif self.key == "R6":
                    # N1 Limit 页面
                    self.currentPage = ss.pageIndex.N1
                    self.currentPageIndex = 1
                    pass
                pass
            elif self.currentPageIndex == 2:
                if self.key == "L6":
                    # Index 页面
                    self.currentPage = ss.pageIndex.INDEX
                    pass
                elif self.key == "R6":
                    # RTA 页面
                    self.currentPage = ss.pageIndex.PROGRESS
                    self.currentPageIndex = 3
                    pass
                pass
            pass
        # Take Off 页面
        elif self.currentPage == ss.pageIndex.TAKEOFF:
            if self.currentPageIndex == 1:
                if self.key == "L6":
                    # PERF 页面
                    self.currentPage = ss.pageIndex.PERF
                    self.currentPageIndex = 1
                    pass
                pass
            elif self.currentPageIndex == 2:
                if self.key == "L6":
                    # PERF 页面
                    self.currentPage = ss.pageIndex.PERF
                    self.currentPageIndex = 1
                    pass
                pass
            pass
        # Approach 页面
        elif self.currentPage == ss.pageIndex.APPROACH:
            if self.currentPageIndex == 1:
                if self.key == "L6":
                    # INDEX 页面
                    self.currentPage = ss.pageIndex.INDEX
                    pass
                pass
        # OFFSET 页面
        elif self.currentPage == ss.pageIndex.OFFSET:
            pass
        # Route 页面
        elif self.currentPage == ss.pageIndex.ROUTE:
            pass
        # CLB 页面
        elif self.currentPage == ss.pageIndex.CLB:
            pass
        # CRZ 页面
        elif self.currentPage == ss.pageIndex.CRZ:
            pass
        # DES 页面
        elif self.currentPage == ss.pageIndex.DES:
            pass
        # LEGS 页面
        elif self.currentPage == ss.pageIndex.LEGS:
            pass
        # DEPARR 页面
        elif self.currentPage == ss.pageIndex.DEPARR:
            pass
        # HOLD 页面
        elif self.currentPage == ss.pageIndex.HOLD:
            pass
        # PROGRESS 页面
        elif self.currentPage == ss.pageIndex.PROGRESS:
            pass
        # N1 页面
        elif self.currentPage == ss.pageIndex.N1:
            if self.key == "L6":
                # PERF 页面
                self.currentPage = ss.pageIndex.PERF
                self.currentPageIndex = 1
                pass
            elif self.key == "R6":
                # TAKEOFF 页面
                self.currentPage = ss.pageIndex.TAKEOFF
                self.currentPageIndex = 1
                pass
            pass
        # FIX 页面
        elif self.currentPage == ss.pageIndex.FIX:
            pass
    else:
        # 如果按下的是加减符号
        if self.key == "plus":
            if self.inputLine[1]=="" and self.inputLine[2]=="":
                if len(self.inputLine[0])>0:
                    if self.inputLine[0][-1] == "+":
                        self.inputLine[0] = self.inputLine[0][0:-1] + "-"
                    elif self.inputLine[0][-1] == "-":
                        self.inputLine[0] = self.inputLine[0][0:-1] + "+"
                    else:
                        self.inputLine[0] = self.inputLine[0] + "-"
                else:
                    self.inputLine[0] = self.inputLine[0]+"-"
            pass
        # 如果按下的是空格符号
        elif self.key == "SP":
            if self.inputLine[1]=="" and self.inputLine[2]=="":
                self.inputLine[0] = self.inputLine[0] + " "
            pass
        # 如果按下的是删除符号
        elif self.key == "DEL":
            if self.inputLine[1]=="":
                self.inputLine[1] = "DELETE"
            elif self.inputLine[1]=="DELETE":
                self.inputLine[1] = ""
            pass
        # 如果按下的是清除符号
        elif self.key == "CLR":
            # 如果当前有msg，则清除msg
            if not self.inputLine[2]=="":
                self.inputLine[2]=""
            # 如果当前有delete，则清除delete
            elif not self.inputLine[1]=="":
                self.inputLine[1]=""
            # 正常情况，判断是否为空
            else:
                if not len(self.inputLine) == 0:
                    self.inputLine[0] = self.inputLine[0][0:-1]
                else:
                    pass
                pass
            pass
        # 如果按下的是小数点符号
        elif self.key == "dot":
            if self.inputLine[1]=="" and self.inputLine[2]=="":
                self.inputLine[0] = self.inputLine[0] + "."
            pass
        # 如果按下的是下一页
        elif self.key == "NEXT":
            self.currentPageIndex = self.currentPageIndex + 1
            pass
        # 如果按下的是上一页
        elif self.key == "PREV":
            self.currentPageIndex = self.currentPageIndex - 1
            pass
        # 其他的按键
        else:
            # 如果不是在删除模式，则可以增加字母
            if self.inputLine[1]=="" and self.inputLine[2]=="":
                self.inputLine[0] = self.inputLine[0] + self.key
            pass

        # 如果一行的字母过多，则仅保留前24个
        if len(self.inputLine[0])>24:
            self.inputLine[0] = self.inputLine[0][0:24]
            pass

