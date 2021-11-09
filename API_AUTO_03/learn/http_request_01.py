#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2021/10/31 21:24
# @Author   :day day up up
# @File     :http_request_01.py
import requests
class HttpRequest:
    def http_request(self,url,data,http_method,cookie = None):
        try:
            if http_method.upper() == "GET":
                res = requests.get(url,data,cookies = cookie)
            elif http_method.upper() == "POST":
                res = requests.post(url,data,cookies = cookie)
            else:
                print("输入的请求方法错误")
        except Exception as e:
            print("请求报错了{}".format(e))
            raise e
        return res
if __name__ == '__main__':
    #注册
    register_url = "https://www.apishop.net/common/Guest/mailRegister"
    register_data = {"userMail":"xuezheng0008@126.com","userPassword":"913f3aa5ccc179140d8352b3e766e644"}
    # register_res = requests.post(register_url,register_data)
    # print("text的解析结果：",register_res.text)
    # print("json的解析结果：",register_res.json())
    # print(register_res.status_code)

    #成功登录：需要拿到请求头中的verifyCode，作为输入参数
    session = requests.session()
    session.headers['cookie'] = 'gr_user_id=151ec259-b48c-4402-b137-5294bcb706b3; gr_session_id_9944ca777cab9409=281d333a-5a9a-4c4d-9612-f04de88f9647; gr_session_id_9944ca777cab9409_281d333a-5a9a-4c4d-9612-f04de88f9647=true; verifyCode=7d277af1e4cf45baf920474ebba56bd9'
    # print(session.headers['cookie'].split("=")[-1])
    login_url = "https://www.apishop.net/common/Guest/login"
    login_data = {"loginCall":"xuezheng08@126.com","loginPassword":"913f3aa5ccc179140d8352b3e766e644","verifyCode":"cookie_dict.split('=')[-1]"}

    #查询
    search_url = "https://www.apishop.net/apiStore/Product/searchProduct"
    search_data = {"keyWord": "短信服务","page": "1"}

    #新增ip
    add_ip_url = "https://www.apishop.net/apiStore/IPConfig/addIPConfigGroup"
    add_ip_data = {"groupName": "test03", "ipList": "192.0.0.3"}

    login_res = HttpRequest().http_request(login_url,login_data,'get')
    print(login_data)
    print(login_res.json())
    # search_res = HttpRequest().http_request(search_url,search_data,'post',login_res.cookies)
    # print(search_res.json())
    # add_ip_res = HttpRequest().http_request(add_ip_url,add_ip_data,'post',login_res.cookies)
    # print(add_ip_res.json())

