from tools.read_json import ReadJson
from produce.login import Login
from api.api_ecStockoperation import ApiProcessReceipt

def get_url(url_file):
    return ReadJson().read_json(url_file)

def get_authorization(token_file):
    return Login().get_authorization(token_file)

def get_data(data_file):
    return ReadJson().read_json(data_file)

class ProcessReceipt(object):

    def add_combination(self, url_file, data_file, token_file):

        url = get_url(url_file)["process_receipt"]["process_url"]
        authorization = get_authorization(token_file)
        datas = get_data(data_file)["combination"]
        res = ApiProcessReceipt().api_post_process_receipt(url, authorization, datas)
        print(res.json())


    def add_split(self, url_file, data_file, token_file):

        url = get_url(url_file)["process_receipt"]["process_url"]
        authorization = get_authorization(token_file)
        datas = get_data(data_file)["split"]
        res = ApiProcessReceipt().api_post_process_receipt(url, authorization, datas)
        print(res.json())

    def batch_approve_pass(self, url_file, data_file, token_file):

        url = get_url(url_file)["process_receipt"]["batch_process_url"]
        authorization = get_authorization(token_file)
        datas = get_data(data_file)["audit_pass"]
        res = ApiProcessReceipt().api_post_batch_process(url, authorization, datas)
        print(res.json())

    def batch_approve_fail(self, url_file, data_file, token_file):

        url = get_url(url_file)["process_receipt"]["batch_process_url"]
        authorization = get_authorization(token_file)
        datas = get_data(data_file)["audit_fail"]
        res = ApiProcessReceipt().api_post_batch_process(url, authorization, datas)
        print(res.json())

    def process_page(self, url_file, data_file, token_file):

        url = get_url(url_file)["process_receipt"]["page_process_url"]
        authorization = get_authorization(token_file)
        datas = get_data(data_file)

        res = ApiProcessReceipt().api_post_page(url, authorization, datas)
        data_list = res.json()['data']['records']
        if data_list:
            for data in data_list:
                print(data)
        else:
            print("暂无查询数据")

if __name__ == '__main__':
    #加工单-组合
    #ProcessReceipt().add_combination("url.json", "process_receipt.json", "login.json")
    #加工单-拆分
    #ProcessReceipt().add_split("url.json", "process_receipt.json", "login.json")

    #加工单审核-通过
    #ProcessReceipt().batch_approve_pass("url.json", "batch_audit.json", "login.json")
    #加工单审核-驳回
    #ProcessReceipt().batch_approve_fail("url.json", "batch_audit.json", "login.json")
    #查询加工单
    ProcessReceipt().process_page("url.json", "page_process.json", "login.json")