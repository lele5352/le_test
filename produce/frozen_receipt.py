from api.api_ecStockoperation import ApiFrozenReceipt
from tools.read_json import ReadJson
from produce.login import Login


def get_data(filepath):

    return ReadJson(filepath).read_json()

class FrozenReceipt(object):

    #冻结单
    def add_frozen_receipt(self, filepath):

        datas = get_data(filepath)
        #获取token
        authorization = Login().get_authorization("login.json")

        url = datas.get("url")
        frozen_count = datas.get("frozenCount")
        storage_location_id = datas.get("storageLocationId")
        supplier_id = datas.get("supplierId")
        supplier_name = datas.get("supplierName")
        frozen_reason = datas.get("frozenReason")
        remark = datas.get("remark")
        storage_location_code = datas.get("storageLocationCode")
        wares_sku_code = datas.get("waresSkuCode")

        res = ApiFrozenReceipt().api_post_frozen_receipt(
            url,
            authorization,
            frozen_count,
            storage_location_id,
            supplier_id,
            supplier_name,
            frozen_reason,
            remark,
            storage_location_code,
            wares_sku_code
        )
        print(res.json())




    #解冻/批量解冻单
    def batch_defrost(self,filepath):
        datas = get_data(filepath)
        # 获取token
        authorization = Login().get_authorization("login.json")

        url = datas.get("url")
        integers = datas.get("integers")

        res = ApiFrozenReceipt().api_post_batch_defrost(url, authorization, integers)
        print(res.json())


    #冻结单列表查询
    def frozen_page(self,filepath):
        datas = get_data(filepath)
        # 获取token
        authorization = Login().get_authorization("login.json")

        url = datas.get("url")
        wares_sku_code = datas.get("waresSkuCode")
        storage_location_code = datas.get("storageLocationCode")
        goods_sku_code = datas.get("goodsSkuCode")
        frozenReceiptCode = datas.get("frozenReceiptCode")
        status = datas.get("status")
        frozenReason = datas.get("frozenReason")
        field = datas.get("field")
        type = datas.get("type")
        size = datas.get("size")
        current = datas.get("current")

        res = ApiFrozenReceipt().api_post_page(url, authorization, wares_sku_code, storage_location_code, goods_sku_code,
                      frozenReceiptCode, status, frozenReason, field, type, size, current)
        data_list = res.json()['data']['records']
        for data in data_list:
            print(data)

if __name__ == '__main__':
    # 生成冻结单，需要传参数所在的json文档
    #FrozenReceipt().add_frozen_receipt("frozen_receipt.json")

    #解冻单，需要传冻结单id，目前需要手动去页面查询后查看单据id，然后修改到json文件内
    #FrozenReceipt().batch_defrost('batch_defrost.json')

    #查看冻结单列表
    FrozenReceipt().frozen_page('page_frozen.json')