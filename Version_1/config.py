# -*- coding: utf-8 -*-
# @File       : config.py
# @Author     : Yuchen Chai
# @Date       : 2019/12/26 18:30
# @Description:

from Version_1 import settings as ss
import os
import configparser
from Version_1.logger import logger

class Configuration:
    def __init__(self):
        '''
        Check the direction and file
        '''

        # Initialize the name and path of file
        self.file_name = ss.CONFIG_FILE_NAME
        self.file_path = ss.CONFIG_FILE_PATH + "/" + ss.CONFIG_FILE_NAME

        # Initialize the default content of file
        self._config = self._Configuration_Get_Default_Config_File()

        # If file not existed, create file
        if not os.path.exists(self.file_path):
            logger.info('    Config.ini is not existed, creating a new one')
            self._Configuration_Write_Config_File()
            pass

        # Read in latest file
        self._Configuration_Read_Config_File()
        logger.info('Config.ini loaded successfully')

        pass

    def _Configuration_Get_Default_Config_File(self):
        '''
        Get the default data structure of configuration
        :return:
        '''
        config = configparser.ConfigParser()
        config['App'] = {'Position_X': ss.CDU_POSITION_X,
                         'Position_Y': ss.CDU_POSITION_Y,
                         'Window_Width': ss.CDU_WINDOW_WIDTH,
                         'Window_Height': ss.CDU_WINDOW_HEIGHT}

        return config

    def _Configuration_Write_Config_File(self):
        '''
        Write config file according to input data
        :return:
        '''

        with open(self.file_path,'w') as configfile:
            self._config.write(configfile)
            pass

        pass

    def _Configuration_Read_Config_File(self):
        '''
        Read config file
        :return:
        '''

        # In case the file is not existed
        if not os.path.exists(self.file_path):
            logger.info('Config.ini is not existed, create a new one')
            self._Configuration_Write_Config_File()
            pass

        try:
            config = configparser.ConfigParser()
            config.read(self.file_path)

            self._config['App']['Position_X'] = config['App']['Position_X']
            self._config['App']['Position_Y'] = config['App']['Position_Y']
            self._config['App']['Window_Width'] = config['App']['Window_Width']
            self._config['App']['Window_Height'] = config['App']['Window_Height']

        except Exception:
            logger.warning('Config.ini loss data, recreate the file')

            # Get a new default config structure
            self._config = self._Configuration_Get_Default_Config_File()
            self._Configuration_Write_Config_File()
            self._Configuration_Read_Config_File()
            pass
        pass

    def Configuration_Interface_Set_Config(self, config):
        '''
        Set config file to self._config
        :param config:
        :return:
        '''

        self._config = config
        self._Configuration_Write_Config_File()
        pass

    def Configuration_Interface_Get_Config(self):
        '''
        Get config file from self._config
        :return:
        '''

        return self._config

