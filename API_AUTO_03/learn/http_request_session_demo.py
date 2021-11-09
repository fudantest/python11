#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2021/11/1 19:29
# @Author   :day day up up
# @File     :http_request_session_demo.py
import requests
class HttpRequest:
    #成功登录：需要拿到请求头中的verifyCode，作为输入参数
    session = requests.session()
    session.headers['cookie'] = 'gr_user_id=151ec259-b48c-4402-b137-5294bcb706b3; gr_session_id_9944ca777cab9409=281d333a-5a9a-4c4d-9612-f04de88f9647; gr_session_id_9944ca777cab9409_281d333a-5a9a-4c4d-9612-f04de88f9647=true; verifyCode=7d277af1e4cf45baf920474ebba56bd9'
    print(session.headers['cookie'].split("=")[-1])
    login_url = "https://www.apishop.net/common/Guest/login"
    login_data = {"loginCall":"xuezheng08@126.com","loginPassword":"913f3aa5ccc179140d8352b3e766e644","verifyCode":"cookie_dict.split('=')[-1]"}
    res = requests.session().post(url = login_url,data = login_data)
    print(res.text)





# # 新增ip
# add_ip_url = "https://www.apishop.net/apiStore/IPConfig/addIPConfigGroup"
# add_ip_data = {"groupName": "test04","ipList": "192.0.0.4"}
# add_ip_res = requests.post(add_ip_url,add_ip_data,cookies = login_res.cookies)
# print(add_ip_res.json())
# print(add_ip_res.status_code)

#
# res1 = requests.session().post(add_ip_url,add_ip_data)
# print(res1.text)

# # 修改ip
    edit_ip_url = "https://www.apishop.net/apiStore/IPConfig/editIPConfigGroup"
    edit_ip_data ={"groupName":"test03","ipList":"192.0.0.2","groupID":"66"}
    edit_ip_res = requests.post(edit_ip_url,edit_ip_data,res.cookies)
    print(edit_ip_res.json())
    print(edit_ip_res.status_code)
# 通过session会话去发送接口请求