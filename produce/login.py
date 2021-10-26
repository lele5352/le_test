from tools.read_json import ReadJson
from tools.read_json import GetData
from api.api_login import ApiLogin
from data.get_data import GetAuthorization
import json


# def get_data(filepath):
#     return ReadJson().read_json(filepath)

class Login(object):

    # 获取token
    def get_authorization(self, url_file, data_file):

        url = GetData().get_data(url_file)["login"]["login_url"]
        datas = GetData().get_data(data_file)
        res = ApiLogin().api_post_login(url, datas)
        res_data = res.json()["data"]
        authorization = res_data["tokenHead"] + " " + res_data["token"]
        # 获取token后通过反射存储获取的token
        #setattr(GetAuthorization, "authorization", authorization)

        #将获取的token存储到config文件内，为了存储的数据格式正确性，需要如下先打开文件读数据，然后再打开文件写数据
        filepath = '../data/' + data_file
        with open(filepath, 'r', encoding='utf-8') as f:
            res = json.load(f)
            res["authorization"] = authorization
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(res, f, indent="    ", ensure_ascii=False)  # indent设置写入json文件的缩进格式 , indent="\t"
            print("生成authorization成功！")


if __name__ == '__main__':
    Login().get_authorization("url.json", "config.json")
