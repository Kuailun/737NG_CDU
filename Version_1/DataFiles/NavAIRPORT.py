# -*- coding: utf-8 -*-
# @File       : NavAIRPORT.py
# @Author     : Yuchen Chai
# @Date       : 2020/2/9 14:25
# @Description:

import settings as ss

if ss.APPLICATION_MODE == "DEVELOPMENT":
    from Version_1.Database import database
    from Version_1.logger import logger
else:
    from database import database
    from logger import logger

class NavAIRPORT(database):
    '''
    导航数据有效性数据库
    '''

    def __init__(self, p_path, p_name, p_type):
        '''
        初始化数据库
        '''

        super(NavAIRPORT, self).__init__(p_path, p_name, p_type)

        self._database = {}

        # # Check whether database is existed
        # status = self._Database_Path_Existing(createFile=False)
        #
        # if not status:
        #     msg = "{0} {1}.{2} not found. Error!".format(p_path, p_name, p_type)
        #     logger.critical(msg)
        #     raise(msg)
        #
        # _,_,self._database = self._Database_ReadFile()
        pass

    def _Database_CreateFile(self):
        '''
        No need to createFile
        :return:
        '''
        return True

    def _Database_ReadFile(self):
        '''
        Read data from file
        :return:
        '''
        status = True
        msg =''
        data = []

        # Read all lines into the database
        with open(self._database_path, 'r') as f:
            line = f.readline()
            data.append(line)

            while line:
                line = f.readline()
                data.append(line)
                pass
            pass

        AIRAC_CYCLE = data[15][2:-1]
        logger.info(r'AIRPORTS {0} database version: {1}'.format(self._name, AIRAC_CYCLE))

        data = data[17:-1]

        state = 0
        index = -1

        FIXES = {}
        RNWS = {}
        SIDS = {}
        STARS = {}
        APPROACHES = {}
        GATES = {}

        LATLON = {"N":1,"S":-1,"E":1,"W":-1}

        SIDContent = []
        STARContent = []
        APPROACHESContent = []

        while index < len(data)-1:
            index = index + 1
            content = data[index].replace("\n","")

            # 状态机转换
            if content == "FIXES":
                state = 0
                continue
            elif content == "RNWS":
                state = 1
                continue
            elif content == "SIDS":
                state = 2
                continue
            elif content == "STARS":
                state = 3
                continue
            elif content == "APPROACHES":
                state = 4
                continue
            elif content == "GATES":
                state = 5
                continue
            elif content == "" or content == "ENDFIXES" or content == "ENDRNWS"or content == "ENDGATES":
                continue

            # FIXES
            if state == 0:
                content = content.split(" ")
                LAT = round(LATLON[content[3]] * (int(content[4]) + float(content[5])/60),6)
                LON = round(LATLON[content[6]] * (int(content[7]) + float(content[8])/60),6)
                FIXES[content[1]] = {"Latitude": LAT, "Longitude": LON}
                pass
            # RNWS
            elif state == 1:
                content = content.split(" ")
                RNWS[content[1]] = {"RUNWAY":content[1], "SIDS":[]}
                pass
            # SIDS
            elif state == 2:
                if content[0] == "S" or content == "ENDSIDS":
                    # 暂存位置为空，则放进去
                    if len(SIDContent) == 0:
                        SIDContent.append(content)
                        pass
                    else:
                        # 处理，然后加进去
                        SIDName, mData = self._Database_ProcessSID(SIDContent)
                        SIDS[SIDName] = mData

                        # 清空暂存盘
                        SIDContent = []
                        SIDContent.append(content)
                        pass
                    pass
                else:
                    SIDContent.append(content)

                pass
            # STARS
            elif state == 3:
                if content[0] == "S" or content == "ENDSTARS":
                    # 暂存位置为空，则放进去
                    if len(STARContent) == 0:
                        STARContent.append(content)
                        pass
                    else:
                        # 处理，然后加进去
                        STARName, mStarData = self._Database_ProcessSTAR(STARContent)
                        STARS[STARName] = mStarData

                        # 清空暂存盘
                        STARContent = []
                        STARContent.append(content)
                        pass
                    pass
                else:
                    STARContent.append(content)
                pass
            # APPROACHES
            elif state == 4:
                if content[0] == "A" or content == "ENDAPPROACHES":
                    # 暂存位置为空，则放进去
                    if len(APPROACHESContent) == 0:
                        APPROACHESContent.append(content)
                        pass
                    else:
                        # 处理，然后加进去
                        APPROACHESName, mAPPROACHESData = self._Database_ProcessAPPROACH(APPROACHESContent)
                        APPROACHES[APPROACHESName] = mAPPROACHESData

                        # 清空暂存盘
                        APPROACHESContent = []
                        APPROACHESContent.append(content)
                        pass
                    pass
                else:
                    APPROACHESContent.append(content)
                pass
            # GATES
            elif state == 5:
                content = content.split(" ")
                Latitude = int(content[3]) + float(content[4])/60
                Longitude = int(content[6]) + float(content[7])/60

                if content[2] == "S":
                    Latitude = -Latitude
                    pass

                if content[5] == "W":
                    Longitude = -Longitude
                GATES[content[1]] = {"Gate":content[1], "Latitude":Latitude, "Longitude":Longitude}
                pass
            pass

        # 扫描一遍SIDS，为RNWS产生内容
        for item in SIDS:
            item = SIDS[item]
            for i in range(len(item["Runways"])):
                RNWS[item["Runways"][i]]["SIDS"].append(item["SID"])
                pass
            pass

        ret_data = {"ICAO":self._name,'AIRAC':AIRAC_CYCLE,'FIXES':FIXES, 'RNWS':RNWS, "SIDS": SIDS, "STARS":STARS, "APPROACHES":APPROACHES, "GATES":GATES}

        return status, msg, ret_data

    def _Database_ProcessSID(self, content):
        """
        将SID数据处理成需要而格式
        :return:
        """
        SID = ""
        Runways = []
        Transitions = []
        RunwaysData = {}
        TransitionsData = {}

        if len(content) == 1:
            content = content[0]
            content = content.split(" ")

            SID = content[1]
            Runways.append(content[3])
            RunwaysData[Runways[-1]] = content[4:]

            # index = 3
            # FIXES = []
            # temp = []
            # while(index < len(content)-1):
            #     index = index + 1
            #     if content[index] == "FIX" or content[index] == "TRK":
            #         if len(temp) == 0:
            #             temp.append(content[index])
            #             pass
            #         else:
            #             FIXES.append(temp)
            #             temp = []
            #             temp.append(content[index])
            #             pass
            #         pass
            #     else:
            #         temp.append(content[index])
            #         pass
            #     pass
            # FIXES.append(temp)
            # temp = []

        else:
            for i in range(len(content)):
                # Transition
                if content[i][1] == " ":
                    transition = content[i].split(" ")
                    Transitions.append(transition[3])
                    TransitionsData[Transitions[-1]] = transition[4:]
                    pass
                # Runway
                elif content[i][0] == " ":
                    runway = content[i].split(" ")
                    Runways.append(runway[2])
                    RunwaysData[Runways[-1]] = runway[3:]
                    pass
                # Sid
                else:
                    SIDContent = content[i].split(" ")
                    SID = SIDContent[1]

                    # 有些情况下多个跑道会写成一行
                    if len(SIDContent) > 2:
                        RNWContent = SIDContent[2:]
                        index = -1
                        runwayData = []
                        while(index < len(RNWContent)):
                            index = index + 1
                            if RNWContent[index] == "RNW":
                                Runways.append(RNWContent[index+1])
                                index = index + 1
                            else:
                                runwayData = RNWContent[index:]
                                index = len(RNWContent)
                                pass
                            pass

                        # 将相同的指令分别复制到runways中
                        for i in range(len(Runways)):
                            RunwaysData[Runways[i]] = runwayData
                            pass
                        pass
                    pass
                pass
            pass
        return SID, {"SID":SID, "Runways":Runways, "RunwaysData":RunwaysData, "Transitions":Transitions, "TransitionsData":TransitionsData}

    def _Database_ProcessSTAR(self, content):
        """
        将STAR数据处理成需要而格式
        :return:
        """
        STAR = ""
        Runways = []
        StarData = []
        Transitions = []
        TransitionsData = {}

        if len(content) == 2:
            contentStar = content[0]
            contentStar = contentStar.split(" ")

            contentRny = content[1]
            contentRny = contentRny.split(" ")

            STAR = contentStar[1]

            index = -1
            while(index<len(contentRny)-1):
                index = index + 1
                if contentRny[index] == "RNW":
                    Runways.append(contentRny[index+1])
                    index = index + 1
                    pass
                pass

            StarData.append(contentStar[2:])

        else:
            for i in range(len(content)):
                # Runway
                if content[i][1] == " ":
                    contentRny = content[i].split(" ")

                    index = -1
                    while (index < len(contentRny) - 1):
                        index = index + 1
                        if contentRny[index] == "RNW":
                            Runways.append(contentRny[index + 1])
                            index = index + 1
                            pass
                        pass
                    pass
                # Transition
                elif content[i][0] == " ":
                    transition = content[i].split(" ")
                    Transitions.append(transition[2])
                    TransitionsData[Transitions[-1]] = transition[3:]
                    pass
                # STAR
                else:
                    Star = content[i].split(" ")
                    STAR = Star[1]
                    StarData = Star[2:]
                    pass
                pass
            pass
        return STAR, {"STAR":STAR, "Runways":Runways, "StarData":StarData, "Transitions":Transitions, "TransitionsData":TransitionsData}

    def _Database_ProcessAPPROACH(self, content):
        """
        将APPROACHES数据处理成需要的格式
        :return:
        """
        APPROACH = ""
        Runway = ""
        APPROACHESData = []
        Transitions = []
        TransitionsData = {}

        # Approach信息
        Approach = content[0].split(" ")
        AppData = Approach[1]
        APPROACHESData = Approach[2:]
        m = AppData[-1]
        if AppData[-1] == "L" or AppData[-1] == "R":
            Runway = AppData[-3:]
            APPROACH = AppData[:-3]
            APPROACH = APPROACH + " " + Runway
        elif AppData[-1] == "A" or AppData[-1] == "B" or AppData[-1]=="Y" or AppData[-1]=="Z":
            Runway = AppData[-4:-1]
            APPROACH = AppData[:-4] + AppData[-1] + " " + Runway

        else:
            Runway = AppData[-2:]
            APPROACH = AppData[:-2]
            APPROACH = APPROACH + " " + Runway
            pass



        # Transitions
        index = 0
        while (index < len(content) - 1):
            index = index + 1
            transition = content[index].split(" ")
            Transitions.append(transition[2])
            TransitionsData[Transitions[-1]] = transition[3:]
            pass

        return APPROACH, {"Approach":APPROACH, "Runway":Runway, "ApproachData":APPROACHESData, "Transitions":Transitions, "TransitionsData":TransitionsData}


    def Interface_Set_Airport(self, target):
        '''
        查询代码是否在数据库中
        :return:
        '''
        self._name = target
        self._database_path = self._path + self._name + "." + self._type

        status = self._Database_Path_Existing(createFile=False)

        if not status:
            msg = "{0} not found. Error!".format(self._database_path)
            logger.critical(msg)
            raise(msg)

        _,_,self._database = self._Database_ReadFile()

        return self._database

