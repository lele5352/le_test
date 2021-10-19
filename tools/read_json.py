# 导包
import json


# 打开文件并获取文件流

# def read_json():
#     with open('../data/login.json', "r", encoding="utf-8") as f:
#         #调用load方法加载文件流
#         data = json.load(f)
#         return data

class ReadJson(object):
    def __init__(self, filename):
        self.filepath = "./data/" + filename

    def read_json(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            # 调用load方法加载文件流
            return json.load(f)


if __name__ == "__main__":
    datas = ReadJson("login.json").read_json()
    arrs = []
    for data in datas.values():
        arrs.append((data.get('url'),
                     data.get('username'),
                     data.get('password'),
                     data.get('grant_type'),
                     data.get('expect_result'),
                     data.get('status_code')
                     ))
    print(arrs)
