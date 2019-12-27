# -*- coding: utf-8 -*-
# @File       : run.py
# @Author     : Yuchen Chai
# @Date       : 2019/12/26 18:20
# @Description: Start File

from Version_1.logger import logger
from Version_1.CDU import CDU
from PyQt5.QtWidgets import *

logger.info('Starting 737NG CDU')

logger.info('Start Detecting Register Check')

if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("FYCYC-CDU-737NG")

    cdu = CDU()
    cdu.show()
    app.exec_()