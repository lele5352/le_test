import requests
import json

class ApiFrozenReceipt(object):

    #冻结单
    def api_post_frozen_receipt(self, url, authorization, frozen_count, storage_location_id, supplier_id,
                                supplier_name, frozen_reason, remark, storage_location_code,
                                wares_sku_code):
        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Authorization': authorization}
        data = [{
            'frozenCount': frozen_count,
            'frozenReason': frozen_reason,
            "storageLocationId": storage_location_id,
            "supplierId": supplier_id,
            "supplierName": supplier_name,
            'remark': remark,
            'storageLocationCode': storage_location_code,
            'waresSkuCode': wares_sku_code}]

        return requests.post(url, headers=headers, json=data)


    #解冻/批量解冻单
    def api_post_batch_defrost(self, url, authorization, integers):
        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Authorization': authorization}
        data = [str(integers)]
        #请求body内仅有一个参数时，使用下面json方法格式化一下数据
        datas = json.dumps(data)

        return requests.post(url, headers=headers, data=datas)


    #冻结单列表查询
    def page(self):
        pass