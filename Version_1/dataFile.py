# -*- coding: utf-8 -*-
# @File       : dataFile.py
# @Author     : Yuchen Chai
# @Date       : 2020/1/31 13:12
# @Description:

from Version_1.DataFiles.NavRTE import NavRTE
from Version_1 import settings as ss
from Version_1.logger import logger

class DataFile():
    '''
    Control all databases and handle the request from other part in the program
    '''

    def __init__(self):
        '''
        Initialize the databases we need
        '''

        # Database for Navigation Routes
        self._NavRTE = NavRTE(ss.APPLICATION_PATH + '/Database/', 'wpNavRTE', 'txt')

        # CDU 中需要用到的数据
        self._Data = {
            ss.variable.IDENT_MODEL: "737-900ER SSM",
            ss.variable.IDENT_ENG_RATING: "26K",
            ss.variable.IDENT_NAV_DATA_RELEASE: "AIRAC-2002",
            ss.variable.IDENT_NAV_ACTIVE:"JAN30FEB27/20",
            "GMT-MON/DY": "2012.1z 05/30",
            "LAST POS": "N30°30.0 W086°30.7",
            "FMC POS": "N30°30.0 W086°30.7",
            "IRS L": "N30°30.0 W086°30.7",
            "IRS R": "N30°30.0 W086°30.8",
            "GPS L": "N30°30.0 W086°30.7",
            "GPS R": "N30°30.0 W086°30.7",
            "CRZ CG": "21.4%",
            "FUEL": "45.6",
            ss.variable.PERF_COST_INDEX: None,
            ss.variable.PERF_GROSS_WEIGHT: None,
            ss.variable.PERF_CRUISE_CENTER_OF_GRAVITY: 24.3,
            ss.variable.PERF_FUEL: 16.5,
            ss.variable.PERF_ZERO_FUEL_WEIGHT: None,
        }

        pass

    def Interface_RTE_START_END(self, start, end):
        '''
        检查是否有个通路连接起点和终点
        :param start: FIX点，例如 YQG
        :param end: FIX点，例如 DALIM
        :return: 状态，数据
        '''

        status, start_route = self._NavRTE.Interface_GetRoute(start)
        if not status:
            return False, None

        status, end_route = self._NavRTE.Interface_GetRoute(end)
        if not status:
            return False, None

        for i in range(len(start_route)):
            for j in range(len(end_route)):
                if(start_route[i] == end_route[j]):
                    return True, start_route[i]
                pass
            pass

        return False, None

    def Interface_RTE_ROUTE_FIX(self, route, fix):
        '''
        检查route是否与fix点相连
        :param route: route路径，例如 W577
        :param fix: fix点，例如 DBL
        :return: 状态
        '''

        status, target = self._NavRTE.Interface_GetRoute(fix)
        if not status:
            return False

        for i in range(len(target)):
            if route == target[i]:
                return True
            pass

        return False

    def Interface_DATA_KEYWORDS(self, key):
        '''
        根据关键词查询数据并返回
        :param key: 关键词
        :return:
        '''

        if key in self._Data:
            return self._Data[key]

        msg = r"所查询的关键词不存在，错误！ {0}".format(key)
        logger.warning(msg)

        raise()

    def Interface_DATA_SET(self, key, value):
        """
        将数据置入数据库中
        :param key: 关键词
        :param value: 值
        :return:
        """
        if key in self._Data:
            self._Data[key] = value
            return

        msg = r"所查询的关键词不存在，错误！ {0}".format(key)
        logger.warning(msg)

        raise ()