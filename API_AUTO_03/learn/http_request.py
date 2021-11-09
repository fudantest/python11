#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2021/10/31 21:24
# @Author   :day day up up
# @File     :http_request.py
import requests
#注册
register_url = "https://www.apishop.net/common/Guest/mailRegister"
register_data = {"userMail":"xuezheng0008@126.com","userPassword":"913f3aa5ccc179140d8352b3e766e644"}
register_res = requests.post(register_url,register_data)
print("text的解析结果：",register_res.text)
print("json的解析结果：",register_res.json())
print(register_res.status_code)


#成功登录：需要拿到请求头中的verifyCode，作为输入参数
session = requests.session()
session.headers['cookie'] = 'gr_user_id=151ec259-b48c-4402-b137-5294bcb706b3; gr_session_id_9944ca777cab9409=281d333a-5a9a-4c4d-9612-f04de88f9647; gr_session_id_9944ca777cab9409_281d333a-5a9a-4c4d-9612-f04de88f9647=true; verifyCode=7d277af1e4cf45baf920474ebba56bd9'
print(session.headers['cookie'].split("=")[-1])
login_url = "https://www.apishop.net/common/Guest/login"
login_data = {"loginCall":"xuezheng08@126.com","loginPassword":"913f3aa5ccc179140d8352b3e766e644","verifyCode":"cookie_dict.split('=')[-1]"}
login_res = requests.get(login_url,login_data)
print("text的解析结果：",login_res.text)
print("json的解析结果：",login_res.json())
print(login_res.status_code)
print(login_res.cookies)

#查询
search_url = "https://www.apishop.net/apiStore/Product/searchProduct"
search_data = {"keyWord": "短信服务","page": "1"}
search_res = requests.post(search_url,search_data,cookies=login_res.cookies)
print("text的解析结果：",search_res.text)
print("json的解析结果：",search_res.json())
print(search_res.status_code)

# 新增ip
add_ip_url = "https://www.apishop.net/apiStore/IPConfig/addIPConfigGroup"
add_ip_data = {"groupName": "test03","ipList": "192.0.0.3"}
add_ip_res = requests.post(add_ip_url,add_ip_data,cookies = login_res.cookies)
print(add_ip_res.json())
print(add_ip_res.status_code)
# 修改ip
edit_ip_url = "https://www.apishop.net/apiStore/IPConfig/editIPConfigGroup"
edit_ip_data ={"groupName":"test04","ipList":"192.0.0.1","groupID":"65"}
edit_ip_res = requests.post(edit_ip_url,edit_ip_data,login_res.cookies)
print(edit_ip_res.json())
print(edit_ip_res.status_code)


