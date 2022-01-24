from tools.read_ever import GetData
from api.api_login import ApiLogin
import json


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
            print("获取最新authorization成功！")


    def get_warehouse_info(self, url_file, token_file, warehouse_file):

        url = GetData().get_url(url_file)["login"]["list_warehouse_url"]
        authorization = GetData().get_data(token_file)["authorization"]
        datas = {"warehouseStatus":0,"sortField":[{"field":"create_time","type":"DESC"}],"operatingMode":'',"warehouseCode":'',"warehouseAbbreviation":'',"warehouseNameEn":'',"warehouseNameCn":'',"cnWarehouseFlag":'',"size":50,"current":2}
        res = ApiLogin().api_get_warehouse_list(url, authorization,datas)
        res = (res.json()["data"])
        list_warehouse_info = []
        for item in res:
            warehouseinfo = {
                "id": item["id"],
                "abbreviation": item["ext"]["abbreviation"],
                "warehouseId": item["ext"]["warehouseId"],
                "warehouseName": item["ext"]["warehouseName"],
                "warehouseCode": item["ext"]["warehouseCode"],
            }
            list_warehouse_info.append(warehouseinfo)
        filepath = '../data/' + warehouse_file
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(list_warehouse_info, f, indent="\t", ensure_ascii=False)
            print("写入仓库信息json文件成功")

    def switch_warehouse(self, url_file, token_file, warehouse_code):
        url = GetData().get_url(url_file)["login"]["switch_url"]
        authorization = GetData().get_data(token_file)["authorization"]
        warehouse_info = GetData().get_wareshouse_info(warehouse_code)
        datas = {
            "dataPermId": warehouse_info.get("warehouseId")
        }
        res = ApiLogin().api_put_switch_warehouse(url, authorization, datas)
        print(res.json().get("message"),"切换仓库结果：", warehouse_code)
        return warehouse_info

if __name__ == '__main__':
    Login().get_authorization("url.json", "config.json")
    # Login().get_warehouse_info("url.json", "config.json", "warehouse.json")
    res = Login().switch_warehouse("url.json", "config.json", "FSZZ")
    print(res)