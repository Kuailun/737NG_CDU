# -*- coding: utf-8 -*-
# @File       : CDU.py
# @Author     : Yuchen Chai
# @Date       : 2019/12/26 18:48
# @Description:

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Version_1.logger import logger
from Version_1 import settings as ss
from Version_1.config import Configuration

class CDU(QWidget):
    def __init__(self, *args, **kwargs):
        '''
        Initialize the database and read in configs
        :param args:
        :param kwargs:
        '''
        super().__init__()

        logger.info('Start Reading Config')
        # Configuration Instance
        self.configuration = Configuration()
        # Config Data Structure
        self.config = self.configuration.Configuration_Interface_Get_Config()

        logger.info('Start Reading Database')

        logger.info('Start Running Simulator')

        self.title = ss.CDU_WINDOW_TITLE
        self.imagePath = ss.CDU_WINDOW_BACKGROUND
        self.window_width = int(self.config['App']['Window_Width'])
        self.window_height = int(self.config['App']['Window_Height'])
        self.window_x = int(self.config['App']['Position_X'])
        self.window_y = int(self.config['App']['Position_Y'])
        self.window_background_pxmap = QPixmap(self.imagePath)




        # Initialize the UI
        self.initUI()

        pass

    def initUI(self):
        '''
        Initialize the UI
        :return:
        '''

        self.setWindowTitle(self.title)

        self.resize(self.window_width,self.window_height)
        pass

    def update(self):
        '''
        Update the UI
        :return:
        '''


    def paintEvent(self, event):
        '''
        Customized paint event
        :param event:
        :return:
        '''

        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.drawPixmap(0,0,self.window_width,self.window_height,self.window_background_pxmap)

        pass

    def resizeEvent(self,event):
        '''
        Customized resize event
        :param event:
        :return:
        '''

        self.window_width = self.frameGeometry().width()
        self.window_height = self.frameGeometry().height()-30

        # Update the config file
        self.UpdateConfig()


    def UpdateConfig(self):
        '''
        Update the configuration file
        :return:
        '''

        self.config['App']['Window_Width'] = str(self.window_width)
        self.config['App']['Window_Height'] = str(self.window_height)
        self.config['App']['Position_X'] = str(self.window_x)
        self.config['App']['Position_Y'] = str(self.window_y)

        # Write content to ini
        self.configuration.Configuration_Interface_Set_Config(self.config)

        pass