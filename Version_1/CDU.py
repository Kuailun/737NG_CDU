# -*- coding: utf-8 -*-
# @File       : CDU.py
# @Author     : Yuchen Chai
# @Date       : 2019/12/26 18:48
# @Description:

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt,QRectF
from Version_1.logger import logger
from Version_1 import settings as ss
from Version_1.config import Configuration
from Version_1.dataFile import DataFile
from Version_1.logic import pageLogic
from Version_1.logic import drawLogic


class CDU(QWidget):
    def __init__(self, *args, **kwargs):
        '''
        Initialize the database and read in configs
        :param args:
        :param kwargs:
        '''
        super().__init__()

        logger.info('开始加载配置文件')
        # Configuration Instance
        self.configuration = Configuration()
        # Config Data Structure
        self.config = self.configuration.Configuration_Interface_Get_Config()

        logger.info('开始加载数据库')
        # Datafile
        self.dataFile = DataFile()



        logger.info('启动FYCYC-CDU')

        self.title = ss.CDU_WINDOW_TITLE
        self.imagePath = ss.CDU_WINDOW_BACKGROUND
        self.window_width = int(self.config['App']['Window_Width'])
        self.window_height = int(self.config['App']['Window_Height'])
        self.window_x = int(self.config['App']['Position_X'])
        self.window_y = int(self.config['App']['Position_Y'])
        self.window_background_pxmap = QPixmap(self.imagePath)

        self.currentPage = ss.pageIndex.INDEX
        self.currentPageIndex = 1
        self.key = ""
        self.inputLine = ["","","",""]
        self.delFlag = False
        self.lineDisplay = self.ResetLineDisplay()

        # Initialize the UI
        self.initUI()

        pass

    def initUI(self):
        '''
        Initialize the UI
        :return:
        '''

        self.setWindowTitle(self.title)

        self.setFixedSize(self.window_width,self.window_height)
        self.move(self.window_x,self.window_y)
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

        # Draw the background image
        painter.drawPixmap(0,0,self.window_width,self.window_height,self.window_background_pxmap)

        pageLogic.pageLocig(self)
        drawLogic.pageDraw(self,painter)
        self.key = ""

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
        pass

    def moveEvent(self,event):
        '''
        Customized move event
        :param event:
        :return:
        '''

        self.window_x = self.frameGeometry().x()
        self.window_y = self.frameGeometry().y()

        # Update the config file
        self.UpdateConfig()

    def mousePressEvent(self, event):
        '''
        Customized mouse click event
        :param event:
        :return:
        '''

        # Get mouse position
        mousePosition = event.windowPos()
        print("{0}, {1}".format(mousePosition.x(), mousePosition.y()))

        # Leftbutton event
        if event.buttons() == Qt.LeftButton:
            for button in ss.CDU_KEY_LIST:
                button = ss.CDU_KEY_LIST[button]
                if ((mousePosition.x() >= button[0]) and (mousePosition.x() <= button[0] + button[2]) and (mousePosition.y() >= button[1]) and (mousePosition.y() <= button[1] + button[3])):
                    self.key = button[4]
                    pass

        self.repaint()
        pass

    def ResetLineDisplay(self):
        """
        重置屏幕的显示
        :return:
        """
        lineDisplay = {"L0M": None,"L1M": None,"L2M": None,"L3M": None,"L4M": None,"L5M": None,"L6M": None,"L7M": None,
            "R0M": None,"R1M": None,"R2M": None,"R3M": None,"R4M": None,"R5M": None,"R6M": None,"R7M": None,
            "L1S": None,"L2S": None,"L3S": None,"L4S": None,"L5S": None,"L6S": None,
            "R1S": None,"R2S": None,"R3S": None,"R4S": None,"R5S": None,"R6S": None
        }
        return lineDisplay



    def UpdateConfig(self):
        '''
        Update the configuration file
        :return:
        '''

        # self.config['App']['Window_Width'] = str(self.window_width)
        # self.config['App']['Window_Height'] = str(self.window_height)
        self.config['App']['Position_X'] = str(self.window_x)
        self.config['App']['Position_Y'] = str(self.window_y)

        # Write content to ini
        self.configuration.Configuration_Interface_Set_Config(self.config)

        pass

    def DrawLine(self, painter, contentPlace, content):
        '''
        根据页面、配置、状态不同，绘制一行
        :param painter: 绘制句柄
        :param contentPlace: 标注绘制的位置：L1, L2... R1, R2...
        :param content: 数组形式的内容
        :return:
        '''

        # 获得绘制的位置
        horrizontalPlace = contentPlace[0]
        verticalPlace = int(contentPlace[1])
        # 主要行（M），子行（S），底部输入板（I）
        typePlace = contentPlace[2]

        # 绘制正常行
        if horrizontalPlace == "L" and typePlace == "M":
            startingPostion = ss.POS_CDU_CONTENT_LINE[horrizontalPlace][verticalPlace]
            horizontalOffset = 0
            for i in range(len(content)):
                painter.setPen(content[i]['Color'])

                # 设置特殊定义的字体
                if "Font" in content[i]:
                    painter.setFont(content[i]["Font"])
                    pass
                else:
                    painter.setFont(ss.FONT_CDU_TITLE_NORMAL)
                    pass

                for j in range(len(content[i]['Content'])):
                    painter.drawText(horizontalOffset+startingPostion[0],startingPostion[1],content[i]['Content'][j])
                    horizontalOffset = horizontalOffset + 16
                    pass

                pass
        # 绘制右侧正常行
        elif horrizontalPlace == "R" and typePlace == "M":
            startingPostion = ss.POS_CDU_CONTENT_LINE[horrizontalPlace][verticalPlace]
            horizontalOffset = 0
            for i in range(len(content)):
                horizontalOffset = horizontalOffset - len(content[i]["Content"]) * 16
                pass

            for i in range(len(content)):
                painter.setPen(content[i]['Color'])

                # 设置特殊定义的字体
                if "Font" in content[i]:
                    painter.setFont(content[i]["Font"])
                    pass
                else:
                    painter.setFont(ss.FONT_CDU_TITLE_NORMAL)
                    pass

                for j in range(len(content[i]['Content'])):
                    painter.drawText(horizontalOffset+startingPostion[0],startingPostion[1],content[i]['Content'][j])
                    horizontalOffset = horizontalOffset + 16
                    pass
                pass
            pass

        # 绘制左侧子行
        elif horrizontalPlace == "L" and typePlace == "S":
            key = horrizontalPlace + typePlace
            startingPostion = ss.POS_CDU_CONTENT_LINE[key][verticalPlace]
            horizontalOffset = 1
            for i in range(len(content)):
                painter.setPen(content[i]['Color'])

                # 设置特殊定义的字体
                if "Font" in content[i]:
                    painter.setFont(content[i]["Font"])
                    pass
                else:
                    painter.setFont(ss.FONT_CDU_TITLE_SMALL)
                    pass

                for j in range(len(content[i]['Content'])):
                    painter.drawText(horizontalOffset+startingPostion[0],startingPostion[1],content[i]['Content'][j])
                    horizontalOffset = horizontalOffset + 16
                    pass
            pass

        # 绘制右侧子行
        elif horrizontalPlace == "R" and typePlace == "S":
            key = horrizontalPlace + typePlace
            startingPostion = ss.POS_CDU_CONTENT_LINE[key][verticalPlace]
            horizontalOffset = 2
            for i in range(len(content)):
                horizontalOffset = horizontalOffset - len(content[i]["Content"]) * 16
                horizontalOffset = horizontalOffset - 16
                pass
            horizontalOffset = horizontalOffset + 16

            for i in range(len(content)):
                painter.setPen(content[i]['Color'])

                # 设置特殊定义的字体
                if "Font" in content[i]:
                    painter.setFont(content[i]["Font"])
                    pass
                else:
                    painter.setFont(ss.FONT_CDU_TITLE_SMALL)
                    pass

                for j in range(len(content[i]['Content'])):
                    painter.drawText(horizontalOffset+startingPostion[0],startingPostion[1],content[i]['Content'][j])
                    horizontalOffset = horizontalOffset + 16
                    pass
                pass
            pass


