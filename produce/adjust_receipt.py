from tools.read_ever import GetData
from api.api_ecStockoperation import ApiAdjustReceipt

class AdjustReceipt(object):

    #新增调整单-盘盈
    def add_adjust_receipt(self, url_file, data_file, token_file):
        url = GetData().get_url(url_file)["adjust_receipt"]["adjust_url"]
        authorization = GetData().get_data(token_file)["authorization"]
        datas = GetData().get_data(data_file)["adjust_add"]

        res = ApiAdjustReceipt().api_post_adjust_receipt(url, authorization, datas)
        print(res.json())

    #新增调整单-盘亏
    def reduce_adjust_receipt(self, url_file, data_file, token_file):
        url = GetData().get_url(url_file)["adjust_receipt"]["adjust_url"]
        authorization = GetData().get_data(token_file)["authorization"]
        datas = GetData().get_data(data_file)["adjust_reduce"]

        res = ApiAdjustReceipt().api_post_adjust_receipt(url, authorization, datas)
        print(res.json())

    #审批调整单-通过
    def pass_batch_adjust(self, url_file, data_file, token_file):

        url = GetData.get_url(url_file)["adjust_receipt"]["batch_adjust_url"]
        datas = GetData.get_data(data_file)["audit_pass"]
        authorization = GetData.get_data(token_file)["authorization"]

        res = ApiAdjustReceipt().api_post_batch_adjust(url, authorization, datas)
        print(res.json())

    #审批调整单-驳回
    def fail_batch_adjust(self, url_file, data_file, token_file):

        url = GetData().get_url(url_file)["adjust_receipt"]["batch_adjust_url"]
        authorization = GetData().get_data(token_file)["authorization"]
        datas = GetData().get_data(data_file)["audit_fail"]

        res = ApiAdjustReceipt().api_post_batch_adjust(url, authorization, datas)
        print(res.json())


    #查询调整单
    def adjust_page(self, url_file, data_file, token_file):

        url = GetData().get_url(url_file)["adjust_receipt"]["page_adjust_url"]
        datas = GetData().get_data(data_file)
        authorization = GetData().get_data(token_file)["authorization"]

        res = ApiAdjustReceipt().api_post_page(url, authorization, datas)
        data_list = res.json()["data"]["records"]
        if data_list:
            for data in data_list:
                print(data)
        else:
            print("暂无查询数据")



if __name__ == '__main__':

    # 新增调整单--盘盈
    AdjustReceipt().add_adjust_receipt('url.json', 'adjust_receipt.json', 'config.json')

    # 新增调整单--盘亏
    #AdjustReceipt().reduce_adjust_receipt('url.json', 'adjust_receipt.json', 'config.json')

    # 审批调整单-通过
    #AdjustReceipt().pass_batch_adjust('url.json', 'batch_audit.json', 'config.json')

    # 审批调整单-驳回
    #AdjustReceipt().fail_batch_adjust('url.json', 'batch_audit.json', 'config.json')

    # 查询调整单
    #AdjustReceipt().adjust_page('url.json', 'page_adjust.json', 'config.json')