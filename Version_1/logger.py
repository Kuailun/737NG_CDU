# -*- coding: utf-8 -*-
# @File       : logger.py
# @Author     : Yuchen Chai
# @Date       : 2019/12/19 11:19
# @Description:

import logging
import os
import time
import coloredlogs
from Version_1.settings import LOGGING_CONSOLE_FLAG,LOGGING_FILE_LOG,LOGGING_CURRENT_LEVEL

# -----------------------------------------------------------------------------
# 创建或获取 Logger 实例
# -----------------------------------------------------------------------------
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# 设置日志格式
# -----------------------------------------------------------------------------
fmt = '%(asctime)s - [%(name)s] - %(filename)s [line:%(lineno)d] - %(levelname)s: %(message)s'
formatter = logging.Formatter(fmt)

# -----------------------------------------------------------------------------
# 创建 Handler, 输出日志到控制台和文件
# -----------------------------------------------------------------------------
# 日志文件 FileHandler
basedir = os.path.abspath(os.path.dirname(__file__))
log_dest = os.path.join(basedir, 'Log')  # 日志文件所在目录
if not os.path.isdir(log_dest):
    os.mkdir(log_dest)
filename = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + '.log'  # 日志文件名，以当前时间命名




# -----------------------------------------------------------------------------
# 为 Logger 添加 Handler
# -----------------------------------------------------------------------------
if(LOGGING_FILE_LOG):
    file_handler = logging.FileHandler(os.path.join(log_dest, filename), encoding='utf-8')  # 创建日志文件handler
    file_handler.setFormatter(formatter)  # 设置Formatter
    logger.addHandler(file_handler)
if(LOGGING_CONSOLE_FLAG):
    # 控制台日志 StreamHandler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

# -----------------------------------------------------------------------------
# 设置日志级别
# -----------------------------------------------------------------------------
logger.setLevel(logging.DEBUG)

# -----------------------------------------------------------------------------
# 当日志输出到控制台时，会带有颜色
# -----------------------------------------------------------------------------
coloredlogs.DEFAULT_FIELD_STYLES = dict(
    asctime=dict(color='green'),
    name=dict(color='blue'),
    filename=dict(color='magenta'),
    lineno=dict(color='cyan'),
    levelname=dict(color='black', bold=True),
)

# 设置coloredlogs打印输出等级
if not LOGGING_CONSOLE_FLAG:
    coloredlogs.install(fmt=fmt, level='CRITICAL', logger=logger)
else:
    coloredlogs.install(fmt=fmt, level=LOGGING_CURRENT_LEVEL, logger=logger)
