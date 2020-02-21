# -*- coding: utf-8 -*-
# @File       : CDU.py
# @Author     : Yuchen Chai
# @Date       : 2019/12/26 18:48
# @Description:

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt,QThread,pyqtSignal
import time
import settings as ss

if ss.APPLICATION_MODE == "DEVELOPMENT":
    from Version_1.logger import logger
    from Version_1.config import Configuration
    from Version_1.dataFile import DataFile
    from Version_1.logic import pageLogic
    from Version_1.logic import drawLogic
    from Version_1 import Utils as ut
    from Version_1 import variable
else:
    from logger import logger
    from config import Configuration
    from dataFile import DataFile
    import pageLogic
    import drawLogic
    import Utils as ut
    import variable

class GridData(QTableWidget):
    def __init__(self):
        QTableWidget.__init__(self)
        self.setWindowTitle("内部开发数据看板")
        self.resize(800,800)
        self.setColumnCount(2)

        self.setColumnWidth(0,300)
        self.setColumnWidth(1,450)


        column_name = ['序号','名称','值']
        self.setHorizontalHeaderLabels(column_name)
        pass

    def update_item_data(self, data):
        """更新内容"""
        self.setRowCount(len(data))
        index = 0
        keys = sorted(data.keys())
        for key in keys:
            if type(data[key]) == int or type(data[key]) == str or type(data[key]) == list or type(data[key]) == dict:
                self.setItem(index, 0, QTableWidgetItem(key))
                self.setItem(index, 1, QTableWidgetItem(str(data[key])))
                index = index + 1
            elif not data[key]:
                self.setItem(index, 0, QTableWidgetItem(key))
                self.setItem(index, 1, QTableWidgetItem(""))
                index = index + 1
        pass
    pass

class UpdateData(QThread):
    """更新数据类"""
    update_date = pyqtSignal(object)  # pyqt5 支持python3的str，没有Qstring

    CDU = None

    def setCDU(self,cdu):
        """
        设置CDU数据
        :param cdu:
        :return:
        """
        self.CDU = cdu

    def run(self):
        while True:
            transmitData = self.assembleData()
            self.update_date.emit(transmitData)  # 发射信号
            time.sleep(0.5)
            pass
        pass

    def assembleData(self):
        """
        准备发送的数据
        :return:
        """
        if self.CDU == None:
            return False,None

        transmitData = self.CDU.dataFile.Interface_DATA_COPY()
        cduData = {
            ss.variable.CDU_WINDOW_TITLE : self.CDU.title,
            ss.variable.CDU_WINDOW_WIDTH : self.CDU.window_width,
            ss.variable.CDU_WINDOW_HEIGHT: self.CDU.window_height,
            ss.variable.CDU_WINDOW_X : self.CDU.window_x,
            ss.variable.CDU_WINDOW_Y : self.CDU.window_y,
            ss.variable.CDU_CURRENT_PAGE : self.CDU.currentPage,
            ss.variable.CDU_CURRENT_PAGE_INDEX : self.CDU.currentPageIndex
        }
        transmitData.update(cduData)
        return transmitData

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

        self.currentPage = variable.page_index.INDEX
        self.currentPageIndex = 1
        self.key = ""
        self.inputLine = ["","",""]
        self.msgFlag = False # True代表消息被清除了，但是不是CLR方式清除的，还需要再CLR一下
        # 0-INPUT, 1-DELETE, 2-MSG
        self.inputDisplayMode = variable.input_line_display_mode.SELFINPUT
        self.lineDisplay = self.ResetLineDisplay()

        # 启动更新线程
        self.gridData = GridData()
        self.update_data_thread = UpdateData()
        self.update_data_thread.setCDU(self)
        self.update_data_thread.update_date.connect(self.gridData.update_item_data)
        self.update_data_thread.start()

        # 右键菜单
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.rightMenuShow)
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

    def rightMenuShow(self):
        """
        右键菜单
        :return:
        """
        try:
            self.contextMenu = QMenu()
            if ss.APPLICATION_MODE == "DEVELOP":
                self.menuData = self.contextMenu.addAction(u'DataTable')
                self.menuData.triggered.connect(self.actionMenuData)
                self.contextMenu.popup(QCursor.pos())
                self.contextMenu.show()
        except Exception as e:
            logger.warning(e)
            pass
        pass

    def actionMenuData(self):
        """
        数据查看器的页面
        :return:
        """
        self.gridData.show()

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

        # 得到当前的显示模式
        self.updateInputLine()

        pageLogic.pageLogic(self)
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
                buttonItem = ss.CDU_KEY_LIST[button]
                if ((mousePosition.x() >= buttonItem[0]) and (mousePosition.x() <= buttonItem[0] + buttonItem[2]) and (mousePosition.y() >= buttonItem[1]) and (mousePosition.y() <= buttonItem[1] + buttonItem[3])):
                    self.key = button
                    pass

        self.repaint()
        pass

    def closeEvent(self,event):
        """
        关闭窗口时的动作
        :param event:
        :return:
        """
        try:
            self.menudata.close()
            self.menudata = None
        except:
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

    def insertMsg(self, msg):
        """
        插入一条msg
        :param msg:
        :return:
        """
        # 插入需要显示的消息
        if len(self.inputLine) >= 3:
            # 逻辑需要
            self.inputLine.append(msg)
            self.msgFlag = True
        pass

    def removeMsg(self):
        """
        移除一条msg
        :return:
        """
        if len(self.inputLine) == 3:
            # 什么都不做
            pass
        elif len(self.inputLine) >= 4:
            self.inputLine.pop()
            pass
        else:
            # 不应该出现该情况
            logger.warning(r"msg系统错误: 删除 {0}".format(self.inputLine[-1]))
            pass
        pass

    def resetInput(self):
        """
        清空输入行
        :return:
        """
        self.inputLine[1] = ""
        self.updateInputLine()
        pass

    def updateInputLine(self):
        """
        更新输入区的显示
        :return:
        """
        # 如果一行的字母过多，则仅保留前24个
        if len(self.inputLine[1]) > 24:
            self.inputLine[1] = self.inputLine[1][0:24]
            pass

        # 如果没有msg，也没有delete，则显示输入行
        if len(self.inputLine) == 3 and self.inputLine[2] == "":
            self.inputLine[0] = self.inputLine[1]
        elif len(self.inputLine) == 3 and self.inputLine[2] == "DELETE":
            self.inputLine[0] = self.inputLine[2]
        elif len(self.inputLine) >= 4:
            self.inputLine[0] = self.inputLine[-1]
            pass

        """当前的显示模式 0-输入，1-DELETE，2-MSG"""
        # 显示自己输入的内容
        if self.inputLine[0] == self.inputLine[1]:
            self.inputDisplayMode = variable.input_line_display_mode.SELFINPUT
        # 显示删除
        elif self.inputLine[0] == "DELETE" and self.inputLine[2] == "DELETE":
            self.inputDisplayMode = variable.input_line_display_mode.DELETE
        # 显示消息
        elif len(self.inputLine) > 3 and self.inputLine[0] == self.inputLine[-1]:
            self.inputDisplayMode = variable.input_line_display_mode.MESSAGE
            pass
        pass


    def UpdateConfig(self):
        '''
        Update the configuration file
        :return:
        '''

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


