#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2021/11/2 21:54
# @Author   :day day up up
# @File     :project_path.py
import os
'''专门读取路径的值'''
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
#测试数据的路径
test_data_path = os.path.join(project_path,"test_data","test_data.xlsx")
#测试报告的路径
test_report_path = os.path.join(project_path,"test_result","html_report","test_api.html")
#配置文件路径
case_config_path = os.path.join(project_path,"conf","case.config")
print(case_config_path)
