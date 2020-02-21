# -*- coding: utf-8 -*-
# @File       : run.py
# @Author     : Yuchen Chai
# @Date       : 2019/12/26 18:20
# @Description: Start File

from PyQt5.QtWidgets import *
import sys
import settings as ss

if ss.APPLICATION_MODE == "DEVELOPMENT":
    from Version_1.logger import logger
    from Version_1.CDU import CDU
else:
    from logger import logger
    from CDU import CDU

logger.info('启动 FYCYC-737NG-CDU程序')

logger.info('检测用户注册状态')

if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("FYCYC-CDU-737NG")

    cdu = CDU()
    cdu.show()
    sys.exit(app.exec_())