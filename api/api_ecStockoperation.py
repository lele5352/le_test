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

        return requests.post(url, headers=headers, data=json.dumps(data))


    #冻结单列表查询
    def api_post_page(self, url, authorization, wares_sku_code, storage_location_code, goods_sku_code,
                      frozenReceiptCode, status, frozenReason, field, type, size, current):
        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Authorization': authorization}
        datas = {
            "waresSkuCode": wares_sku_code,
            "storageLocationCode": storage_location_code,
            "goodsSkuCode": goods_sku_code,
            "frozenReceiptCode": frozenReceiptCode,
            "status": status,
            "frozenReason": frozenReason,
            #"sortField": sortField,
            "field": field,
            "type": type,
            "size": size,
            "current": current
        }

        return requests.post(url, headers=headers, data=json.dumps(datas))


class ApiAdjustReceipt(object):

    def api_post_adjust_receipt(self, url, authorization, adjustReason, changeCount, changeType, remark,
                                storageLocationCode, waresSkuCode):
        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Authorization': authorization}
        datas = [{
            "adjustReason": adjustReason,
            "changeCount": changeCount,
            "changeType": changeType,
            "remark": remark,
            "storageLocationCode": storageLocationCode,
            "waresSkuCode": waresSkuCode,
            }]

        return requests.post(url, headers=headers, data=json.dumps(datas))

    def api_post_batch_adjust(self, url, authorization, auditResult, ids, rejectReason):
        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Authorization': authorization}
        datas = {
                  "auditResult": auditResult,
                  "ids": ids,
                  "rejectReason": rejectReason
                }
        return requests.post(url, headers=headers, data=json.dumps(datas))

    def api_post_page(self, url, authorization, adjustReason, adjustReceiptCode, beginAuditTime, changeType,
                      current, endAuditTime, relationNo, size, field, type, source, status, storageLocationCode,
                      waresSkuCode):
        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Authorization': authorization}
        datas = {
              "adjustReason": adjustReason,
              "adjustReceiptCode": adjustReceiptCode,
              "beginAuditTime": beginAuditTime,
              "changeType": changeType,
              "current": current,
              "endAuditTime": endAuditTime,
              "relationNo": relationNo,
              "size": size,
              "sortField": [
                {
                  "field": field,
                  "type": type
                }
              ],
              "source": source,
              "status": status,
              "storageLocationCode": storageLocationCode,
              "waresSkuCode": waresSkuCode
            }

        return requests.post(url, headers=headers, data=json.dumps(datas))


