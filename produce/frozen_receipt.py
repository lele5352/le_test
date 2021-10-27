from api.api_ecStockoperation import ApiFrozenReceipt
from tools.read_ever import GetData
from produce.login import Login




class FrozenReceipt(object):

    #冻结单
    def add_frozen_receipt(self, url_file, data_file, token_file):

        url = GetData().get_url(url_file)["frozen_receipt"]["frozen_url"]
        authorization = GetData().get_authorization(token_file)["authorization"]
        datas = GetData().get_data(data_file)
        res = ApiFrozenReceipt().api_post_frozen_receipt(url, authorization, datas)
        print(res.json())



    #解冻/批量解冻单
    def batch_defrost(self, url_file, data_file, token_file):
        url = GetData().get_url(url_file)["frozen_receipt"]["batch_defrost_url"]
        authorization = GetData().get_authorization(token_file)["authorization"]
        datas = GetData().get_data(data_file)
        res = ApiFrozenReceipt().api_post_batch_defrost(url, authorization, datas)
        print(res.json())


    #冻结单列表查询
    def frozen_page(self,url_file, data_file, token_file):
        url = GetData().get_url(url_file)["frozen_receipt"]["page_frozen_url"]
        authorization = GetData().get_authorization(token_file)["authorization"]
        datas = GetData().get_data(data_file)
        res = ApiFrozenReceipt().api_post_page(url, authorization, datas)
        data_list = res.json()['data']['records']
        if data_list:
            for data in data_list:
                print(data)
        else:
            print("暂无查询数据")

if __name__ == '__main__':
    #生成冻结单，需要传参数所在的json文档
    #FrozenReceipt().add_frozen_receipt('url.json', "frozen_receipt.json", 'config.json')

    #解冻单，需要传冻结单id，目前需要手动去页面查询后查看单据id，然后修改到json文件内
    #FrozenReceipt().batch_defrost('url.json', 'batch_defrost.json', 'config.json')

    #查看冻结单列表
    FrozenReceipt().frozen_page('url.json', 'page_frozen.json', 'config.json')