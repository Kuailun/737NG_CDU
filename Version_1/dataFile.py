# -*- coding: utf-8 -*-
# @File       : dataFile.py
# @Author     : Yuchen Chai
# @Date       : 2020/1/31 13:12
# @Description:


import settings as ss

if ss.APPLICATION_MODE == "DEVELOPMENT":
    from Version_1.logger import logger
    from Version_1.DataFiles.NavRTE import NavRTE
    from Version_1.DataFiles.NavIDENT import NavIDENT
    from Version_1.DataFiles.NavAIRPORTS import NavAIRPORTS
    from Version_1.DataFiles.NavAIRPORT import NavAIRPORT

else:
    from logger import logger
    from NavRTE import NavRTE
    from NavIDENT import NavIDENT
    from NavAIRPORTS import NavAIRPORTS
    from NavAIRPORT import NavAIRPORT

class DataFile():
    '''
    Control all databases and handle the request from other part in the program
    '''

    def __init__(self):
        '''
        Initialize the databases we need
        '''

        # FMC发布日期数据库
        self._NavIDENT = NavIDENT(ss.APPLICATION_PATH + "/Database/", "fmc_ident", "txt")
        # 导航点数据库
        self._NavRTE = NavRTE(ss.APPLICATION_PATH + '/Database/', 'wpNavRTE', 'txt')
        # 机场数据库
        self._NavAIRPORTS = NavAIRPORTS(ss.APPLICATION_PATH + '/Database/', 'airports', 'dat')
        # 起飞机场数据库
        self._NavDepAirport = NavAIRPORT(ss.APPLICATION_PATH + '/Database/SIDSTARS/','   ','txt')
        # 降落机场数据库
        self._NavArrAirport = NavAIRPORT(ss.APPLICATION_PATH + '/Database/SIDSTARS/','   ','txt')


        # CDU 中需要用到的数据
        self._Data = {
            ss.variable.IDENT_MODEL: "737-900ER SSM",
            ss.variable.IDENT_ENG_RATING: "26K",
            ss.variable.IDENT_NAV_DATA_RELEASE: None,
            ss.variable.IDENT_NAV_ACTIVE:None,
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

            ss.variable.RTE_ORIGIN: None,
            ss.variable.RTE_ORIGIN_LOCATION: None,
            ss.variable.RTE_DEST: None,
            ss.variable.RTE_DEST_LOCATION: None,

            ss.variable.DEPARR_DEP_AIRPORTS_DATA: None,     # 离场机场的全部导航数据
            ss.variable.DEPARR_DEP_PAGE_FLAG: None,         # 在DEPARR页面是否可以进入DEPARTURE的标志
            ss.variable.DEPARTURES_SID: None,               # 在DEPARTURE页面选定的SID的长期储存结果，用于标明ACT
            ss.variable.DEPARTURES_SID_TEMP: None,          # 在DEPARTURE页面用户临时选定SID的结果，用于更改显示
            ss.variable.DEPARTURES_TRANSITION: None,        # 在DEPARTURE页面选定的Transition的长期储存结果，用于标明ACT
            ss.variable.DEPARTURES_TRANSITION_TEMP: None,   # 在DEPARTURE页面用户临时选定Transition的结果，用于更改显示
            ss.variable.DEPARTURES_RUNWAY: None,            # 在DEPARTURE页面选定的SID的长期储存结果，用于标明ACT
            ss.variable.DEPARTURES_RUNWAY_TEMP: None,       # 在DEPARTURE页面用户临时选定Runway的结果，用于更改显示

            ss.variable.POS_REF_AIRPORT:None,               # 在POS页面的REF AIRPORT信息
            ss.variable.POS_REF_GATE:None,                  # 在POS页面的REF GATE信息
        }

        # 数据加载后设置
        self._SetData()

        pass

    def _SetData(self):
        """
        在此处进行Data的初始化设置
        :return:
        """
        _,cycle_data = self._NavIDENT.Interface_AIRAC_CYCLE()
        self._Data[ss.variable.IDENT_NAV_DATA_RELEASE] = cycle_data["AIRAC"]
        self._Data[ss.variable.IDENT_NAV_ACTIVE] = cycle_data["Date"]

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

    def Interface_ORIGIN_DEST(self, airport):
        """
        检查机场代号是否合法
        :param airport:
        :return:
        """

        status, data = self._NavAIRPORTS.Interface_Airport_in_Database(airport)
        if not status:
            return status, None, None
        else:
            return status, None, data

    def Interface_DEPARTURES_AIRPORT_SET(self, airport):
        """
        设置起飞机场
        :param airport:
        :return:
        """
        # 机场数据库读取相关数据并返回
        m_airport = self._NavDepAirport.Interface_Set_Airport(airport)

        # 将机场数据置入DataFile中进行统一管理
        self.Interface_DATA_SET(ss.variable.DEPARR_DEP_AIRPORTS_DATA, m_airport)

        # 清除一些变量
        self.Interface_DATA_SET(ss.variable.DEPARTURES_SID, None)
        self.Interface_DATA_SET(ss.variable.DEPARTURES_SID_TEMP, None)
        self.Interface_DATA_SET(ss.variable.DEPARTURES_RUNWAY, None)
        self.Interface_DATA_SET(ss.variable.DEPARTURES_RUNWAY_TEMP, None)
        self.Interface_DATA_SET(ss.variable.DEPARTURES_TRANSITION, None)
        self.Interface_DATA_SET(ss.variable.DEPARTURES_TRANSITION_TEMP, None)
        return True, None, None

    def Interface_REF_AIRPORT_SET(self, airport):
        """
        设置参考机场
        :param airport:
        :return:
        """
        # 机场数据库读取相关数据并返回
        m_airport = self._NavDepAirport.Interface_Set_Airport(airport)

        # 将机场数据置入DataFile中进行统一管理
        self.Interface_DATA_SET(ss.variable.POS_REF_AIRPORT, m_airport)

        # 清除一些变量
        self.Interface_DATA_SET(ss.variable.POS_REF_GATE, None)
        return True, None, None

    def Interface_AIRPORT_COORDINATION(self, airport):
        """
        返回查询机场的坐标
        :param airport:
        :return:
        """
        status, data = self._NavAIRPORTS.Interface_Airport_in_Database(airport)
        return data


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

    def Interface_DATA_VALID(self, key):
        """
        查看关键词是否为空
        :param key: 关键词
        :return:
        """

        if key in self._Data:
            if self._Data[key]:
                return True
            else:
                return False
            pass

        msg = r"所查询的关键词不存在，错误！ {0}".format(key)
        logger.warning(msg)

        raise ()

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

    def Interface_DATA_COPY(self):
        """
        复制整个Data数据库
        :return:
        """
        return self._Data