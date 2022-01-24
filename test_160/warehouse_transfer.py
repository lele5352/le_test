from tools import read_db
import requests
import json

#冻结单接口
class ApiOtherIn(object):

    #冻结单
    def api_post_frozen_receipt(self, url, authorization, datas):

        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Authorization': authorization}
        datas = [datas]
        return requests.post(url, headers=headers, data=json.dumps(datas))


    #解冻/批量解冻单
    def api_post_batch_defrost(self, url, authorization, datas):

        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Authorization': authorization}
        return requests.post(url, headers=headers, data=json.dumps(datas))