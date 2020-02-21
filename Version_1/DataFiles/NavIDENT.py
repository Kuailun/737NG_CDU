# -*- coding: utf-8 -*-
# @File       : NavIDENT.py
# @Author     : Yuchen Chai
# @Date       : 2020/2/9 11:30
# @Description:

import settings as ss

if ss.APPLICATION_MODE == "DEVELOPMENT":
    from Version_1.Database import database
    from Version_1.logger import logger
else:
    from database import database
    from logger import logger

class NavIDENT(database):
    '''
    导航数据有效性数据库
    '''

    def __init__(self, p_path, p_name, p_type):
        '''
        初始化数据库
        '''

        super(NavIDENT, self).__init__(p_path, p_name, p_type)

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

        AIRAC_CYCLE = data[1][8:-1]
        Date = data[2][10:-1]
        logger.info(r'Navigation IDENT database version: {0}'.format(AIRAC_CYCLE))

        ret_data = {'AIRAC':AIRAC_CYCLE, 'Date': Date}

        return status, msg, ret_data

    def Interface_AIRAC_CYCLE(self):
        '''
        获取导航数据库发布信息
        :return:
        '''

        return True, self._database
