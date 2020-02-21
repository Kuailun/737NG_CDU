# -*- coding: utf-8 -*-
# @File       : test.py
# @Author     : Yuchen Chai
# @Date       : 2020/1/31 14:05
# @Description:

from dataFile import DataFile

TEST_TARGET = "Class"

if TEST_TARGET == "":
    print("开始测试，请选择测试内容")
    pass
elif TEST_TARGET == "NavRTE":
    mDataFile = DataFile()
    print(mDataFile.Interface_RTE_ROUTE_FIX("W577", "DBL"))
    print(mDataFile.Interface_RTE_START_END("VMB", "DALIM"))
    pass
elif TEST_TARGET == "Class":
    class variable:
        mVariable="mVariable"
        pass

    print(variable.mVariable)
    pass