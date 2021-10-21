import requests

class FrozenReceipt(object):

    #冻结单
    def api_post_frozen_receipt(self, url, frozenCount, frozenReason, remark, storageLocationCode, waresSkuCode):
        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
        url = url
        data = {
            "frozenCount": frozenCount,
            "frozenReason": frozenReason,
            "remark": remark,
            "storageLocationCode": storageLocationCode,
            "waresSkuCode": waresSkuCode
        }
        return requests.post(url, data=data, headers=headers)




    #解冻/批量解冻单
    def batch_defrost(self):
        pass

    #冻结单列表查询
    def page(self):
        pass