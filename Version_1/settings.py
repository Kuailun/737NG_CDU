# -*- coding: utf-8 -*-
# @File       : settings.py
# @Author     : Yuchen Chai
# @Date       : 2019/12/26 18:21
# @Description: Gerneral Settings

import os

# -----------------------------------------------------------------------------
# Settings for application
# -----------------------------------------------------------------------------
APPLICATION_PATH = os.path.dirname(os.path.realpath(__file__))
APPLICATION_IMAGE_PATH = APPLICATION_PATH + '/Img/'


# -----------------------------------------------------------------------------
# Settings for config
# -----------------------------------------------------------------------------
CONFIG_FILE_NAME = 'config.ini'
CONFIG_FILE_PATH = APPLICATION_PATH


# -----------------------------------------------------------------------------
# Settings for logger
# -----------------------------------------------------------------------------
# Whether print to console
LOGGING_CONSOLE_FLAG = True

# Whether output to file
LOGGING_FILE_LOG = True

# Level of output
LOGGING_LEVEL = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
LOGGING_CURRENT_LEVEL = LOGGING_LEVEL[0]


# -----------------------------------------------------------------------------
# Settings for CDU
# -----------------------------------------------------------------------------
CDU_WINDOW_TITLE = "FYCYC-CDU-737NG"
CDU_WINDOW_BACKGROUND = APPLICATION_IMAGE_PATH + 'PRO20Series-737NG-CDU.jpg'
CDU_POSITION_X = 200
CDU_POSITION_Y = 200
CDU_WINDOW_WIDTH = 581
CDU_WINDOW_HEIGHT = 900