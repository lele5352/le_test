from tools.read_ever import GetData
from api.api_ecStockoperation import ApiProcessReceipt


class ProcessReceipt(object):

    def add_combination(self, url_file, data_file, token_file):

        url = GetData().get_url(url_file)["process_receipt"]["process_url"]
        authorization = GetData().get_authorization(token_file)["authorization"]
        datas = GetData().get_data(data_file)["combination"]
        res = ApiProcessReceipt().api_post_process_receipt(url, authorization, datas)
        print(res.json())


    def add_split(self, url_file, data_file, token_file):

        url = GetData().get_url(url_file)["process_receipt"]["process_url"]
        authorization = GetData().get_authorization(token_file)["authorization"]
        datas = GetData().get_data(data_file)["split"]
        res = ApiProcessReceipt().api_post_process_receipt(url, authorization, datas)
        print(res.json())

    def batch_approve_pass(self, url_file, data_file, token_file):

        url = GetData().get_url(url_file)["process_receipt"]["batch_process_url"]
        authorization = GetData().get_authorization(token_file)["authorization"]
        datas = GetData().get_data(data_file)["audit_pass"]
        res = ApiProcessReceipt().api_post_batch_process(url, authorization, datas)
        print(res.json())

    def batch_approve_fail(self, url_file, data_file, token_file):

        url = GetData().get_url(url_file)["process_receipt"]["batch_process_url"]
        authorization = GetData().get_authorization(token_file)["authorization"]
        datas = GetData().get_data(data_file)["audit_fail"]
        res = ApiProcessReceipt().api_post_batch_process(url, authorization, datas)
        print(res.json())

    def process_page(self, url_file, data_file, token_file):

        url = GetData().get_url(url_file)["process_receipt"]["page_process_url"]
        authorization = GetData().get_authorization(token_file)["authorization"]
        datas = GetData().get_data(data_file)

        res = ApiProcessReceipt().api_post_page(url, authorization, datas)
        data_list = res.json()['data']['records']
        if data_list:
            for data in data_list:
                print(data)
        else:
            print("暂无查询数据")

if __name__ == '__main__':
    #加工单-组合
    #ProcessReceipt().add_combination("url.json", "process_receipt.json", "config.json")
    #加工单-拆分
    #ProcessReceipt().add_split("url.json", "process_receipt.json", "config.json")

    #加工单审核-通过
    #ProcessReceipt().batch_approve_pass("url.json", "batch_audit.json", "config.json")
    #加工单审核-驳回
    #ProcessReceipt().batch_approve_fail("url.json", "batch_audit.json", "config.json")
    #查询加工单
    ProcessReceipt().process_page("url.json", "page_process.json", "config.json")