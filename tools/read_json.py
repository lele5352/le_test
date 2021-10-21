# 导包
import json
import os

class ReadJson(object):
    def __init__(self, filename):
        #调试时候使用路径
        self.filepath = "../data/" + filename
        #跑脚本时使用
        #self.filepath = "./data/" + filename

    def read_json(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            # 调用load方法加载文件流
            return json.load(f)


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