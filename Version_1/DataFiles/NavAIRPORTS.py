# -*- coding: utf-8 -*-
# @File       : NavAIRPORTS.py
# @Author     : Yuchen Chai
# @Date       : 2020/2/9 11:47
# @Description:

import settings as ss

if ss.APPLICATION_MODE == "DEVELOPMENT":
    from Version_1.Database import database
    from Version_1.logger import logger
else:
    from database import database
    from logger import logger

class NavAIRPORTS(database):
    '''
    导航数据有效性数据库
    '''

    def __init__(self, p_path, p_name, p_type):
        '''
        初始化数据库
        '''

        super(NavAIRPORTS, self).__init__(p_path, p_name, p_type)

        self._database = {}

        # Check whether database is existed
        status = self._Database_Path_Existing(createFile=False)

        if not status:
            msg = "{0} {1}.{2} not found. Error!".format(p_path, p_name, p_type)
            logger.critical(msg)
            raise(msg)

        _,_,self._database = self._Database_ReadFile()
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

        AIRAC_CYCLE = data[14][1:-1]
        logger.info(r'Navigation AIRPORTS database version: {0}'.format(AIRAC_CYCLE))

        data = data[16:]

        mData = {}
        for i in range(len(data)-1):
            mData[data[i][0:4]] = {"Longitude": float(data[i][14:]), "Latitude": float(data[i][4:14])}

        ret_data = {'AIRAC':AIRAC_CYCLE,'AIRPORTS':mData}

        return status, msg, ret_data

    def Interface_Airport_in_Database(self, target):
        '''
        查询代码是否在数据库中
        :return:
        '''

        if target in self._database['AIRPORTS']:
            return True, self._database['AIRPORTS'][target]
        else:
            return False, None