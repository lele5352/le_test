from api.api_ecStockoperation import ApiFrozenReceipt
from tools.read_json import ReadJson
from parameterized import parameterized


def get_data(filepath):

    return ReadJson(filepath).read_json()

class FrozenReceipt(object):

    #冻结单
    def add_frozen_receipt(self, filepath):

        datas = get_data(filepath)
        url = datas.get("url")
        authorization = datas.get("authorization")
        frozen_count = datas.get("frozen_count")
        frozen_reason = datas.get("frozen_reason")
        remark = datas.get("remark")
        storage_location_code = datas.get("storage_location_code")
        wares_sku_code = datas.get("wares_sku_code")

        res = ApiFrozenReceipt().api_post_frozen_receipt(
           url,
           authorization,
           frozen_count,
           frozen_reason,
           remark,
           storage_location_code,
           wares_sku_code
        )
        print(res.json())




    #解冻/批量解冻单
    def batch_defrost(self):
        pass

    #冻结单列表查询
    def page(self):
        pass

if __name__ == '__main__':
    FrozenReceipt().add_frozen_receipt("stockoperation.json")