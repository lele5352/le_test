import requests

class ApiFrozenReceipt(object):

    #冻结单
    def api_post_frozen_receipt(self, url, authorization, frozen_count, frozen_reason, remark, storage_location_code, wares_sku_code):
        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Authorization': authorization}
        url = url
        data = {
            "frozenCount": frozen_count,
            "frozenReason": frozen_reason,
            "remark": remark,
            "storageLocationCode": storage_location_code,
            "waresSkuCode": wares_sku_code
        }
        return requests.post(url, data=data, headers=headers)




    #解冻/批量解冻单
    def batch_defrost(self):
        pass

    #冻结单列表查询
    def page(self):
        pass