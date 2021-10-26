import requests
import json

#冻结单接口
class ApiFrozenReceipt(object):

    #冻结单
    def api_post_frozen_receipt(self, url, authorization, datas):

        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Authorization': authorization}
        datas = [datas]
        return requests.post(url, headers=headers, data=json.dumps(datas))


    #解冻/批量解冻单
    def api_post_batch_defrost(self, url, authorization, datas):

        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Authorization': authorization}
        return requests.post(url, headers=headers, data=json.dumps(datas))


    #冻结单列表查询
    def api_post_page(self, url, authorization, datas):

        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Authorization': authorization}
        return requests.post(url, headers=headers, data=json.dumps(datas))

#调整单接口
class ApiAdjustReceipt(object):

    def api_post_adjust_receipt(self, url, authorization, datas):

        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Authorization': authorization}
        datas = [datas]

        return requests.post(url, headers=headers, data=json.dumps(datas))

    def api_post_batch_adjust(self, url, authorization, datas):

        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Authorization': authorization}
        return requests.post(url, headers=headers, data=json.dumps(datas))


    def api_post_page(self, url, authorization, datas):

        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Authorization': authorization}
        return requests.post(url, headers=headers, data=json.dumps(datas))

#加工单接口
class ApiProcessReceipt(object):

    def api_post_process_receipt(self, url, authorization, datas):
        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Authorization': authorization}
        return requests.post(url, headers=headers, data=json.dumps(datas))

    def api_post_batch_process(self, url, authorization, datas):
        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Authorization': authorization}
        return requests.post(url, headers=headers, data=json.dumps(datas))

    def api_post_page(self, url, authorization, datas):
        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Authorization': authorization}
        return requests.post(url, headers=headers, data=json.dumps(datas))

#PDA库内作业
class ApiPdaInnerLocation(object):

    def api_post_batch_move(self, url, authorization, datas):
        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Authorization': authorization}
        return requests.post(url, headers=headers, data=json.dumps(datas))

    def api_post_single(self, url, authorization, datas):
        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Authorization': authorization}
        return requests.post(url, headers=headers, data=json.dumps(datas))

    def api_post_to_bad(self, url, authorization, datas):
        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Authorization': authorization}
        return requests.post(url, headers=headers, data=json.dumps(datas))

    def api_post_to_good(self, url, authorization, datas):
        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Authorization': authorization}
        return requests.post(url, headers=headers, data=json.dumps(datas))
