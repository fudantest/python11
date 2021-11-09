#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2021/11/2 20:27
# @Author   :day day up up
# @File     :test_http_request.py
import unittest
from tools.http_request import HttpRequest
from tools.get_cookie import GetCookie
from ddt import ddt,data#列表嵌套列表，列表嵌套字典
from tools.do_excel import DoExcel
from tools.project_path import *
from tools.my_log import MyLog
my_logger = MyLog()
test_data = DoExcel(test_data_path).get_data()#执行所有的测试用例
@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    @data(*test_data)
    def test_api(self,item):
        res = HttpRequest.http_request(item["url"],eval(item["data"]),item["http_method"],getattr(GetCookie,"Cookie"))
        if res.cookies:
            setattr(GetCookie,"Cookie",res.cookies)
        try:
            self.assertEqual(str(item["expected"]),res.json()["statusCode"])#断言
            TestResult = "PASS"#测试执行结果
        except AssertionError as e:
            TestResult = "FAIL"
            my_logger.error("执行用例出错{0}".format(e))
            raise e
        finally:
            DoExcel(test_data_path).write_back(item["sheet_name"],item["case_id"] + 1,str(res.json()),TestResult)#写回excel数据
            my_logger.info("获取到的结果是:{0}".format(res.json()))
if __name__ == '__main__':
    TestHttpRequest().test_api()