# -*- coding: utf-8 -*-
# @File       : settings.py
# @Author     : Yuchen Chai
# @Date       : 2019/12/26 18:21
# @Description: Gerneral Settings

import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import QRectF
import variable

# -----------------------------------------------------------------------------
# Settings for application
# -----------------------------------------------------------------------------
APPLICATION_PATH = os.path.dirname(os.path.realpath(__file__))
APPLICATION_IMAGE_PATH = APPLICATION_PATH + '/Resource/Img/'
# 开发用Develop，生成时用Generate
APPLICATION_MODE_SELECTION = {"DEVELOP","GENERATE"}
APPLICATION_MODE = "DEVELOP"
sys.path.append(APPLICATION_PATH+"/")
sys.path.append(APPLICATION_PATH+"/logic")
sys.path.append(APPLICATION_PATH+"/DataFiles")


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
LOGGING_CURRENT_LEVEL = variable.logging_level.DEBUG

# -----------------------------------------------------------------------------
# Settings for CDU
# -----------------------------------------------------------------------------
CDU_WINDOW_TITLE = "FYCYC-CDU-737NG"
CDU_WINDOW_BACKGROUND = APPLICATION_IMAGE_PATH + 'PRO20Series-737NG-CDU.jpg'
CDU_POSITION_X = 200
CDU_POSITION_Y = 200
CDU_WINDOW_WIDTH = 581
CDU_WINDOW_HEIGHT = 900
CDU_KEY_LIST = {
    variable.key_press_content.L1: [9, 116, 40, 28],
    variable.key_press_content.L2: [9, 156, 40, 28],
    variable.key_press_content.L3: [9, 196, 40, 28],
    variable.key_press_content.L4: [9, 236, 40, 28],
    variable.key_press_content.L5: [9, 276, 40, 28],
    variable.key_press_content.L6: [9, 316, 40, 28],
    variable.key_press_content.R1: [534, 116, 40, 28],
    variable.key_press_content.R2: [534, 156, 40, 28],
    variable.key_press_content.R3: [534, 196, 40, 28],
    variable.key_press_content.R4: [534, 236, 40, 28],
    variable.key_press_content.R5: [534, 276, 40, 28],
    variable.key_press_content.R6: [534, 316, 40, 28],
    variable.key_press_content.INIT_REF: [71, 436, 57, 38],
    variable.key_press_content.RTE: [143, 436, 57, 38],
    variable.key_press_content.CLB: [214, 436, 57, 38],
    variable.key_press_content.CRZ: [286, 436, 57, 38],
    variable.key_press_content.DES: [358, 436, 57, 38],
    variable.key_press_content.MENU: [71, 489, 57, 38],
    variable.key_press_content.LEGS: [143, 489, 57, 38],
    variable.key_press_content.DEPARR: [214, 489, 57, 38],
    variable.key_press_content.HOLD: [286, 489, 57, 38],
    variable.key_press_content.PROG: [358, 489, 57, 38],
    variable.key_press_content.N1_LIMIT: [71, 540, 57, 38],
    variable.key_press_content.FIX: [143, 540, 57, 38],
    variable.key_press_content.PREV_PAGE: [71, 593, 57, 38],
    variable.key_press_content.NEXT_PAGE: [143, 593, 57, 38],
    variable.key_press_content.EXECUTE: [450, 500, 57, 26],
    variable.key_press_content.BRTD: [450, 436, 24, 38],
    variable.key_press_content.BRTU: [485, 436, 24, 38],
    variable.key_press_content.ONE: [67, 657, 33, 30],
    variable.key_press_content.TWO: [122, 657, 33, 30],
    variable.key_press_content.THREE: [179, 657, 33, 30],
    variable.key_press_content.FOUR: [67, 713, 33, 30],
    variable.key_press_content.FIVE: [122, 713, 33, 30],
    variable.key_press_content.SIX: [179, 713, 33, 30],
    variable.key_press_content.SEVEN: [67, 771, 33, 30],
    variable.key_press_content.EIGHT: [122, 771, 33, 30],
    variable.key_press_content.NINE: [179, 771, 33, 30],
    variable.key_press_content.DOT: [67, 830, 33, 30],
    variable.key_press_content.ZERO: [122, 830, 33, 30],
    variable.key_press_content.PLUS_SUBSTRACT: [179, 830, 33, 30],
    variable.key_press_content.A: [241, 548, 37, 37],
    variable.key_press_content.B: [298, 548, 37, 37],
    variable.key_press_content.C: [356, 548, 37, 37],
    variable.key_press_content.D: [414, 548, 37, 37],
    variable.key_press_content.E: [472, 548, 37, 37],
    variable.key_press_content.F: [241, 603, 37, 37],
    variable.key_press_content.G: [298, 603, 37, 37],
    variable.key_press_content.H: [356, 603, 37, 37],
    variable.key_press_content.I: [414, 603, 37, 37],
    variable.key_press_content.J: [472, 603, 37, 37],
    variable.key_press_content.K: [241, 658, 37, 37],
    variable.key_press_content.L: [298, 658, 37, 37],
    variable.key_press_content.M: [356, 658, 37, 37],
    variable.key_press_content.N: [414, 658, 37, 37],
    variable.key_press_content.O: [472, 658, 37, 37],
    variable.key_press_content.P: [241, 714, 37, 37],
    variable.key_press_content.Q: [298, 714, 37, 37],
    variable.key_press_content.R: [356, 714, 37, 37],
    variable.key_press_content.S: [414, 714, 37, 37],
    variable.key_press_content.T: [472, 714, 37, 37],
    variable.key_press_content.U: [241, 770, 37, 37],
    variable.key_press_content.V: [298, 770, 37, 37],
    variable.key_press_content.W: [356, 770, 37, 37],
    variable.key_press_content.X: [414, 770, 37, 37],
    variable.key_press_content.Y: [472, 770, 37, 37],
    variable.key_press_content.Z: [241, 827, 37, 37],
    variable.key_press_content.SPACE: [298, 827, 37, 37],
    variable.key_press_content.DELETE: [356, 827, 37, 37],
    variable.key_press_content.SLASH: [414, 827, 37, 37],
    variable.key_press_content.CLEAR: [472, 827, 37, 37]
}

# -----------------------------------------------------------------------------
# Font for CDU
# -----------------------------------------------------------------------------
# FONT_CDU_TITLE_NORMAL = QFont("Roboto Mono Medium", 18)
FONT_CDU_TITLE_NORMAL = QFont("Roboto Mono Medium", 18)
FONT_CDU_TITLE_SMALL = QFont("Roboto Mono Medium", 14)

# -----------------------------------------------------------------------------
# Color for CDU
# -----------------------------------------------------------------------------
COLOR_WHITE = QColor(230,230,230)
COLOR_WEAK_WHITE = QColor(115,115,115)
COLOR_CYAN = QColor(0,255,255)
COLOR_GREEN = QColor(0,255,0)
COLOR_MAGENTA = QColor(255,0,204)

# -----------------------------------------------------------------------------
# Position for CDU
# -----------------------------------------------------------------------------
POS_CDU_TITLE_MIDDLE = QRectF(94.0, 50.0, 394.0, 32.0)
POS_CDU_TITLE_LEFT = QRectF(198.0,50.0,287.0,32.0)
POS_CDU_TITLE_PAGE_LEFT = QRectF(412.0,56.0,70.0,20.0)
POS_CDU_TITLE_ACT_LEFT = QRectF(136.0,50.0,394.0,32.0)
POS_CDU_CONTENT_LINE = {
    "L":[
        [100.0, 79.0, 180.0, 32.0],
        [100.0, 139.0, 180.0, 32.0],
        [100.0, 179.0, 180.0, 32.0],
        [100.0, 219.0, 180.0, 32.0],
        [100.0, 259.0, 180.0, 32.0],
        [100.0, 299.0, 180.0, 32.0],
        [100.0, 339.0, 180.0, 32.0],
        [100.0, 361.0, 180.0, 32.0],
    ],
    "R":[
        None,
        [484.0, 139.0, 180.0, 32.0],
        [484.0, 179.0, 180.0, 32.0],
        [484.0, 219.0, 180.0, 32.0],
        [484.0, 259.0, 180.0, 32.0],
        [484.0, 299.0, 180.0, 32.0],
        [484.0, 339.0, 180.0, 32.0],
    ],
    "LS":[
        None,
        [100.0, 119.0, 180.0, 20.0],
        [100.0, 159.0, 180.0, 32.0],
        [100.0, 199.0, 180.0, 32.0],
        [100.0, 239.0, 180.0, 32.0],
        [100.0, 279.0, 180.0, 32.0],
        [100.0, 319.0, 180.0, 32.0],
    ],
    "RS":[
        [484.0, 79.0, 180.0, 20.0],
        [484.0, 119.0, 180.0, 20.0],
        [484.0, 159.0, 180.0, 32.0],
        [484.0, 199.0, 180.0, 32.0],
        [484.0, 239.0, 180.0, 32.0],
        [484.0, 279.0, 180.0, 32.0],
        [484.0, 319.0, 180.0, 32.0],
    ],
}


# -----------------------------------------------------------------------------
# Variables for CDU
# -----------------------------------------------------------------------------
class variable:

    CDU_WINDOW_TITLE = "CDU_WINDOW_TITLE"
    CDU_WINDOW_WIDTH = "CDU_WINDOW_WIDTH"
    CDU_WINDOW_HEIGHT = "CDU_WINDOW_HEIGHT"
    CDU_WINDOW_X = "CDU_WINDOW_X"
    CDU_WINDOW_Y = "CDU_WINDOW_Y"
    CDU_CURRENT_PAGE = "CDU_CURRENT_PAGE"
    CDU_CURRENT_PAGE_INDEX = "CDU_CURRENT_PAGE_INDEX"



    IDENT_MODEL = "IDENT_MODEL"
    IDENT_ENG_RATING = "IDENT_ENG_RATING"
    IDENT_NAV_DATA_RELEASE = "IDENT_NAV_DATA_RELEASE"
    IDENT_NAV_ACTIVE = "IDENT_NAV_ACTIVE"

    PERF_COST_INDEX = "PERF_COST_INDEX"
    PERF_GROSS_WEIGHT = "PERF_GROSS_WEIGHT"
    PERF_CRUISE_CENTER_OF_GRAVITY = "PERF_CRUISE_CENTER_OF_GRAVITY"
    PERF_FUEL = "PERF_FUEL"
    PERF_ZERO_FUEL_WEIGHT = "PERF_ZERO_FUEL_WEIGHT"

    RTE_ORIGIN = "RTE_ORIGIN"
    RTE_ORIGIN_LOCATION = "RTE_ORIGIN_LOCATION"
    RTE_DEST = "RTE_DEST"
    RTE_DEST_LOCATION = "RTE_DEST_LOCATION"
    RTE_RUNWAY = "RTE_RUNWAY"

    DEPARR_DEP_AIRPORTS_DATA = "DEPARR_DEP_AIRPORTS_DATA"        # 离场机场的全部导航数据
    DEPARR_DEP_PAGE_FLAG = "DEPARR_DEP_PAGE_FLAG"                # 在DEPARR页面是否可以进入DEPARTURE的标志

    DEPARTURES_SID = "DEPARTURES_SID"              # 在DEPARTURE页面选定的SID的长期储存结果，用于标明ACT
    DEPARTURES_SID_TEMP = "DEPARTURES_SID_TEMP"         # 在DEPARTURE页面用户临时选定SID的结果，用于更改显示
    DEPARTURES_TRANSITION = "DEPARTURES_TRANSITION"       # 在DEPARTURE页面选定的Transition的长期储存结果，用于标明ACT
    DEPARTURES_TRANSITION_TEMP = "DEPARTURES_TRANSITION_TEMP"  # 在DEPARTURE页面用户临时选定Transition的结果，用于更改显示
    DEPARTURES_RUNWAY = "DEPARTURES_RUNWAY"           # 在DEPARTURE页面选定的SID的长期储存结果，用于标明ACT
    DEPARTURES_RUNWAY_TEMP = "DEPARTURES_RUNWAY_TEMP"      # 在DEPARTURE页面用户临时选定Runway的结果，用于更改显示
    DEPARTURES_KEY_PRESSED = "DEPARTURES_KEY_PRESSED"          # 在DEPARTURES页面按下按键的标志

    POS_REF_AIRPORT = "POS_REF_AIRPORT" # POS INIT页面REF AIRPORT数据
    POS_REF_GATE = "POS_REF_GATE"       # POS INIT页面REF GATE

    pass

# -----------------------------------------------------------------------------
# Messages for CDU
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Messages for CDU
# -----------------------------------------------------------------------------
class message:
    INVALID_ENTRY = "INVALID_ENTRY"
    INVALID_DELETE = "INVALID_DELETE"
    RUNWAY_NA_FOR_SID = "RUNWAY N/A FOR SID"
    NOT_IN_DATA_BASE = "NOT IN DATA BASE"
    pass