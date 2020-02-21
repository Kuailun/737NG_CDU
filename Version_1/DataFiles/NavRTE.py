# -*- coding: utf-8 -*-
# @File       : NavRTE.py
# @Author     : Yuchen Chai
# @Date       : 2020/1/31 12:54
# @Description:

import settings as ss

if ss.APPLICATION_MODE == "DEVELOPMENT":
    from Version_1.Database import database
    from Version_1.logger import logger
else:
    from database import database
    from logger import logger

class NavRTE(database):
    '''
    Database for routes
    '''

    def __init__(self, p_path, p_name, p_type):
        '''
        initialize the database for routes
        '''

        super(NavRTE, self).__init__(p_path, p_name, p_type)

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

        AIRAC_CYCLE = data[14][1:-2]
        logger.info(r'Navigation RTE database version: {0}'.format(AIRAC_CYCLE))

        # Get data from the file
        data = data[16:]

        split_data = []
        route_data = {}
        fix_data = {}
        # Split route, fix
        for i in range(len(data)-1):
            item = data[i]
            item = item.replace('\n','').split(' ')
            split_data.append(item)

            # Organize the data according to route:
            if item[0] not in route_data:
                route_data[item[0]]=[]
                route_data[item[0]].append(item[2])
                pass
            else:
                route_data[item[0]].append(item[2])
                pass

            # Organize the data according to Fixes:
            if item[2] not in fix_data:
                fix_data[item[2]] = []
                fix_data[item[2]].append(item[0])
                pass
            else:
                fix_data[item[2]].append(item[0])
                pass
            pass

        ret_data = {'AIRAC':AIRAC_CYCLE, 'Raw': split_data, 'Fix': fix_data, 'Route':route_data}

        return status, msg, ret_data

    def Interface_GetRoute(self, target):
        '''
        获取有关目标的全部路径
        :param target:
        :return:
        '''

        if target in self._database['Fix']:
            return True, self._database['Fix'][target]
        else:
            msg = r'所查询的目标Fix不在数据库中: {0}'.format(target)
            logger.warning(msg)
            return False, None

    def Interface_GetFix(self, target):
        '''
        获取有关目标的全部Fix点
        :param target:
        :return:
        '''
        if target in self._database['Route']:
            return True, self._database['Route'][target]
        else:
            msg = r'所查询的目标Route不在数据库中: {0}'.format(target)
            logger.warning(msg)
            return False, None
