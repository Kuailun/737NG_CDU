# -*- coding: utf-8 -*-
# @File       : variable.py
# @Author     : Yuchen Chai
# @Date       : 2020/2/15 15:37
# @Description:

# -----------------------------------------------------------------------------
# 变量枚举范围
# -----------------------------------------------------------------------------

"""logging日志的记录等级"""
class logging_level():
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = "ERROR"
    CRITICAL = 'CRITICAL'
    pass

"""按键按下后key的内容"""
class key_press_content():
    L1 = "L1"
    L2 = "L2"
    L3 = "L3"
    L4 = "L4"
    L5 = "L5"
    L6 = "L6"
    R1 = "R1"
    R2 = "R2"
    R3 = "R3"
    R4 = "R4"
    R5 = "R5"
    R6 = "R6"
    INIT_REF = "INIT"
    RTE = "RTE"
    CLB = "CLB"
    CRZ = "CRZ"
    DES = "DES"
    MENU = "MENU"
    LEGS = "LEGS"
    DEPARR = "DEPARR"
    HOLD = "HOLD"
    PROG = "PROG"
    N1_LIMIT = "N1"
    FIX = "FIX"
    PREV_PAGE = "PREV"
    NEXT_PAGE = "NEXT"
    BRTD = "BRT-"
    BRTU = "BRT+"
    EXECUTE = "EXEC"
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    ZERO = "0"
    DOT = "."
    PLUS_SUBSTRACT = "-"
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    H = "H"
    I = "I"
    J = "J"
    K = "K"
    L = "L"
    M = "M"
    N = "N"
    O = "O"
    P = "P"
    Q = "Q"
    R = "R"
    S = "S"
    T = "T"
    U = "U"
    V = "V"
    W = "W"
    X = "X"
    Y = "Y"
    Z = "Z"
    SPACE = " "
    DELETE = "DELETE"
    SLASH = "/"
    CLEAR = "CLR"
    pass

"""页面编号"""
class page_index:
    INDEX = "INDEX"
    IDENT = "IDENTIFICATION"
    POS = "POSITION"
    PERF = "PERFORMANCE"
    TAKEOFF = "TAKEOFF"
    APPROACH = "APPROACH"
    OFFSET = "OFFSET"
    ROUTE = "ROUTE"
    N1 = "N1 LIMIT"
    PROGRESS = "PROGRESS"
    CLB = "CLIMB"
    CRZ = "CRUISE"
    DES = "DESCEND"
    LEGS = "LEGS"
    DEPARR = "DEPARR"
    HOLD = "HOLD"
    FIX = "FIX"
    DEPARTURES = "DEPARTURES"

    LOGO = "LOGO"
    pass

"""当前输入行的显示模式"""
class input_line_display_mode:
    SELFINPUT = 0
    DELETE = 1
    MESSAGE = 2
    pass

"""当前输入行的显示模式"""
class line_select_mode:
    INPUT_DELETE = 0
    PAGE = 1
    pass

"""变量的类型"""
class variable_type:
    INTEGER = 0
    FLOAT = 1
    STRING = 2
    pass

"""经纬度类型区分"""
class variable_coordination_type:
    LATITUDE = 0
    LONGITUDE = 1




"""COST INDEX的允许输入最大值最小值"""
class Limit_COST_INDEX:
    MIN = 0
    MAX = 500.0
    pass

"""GROSS WEIGHT的允许输入最大值最小值"""
class Limit_GROSS_WEIGHT:
    MIN = None
    MAX = 999.9
    pass

"""CENTER OF GRAVITY的允许输入最大值最小值"""
class Limit_CRUISE_CENTER_OF_GRAVITY:
    MIN = 6.0
    MAX = 33.0
    pass