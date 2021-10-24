from tools.read_json import ReadJson
from produce.login import Login
from api.api_ecStockoperation import ApiAdjustReceipt
from data.get_data import GetData

def get_data(data_paht):
    return ReadJson(data_paht).read_json()
def get_authorization(token_paht):
    return Login().get_authorization(token_paht)

class AdjustReceipt(object):

    #新增调整单
    def add_adjust_receipt(self, data_path, token_path):
        datas = get_data(data_path)
        authorization = get_authorization(token_path)


        datas = datas["adjust_add"]
        url = datas.get("url")
        adjustReason = datas.get("adjustReason")
        changeCount = datas.get("changeCount")
        changeType = datas.get("changeType")
        remark = datas.get("remark")
        storageLocationCode = datas.get("storageLocationCode")
        waresSkuCode = datas.get("waresSkuCode")

        res = ApiAdjustReceipt().api_post_adjust_receipt(url, authorization, adjustReason, changeCount, changeType, remark,
                                storageLocationCode, waresSkuCode)
        print(res.json())

    def reduce_adjust_receipt(self, data_path, token_path):
        datas = get_data(data_path)
        authorization = get_authorization(token_path)

        datas = datas["adjust_reduce"]
        url = datas.get("url")
        adjustReason = datas.get("adjustReason")
        changeCount = datas.get("changeCount")
        changeType = datas.get("changeType")
        remark = datas.get("remark")
        storageLocationCode = datas.get("storageLocationCode")
        waresSkuCode = datas.get("waresSkuCode")

        res = ApiAdjustReceipt().api_post_adjust_receipt(url, authorization, adjustReason, changeCount, changeType,
                                                         remark,
                                                         storageLocationCode, waresSkuCode)
        print(res.json())


    def pass_batch_adjust(self, data_path, token_path):
        datas = get_data(data_path)
        authorization = get_authorization(token_path)

        datas = datas["adjust_pass"]
        url = datas.get("url")
        auditResult = datas.get("auditResult")
        ids = datas.get("ids")
        rejectReason = datas.get("rejectReason")

        res = ApiAdjustReceipt().api_post_batch_adjust(url, authorization, auditResult, ids, rejectReason)
        print(res.json())

    def fail_batch_adjust(self, data_path, token_path):
        datas = get_data(data_path)
        authorization = get_authorization(token_path)

        datas = datas["adjust_fail"]
        url = datas.get("url")
        auditResult = datas.get("auditResult")
        ids = datas.get("ids")
        rejectReason = datas.get("rejectReason")

        res = ApiAdjustReceipt().api_post_batch_adjust(url, authorization, auditResult, ids, rejectReason)
        print(res.json())

    #查询调整单
    def adjust_page(self, data_path, token_path):

        datas = get_data(data_path)
        authorization = get_authorization(token_path)

        url = datas.get("url")
        adjustReason =datas.get("adjustReason")
        adjustReceiptCode =datas.get("adjustReceiptCode")
        beginAuditTime = datas.get("beginAuditTime")
        changeType = datas.get("changeType")
        current = datas.get("current")
        endAuditTime = datas.get("endAuditTime")
        relationNo = datas.get("relationNo")
        size = datas.get("size")
        field = datas.get("field")
        type = datas.get("type")
        source = datas.get("source")
        status = datas.get("status")
        storageLocationCode = datas.get("storageLocationCode")
        waresSkuCode = datas.get("waresSkuCode")


        res = ApiAdjustReceipt().api_post_page(url, authorization, adjustReason, adjustReceiptCode, beginAuditTime, changeType,
                      current, endAuditTime, relationNo, size, field, type, source, status, storageLocationCode,
                      waresSkuCode)
        datas = res.json()["data"]["records"]
        if datas:
            for data in datas:
                print(data)
        else:
            print("暂无查询数据")



if __name__ == '__main__':

    #新增调整单--盘盈
    #AdjustReceipt().add_adjust_receipt('adjust_receipt.json', 'login.json')

    # 新增调整单--盘亏
    #AdjustReceipt().reduce_adjust_receipt('adjust_receipt.json', 'login.json')

    # 审批调整单-通过
    #AdjustReceipt().pass_batch_adjust('batch_adjust.json', 'login.json')

    #审批调整单-驳回
    #AdjustReceipt().fail_batch_adjust('batch_adjust.json', 'login.json')

    # 查询调整单
    AdjustReceipt().adjust_page('page_adjust.json', 'login.json')