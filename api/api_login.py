"""
    目标：实现登录接口类封装
"""
#导包
import requests
#新建类 登录接口对象
class ApiLogin(object):
#新建方法 登录方法
    def api_post_login(self, url, datas):
        #headers 定义
        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
        #调用并返回响应对象
        return requests.post(url, headers=headers, json=datas)
    def api_get_warehouse_list(self, url, authorization):
        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', "authorization": authorization}
        return requests.get(url, headers=headers)