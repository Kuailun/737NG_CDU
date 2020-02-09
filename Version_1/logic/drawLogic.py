# -*- coding: utf-8 -*-
# @File       : drawLogic.py
# @Author     : Yuchen Chai
# @Date       : 2020/2/8 14:21
# @Description:

from Version_1 import settings as ss

def COST_INDEX(self):
    """
    根据数据库内容，判断显示内容
    :return:
    """
    value = self.dataFile.Interface_DATA_KEYWORDS(ss.variable.PERF_COST_INDEX)
    if not value:
        return "***"
    else:
        if value < 10:
            return "  " + str(value)
        elif value < 100:
            return " " + str(value)
        return str(value)
    pass
def GW_CRZ_CG(self):
    """
    根据数据库内容，返回GW CRZ CG的显示内容
    :param self:
    :return:
    """
    gross_weight = self.dataFile.Interface_DATA_KEYWORDS(ss.variable.PERF_GROSS_WEIGHT)
    crz_center = self.dataFile.Interface_DATA_KEYWORDS(ss.variable.PERF_CRUISE_CENTER_OF_GRAVITY)

    if not gross_weight:
        return "***.*/"+str(crz_center) + "%"
    else:
        if gross_weight < 100:
            return " " + str(gross_weight) + "/" + str(crz_center) + "%"
        else:
            return str(gross_weight) + "/" + str(crz_center) + "%"
        pass
    pass
def Zero_Fuel_Weight(self):
    """
    根据数据库内容，返回ZFW的显示内容
    :param self:
    :return:
    """
    zero_fuel_weight = self.dataFile.Interface_DATA_KEYWORDS(ss.variable.PERF_ZERO_FUEL_WEIGHT)

    if not zero_fuel_weight:
        return "***.*"
    else:
        if zero_fuel_weight < 100:
            return " " + str(zero_fuel_weight)
        pass
    pass

def pageDraw(self, painter):

    # 清除line display的内容
    self.lineDisplay = self.ResetLineDisplay()

    # 得到当前输入行
    if not self.inputLine[2] == "":
        self.inputLine[3] = self.inputLine[2]
    elif not self.inputLine[1] == "":
        self.inputLine[3] = self.inputLine[1]
    else:
        self.inputLine[3] = self.inputLine[0]

    # Index 索引页
    if self.currentPage == ss.pageIndex.INDEX:
        # Draw the screen title
        self.lineDisplay["L0M"] = [{"Color": ss.COLOR_WHITE, "Content": "     INIT/REF INDEX"}]
        self.lineDisplay["L1M"] = [{"Color": ss.COLOR_WHITE, "Content": "<IDENT"}]
        self.lineDisplay["L2M"] = [{"Color": ss.COLOR_WHITE, "Content": "<POS"}]
        self.lineDisplay["L3M"] = [{"Color": ss.COLOR_WHITE, "Content": "<PERF"}]
        self.lineDisplay["L4M"] = [{"Color": ss.COLOR_WHITE, "Content": "<TAKEOFF"}]
        self.lineDisplay["L5M"] = [{"Color": ss.COLOR_WHITE, "Content": "<APPROACH"}]
        self.lineDisplay["L6M"] = [{"Color": ss.COLOR_WHITE, "Content": "<OFFSET"}]
        self.lineDisplay["L7M"] = [{"Color": ss.COLOR_WHITE, "Content": self.inputLine[-1]}]

        self.lineDisplay["R1M"] = [{"Color": ss.COLOR_WHITE, "Content": "NAV DATA>"}]
        self.lineDisplay["R2M"] = [{"Color": ss.COLOR_WEAK_WHITE, "Content": "MSG RECALL>"}]
        self.lineDisplay["R3M"] = [{"Color": ss.COLOR_WHITE, "Content": "ALTN DEST>"}]
        self.lineDisplay["R4M"] = [{"Color": ss.COLOR_WHITE, "Content": ""}]
        self.lineDisplay["R5M"] = [{"Color": ss.COLOR_WHITE, "Content": "SEL CONFIG>"}]
        self.lineDisplay["R6M"] = [{"Color": ss.COLOR_WHITE, "Content": "MAINT>"}]
        pass
    # Ident 页面
    elif self.currentPage == ss.pageIndex.IDENT:
        self.lineDisplay["L0M"] = [{"Color": ss.COLOR_WHITE, "Content": " "*10+"IDENT"}]
        self.lineDisplay["L1M"] = [{"Color": ss.COLOR_WHITE, "Content": self.dataFile.Interface_DATA_KEYWORDS(ss.variable.IDENT_MODEL)}]
        self.lineDisplay["L2M"] = [{"Color": ss.COLOR_WHITE, "Content": self.dataFile.Interface_DATA_KEYWORDS(ss.variable.IDENT_NAV_DATA_RELEASE)}]
        self.lineDisplay["L4M"] = [{"Color": ss.COLOR_WHITE, "Content": "2.90.9961-RTM"}]
        self.lineDisplay["L6M"] = [{"Color": ss.COLOR_WHITE, "Content": "<INDEX"}]
        self.lineDisplay["L7M"] = [{"Color": ss.COLOR_WHITE, "Content": self.inputLine[-1]}]

        self.lineDisplay["R1M"] = [{"Color": ss.COLOR_WHITE, "Content": self.dataFile.Interface_DATA_KEYWORDS(ss.variable.IDENT_ENG_RATING)}]
        self.lineDisplay["R2M"] = [{"Color": ss.COLOR_WHITE, "Content": self.dataFile.Interface_DATA_KEYWORDS(ss.variable.IDENT_NAV_ACTIVE)}]
        self.lineDisplay["R6M"] = [{"Color": ss.COLOR_WHITE, "Content": "POS INIT>"}]

        self.lineDisplay["L1S"] = [{"Color": ss.COLOR_WHITE, "Content": " MODEL"}]
        self.lineDisplay["L2S"] = [{"Color": ss.COLOR_WHITE, "Content": " NAV DATA"}]
        self.lineDisplay["L4S"] = [{"Color": ss.COLOR_WHITE, "Content": " OP PROGRAM"}]
        self.lineDisplay["R1S"] = [{"Color": ss.COLOR_WHITE, "Content": "ENG RATING"}]
        self.lineDisplay["R2S"] = [{"Color": ss.COLOR_WHITE, "Content": "ACTIVE"}]
        self.lineDisplay["R5S"] = [{"Color": ss.COLOR_WHITE, "Content": "SUPP DATA"}]
        self.lineDisplay["L6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 24}]
        pass
    # POS INIT 页面
    elif self.currentPage == ss.pageIndex.POS:
        # 检查页码并作规范
        if self.currentPageIndex < 1:
            self.currentPageIndex = 3
        elif self.currentPageIndex > 3:
            self.currentPageIndex = 1
            pass
        # POS第一页
        if self.currentPageIndex == 1:
            # Draw the screen title
            self.lineDisplay["L0M"] = [{"Color": ss.COLOR_WHITE, "Content": " " * 8 + "POS INIT"}]
            self.lineDisplay["R0S"] = [{"Color": ss.COLOR_WHITE, "Content": "1/3 "}]
            # self.lineDisplay["L1M",[{"Color": ss.COLOR_WHITE, "Content": "<INDENT"}]
            self.lineDisplay["L2M"] = [{"Color": ss.COLOR_WHITE, "Content": "----"}]
            self.lineDisplay["L3M"] = [{"Color": ss.COLOR_WHITE, "Content": "----"}]
            # self.lineDisplay["L4M"] = [{"Color": ss.COLOR_WHITE, "Content": "<TAKEOFF"}]
            self.lineDisplay["L5M"] = [{"Color": ss.COLOR_WHITE, "Content": self.dataFile.Interface_DATA_KEYWORDS("GMT-MON/DY")}]
            self.lineDisplay["L6M"] = [{"Color": ss.COLOR_WHITE, "Content": "<INDEX"}]
            self.lineDisplay["L7M"] = [{"Color": ss.COLOR_WHITE, "Content": self.inputLine[-1]}]

            self.lineDisplay["R1M"] =  [{"Color": ss.COLOR_WHITE, "Content": self.dataFile.Interface_DATA_KEYWORDS("LAST POS")}]
            # self.lineDisplay["R2M"] = [{"Color": ss.COLOR_WEAK_WHITE, "Content": "MSG RECALL>"}]
            # self.lineDisplay["R3M"] = [{"Color": ss.COLOR_WHITE, "Content": "ALTN DEST>"}]
            # self.lineDisplay["R4M"] = [{"Color": ss.COLOR_WHITE, "Content": ""}]
            # self.lineDisplay["R5M"] = [{"Color": ss.COLOR_WHITE, "Content": "SEL CONFIG>"}]
            self.lineDisplay["R6M"] = [{"Color": ss.COLOR_WHITE, "Content": "ROUTE>"}]

            self.lineDisplay["L2S"] = [{"Color": ss.COLOR_WHITE, "Content": " REF AIRPORT"}]
            self.lineDisplay["L3S"] = [{"Color": ss.COLOR_WHITE, "Content": " GATE"}]
            self.lineDisplay["L5S"] = [{"Color": ss.COLOR_WHITE, "Content": "GMT-MON/DY"}]
            self.lineDisplay["L6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 24}]
            self.lineDisplay["R1S"] = [{"Color": ss.COLOR_WHITE, "Content": "LAST POS"}]
            pass
        # POS第二页
        elif self.currentPageIndex == 2:
            # Draw the screen title
            self.lineDisplay["L0M"] = [{"Color": ss.COLOR_WHITE, "Content": " " * 9 + "POS REF"}]
            self.lineDisplay["R0S"] = [{"Color": ss.COLOR_WHITE, "Content": "2/3 "}]
            self.lineDisplay["L1M"] = [{"Color": ss.COLOR_WHITE, "Content": self.dataFile.Interface_DATA_KEYWORDS("FMC POS")}]
            self.lineDisplay["L2M"] = [{"Color": ss.COLOR_WHITE, "Content": self.dataFile.Interface_DATA_KEYWORDS("IRS L")}]
            self.lineDisplay["L3M"] = [{"Color": ss.COLOR_WHITE, "Content": self.dataFile.Interface_DATA_KEYWORDS("IRS R")}]
            self.lineDisplay["L4M"] = [{"Color": ss.COLOR_WHITE, "Content": self.dataFile.Interface_DATA_KEYWORDS("GPS L")}]
            self.lineDisplay["L5M"] = [{"Color": ss.COLOR_WHITE, "Content": self.dataFile.Interface_DATA_KEYWORDS("GPS R")}]
            # self.lineDisplay["L6M"] = [{"Color": ss.COLOR_WHITE, "Content": "<INDEX"}]
            self.lineDisplay["L7M"] = [{"Color": ss.COLOR_WHITE, "Content": self.inputLine[-1]}]

            self.lineDisplay["R1M"] = [{"Color": ss.COLOR_WHITE, "Content": "??"}]
            self.lineDisplay["R2M"] = [{"Color": ss.COLOR_WHITE, "Content": "??"}]
            self.lineDisplay["R3M"] = [{"Color": ss.COLOR_WHITE, "Content": "??"}]
            # self.lineDisplay["R4M"] = [{"Color": ss.COLOR_WHITE, "Content": ""}]
            # self.lineDisplay["R5M"] = [{"Color": ss.COLOR_WHITE, "Content": "SEL CONFIG>"}]
            # self.lineDisplay["R6M"] = [{"Color": ss.COLOR_WHITE, "Content": "ROUTE>"}]

            self.lineDisplay["L1S"] = [{"Color": ss.COLOR_WHITE, "Content": " FMC POS"}]
            self.lineDisplay["L2S"] = [{"Color": ss.COLOR_WHITE, "Content": " IRS L"}]
            self.lineDisplay["L3S"] = [{"Color": ss.COLOR_WHITE, "Content": " IRS R"}]
            self.lineDisplay["L4S"] = [{"Color": ss.COLOR_WHITE, "Content": " GPS L"}]
            self.lineDisplay["L5S"] = [{"Color": ss.COLOR_WHITE, "Content": " GPS R"}]
            self.lineDisplay["L6S"] = [{"Color": ss.COLOR_WHITE, "Content": " RADIO"}]
            self.lineDisplay["R1S"] = [{"Color": ss.COLOR_WHITE, "Content": "GS"}]
            pass
        # POS第三页
        elif self.currentPageIndex == 3:
            # Draw the screen title
            self.lineDisplay["L0M"] = [{"Color": ss.COLOR_WHITE, "Content": " " * 8 + "POS SHIFT"}]
            self.lineDisplay["R0S"] = [{"Color": ss.COLOR_WHITE, "Content": "3/3 "}]
            self.lineDisplay["L1M"] = [{"Color": ss.COLOR_WHITE, "Content": "??"}]
            self.lineDisplay["L2M"] = [{"Color": ss.COLOR_WHITE, "Content": "??"}]
            self.lineDisplay["L3M"] = [{"Color": ss.COLOR_WHITE, "Content": "??"}]
            self.lineDisplay["L4M"] = [{"Color": ss.COLOR_WHITE, "Content": "??"}]
            # self.lineDisplay["L5M"] = [{"Color": ss.COLOR_WHITE, "Content": self.dataFile.Interface_DATA_KEYWORDS("GPS R")}]
            self.lineDisplay["L6M"] = [{"Color": ss.COLOR_WHITE, "Content": "<INDEX"}]
            self.lineDisplay["L7M"] = [{"Color": ss.COLOR_WHITE, "Content": self.inputLine[-1]}]

            self.lineDisplay["R1M"] = [{"Color": ss.COLOR_WHITE, "Content": "??"}]
            self.lineDisplay["R2M"] = [{"Color": ss.COLOR_WHITE, "Content": "??"}]
            self.lineDisplay["R3M"] = [{"Color": ss.COLOR_WHITE, "Content": "??"}]
            # self.lineDisplay["R4M"] = [{"Color": ss.COLOR_WHITE, "Content": ""}]
            self.lineDisplay["R5M"] = [{"Color": ss.COLOR_WHITE, "Content": "NAV STATUS>"}]
            # self.lineDisplay["R6M"] = [{"Color": ss.COLOR_WHITE, "Content": "ROUTE>"}]

            self.lineDisplay["L1S"] = [{"Color": ss.COLOR_WHITE, "Content": "FMC-L"}]
            self.lineDisplay["L2S"] = [{"Color": ss.COLOR_WHITE, "Content": "GPS-L"}]
            self.lineDisplay["L3S"] = [{"Color": ss.COLOR_WHITE, "Content": "IRS-L"}]
            self.lineDisplay["L4S"] = [{"Color": ss.COLOR_WHITE, "Content": "RNP/ACTUAL"}]
            self.lineDisplay["L5S"] = [{"Color": ss.COLOR_WHITE, "Content": "-"*24}]
            # self.lineDisplay["L6S"] = [{"Color": ss.COLOR_WHITE, "Content": " RADIO"}]
            self.lineDisplay["R1S"] = [{"Color": ss.COLOR_WHITE, "Content": "FMC-R"}]
            self.lineDisplay["R2S"] = [{"Color": ss.COLOR_WHITE, "Content": "GPS-R"}]
            self.lineDisplay["R3S"] = [{"Color": ss.COLOR_WHITE, "Content": "IRS-R"}]
            self.lineDisplay["R4S"] = [{"Color": ss.COLOR_WHITE, "Content": "RADIO"}]
            pass
        pass
    # PERF INIT 页面
    elif self.currentPage == ss.pageIndex.PERF:
        # 检查页码并作规范
        if self.currentPageIndex < 1:
            self.currentPageIndex = 2
        elif self.currentPageIndex > 2:
            self.currentPageIndex = 1
            pass
        # PERF 第一页
        if self.currentPageIndex == 1:
            # Draw the screen title
            self.lineDisplay["L0M"] = [{"Color": ss.COLOR_WHITE, "Content": " " * 6 + "PERF INIT"}]
            self.lineDisplay["R0S"] = [{"Color": ss.COLOR_WHITE, "Content": "1/2 "}]
            self.lineDisplay["L1M"] = [{"Color": ss.COLOR_WHITE, "Content": GW_CRZ_CG(self)}]
            self.lineDisplay["L2M"] = [{"Color": ss.COLOR_WHITE, "Content": "---.-/"+self.dataFile.Interface_DATA_KEYWORDS("FUEL")}]
            self.lineDisplay["L3M"] = [{"Color": ss.COLOR_WHITE, "Content": Zero_Fuel_Weight(self)}]
            self.lineDisplay["L4M"] = [{"Color": ss.COLOR_WHITE, "Content": "**.*"}]
            self.lineDisplay["L5M"] = [{"Color": ss.COLOR_WHITE, "Content": COST_INDEX(self)}]
            self.lineDisplay["L6M"] = [{"Color": ss.COLOR_WHITE, "Content": "<INDEX"}]
            self.lineDisplay["L7M"] = [{"Color": ss.COLOR_WHITE, "Content": self.inputLine[-1]}]

            self.lineDisplay["R1M"] = [{"Color": ss.COLOR_WHITE, "Content": "/*****"}]
            self.lineDisplay["R2M"] = [{"Color": ss.COLOR_WHITE, "Content": "---°/---"}]
            self.lineDisplay["R3M"] = [{"Color": ss.COLOR_WHITE, "Content": "---°F ---°C"}]
            self.lineDisplay["R4M"] = [{"Color": ss.COLOR_WHITE, "Content": "18000"}]
            self.lineDisplay["R5M"] = [{"Color": ss.COLOR_WHITE, "Content": "REQUEST>"}]
            self.lineDisplay["R6M"] = [{"Color": ss.COLOR_WHITE, "Content": "N1 LIMIT>"}]

            self.lineDisplay["L1S"] = [{"Color": ss.COLOR_WHITE, "Content": " GW/CRZ CG"}]
            self.lineDisplay["L2S"] = [{"Color": ss.COLOR_WHITE, "Content": " PLAN/FUEL"}]
            self.lineDisplay["L3S"] = [{"Color": ss.COLOR_WHITE, "Content": " ZFW"}]
            self.lineDisplay["L4S"] = [{"Color": ss.COLOR_WHITE, "Content": " RESERVES"}]
            self.lineDisplay["L5S"] = [{"Color": ss.COLOR_WHITE, "Content": " COST INDEX"}]
            self.lineDisplay["L6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-"*24}]

            self.lineDisplay["R1S"] = [{"Color": ss.COLOR_WHITE, "Content": "TRIP/CRZ ALT"}]
            self.lineDisplay["R2S"] = [{"Color": ss.COLOR_WHITE, "Content": "CRZ WIND"}]
            self.lineDisplay["R3S"] = [{"Color": ss.COLOR_WHITE, "Content": "T/C OAT"}]
            self.lineDisplay["R4S"] = [{"Color": ss.COLOR_WHITE, "Content": "TRANS ALT"}]
            self.lineDisplay["R5S"] = [{"Color": ss.COLOR_WHITE, "Content": "PERF INIT"}]
            # self.lineDisplay["R6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 24}]
            pass
        # POS第二页
        elif self.currentPageIndex == 2:
            # Draw the screen title
            self.lineDisplay["L0M"] = [{"Color": ss.COLOR_WHITE, "Content": " " * 6 + "PERF LIMITS"}]
            self.lineDisplay["R0S"] = [{"Color": ss.COLOR_WHITE, "Content": "2/2 "}]
            self.lineDisplay["L1M"] = [{"Color": ss.COLOR_WHITE, "Font":ss.FONT_CDU_TITLE_SMALL, "Content": "  30 SEC AT RTA WPT"}]
            self.lineDisplay["L2M"] = [{"Color": ss.COLOR_WHITE, "Font":ss.FONT_CDU_TITLE_SMALL, "Content": "100/.400"}]
            self.lineDisplay["L3M"] = [{"Color": ss.COLOR_WHITE, "Font":ss.FONT_CDU_TITLE_SMALL, "Content": "100/.400"}]
            self.lineDisplay["L4M"] = [{"Color": ss.COLOR_WHITE, "Font":ss.FONT_CDU_TITLE_SMALL, "Content": "100/.400"}]
            # self.lineDisplay["L5M"] = [{"Color": ss.COLOR_WHITE, "Content": "***"}]
            self.lineDisplay["L6M"] = [{"Color": ss.COLOR_WHITE, "Content": "<INDEX"}]
            self.lineDisplay["L7M"] = [{"Color": ss.COLOR_WHITE, "Content": self.inputLine[-1]}]

            # self.lineDisplay["R1M"] = [{"Color": ss.COLOR_WHITE, "Content": "/*****"}]
            self.lineDisplay["R2M"] = [{"Color": ss.COLOR_WHITE, "Font":ss.FONT_CDU_TITLE_SMALL, "Content": "340/.820"}]
            self.lineDisplay["R3M"] = [{"Color": ss.COLOR_WHITE, "Font":ss.FONT_CDU_TITLE_SMALL, "Content": "340/.820"}]
            self.lineDisplay["R4M"] = [{"Color": ss.COLOR_WHITE, "Font":ss.FONT_CDU_TITLE_SMALL, "Content": "340/.820"}]
            # self.lineDisplay["R5M"] = [{"Color": ss.COLOR_WHITE, "Content": "REQUEST>"}]
            self.lineDisplay["R6M"] = [{"Color": ss.COLOR_WHITE, "Content": "RTA>"}]

            self.lineDisplay["L1S"] = [{"Color": ss.COLOR_WHITE, "Content": " TIME ERROR TOLERANCE"}]
            self.lineDisplay["L2S"] = [{"Color": ss.COLOR_WHITE, "Content": " MIN SPD --CLB-- MAX SPD"}]
            self.lineDisplay["L3S"] = [{"Color": ss.COLOR_WHITE, "Content": "         --CRZ--"}]
            self.lineDisplay["L4S"] = [{"Color": ss.COLOR_WHITE, "Content": "         --DES--"}]
            # self.lineDisplay["L5S"] = [{"Color": ss.COLOR_WHITE, "Content": "COST INDEX"}]
            self.lineDisplay["L6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 24}]

            # self.lineDisplay["R1S"] = [{"Color": ss.COLOR_WHITE, "Content": "TRIP/CRZ ALT"}]
            # self.lineDisplay["R2S"] = [{"Color": ss.COLOR_WHITE, "Content": "CRZ WIND"}]
            # self.lineDisplay["R3S"] = [{"Color": ss.COLOR_WHITE, "Content": "T/C OAT"}]
            # self.lineDisplay["R4S"] = [{"Color": ss.COLOR_WHITE, "Content": "TRANS ALT"}]
            # self.lineDisplay["R5S"] = [{"Color": ss.COLOR_WHITE, "Content": "PERF INIT"}]
            # self.lineDisplay["R6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 24}]
            pass
    # TAKE OFF 页面
    elif self.currentPage == ss.pageIndex.TAKEOFF:
        # 检查页码并作规范
        if self.currentPageIndex < 1:
            self.currentPageIndex = 2
        elif self.currentPageIndex > 2:
            self.currentPageIndex = 1
            pass
        # Take Off第一页
        if self.currentPageIndex == 1:
            # Draw the screen title
            self.lineDisplay["L0M"] = [{"Color": ss.COLOR_WHITE, "Content": " " * 7 + "TAKEOFF REF"}]
            self.lineDisplay["R0S"] = [{"Color": ss.COLOR_WHITE, "Content": "1/2 "}]
            self.lineDisplay["L1M"] = [{"Color": ss.COLOR_WHITE, "Content": "**°"}]
            self.lineDisplay["L2M"] = [{"Color": ss.COLOR_WHITE, "Content": "100.7/100.7"}]
            self.lineDisplay["L3M"] = [{"Color": ss.COLOR_WHITE, "Content": "--。-%"}]
            # self.lineDisplay["L4M"] = [{"Color": ss.COLOR_WHITE, "Content": "**.*"}]
            # self.lineDisplay["L5M"] = [{"Color": ss.COLOR_WHITE, "Content": "***"}]
            self.lineDisplay["L6M"] = [{"Color": ss.COLOR_WHITE, "Content": "<PERF INIT"}]
            self.lineDisplay["L7M"] = [{"Color": ss.COLOR_WHITE, "Content": self.inputLine[-1]}]

            self.lineDisplay["R1M"] = [{"Color": ss.COLOR_WHITE, "Content": "---"}]
            self.lineDisplay["R2M"] = [{"Color": ss.COLOR_WHITE, "Content": "---"}]
            self.lineDisplay["R3M"] = [{"Color": ss.COLOR_WHITE, "Content": "---"}]
            # self.lineDisplay["R4M"] = [{"Color": ss.COLOR_WHITE, "Content": "18000"}]
            # self.lineDisplay["R5M"] = [{"Color": ss.COLOR_WHITE, "Content": "REQUEST>"}]
            self.lineDisplay["R6M"] = [{"Color": ss.COLOR_WHITE, "Content": "QRH OFF>"}]

            self.lineDisplay["L1S"] = [{"Color": ss.COLOR_WHITE, "Content": " FLAPS"}]
            self.lineDisplay["L2S"] = [{"Color": ss.COLOR_WHITE, "Content": " 27K N1"}]
            self.lineDisplay["L3S"] = [{"Color": ss.COLOR_WHITE, "Content": " CG    TRIM"}]
            # self.lineDisplay["L4S"] = [{"Color": ss.COLOR_WHITE, "Content": " RESERVES"}]
            self.lineDisplay["L5S"] = [{"Color": ss.COLOR_WHITE, "Content": "RUNWAY"}]
            self.lineDisplay["L6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 18 + "SELECT"}]

            self.lineDisplay["R1S"] = [{"Color": ss.COLOR_WHITE, "Content": "QRH  V1"}]
            self.lineDisplay["R2S"] = [{"Color": ss.COLOR_WHITE, "Content": "VR"}]
            self.lineDisplay["R3S"] = [{"Color": ss.COLOR_WHITE, "Content": "V2"}]
            self.lineDisplay["R4S"] = [{"Color": ss.COLOR_WHITE, "Content": "GW  / TOW"}]
            self.lineDisplay["R5S"] = [{"Color": ss.COLOR_WHITE, "Content": "RWY REMAIN"}]
            # self.lineDisplay["R6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 24}]
            pass
        # TAKE OFF 第二页
        elif self.currentPageIndex == 2:
            # Draw the screen title
            self.lineDisplay["L0M"] = [{"Color": ss.COLOR_WHITE, "Content": " " * 7 + "TAKEOFF REF"}]
            self.lineDisplay["R0S"] = [{"Color": ss.COLOR_WHITE, "Content": "2/2 "}]
            self.lineDisplay["L1M"] = [{"Color": ss.COLOR_WHITE, "Content": "---°/---"}]
            self.lineDisplay["L2M"] = [{"Color": ss.COLOR_WHITE, "Content": "--.-%/"}]
            # self.lineDisplay["L3M"] = [{"Color": ss.COLOR_WHITE, "Content": "100/.400"}]
            self.lineDisplay["L4M"] = [{"Color": ss.COLOR_WHITE, "Font":ss.FONT_CDU_TITLE_SMALL,"Content": "1500AGL"}]
            self.lineDisplay["L5M"] = [{"Color": ss.COLOR_WHITE, "Font":ss.FONT_CDU_TITLE_SMALL,"Content": "1500AGL"}]
            self.lineDisplay["L6M"] = [{"Color": ss.COLOR_WHITE, "Content": "<PERF INIT"}]
            self.lineDisplay["L7M"] = [{"Color": ss.COLOR_WHITE, "Content": self.inputLine[-1]}]

            self.lineDisplay["R1M"] = [{"Color": ss.COLOR_GREEN, "Content": "DRY"},{"Color": ss.COLOR_WHITE, "Content": "/WET/SK-R>"}]
            self.lineDisplay["R2M"] = [{"Color": ss.COLOR_WHITE, "Content": "----/"},{"Color": ss.COLOR_WHITE,"Font":ss.FONT_CDU_TITLE_SMALL, "Content": " +16°C"}]
            # self.lineDisplay["R3M"] = [{"Color": ss.COLOR_WHITE, "Content": "340/.820"}]
            self.lineDisplay["R4M"] = [{"Color": ss.COLOR_WHITE, "Font":ss.FONT_CDU_TITLE_SMALL,"Content": "800AGL"}]
            self.lineDisplay["R5M"] = [{"Color": ss.COLOR_WHITE, "Content": "CLB         "}]
            self.lineDisplay["R6M"] = [{"Color": ss.COLOR_WHITE, "Font":ss.FONT_CDU_TITLE_SMALL, "Content": "ON"},{"Color": ss.COLOR_WHITE, "Content": "/"},{"Color": ss.COLOR_GREEN, "Content": "OFF"}]

            self.lineDisplay["L1S"] = [{"Color": ss.COLOR_WHITE, "Content": " RW WIND"}]
            self.lineDisplay["L2S"] = [{"Color": ss.COLOR_WHITE, "Content": " RW SLOPE/HDG"}]
            # self.lineDisplay["L3S"] = [{"Color": ss.COLOR_WHITE, "Content": "         --CRZ--"}]
            self.lineDisplay["L4S"] = [{"Color": ss.COLOR_WHITE, "Content": " ACCEL HT"}]
            self.lineDisplay["L5S"] = [{"Color": ss.COLOR_WHITE, "Content": "REDUCTION"}]
            self.lineDisplay["L6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 17 + "CUTBACK"}]

            self.lineDisplay["R1S"] = [{"Color": ss.COLOR_WHITE, "Content": "RW COND"}]
            self.lineDisplay["R2S"] = [{"Color": ss.COLOR_WHITE, "Content": "SEL/OAT"}]
            # self.lineDisplay["R3S"] = [{"Color": ss.COLOR_WHITE, "Content": "T/C OAT"}]
            self.lineDisplay["R4S"] = [{"Color": ss.COLOR_WHITE, "Content": "EO ACCEL HT"}]
            self.lineDisplay["R5S"] = [{"Color": ss.COLOR_WHITE, "Content": "THR         "}]
            # self.lineDisplay["R6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 24}]
            pass
        pass
    # Approach 页面
    elif self.currentPage == ss.pageIndex.APPROACH:
        # 检查页码并作规范
        if self.currentPageIndex < 1:
            self.currentPageIndex = 1
        elif self.currentPageIndex > 1:
            self.currentPageIndex = 1
            pass
        # Approach第一页
        if self.currentPageIndex == 1:
            # Draw the screen title
            self.lineDisplay["L0M"] = [{"Color": ss.COLOR_WHITE, "Content": " " * 6 + "APPROACH REF"}]
            self.lineDisplay["R0S"] = [{"Color": ss.COLOR_WHITE, "Content": "1/1 "}]
            self.lineDisplay["L1M"] = [{"Color": ss.COLOR_WHITE, "Content": "***.*"}]
            # self.lineDisplay["L2M"] = [{"Color": ss.COLOR_WHITE, "Content": "100.7/100.7"}]
            # self.lineDisplay["L3M"] = [{"Color": ss.COLOR_WHITE, "Content": "--。-%"}]
            # self.lineDisplay["L4M"] = [{"Color": ss.COLOR_WHITE, "Content": "**.*"}]
            # self.lineDisplay["L5M"] = [{"Color": ss.COLOR_WHITE, "Content": "***"}]
            self.lineDisplay["L6M"] = [{"Color": ss.COLOR_WHITE, "Content": "<INDEX"}]
            self.lineDisplay["L7M"] = [{"Color": ss.COLOR_WHITE, "Content": self.inputLine[-1]}]

            self.lineDisplay["R1M"] = [{"Color": ss.COLOR_WHITE, "Content": "15°     "},{"Color": ss.COLOR_WHITE, "Font":ss.FONT_CDU_TITLE_SMALL,"Content": "KT"}]
            self.lineDisplay["R2M"] = [{"Color": ss.COLOR_WHITE, "Content": "30°     "},{"Color": ss.COLOR_WHITE, "Font": ss.FONT_CDU_TITLE_SMALL, "Content": "KT"}]
            self.lineDisplay["R3M"] = [{"Color": ss.COLOR_WHITE, "Content": "45°     "},{"Color": ss.COLOR_WHITE, "Font": ss.FONT_CDU_TITLE_SMALL, "Content": "KT"}]
            self.lineDisplay["R4M"] = [{"Color": ss.COLOR_WHITE, "Content": "--/---"}]
            self.lineDisplay["R5M"] = [{"Color": ss.COLOR_WHITE, "Font":ss.FONT_CDU_TITLE_SMALL,"Content": "+05KT"}]
            self.lineDisplay["R6M"] = [{"Color": ss.COLOR_WHITE, "Content": "ALTN DEST>"}]

            self.lineDisplay["L1S"] = [{"Color": ss.COLOR_WHITE, "Content": " GROSS WT"}]
            # self.lineDisplay["L2S"] = [{"Color": ss.COLOR_WHITE, "Content": " 27K N1"}]
            # self.lineDisplay["L3S"] = [{"Color": ss.COLOR_WHITE, "Content": " CG    TRIM"}]
            # self.lineDisplay["L4S"] = [{"Color": ss.COLOR_WHITE, "Content": " RESERVES"}]
            # self.lineDisplay["L5S"] = [{"Color": ss.COLOR_WHITE, "Content": "RUNWAY"}]
            self.lineDisplay["L6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 24}]

            self.lineDisplay["R1S"] = [{"Color": ss.COLOR_WHITE, "Content": "FLAPS  VERF"}]
            # self.lineDisplay["R2S"] = [{"Color": ss.COLOR_WHITE, "Content": "VR"}]
            # self.lineDisplay["R3S"] = [{"Color": ss.COLOR_WHITE, "Content": "V2"}]
            self.lineDisplay["R4S"] = [{"Color": ss.COLOR_WHITE, "Content": "FLAP/SPD"}]
            self.lineDisplay["R5S"] = [{"Color": ss.COLOR_WHITE, "Content": "WIND COR"}]
            # self.lineDisplay["R6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 24}]
            pass
        pass
    # Offset 页面
    elif self.currentPage == ss.pageIndex.OFFSET:
        # 检查页码并作规范
        if self.currentPageIndex < 1:
            self.currentPageIndex = 1
        elif self.currentPageIndex > 1:
            self.currentPageIndex = 1
            pass
        # Offset第一页
        if self.currentPageIndex == 1:
            # Draw the screen title
            self.lineDisplay["L0M"] = [{"Color": ss.COLOR_WHITE, "Content": " " * 5 + "LATERAL OFFSET"}]
            self.lineDisplay["R0S"] = [{"Color": ss.COLOR_WHITE, "Content": "1/1 "}]
            # self.lineDisplay["L1M"] = [{"Color": ss.COLOR_WHITE, "Content": "***.*"}]
            # self.lineDisplay["L2M"] = [{"Color": ss.COLOR_WHITE, "Content": "100.7/100.7"}]
            # self.lineDisplay["L3M"] = [{"Color": ss.COLOR_WHITE, "Content": "--。-%"}]
            # self.lineDisplay["L4M"] = [{"Color": ss.COLOR_WHITE, "Content": "**.*"}]
            # self.lineDisplay["L5M"] = [{"Color": ss.COLOR_WHITE, "Content": "***"}]
            # self.lineDisplay["L6M"] = [{"Color": ss.COLOR_WHITE, "Content": "<INDEX"}]
            self.lineDisplay["L7M"] = [{"Color": ss.COLOR_WHITE, "Content": self.inputLine[-1]}]

            # self.lineDisplay["R1M"] = [{"Color": ss.COLOR_WHITE, "Content": "15°     "},{"Color": ss.COLOR_WHITE, "Font": ss.FONT_CDU_TITLE_SMALL, "Content": "KT"}]
            # self.lineDisplay["R2M"] = [{"Color": ss.COLOR_WHITE, "Content": "30°     "},{"Color": ss.COLOR_WHITE, "Font": ss.FONT_CDU_TITLE_SMALL, "Content": "KT"}]
            # self.lineDisplay["R3M"] = [{"Color": ss.COLOR_WHITE, "Content": "45°     "},{"Color": ss.COLOR_WHITE, "Font": ss.FONT_CDU_TITLE_SMALL, "Content": "KT"}]
            # self.lineDisplay["R4M"] = [{"Color": ss.COLOR_WHITE, "Content": "--/---"}]
            # self.lineDisplay["R5M"] = [{"Color": ss.COLOR_WHITE, "Font": ss.FONT_CDU_TITLE_SMALL, "Content": "+05KT"}]
            # self.lineDisplay["R6M"] = [{"Color": ss.COLOR_WHITE, "Content": "ALTN DEST>"}]

            # self.lineDisplay["L1S"] = [{"Color": ss.COLOR_WHITE, "Content": " GROSS WT"}]
            self.lineDisplay["L2S"] = [{"Color": ss.COLOR_WHITE, "Content": " OFFSET DIST"}]
            # self.lineDisplay["L3S"] = [{"Color": ss.COLOR_WHITE, "Content": " CG    TRIM"}]
            # self.lineDisplay["L4S"] = [{"Color": ss.COLOR_WHITE, "Content": " RESERVES"}]
            # self.lineDisplay["L5S"] = [{"Color": ss.COLOR_WHITE, "Content": "RUNWAY"}]
            # self.lineDisplay["L6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 24}]

            # self.lineDisplay["R1S"] = [{"Color": ss.COLOR_WHITE, "Content": "FLAPS  VERF"}]
            # self.lineDisplay["R2S"] = [{"Color": ss.COLOR_WHITE, "Content": "VR"}]
            # self.lineDisplay["R3S"] = [{"Color": ss.COLOR_WHITE, "Content": "V2"}]
            # self.lineDisplay["R4S"] = [{"Color": ss.COLOR_WHITE, "Content": "FLAP/SPD"}]
            # self.lineDisplay["R5S"] = [{"Color": ss.COLOR_WHITE, "Content": "WIND COR"}]
            # self.lineDisplay["R6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 24}]
            pass
        pass
    # Route 页面
    elif self.currentPage == ss.pageIndex.ROUTE:
        # 检查页码并作规范
        if self.currentPageIndex < 1:
            self.currentPageIndex = 2
        elif self.currentPageIndex > 2:
            self.currentPageIndex = 1
            pass
        # Offset第一页
        if self.currentPageIndex == 1:
            # Draw the screen title
            self.lineDisplay["L0M"] = [{"Color": ss.COLOR_CYAN, "Content": " " * 6 + "RTE"}]
            self.lineDisplay["R0S"] = [{"Color": ss.COLOR_WHITE, "Content": "1/2 "}]
            self.lineDisplay["L1M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----"}]
            self.lineDisplay["L2M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----"}]
            self.lineDisplay["L3M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----"}]
            # self.lineDisplay["L4M"] = [{"Color": ss.COLOR_WHITE, "Content": "**.*"}]
            # self.lineDisplay["L5M"] = [{"Color": ss.COLOR_WHITE, "Content": "***"}]
            # self.lineDisplay["L6M"] = [{"Color": ss.COLOR_WHITE, "Content": "<INDEX"}]
            self.lineDisplay["L7M"] = [{"Color": ss.COLOR_WHITE, "Content": self.inputLine[-1]}]

            self.lineDisplay["R1M"] = [{"Color": ss.COLOR_WHITE, "Content": "*****"}]
            self.lineDisplay["R2M"] = [{"Color": ss.COLOR_WHITE, "Content": "--------"}]
            self.lineDisplay["R3M"] = [{"Color": ss.COLOR_WHITE, "Content": "REQUEST>"}]
            # self.lineDisplay["R4M"] = [{"Color": ss.COLOR_WHITE, "Content": "--/---"}]
            # self.lineDisplay["R5M"] = [{"Color": ss.COLOR_WHITE, "Font": ss.FONT_CDU_TITLE_SMALL, "Content": "+05KT"}]
            # self.lineDisplay["R6M"] = [{"Color": ss.COLOR_WHITE, "Content": "ALTN DEST>"}]

            self.lineDisplay["L1S"] = [{"Color": ss.COLOR_WHITE, "Content": " ORIGIN"}]
            self.lineDisplay["L2S"] = [{"Color": ss.COLOR_WHITE, "Content": " CO ROUTE"}]
            self.lineDisplay["L3S"] = [{"Color": ss.COLOR_WHITE, "Content": " RUNWAY"}]
            self.lineDisplay["L4S"] = [{"Color": ss.COLOR_WHITE, "Content": "-"*24}]
            # self.lineDisplay["L5S"] = [{"Color": ss.COLOR_WHITE, "Content": "RUNWAY"}]
            # self.lineDisplay["L6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 24}]

            self.lineDisplay["R1S"] = [{"Color": ss.COLOR_WHITE, "Content": "DEST"}]
            self.lineDisplay["R2S"] = [{"Color": ss.COLOR_WHITE, "Content": "FLT NO."}]
            self.lineDisplay["R3S"] = [{"Color": ss.COLOR_WHITE, "Content": "FLT PLAN "}]
            # self.lineDisplay["R4S"] = [{"Color": ss.COLOR_WHITE, "Content": "FLAP/SPD"}]
            # self.lineDisplay["R5S"] = [{"Color": ss.COLOR_WHITE, "Content": "WIND COR"}]
            # self.lineDisplay["R6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 24}]
            pass
        # Offset 后续页
        else:
            # Draw the screen title
            self.lineDisplay["L0M"] = [{"Color": ss.COLOR_CYAN, "Content": " " * 6 + "RTE"}]
            self.lineDisplay["R0S"] = [{"Color": ss.COLOR_WHITE, "Content": "2/2 "}]
            self.lineDisplay["L1M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----"}]
            # self.lineDisplay["L2M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----"}]
            # self.lineDisplay["L3M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----"}]
            # self.lineDisplay["L4M"] = [{"Color": ss.COLOR_WHITE, "Content": "**.*"}]
            # self.lineDisplay["L5M"] = [{"Color": ss.COLOR_WHITE, "Content": "***"}]
            # self.lineDisplay["L6M"] = [{"Color": ss.COLOR_WHITE, "Content": "<INDEX"}]
            self.lineDisplay["L7M"] = [{"Color": ss.COLOR_WHITE, "Content": self.inputLine[-1]}]

            self.lineDisplay["R1M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----"}]
            # self.lineDisplay["R2M"] = [{"Color": ss.COLOR_WHITE, "Content": "--------"}]
            # self.lineDisplay["R3M"] = [{"Color": ss.COLOR_WHITE, "Content": "REQUEST>"}]
            # self.lineDisplay["R4M"] = [{"Color": ss.COLOR_WHITE, "Content": "--/---"}]
            # self.lineDisplay["R5M"] = [{"Color": ss.COLOR_WHITE, "Font": ss.FONT_CDU_TITLE_SMALL, "Content": "+05KT"}]
            # self.lineDisplay["R6M"] = [{"Color": ss.COLOR_WHITE, "Content": "ALTN DEST>"}]

            self.lineDisplay["L1S"] = [{"Color": ss.COLOR_WHITE, "Content": " VIA"}]
            # self.lineDisplay["L2S"] = [{"Color": ss.COLOR_WHITE, "Content": " CO ROUTE"}]
            # self.lineDisplay["L3S"] = [{"Color": ss.COLOR_WHITE, "Content": " RUNWAY"}]
            # self.lineDisplay["L4S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 24}]
            # self.lineDisplay["L5S"] = [{"Color": ss.COLOR_WHITE, "Content": "RUNWAY"}]
            self.lineDisplay["L6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 24}]

            self.lineDisplay["R1S"] = [{"Color": ss.COLOR_WHITE, "Content": "TO"}]
            # self.lineDisplay["R2S"] = [{"Color": ss.COLOR_WHITE, "Content": "FLT NO."}]
            # self.lineDisplay["R3S"] = [{"Color": ss.COLOR_WHITE, "Content": "FLT PLAN "}]
            # self.lineDisplay["R4S"] = [{"Color": ss.COLOR_WHITE, "Content": "FLAP/SPD"}]
            # self.lineDisplay["R5S"] = [{"Color": ss.COLOR_WHITE, "Content": "WIND COR"}]
            # self.lineDisplay["R6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 24}]
            pass
        pass
    # CLB 页面
    elif self.currentPage == ss.pageIndex.CLB:
        # 检查页码并作规范
        if self.currentPageIndex < 1:
            self.currentPageIndex = 1
        elif self.currentPageIndex > 1:
            self.currentPageIndex = 1
            pass
        # CLB第一页
        if self.currentPageIndex == 1:
            # Draw the screen title
            self.lineDisplay["L0M"] = [{"Color": ss.COLOR_WHITE, "Content": " " * 6 + "ECON CLB"}]
            self.lineDisplay["R0S"] = [{"Color": ss.COLOR_WHITE, "Content": "1/1"}]
            self.lineDisplay["L1M"] = [{"Color": ss.COLOR_WHITE, "Content": "*****"}]
            # self.lineDisplay["L2M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----"}]
            self.lineDisplay["L3M"] = [{"Color": ss.COLOR_WHITE, "Content": "250/10000"}]
            # self.lineDisplay["L4M"] = [{"Color": ss.COLOR_WHITE, "Content": "**.*"}]
            self.lineDisplay["L5M"] = [{"Color": ss.COLOR_WHITE, "Content": "<MAX RATE"}]
            self.lineDisplay["L6M"] = [{"Color": ss.COLOR_WHITE, "Content": "<MAX ANGLE"}]
            self.lineDisplay["L7M"] = [{"Color": ss.COLOR_WHITE, "Content": self.inputLine[-1]}]

            # self.lineDisplay["R1M"] = [{"Color": ss.COLOR_WHITE, "Content": "*****"}]
            # self.lineDisplay["R2M"] = [{"Color": ss.COLOR_WHITE, "Content": "TO -----"}]
            # self.lineDisplay["R3M"] = [{"Color": ss.COLOR_WHITE, "Content": "REQUEST>"}]
            # self.lineDisplay["R4M"] = [{"Color": ss.COLOR_WHITE, "Content": "--/---"}]
            self.lineDisplay["R5M"] = [{"Color": ss.COLOR_WHITE, "Content": "ENG OUT>"}]
            self.lineDisplay["R6M"] = [{"Color": ss.COLOR_WHITE, "Content": "RTA>"}]

            self.lineDisplay["L1S"] = [{"Color": ss.COLOR_WHITE, "Content": " CRZ ALT"}]
            self.lineDisplay["L2S"] = [{"Color": ss.COLOR_WHITE, "Content": " TGT SPD"}]
            self.lineDisplay["L3S"] = [{"Color": ss.COLOR_WHITE, "Content": " SPD REST"}]
            # self.lineDisplay["L4S"] = [{"Color": ss.COLOR_WHITE, "Content": "-"*24}]
            # self.lineDisplay["L5S"] = [{"Color": ss.COLOR_WHITE, "Content": "RUNWAY"}]
            # self.lineDisplay["L6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 24}]

            # self.lineDisplay["R1S"] = [{"Color": ss.COLOR_WHITE, "Content": "DEST"}]
            self.lineDisplay["R2S"] = [{"Color": ss.COLOR_WHITE, "Content": "TO -----"}]
            # self.lineDisplay["R3S"] = [{"Color": ss.COLOR_WHITE, "Content": "FLT PLAN "}]
            self.lineDisplay["R4S"] = [{"Color": ss.COLOR_WHITE, "Content": "CLB N1"}]
            self.lineDisplay["R5S"] = [{"Color": ss.COLOR_WHITE, "Content": "------------"}]
            # self.lineDisplay["R6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 24}]
            pass
        pass
    # CRZ 页面
    elif self.currentPage == ss.pageIndex.CRZ:
        # 检查页码并作规范
        if self.currentPageIndex < 1:
            self.currentPageIndex = 1
        elif self.currentPageIndex > 1:
            self.currentPageIndex = 1
            pass
        # CRZ 第一页
        if self.currentPageIndex == 1:
            # Draw the screen title
            self.lineDisplay["L0M"] = [{"Color": ss.COLOR_WHITE, "Content": " " * 6 + "ECON CRZ"}]
            self.lineDisplay["R0S"] = [{"Color": ss.COLOR_WHITE, "Content": "1/1"}]
            self.lineDisplay["L1M"] = [{"Color": ss.COLOR_WHITE, "Content": "*****"}]
            # self.lineDisplay["L2M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----"}]
            # self.lineDisplay["L3M"] = [{"Color": ss.COLOR_WHITE, "Content": "250/10000"}]
            # self.lineDisplay["L4M"] = [{"Color": ss.COLOR_WHITE, "Content": "**.*"}]
            # self.lineDisplay["L5M"] = [{"Color": ss.COLOR_WHITE, "Content": "<MAX RATE"}]
            self.lineDisplay["L6M"] = [{"Color": ss.COLOR_WHITE, "Content": "<LRC"}]
            self.lineDisplay["L7M"] = [{"Color": ss.COLOR_WHITE, "Content": self.inputLine[-1]}]

            # self.lineDisplay["R1M"] = [{"Color": ss.COLOR_WHITE, "Content": "*****"}]
            # self.lineDisplay["R2M"] = [{"Color": ss.COLOR_WHITE, "Content": "TO -----"}]
            # self.lineDisplay["R3M"] = [{"Color": ss.COLOR_WHITE, "Content": "REQUEST>"}]
            # self.lineDisplay["R4M"] = [{"Color": ss.COLOR_WHITE, "Content": "--/---"}]
            self.lineDisplay["R5M"] = [{"Color": ss.COLOR_WHITE, "Content": "ENG OUT>"}]
            self.lineDisplay["R6M"] = [{"Color": ss.COLOR_WHITE, "Content": "RTA>"}]

            self.lineDisplay["L1S"] = [{"Color": ss.COLOR_WHITE, "Content": " CRZ ALT  OPT/MAX"}]
            self.lineDisplay["L2S"] = [{"Color": ss.COLOR_WHITE, "Content": " TGT SPD"}]
            self.lineDisplay["L3S"] = [{"Color": ss.COLOR_WHITE, "Content": " TURB N1"}]
            self.lineDisplay["L4S"] = [{"Color": ss.COLOR_WHITE, "Content": " FUEL AT"}]
            self.lineDisplay["L5S"] = [{"Color": ss.COLOR_WHITE, "Content": "-"*24}]
            # self.lineDisplay["L6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 24}]

            # self.lineDisplay["R1S"] = [{"Color": ss.COLOR_WHITE, "Content": "DEST"}]
            # self.lineDisplay["R2S"] = [{"Color": ss.COLOR_WHITE, "Content": "TO -----"}]
            self.lineDisplay["R3S"] = [{"Color": ss.COLOR_WHITE, "Content": "ACTUAL WIND"}]
            # self.lineDisplay["R4S"] = [{"Color": ss.COLOR_WHITE, "Content": "CLB N1"}]
            # self.lineDisplay["R5S"] = [{"Color": ss.COLOR_WHITE, "Content": "------------"}]
            # self.lineDisplay["R6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 24}]
            pass
        pass
    # DES 页面
    elif self.currentPage == ss.pageIndex.DES:
        # 检查页码并作规范
        if self.currentPageIndex < 1:
            self.currentPageIndex = 1
        elif self.currentPageIndex > 1:
            self.currentPageIndex = 1
            pass
        # DES 第一页
        if self.currentPageIndex == 1:
            # Draw the screen title
            self.lineDisplay["L0M"] = [{"Color": ss.COLOR_WHITE, "Content": " " * 6 + "DES"}]
            self.lineDisplay["R0S"] = [{"Color": ss.COLOR_WHITE, "Content": "1/1"}]
            # self.lineDisplay["L1M"] = [{"Color": ss.COLOR_WHITE, "Content": "*****"}]
            # self.lineDisplay["L2M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----"}]
            self.lineDisplay["L3M"] = [{"Color": ss.COLOR_WHITE, "Content": "240/10000"}]
            # self.lineDisplay["L4M"] = [{"Color": ss.COLOR_WHITE, "Content": "**.*"}]
            # self.lineDisplay["L5M"] = [{"Color": ss.COLOR_WHITE, "Content": "<MAX RATE"}]
            self.lineDisplay["L6M"] = [{"Color": ss.COLOR_WHITE, "Content": "<FORECAST"}]
            self.lineDisplay["L7M"] = [{"Color": ss.COLOR_WHITE, "Content": self.inputLine[-1]}]

            # self.lineDisplay["R1M"] = [{"Color": ss.COLOR_WHITE, "Content": "*****"}]
            # self.lineDisplay["R2M"] = [{"Color": ss.COLOR_WHITE, "Content": "TO -----"}]
            self.lineDisplay["R3M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----/-----"}]
            # self.lineDisplay["R4M"] = [{"Color": ss.COLOR_WHITE, "Content": "--/---"}]
            # self.lineDisplay["R5M"] = [{"Color": ss.COLOR_WHITE, "Content": "ENG OUT>"}]
            # self.lineDisplay["R6M"] = [{"Color": ss.COLOR_WHITE, "Content": "RTA>"}]

            self.lineDisplay["L1S"] = [{"Color": ss.COLOR_WHITE, "Content": " E/D ALT"}]
            self.lineDisplay["L2S"] = [{"Color": ss.COLOR_WHITE, "Content": " TGT SPD"}]
            self.lineDisplay["L3S"] = [{"Color": ss.COLOR_WHITE, "Content": " SPD REST"}]
            # self.lineDisplay["L4S"] = [{"Color": ss.COLOR_WHITE, "Content": " FUEL AT"}]
            self.lineDisplay["L5S"] = [{"Color": ss.COLOR_WHITE, "Content": "-"*24}]
            # self.lineDisplay["L6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 24}]

            # self.lineDisplay["R1S"] = [{"Color": ss.COLOR_WHITE, "Content": "DEST"}]
            # self.lineDisplay["R2S"] = [{"Color": ss.COLOR_WHITE, "Content": "TO -----"}]
            self.lineDisplay["R3S"] = [{"Color": ss.COLOR_WHITE, "Content": "WPT/ALT"}]
            self.lineDisplay["R4S"] = [{"Color": ss.COLOR_WHITE, "Content": "FPA V/B V/S"}]
            # self.lineDisplay["R5S"] = [{"Color": ss.COLOR_WHITE, "Content": "------------"}]
            # self.lineDisplay["R6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 24}]
            pass
        pass
    # LEGS 页面
    elif self.currentPage == ss.pageIndex.LEGS:
        # 检查页码并作规范
        if self.currentPageIndex < 1:
            self.currentPageIndex = 1
        elif self.currentPageIndex > 1:
            self.currentPageIndex = 1
            pass
        # LEGS 第一页
        if self.currentPageIndex == 1:
            # Draw the screen title
            self.lineDisplay["L0M"] = [{"Color": ss.COLOR_CYAN, "Content": " " * 6 + "RTE    LEGS"}]
            self.lineDisplay["R0S"] = [{"Color": ss.COLOR_WHITE, "Content": "1/1"}]
            self.lineDisplay["L1M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----"}]
            # self.lineDisplay["L2M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----"}]
            # self.lineDisplay["L3M"] = [{"Color": ss.COLOR_WHITE, "Content": "240/10000"}]
            # self.lineDisplay["L4M"] = [{"Color": ss.COLOR_WHITE, "Content": "**.*"}]
            # self.lineDisplay["L5M"] = [{"Color": ss.COLOR_WHITE, "Content": "<MAX RATE"}]
            self.lineDisplay["L6M"] = [{"Color": ss.COLOR_WHITE, "Content": "1.00/0.07NM"}]
            self.lineDisplay["L7M"] = [{"Color": ss.COLOR_WHITE, "Content": self.inputLine[-1]}]

            # self.lineDisplay["R1M"] = [{"Color": ss.COLOR_WHITE, "Content": "*****"}]
            # self.lineDisplay["R2M"] = [{"Color": ss.COLOR_WHITE, "Content": "TO -----"}]
            # self.lineDisplay["R3M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----/-----"}]
            # self.lineDisplay["R4M"] = [{"Color": ss.COLOR_WHITE, "Content": "--/---"}]
            # self.lineDisplay["R5M"] = [{"Color": ss.COLOR_WHITE, "Content": "ENG OUT>"}]
            # self.lineDisplay["R6M"] = [{"Color": ss.COLOR_WHITE, "Content": "RTA>"}]

            # self.lineDisplay["L1S"] = [{"Color": ss.COLOR_WHITE, "Content": " E/D ALT"}]
            # self.lineDisplay["L2S"] = [{"Color": ss.COLOR_WHITE, "Content": " TGT SPD"}]
            # self.lineDisplay["L3S"] = [{"Color": ss.COLOR_WHITE, "Content": " SPD REST"}]
            # self.lineDisplay["L4S"] = [{"Color": ss.COLOR_WHITE, "Content": " FUEL AT"}]
            # self.lineDisplay["L5S"] = [{"Color": ss.COLOR_WHITE, "Content": " RNP/ACTUAL"+"-"*13}]
            self.lineDisplay["L6S"] = [{"Color": ss.COLOR_WHITE, "Content": " RNP/ACTUAL"+"-"*13}]

            # self.lineDisplay["R1S"] = [{"Color": ss.COLOR_WHITE, "Content": "DEST"}]
            # self.lineDisplay["R2S"] = [{"Color": ss.COLOR_WHITE, "Content": "TO -----"}]
            # self.lineDisplay["R3S"] = [{"Color": ss.COLOR_WHITE, "Content": "WPT/ALT"}]
            # self.lineDisplay["R4S"] = [{"Color": ss.COLOR_WHITE, "Content": "FPA V/B V/S"}]
            # self.lineDisplay["R5S"] = [{"Color": ss.COLOR_WHITE, "Content": "------------"}]
            # self.lineDisplay["R6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 24}]
            pass
        pass
    # DEPARR 页面
    elif self.currentPage == ss.pageIndex.DEPARR:
        # 检查页码并作规范
        if self.currentPageIndex < 1:
            self.currentPageIndex = 1
        elif self.currentPageIndex > 1:
            self.currentPageIndex = 1
            pass
        # DEPARR 第一页
        if self.currentPageIndex == 1:
            # Draw the screen title
            self.lineDisplay["L0M"] = [{"Color": ss.COLOR_WHITE, "Content": " " * 6 + "DEP/ARR INDEX"}]
            self.lineDisplay["R0S"] = [{"Color": ss.COLOR_WHITE, "Content": "1/1"}]
            self.lineDisplay["L1M"] = [{"Color": ss.COLOR_WHITE, "Content": "<DEP"}]
            # self.lineDisplay["L2M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----"}]
            # self.lineDisplay["L3M"] = [{"Color": ss.COLOR_WHITE, "Content": "240/10000"}]
            # self.lineDisplay["L4M"] = [{"Color": ss.COLOR_WHITE, "Content": "**.*"}]
            # self.lineDisplay["L5M"] = [{"Color": ss.COLOR_WHITE, "Content": "<MAX RATE"}]
            self.lineDisplay["L6M"] = [{"Color": ss.COLOR_WHITE, "Content": "<----"}]
            self.lineDisplay["L7M"] = [{"Color": ss.COLOR_WHITE, "Content": self.inputLine[-1]}]

            self.lineDisplay["R1M"] = [{"Color": ss.COLOR_WHITE, "Content": "ARR>"}]
            self.lineDisplay["R2M"] = [{"Color": ss.COLOR_WHITE, "Content": "ARR>"}]
            # self.lineDisplay["R3M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----/-----"}]
            # self.lineDisplay["R4M"] = [{"Color": ss.COLOR_WHITE, "Content": "--/---"}]
            # self.lineDisplay["R5M"] = [{"Color": ss.COLOR_WHITE, "Content": "ENG OUT>"}]
            self.lineDisplay["R6M"] = [{"Color": ss.COLOR_WHITE, "Content": "---->"}]

            # self.lineDisplay["L1S"] = [{"Color": ss.COLOR_WHITE, "Content": " E/D ALT"}]
            # self.lineDisplay["L2S"] = [{"Color": ss.COLOR_WHITE, "Content": " TGT SPD"}]
            # self.lineDisplay["L3S"] = [{"Color": ss.COLOR_WHITE, "Content": " SPD REST"}]
            # self.lineDisplay["L4S"] = [{"Color": ss.COLOR_WHITE, "Content": " FUEL AT"}]
            # self.lineDisplay["L5S"] = [{"Color": ss.COLOR_WHITE, "Content": " RNP/ACTUAL"+"-"*13}]
            self.lineDisplay["L6S"] = [{"Color": ss.COLOR_WHITE, "Content": " DEP      OTHER"}]

            # self.lineDisplay["R1S"] = [{"Color": ss.COLOR_WHITE, "Content": "DEST"}]
            # self.lineDisplay["R2S"] = [{"Color": ss.COLOR_WHITE, "Content": "TO -----"}]
            # self.lineDisplay["R3S"] = [{"Color": ss.COLOR_WHITE, "Content": "WPT/ALT"}]
            # self.lineDisplay["R4S"] = [{"Color": ss.COLOR_WHITE, "Content": "FPA V/B V/S"}]
            # self.lineDisplay["R5S"] = [{"Color": ss.COLOR_WHITE, "Content": "------------"}]
            self.lineDisplay["R6S"] = [{"Color": ss.COLOR_WHITE, "Content": "ARR"}]
            pass
        pass
    # HOLD 页面
    elif self.currentPage == ss.pageIndex.HOLD:
        # 检查页码并作规范
        if self.currentPageIndex < 1:
            self.currentPageIndex = 1
        elif self.currentPageIndex > 1:
            self.currentPageIndex = 1
            pass
        # HOLD 第一页
        if self.currentPageIndex == 1:
            # Draw the screen title
            self.lineDisplay["L0M"] = [{"Color": ss.COLOR_CYAN, "Content": " " * 6 + "RTE    LEGS"}]
            self.lineDisplay["R0S"] = [{"Color": ss.COLOR_WHITE, "Content": "1/1"}]
            self.lineDisplay["L1M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----"}]
            # self.lineDisplay["L2M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----"}]
            # self.lineDisplay["L3M"] = [{"Color": ss.COLOR_WHITE, "Content": "240/10000"}]
            # self.lineDisplay["L4M"] = [{"Color": ss.COLOR_WHITE, "Content": "**.*"}]
            # self.lineDisplay["L5M"] = [{"Color": ss.COLOR_WHITE, "Content": "<MAX RATE"}]
            self.lineDisplay["L6M"] = [{"Color": ss.COLOR_WHITE, "Content": "*****"}]
            self.lineDisplay["L7M"] = [{"Color": ss.COLOR_WHITE, "Content": self.inputLine[-1]}]

            # self.lineDisplay["R1M"] = [{"Color": ss.COLOR_WHITE, "Content": "*****"}]
            # self.lineDisplay["R2M"] = [{"Color": ss.COLOR_WHITE, "Content": "TO -----"}]
            # self.lineDisplay["R3M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----/-----"}]
            # self.lineDisplay["R4M"] = [{"Color": ss.COLOR_WHITE, "Content": "--/---"}]
            # self.lineDisplay["R5M"] = [{"Color": ss.COLOR_WHITE, "Content": "ENG OUT>"}]
            self.lineDisplay["R6M"] = [{"Color": ss.COLOR_WHITE, "Content": "PPOS>"}]

            # self.lineDisplay["L1S"] = [{"Color": ss.COLOR_WHITE, "Content": " E/D ALT"}]
            # self.lineDisplay["L2S"] = [{"Color": ss.COLOR_WHITE, "Content": " TGT SPD"}]
            # self.lineDisplay["L3S"] = [{"Color": ss.COLOR_WHITE, "Content": " SPD REST"}]
            # self.lineDisplay["L4S"] = [{"Color": ss.COLOR_WHITE, "Content": " FUEL AT"}]
            # self.lineDisplay["L5S"] = [{"Color": ss.COLOR_WHITE, "Content": " RNP/ACTUAL"+"-"*13}]
            self.lineDisplay["L6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-"*8 + "HOLD AT" + "-"*9}]

            # self.lineDisplay["R1S"] = [{"Color": ss.COLOR_WHITE, "Content": "DEST"}]
            # self.lineDisplay["R2S"] = [{"Color": ss.COLOR_WHITE, "Content": "TO -----"}]
            # self.lineDisplay["R3S"] = [{"Color": ss.COLOR_WHITE, "Content": "WPT/ALT"}]
            # self.lineDisplay["R4S"] = [{"Color": ss.COLOR_WHITE, "Content": "FPA V/B V/S"}]
            # self.lineDisplay["R5S"] = [{"Color": ss.COLOR_WHITE, "Content": "------------"}]
            # self.lineDisplay["R6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 24}]
            pass
        pass
    # PROGRESS 页面
    elif self.currentPage == ss.pageIndex.PROGRESS:
        # 检查页码并作规范
        if self.currentPageIndex < 1:
            self.currentPageIndex = 4
        elif self.currentPageIndex > 4:
            self.currentPageIndex = 1
            pass
        # PROGRESS 第一页
        if self.currentPageIndex == 1:
            # Draw the screen title
            self.lineDisplay["L0M"] = [{"Color": ss.COLOR_WHITE, "Content": "  "+"-" * 8 + " PROGRESS"}]
            self.lineDisplay["R0S"] = [{"Color": ss.COLOR_WHITE, "Content": "1/4 "}]
            # self.lineDisplay["L1M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----"}]
            # self.lineDisplay["L2M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----"}]
            # self.lineDisplay["L3M"] = [{"Color": ss.COLOR_WHITE, "Content": "240/10000"}]
            # self.lineDisplay["L4M"] = [{"Color": ss.COLOR_WHITE, "Content": "**.*"}]
            # self.lineDisplay["L5M"] = [{"Color": ss.COLOR_WHITE, "Content": "<MAX RATE"}]
            # self.lineDisplay["L6M"] = [{"Color": ss.COLOR_WHITE, "Content": "*****"}]
            self.lineDisplay["L7M"] = [{"Color": ss.COLOR_WHITE, "Content": self.inputLine[-1]}]

            # self.lineDisplay["R1M"] = [{"Color": ss.COLOR_WHITE, "Content": "*****"}]
            # self.lineDisplay["R2M"] = [{"Color": ss.COLOR_WHITE, "Content": "TO -----"}]
            # self.lineDisplay["R3M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----/-----"}]
            # self.lineDisplay["R4M"] = [{"Color": ss.COLOR_WHITE, "Content": "--/---"}]
            self.lineDisplay["R5M"] = [{"Color": ss.COLOR_WHITE, "Content": "43.9"}]
            self.lineDisplay["R6M"] = [{"Color": ss.COLOR_WHITE, "Content": "NAV STATUS>"}]

            self.lineDisplay["L1S"] = [{"Color": ss.COLOR_WHITE, "Content": " FROM    ALT"}]
            self.lineDisplay["L2S"] = [{"Color": ss.COLOR_WHITE, "Content": "         DTG"}]
            # self.lineDisplay["L3S"] = [{"Color": ss.COLOR_WHITE, "Content": " SPD REST"}]
            # self.lineDisplay["L4S"] = [{"Color": ss.COLOR_WHITE, "Content": " FUEL AT"}]
            # self.lineDisplay["L5S"] = [{"Color": ss.COLOR_WHITE, "Content": " RNP/ACTUAL"+"-"*13}]
            self.lineDisplay["L6S"] = [{"Color": ss.COLOR_WHITE, "Content": " WIND"}]

            self.lineDisplay["R1S"] = [{"Color": ss.COLOR_WHITE, "Content": "ATA   FUEL"}]
            self.lineDisplay["R2S"] = [{"Color": ss.COLOR_WHITE, "Content": "ETA   FUEL"}]
            # self.lineDisplay["R3S"] = [{"Color": ss.COLOR_WHITE, "Content": "WPT/ALT"}]
            # self.lineDisplay["R4S"] = [{"Color": ss.COLOR_WHITE, "Content": "FPA V/B V/S"}]
            self.lineDisplay["R5S"] = [{"Color": ss.COLOR_WHITE, "Content": "FUEL QTG"}]
            # self.lineDisplay["R6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 24}]
            pass
        # PROGRESS 第二页
        elif self.currentPageIndex == 2:
            # Draw the screen title
            self.lineDisplay["L0M"] = [{"Color": ss.COLOR_WHITE, "Content": "  " + "-" * 8 + " PROGRESS"}]
            self.lineDisplay["R0S"] = [{"Color": ss.COLOR_WHITE, "Content": "2/4 "}]
            # self.lineDisplay["L1M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----"}]
            # self.lineDisplay["L2M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----"}]
            # self.lineDisplay["L3M"] = [{"Color": ss.COLOR_WHITE, "Content": "240/10000"}]
            self.lineDisplay["L4M"] = [{"Color": ss.COLOR_WHITE, "Content": "192°"},{"Color": ss.COLOR_WHITE, "Font":ss.FONT_CDU_TITLE_SMALL,"Content": "T"}]
            # self.lineDisplay["L5M"] = [{"Color": ss.COLOR_WHITE, "Content": "<MAX RATE"}]
            self.lineDisplay["L6M"] = [{"Color": ss.COLOR_WEAK_WHITE, "Content": "<REQUEST"}]
            self.lineDisplay["L7M"] = [{"Color": ss.COLOR_WHITE, "Content": self.inputLine[-1]}]

            # self.lineDisplay["R1M"] = [{"Color": ss.COLOR_WHITE, "Content": "*****"}]
            self.lineDisplay["R2M"] = [{"Color": ss.COLOR_WHITE, "Content": "17°"},{"Color": ss.COLOR_WHITE,"Font":ss.FONT_CDU_TITLE_SMALL, "Content": "C"},{"Color": ss.COLOR_WHITE, "Content": "/  3°"},{"Color": ss.COLOR_WHITE,"Font":ss.FONT_CDU_TITLE_SMALL, "Content": "C"}]
            # self.lineDisplay["R3M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----/-----"}]
            self.lineDisplay["R4M"] = [{"Color": ss.COLOR_WHITE, "Content": "0"},{"Color": ss.COLOR_WHITE,"Font":ss.FONT_CDU_TITLE_SMALL, "Content": "KT"}]
            self.lineDisplay["R5M"] = [{"Color": ss.COLOR_WHITE, "Content": "REPORT>"}]
            self.lineDisplay["R6M"] = [{"Color": ss.COLOR_WHITE, "Content": "REPORT>"}]

            # self.lineDisplay["L1S"] = [{"Color": ss.COLOR_WHITE, "Content": " FROM    ALT"}]
            self.lineDisplay["L2S"] = [{"Color": ss.COLOR_WHITE, "Content": " WIND"}]
            self.lineDisplay["L3S"] = [{"Color": ss.COLOR_WHITE, "Content": " XTK ERROR"}]
            self.lineDisplay["L4S"] = [{"Color": ss.COLOR_WHITE, "Content": " GPS-L TRK"}]
            # self.lineDisplay["L5S"] = [{"Color": ss.COLOR_WHITE, "Content": " RNP/ACTUAL"+"-"*13}]
            self.lineDisplay["L6S"] = [{"Color": ss.COLOR_WEAK_WHITE, "Content": " WEATHER"}]

            self.lineDisplay["R1S"] = [{"Color": ss.COLOR_WHITE, "Content": "CROSSWIND"}]
            self.lineDisplay["R2S"] = [{"Color": ss.COLOR_WHITE, "Content": "SAT/ISA DEV"}]
            self.lineDisplay["R3S"] = [{"Color": ss.COLOR_WHITE, "Content": "VERT DEV"}]
            self.lineDisplay["R4S"] = [{"Color": ss.COLOR_WHITE, "Content": "TAS"}]
            self.lineDisplay["R5S"] = [{"Color": ss.COLOR_WHITE, "Content": "PROGRESS "}]
            self.lineDisplay["R6S"] = [{"Color": ss.COLOR_WHITE, "Content": "POSITION"}]
            pass
        # PROGRESS 第三页
        elif self.currentPageIndex == 3:
            # Draw the screen title
            self.lineDisplay["L0M"] = [{"Color": ss.COLOR_WHITE, "Content": " " * 6 + "RTA PROGRESS"}]
            self.lineDisplay["R0S"] = [{"Color": ss.COLOR_WHITE, "Content": "3/4 "}]
            self.lineDisplay["L1M"] = [{"Color": ss.COLOR_WHITE, "Content": "*****"}]
            # self.lineDisplay["L2M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----"}]
            # self.lineDisplay["L3M"] = [{"Color": ss.COLOR_WHITE, "Content": "240/10000"}]
            # self.lineDisplay["L4M"] = [{"Color": ss.COLOR_WHITE, "Content": "192°"},{"Color": ss.COLOR_WHITE, "Font": ss.FONT_CDU_TITLE_SMALL, "Content": "T"}]
            # self.lineDisplay["L5M"] = [{"Color": ss.COLOR_WHITE, "Content": "<MAX RATE"}]
            self.lineDisplay["L6M"] = [{"Color": ss.COLOR_WHITE, "Content": "<LIMITS"}]
            self.lineDisplay["L7M"] = [{"Color": ss.COLOR_WHITE, "Content": self.inputLine[-1]}]

            # self.lineDisplay["R1M"] = [{"Color": ss.COLOR_WHITE, "Content": "*****"}]
            # self.lineDisplay["R2M"] = [{"Color": ss.COLOR_WHITE, "Content": "17°"},
            #                                {"Color": ss.COLOR_WHITE, "Font": ss.FONT_CDU_TITLE_SMALL, "Content": "C"},
            #                                {"Color": ss.COLOR_WHITE, "Content": "/  3°"},
            #                                {"Color": ss.COLOR_WHITE, "Font": ss.FONT_CDU_TITLE_SMALL, "Content": "C"}]
            # # self.lineDisplay["R3M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----/-----"}]
            # self.lineDisplay["R4M"] = [{"Color": ss.COLOR_WHITE, "Content": "0"},
            #                                {"Color": ss.COLOR_WHITE, "Font": ss.FONT_CDU_TITLE_SMALL, "Content": "KT"}]
            # self.lineDisplay["R5M"] = [{"Color": ss.COLOR_WHITE, "Content": "REPORT>"}]
            # self.lineDisplay["R6M"] = [{"Color": ss.COLOR_WHITE, "Content": "REPORT>"}]

            self.lineDisplay["L1S"] = [{"Color": ss.COLOR_WHITE, "Content": " RTA WPT"}]
            # self.lineDisplay["L2S"] = [{"Color": ss.COLOR_WHITE, "Content": " RTA WPT"}]
            # self.lineDisplay["L3S"] = [{"Color": ss.COLOR_WHITE, "Content": " XTK ERROR"}]
            # self.lineDisplay["L4S"] = [{"Color": ss.COLOR_WHITE, "Content": " GPS-L TRK"}]
            # self.lineDisplay["L5S"] = [{"Color": ss.COLOR_WHITE, "Content": " RNP/ACTUAL"+"-"*13}]
            self.lineDisplay["L6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-"*24}]

            # self.lineDisplay["R1S"] = [{"Color": ss.COLOR_WHITE, "Content": "CROSSWIND"}]
            # self.lineDisplay["R2S"] = [{"Color": ss.COLOR_WHITE, "Content": "SAT/ISA DEV"}]
            # self.lineDisplay["R3S"] = [{"Color": ss.COLOR_WHITE, "Content": "VERT DEV"}]
            # self.lineDisplay["R4S"] = [{"Color": ss.COLOR_WHITE, "Content": "TAS"}]
            # self.lineDisplay["R5S"] = [{"Color": ss.COLOR_WHITE, "Content": "PROGRESS "}]
            # self.lineDisplay["R6S"] = [{"Color": ss.COLOR_WHITE, "Content": "POSITION"}]
            pass
        # PROGRESS 第四页
        elif self.currentPageIndex == 4:
            # Draw the screen title
            self.lineDisplay["L0M"] = [{"Color": ss.COLOR_WHITE, "Content": " " * 6 + "RNP PROGRESS"}]
            self.lineDisplay["R0S"] = [{"Color": ss.COLOR_WHITE, "Content": "4/4 "}]
            # self.lineDisplay["L1M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----"}]
            self.lineDisplay["L2M"] = [{"Color": ss.COLOR_WHITE, "Font": ss.FONT_CDU_TITLE_SMALL, "Content": "1.00/0.05NM"}]
            # self.lineDisplay["L3M"] = [{"Color": ss.COLOR_WHITE, "Content": "240/10000"}]
            # self.lineDisplay["L4M"] = [{"Color": ss.COLOR_WHITE, "Content": "192°"},
            #                                {"Color": ss.COLOR_WHITE, "Font": ss.FONT_CDU_TITLE_SMALL, "Content": "T"}]
            # # self.lineDisplay["L5M"] = [{"Color": ss.COLOR_WHITE, "Content": "<MAX RATE"}]
            self.lineDisplay["L6M"] = [{"Color": ss.COLOR_WHITE, "Font": ss.FONT_CDU_TITLE_SMALL, "Content": "0.30NM"}]
            self.lineDisplay["L7M"] = [{"Color": ss.COLOR_WHITE, "Content": self.inputLine[-1]}]

            # self.lineDisplay["R1M"] = [{"Color": ss.COLOR_WHITE, "Content": "*****"}]
            self.lineDisplay["R2M"] = [{"Color": ss.COLOR_WHITE, "Font": ss.FONT_CDU_TITLE_SMALL, "Content": "400/ 51FT"}]
            # # self.lineDisplay["R3M"] = [{"Color": ss.COLOR_WHITE, "Content": "-----/-----"}]
            # self.lineDisplay["R4M"] = [{"Color": ss.COLOR_WHITE, "Content": "0"},
            #                                {"Color": ss.COLOR_WHITE, "Font": ss.FONT_CDU_TITLE_SMALL, "Content": "KT"}]
            # self.lineDisplay["R5M"] = [{"Color": ss.COLOR_WHITE, "Content": "REPORT>"}]
            self.lineDisplay["R6M"] = [{"Color": ss.COLOR_WHITE, "Font": ss.FONT_CDU_TITLE_SMALL, "Content": "400FT"}]

            # self.lineDisplay["L1S"] = [{"Color": ss.COLOR_WHITE, "Content": " FROM    ALT"}]
            self.lineDisplay["L2S"] = [{"Color": ss.COLOR_WHITE, "Content": "RNP/ACTUAL"}]
            self.lineDisplay["L3S"] = [{"Color": ss.COLOR_WHITE, "Content": "XTK ERROR"}]
            # self.lineDisplay["L4S"] = [{"Color": ss.COLOR_WHITE, "Content": " GPS-L TRK"}]
            # self.lineDisplay["L5S"] = [{"Color": ss.COLOR_WHITE, "Content": " RNP/ACTUAL"+"-"*13}]
            self.lineDisplay["L6S"] = [{"Color": ss.COLOR_WHITE, "Content": " RNP--APPROACH--VERT RNP"}]

            # self.lineDisplay["R1S"] = [{"Color": ss.COLOR_WHITE, "Content": "CROSSWIND"}]
            self.lineDisplay["R2S"] = [{"Color": ss.COLOR_WHITE, "Content": "VERT RNP/ANP"}]
            self.lineDisplay["R3S"] = [{"Color": ss.COLOR_WHITE, "Content": "VERT DEV"}]
            # self.lineDisplay["R4S"] = [{"Color": ss.COLOR_WHITE, "Content": "TAS"}]
            # self.lineDisplay["R5S"] = [{"Color": ss.COLOR_WHITE, "Content": "PROGRESS "}]
            # self.lineDisplay["R6S"] = [{"Color": ss.COLOR_WHITE, "Content": "POSITION"}]
            pass
        pass
    # HOLD 页面
    elif self.currentPage == ss.pageIndex.N1:
        # 检查页码并作规范
        if self.currentPageIndex < 1:
            self.currentPageIndex = 1
        elif self.currentPageIndex > 1:
            self.currentPageIndex = 1
            pass
        # N1 第一页
        if self.currentPageIndex == 1:
            # Draw the screen title
            self.lineDisplay["L0M"] = [{"Color": ss.COLOR_WHITE, "Content": " " * 8 + "N1 LIMIT"}]
            self.lineDisplay["R0S"] = [{"Color": ss.COLOR_WHITE, "Content": "1/1"}]
            self.lineDisplay["L1M"] = [{"Color": ss.COLOR_WHITE, "Content": "----/ "},{"Color": ss.COLOR_WHITE, "Font":ss.FONT_CDU_TITLE_SMALL,"Content": "+18°C"}]
            self.lineDisplay["L2M"] = [{"Color": ss.COLOR_WHITE, "Content": "<TO    <ACT>"}]
            self.lineDisplay["L3M"] = [{"Color": ss.COLOR_WHITE, "Content": "<TO-1>"}]
            self.lineDisplay["L4M"] = [{"Color": ss.COLOR_WHITE, "Content": "<TO-2"}]
            # self.lineDisplay["L5M"] = [{"Color": ss.COLOR_WHITE, "Content": "<MAX RATE"}]
            self.lineDisplay["L6M"] = [{"Color": ss.COLOR_WHITE, "Content": "<PERF INIT"}]
            self.lineDisplay["L7M"] = [{"Color": ss.COLOR_WHITE, "Content": self.inputLine[-1]}]

            self.lineDisplay["R1M"] = [{"Color": ss.COLOR_WHITE, "Content": "100.9/100.9"}]
            self.lineDisplay["R2M"] = [{"Color": ss.COLOR_WHITE, "Content": "<SEL>   CLB>"}]
            self.lineDisplay["R3M"] = [{"Color": ss.COLOR_WHITE, "Content": "CLB-1"}]
            self.lineDisplay["R4M"] = [{"Color": ss.COLOR_WHITE, "Content": "CLB-2"}]
            # self.lineDisplay["R5M"] = [{"Color": ss.COLOR_WHITE, "Content": "ENG OUT>"}]
            self.lineDisplay["R6M"] = [{"Color": ss.COLOR_WHITE, "Content": "TAKEOFF>"}]

            self.lineDisplay["L1S"] = [{"Color": ss.COLOR_WHITE, "Content": " SEL/OAT"}]
            self.lineDisplay["L2S"] = [{"Color": ss.COLOR_WHITE, "Content": " 27K"}]
            self.lineDisplay["L3S"] = [{"Color": ss.COLOR_WHITE, "Content": " 26K DERATE"}]
            self.lineDisplay["L4S"] = [{"Color": ss.COLOR_WHITE, "Content": " 24K DERATE"}]
            # self.lineDisplay["L5S"] = [{"Color": ss.COLOR_WHITE, "Content": " RNP/ACTUAL"+"-"*13}]
            self.lineDisplay["L6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-"*24}]

            self.lineDisplay["R1S"] = [{"Color": ss.COLOR_WHITE, "Content": "27K N1"}]
            # self.lineDisplay["R2S"] = [{"Color": ss.COLOR_WHITE, "Content": ""}]
            # self.lineDisplay["R3S"] = [{"Color": ss.COLOR_WHITE, "Content": "WPT/ALT"}]
            # self.lineDisplay["R4S"] = [{"Color": ss.COLOR_WHITE, "Content": "FPA V/B V/S"}]
            # self.lineDisplay["R5S"] = [{"Color": ss.COLOR_WHITE, "Content": "------------"}]
            # self.lineDisplay["R6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 24}]
            pass
        pass
    # FIX 页面
    elif self.currentPage == ss.pageIndex.FIX:
        # 检查页码并作规范
        if self.currentPageIndex < 1:
            self.currentPageIndex = 6
        elif self.currentPageIndex > 6:
            self.currentPageIndex = 1
            pass
        # FIX 页
        if self.currentPageIndex >= 1 and self.currentPageIndex <= 6:
            # Draw the screen title
            self.lineDisplay["L0M"] = [{"Color": ss.COLOR_WHITE, "Content": " " * 8 + "FIX INFO"}]
            self.lineDisplay["R0S"] = [{"Color": ss.COLOR_WHITE, "Content": str(self.currentPageIndex)+"/6"}]
            self.lineDisplay["L1M"] = [{"Color": ss.COLOR_WHITE, "Content": "*****"}]
            # self.lineDisplay["L2M"] = [{"Color": ss.COLOR_WHITE, "Content": "<TO    <ACT>"}]
            # self.lineDisplay["L3M"] = [{"Color": ss.COLOR_WHITE, "Content": "<TO-1>"}]
            # self.lineDisplay["L4M"] = [{"Color": ss.COLOR_WHITE, "Content": "<TO-2"}]
            # self.lineDisplay["L5M"] = [{"Color": ss.COLOR_WHITE, "Content": "<MAX RATE"}]
            # self.lineDisplay["L6M"] = [{"Color": ss.COLOR_WHITE, "Content": "<PERF INIT"}]
            self.lineDisplay["L7M"] = [{"Color": ss.COLOR_WHITE, "Content": self.inputLine[-1]}]

            # self.lineDisplay["R1M"] = [{"Color": ss.COLOR_WHITE, "Content": "100.9/100.9"}]
            # self.lineDisplay["R2M"] = [{"Color": ss.COLOR_WHITE, "Content": "<SEL>   CLB>"}]
            # self.lineDisplay["R3M"] = [{"Color": ss.COLOR_WHITE, "Content": "CLB-1"}]
            # self.lineDisplay["R4M"] = [{"Color": ss.COLOR_WHITE, "Content": "CLB-2"}]
            # self.lineDisplay["R5M"] = [{"Color": ss.COLOR_WHITE, "Content": "ENG OUT>"}]
            # self.lineDisplay["R6M"] = [{"Color": ss.COLOR_WHITE, "Content": "TAKEOFF>"}]

            self.lineDisplay["L1S"] = [{"Color": ss.COLOR_WHITE, "Content": " FIX RAD/DIS"}]
            self.lineDisplay["L2S"] = [{"Color": ss.COLOR_WHITE, "Content": " RAD/DIS  ETA"}]
            # self.lineDisplay["L3S"] = [{"Color": ss.COLOR_WHITE, "Content": " 26K DERATE"}]
            # self.lineDisplay["L4S"] = [{"Color": ss.COLOR_WHITE, "Content": " 24K DERATE"}]
            # self.lineDisplay["L5S"] = [{"Color": ss.COLOR_WHITE, "Content": " RNP/ACTUAL"+"-"*13}]
            # self.lineDisplay["L6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-"*24}]

            self.lineDisplay["R1S"] = [{"Color": ss.COLOR_WHITE, "Content": "FR       "}]
            self.lineDisplay["R2S"] = [{"Color": ss.COLOR_WHITE, "Content": "DTG   ALT"}]
            # self.lineDisplay["R3S"] = [{"Color": ss.COLOR_WHITE, "Content": "WPT/ALT"}]
            # self.lineDisplay["R4S"] = [{"Color": ss.COLOR_WHITE, "Content": "FPA V/B V/S"}]
            # self.lineDisplay["R5S"] = [{"Color": ss.COLOR_WHITE, "Content": "------------"}]
            # self.lineDisplay["R6S"] = [{"Color": ss.COLOR_WHITE, "Content": "-" * 24}]
            pass
        pass
    # 绘制界面
    for key in self.lineDisplay:
        if self.lineDisplay[key]:
            self.DrawLine(painter, key, self.lineDisplay[key])
            pass
        pass
