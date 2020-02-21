# -*- coding: utf-8 -*-
# @File       : database.py
# @Author     : Yuchen Chai
# @Date       : 2019/12/26 18:30
# @Description:

import os
import settings as ss

if ss.APPLICATION_MODE == "DEVELOPMENT":
    from Version_1.logger import logger
else:
    from logger import logger

class database:
    '''
    数据库类的基类，用于连接不同的数据库(Mongodb, txt, excel等等)
    '''

    def __init__(self, p_path, p_name, p_type):
        '''
        初始化数据基类
        :param p_path: 数据库保存路径
        :param p_name: 数据库名称
        :param p_type: 数据库类型（Mongodb, txt, excel等）
        '''

        self._path = p_path
        self._name = p_name
        self._type = p_type
        self._database_path = p_path + p_name + "." + p_type
        self._database_available = True


        pass

    def _Database_Path_Existing(self, createFile):
        '''
        检查数据库文件是否存在
        :return:
        '''

        # 检查数据库的路径是否存在
        if not os.path.exists(self._database_path):
            logger.info(r"{0} 不存在，开始创建".format(self._name))

            # Whether need to create file
            if not createFile:
                return False
            else:
                self._Database_CreateFile()
            pass
        else:
            pass
        return True

    def _Database_CreateFile(self):
        '''
        创建数据库
        :return:
        '''
        raise("_Database_CreateFile函数未初始化")

    def _Database_ReadFile(self):
        '''
        Get data from file
        :return:
        '''
        raise("_Database_ReadFile not initialized yet")