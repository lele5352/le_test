# 导包
import json


class ReadJson(object):
    # def __init__(self, filename):
    #     #调试时候使用路径
    #     self.filepath = "../data/" + filename
    #     #跑脚本时使用
    #     #self.filepath = "./data/" + filename

    def read_json(self, filename):
        #调试时候使用路径
        filepath = "../data/" + filename
        #跑脚本时使用
        #filepath = "./data/" + filename

        with open(filepath, "r", encoding="utf-8") as f:
            # 调用load方法加载文件流
            return json.load(f)


class GetData(object):

    def get_url(self, url_file):
        return ReadJson().read_json(url_file)

    def get_data(self, data_file):
        return ReadJson().read_json(data_file)

    def get_authorization(self, token_file):
        return ReadJson().read_json(token_file)



if __name__ == "__main__":
    # datas = ReadJson("login.json").read_json()
    # arrs = []
    # for data in datas.values():
    #     arrs.append((data.get('url'),
    #                  data.get('username'),
    #                  data.get('password'),
    #                  data.get('grant_type'),
    #                  data.get('expect_result'),
    #                  data.get('status_code')
    #                  ))
    # print(arrs)
    data = ReadJson("frozen_receipt.json").read_json()
    print(data)