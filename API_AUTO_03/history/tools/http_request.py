#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2021/10/21 15:01
# @Author   :day day up up
# @File     :http_request.py
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2021/10/20 19:53
# @Author   :day day up up
# @File     :http_request.py
import requests
class HttpRequest:
    '''利用requests封装http的get、post请求'''
    def http_request(self,url,data,method,cookie=None):
        '''url:请求的地址
           data：请求数据,非必填，以字典形式传输
           method:请求方式支持get、post请求，以字符换形式传输
           cookies：请求的cookies数据'''
        if method.lower() == "get":
            res = requests.get(url, data,cookies=cookie)
        else:
            res = requests.post(url, data,cookies=cookie)
        return res
if __name__ == '__main__':
    #登录：post请求
    url = "http://123.57.77.6:8090/user/login"
    data = {"name": "testyue01", "password": "123456"}
    login_res = HttpRequest().http_request(url,data,"post")
    print("登录响应正文：",login_res.text)
    #获取列表信息：get请求
    list_url="http://123.57.77.6:8090/project/list?sbdoctimestamps=1634800445916"
    list_data = {"sbdoctimestamps":"634800445916"}
    list_res = HttpRequest().http_request(list_url,list_data,"post",login_res.cookies)
    print("项目列表响应正文：",list_res.text)
