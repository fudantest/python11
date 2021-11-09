#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2021/10/26 19:52
# @Author   :day day up up
# @File     :run.py
from tools.http_request import HttpRequest
from tools.do_excel import DoExcel
from tools.test_http_request import TestHttpRequest
import HTMLTestRunnerNew
import unittest
from tools.project_path import *
suite = unittest.TestSuite()
loader = unittest.TestLoader()
# suite.addTest(TestHttpRequest("test_api"))
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))
with open(test_report_path,"wb") as file:
#执行用例
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, title="单元测试报告", description="接口测试")
    runner.run(suite)