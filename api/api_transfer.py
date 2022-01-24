import requests
import json
from tools import read_db,read_ever
import time
from produce import login

class GetWarehouse():

    def switch_warehouse(self, warehouse_code):
        login.Login().get_authorization("url.json", "config.json")
        warehouse_info = login.Login().switch_warehouse("url.json", "config.json", warehouse_code)
        return warehouse_info


class Transfer:
    def __init__(self,authorization):
        self.headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Authorization': authorization}
        self.entryorderid = ''
    #其他入库-新增
    def other_add(self):
        url_other_add = 'https://test-scms.popicorns.com/api/ec-wms-api/entryorder'
        data_add = {
            "entryOrderType": 3,
            #"eta": 1642403631000,
            #"supplierCode": null,
            #"fromOrderCode": null,
            #"remark": null,
            "qualityType": 0,
            #"timestamp": 1642403631000,
            "logisticsInfoList": [],
            "skuInfoList": [
                {
                    "warehouseSkuCode": "53586714577B02",
                    "planSkuQty": 10,
                    "warehouseSkuName": "部件2 2/2 X2",
                    "warehouseSkuWeight": "5",
                    "saleSkuCode": "53586714577",
                    "saleSkuName": "决明子",
                    "bomVersion": "B",
                    "saleSkuImg": "https://img.popicorns.com/dev/file/2021/11/08/8cbba5e1160a48e9bd9b43e54450ab7c.jpg",
                    "warehouseSkuHeight": "10",
                    "warehouseSkuLength": "10",
                    "warehouseSkuWidth": "10"
                },
                {
                    "warehouseSkuCode": "53586714577B01",
                    "planSkuQty": 5,
                    "warehouseSkuName": "部件1 1/2 X1",
                    "warehouseSkuWeight": "5",
                    "saleSkuCode": "53586714577",
                    "saleSkuName": "决明子",
                    "bomVersion": "B",
                    "saleSkuImg": "https://img.popicorns.com/dev/file/2021/11/08/8cbba5e1160a48e9bd9b43e54450ab7c.jpg",
                    "warehouseSkuHeight": "10",
                    "warehouseSkuLength": "10",
                    "warehouseSkuWidth": "10"
                },
                {
                    "warehouseSkuCode": "53586714577D01",
                    "planSkuQty": 10,
                    "warehouseSkuName": "单品2个组成1个销售sku 1/1 X2",
                    "warehouseSkuWeight": "50",
                    "saleSkuCode": "53586714577",
                    "saleSkuName": "决明子",
                    "bomVersion": "D",
                    "saleSkuImg": "https://img.popicorns.com/dev/file/2021/11/08/8cbba5e1160a48e9bd9b43e54450ab7c.jpg",
                    "warehouseSkuHeight": "50",
                    "warehouseSkuLength": "50",
                    "warehouseSkuWidth": "50"
                }
            ],
            "operationFlag": 0
        }
        res = requests.post(url_other_add, headers=self.headers, data=json.dumps(data_add))
        self.entryorderid = res.json().get('data')['entryOrderId']
        print('新增入库单' + res.json().get('message'))

    #其他入库-提交
    def other_submit(self):

        url_other_submit = 'https://test-scms.popicorns.com/api/ec-wms-api/entryorder'
        data_submit = {
            "entryOrderId": self.entryorderid,
            "entryOrderType": 3,
            "eta": 1642348800000,
            #"supplierCode": null,
            #"fromOrderCode": null,
            "qualityType": 0,
            #"remark": null,
            "logisticsInfoList": [],
            "skuInfoList": [
                {
                    "warehouseSkuCode": "53586714577B02",
                    "planSkuQty": 10,
                    "warehouseSkuName": "部件2",
                    "warehouseSkuWeight": "5",
                    "saleSkuCode": "53586714577",
                    "saleSkuName": "决明子",
                    "bomVersion": "B",
                    "saleSkuImg": "https://img1.popicorns.com/fit-in/200x200/dev/file/2021/11/08/8cbba5e1160a48e9bd9b43e54450ab7c.jpg",
                    "warehouseSkuHeight": "10",
                    "warehouseSkuLength": "10",
                    "warehouseSkuWidth": "10"
                },
                {
                    "warehouseSkuCode": "53586714577B01",
                    "planSkuQty": 5,
                    "warehouseSkuName": "部件1",
                    "warehouseSkuWeight": "5",
                    "saleSkuCode": "53586714577",
                    "saleSkuName": "决明子",
                    "bomVersion": "B",
                    "saleSkuImg": "https://img1.popicorns.com/fit-in/200x200/dev/file/2021/11/08/8cbba5e1160a48e9bd9b43e54450ab7c.jpg",
                    "warehouseSkuHeight": "10",
                    "warehouseSkuLength": "10",
                    "warehouseSkuWidth": "10"
                },
                {
                    "warehouseSkuCode": "53586714577D01",
                    "planSkuQty": 10,
                    "warehouseSkuName": "单品2个组成1个销售sku",
                    "warehouseSkuWeight": "50",
                    "saleSkuCode": "53586714577",
                    "saleSkuName": "决明子",
                    "bomVersion": "D",
                    "saleSkuImg": "https://img1.popicorns.com/fit-in/200x200/dev/file/2021/11/08/8cbba5e1160a48e9bd9b43e54450ab7c.jpg",
                    "warehouseSkuHeight": "50",
                    "warehouseSkuLength": "50",
                    "warehouseSkuWidth": "50"
                }
            ],
            "operationFlag": 1
        }
        res = requests.post(url_other_submit, headers=self.headers, data=json.dumps(data_submit))
        print(res.json().get('message'))

    #其他入库-上架
    def other_upper(self):
        url_other_upper = 'https://test-scms.popicorns.com/api/ec-wms-api/entryorder/putOnTheShelf'
        data_upper = {
                        "entryOrderId": self.entryorderid,
                        "skuList": [
                            {
                                "skuCode": "53586714577B02",
                                "shelvesLocationCode": "KW-SJQ-01",
                                "skuQty": "10",
                                "abnormalQty": 0
                            },
                            {
                                "skuCode": "53586714577B01",
                                "shelvesLocationCode": "KW-SJQ-01",
                                "skuQty": "5",
                                "abnormalQty": 0
                            },
                            {
                                "skuCode": "53586714577D01",
                                "shelvesLocationCode": "KW-SJQ-01",
                                "skuQty": "10",
                                "abnormalQty": 0
                            }
                        ]
                    }
        res = requests.post(url_other_upper, headers=self.headers, data=json.dumps(data_upper))
        print('上架' + res.json().get('message'))

    #删除库存
    def del_wares(self):
        sql_ims_list = [
            "DELETE FROM wares_inventory WHERE ware_sku_code LIKE '53586714577%' and warehouse_id IN (517,536);",
            "DELETE FROM goods_inventory WHERE goods_sku_code = '53586714577' and current_warehouse_id IN (517,536);",
            "DELETE FROM central_inventory WHERE goods_sku_code = '53586714577' and warehouse_id IN (517,536);",
            "UPDATE `supply_wms`.`base_warehouse_location` SET `use_state` = 0 WHERE `id` IN (257136,257137,257138);"

        ]

        sql_wms_list = [
            "DELETE FROM trf_transfer_out_order WHERE warehouse_id =536;",
            "DELETE FROM trf_transfer_out_order_detail WHERE warehouse_id =536;",
            "DELETE FROM trf_transfer_in_order WHERE warehouse_id =517;",
            "DELETE FROM trf_transfer_in_order_detail WHERE warehouse_id =536;",
            "DELETE FROM trf_box_order WHERE warehouse_id =536;",
            "DELETE FROM trf_box_order_detail WHERE warehouse_id =536;",
            "DELETE FROM trf_box_order_in WHERE warehouse_id =517;",
            "DELETE FROM trf_box_order_detail_in WHERE warehouse_id =536;",
            "DELETE FROM trf_handover_order WHERE warehouse_id =536;",
            "DELETE FROM trf_transfer_demand WHERE warehouse_id =536;",
            "DELETE FROM trf_transfer_pick_order WHERE warehouse_id =536;",
            "DELETE FROM trf_transfer_pick_order_detail WHERE warehouse_id = 536;"
        ]

        for i in sql_ims_list:
            read_db.ReadDB('ims').execute(i)

        for i in sql_wms_list:
            read_db.ReadDB('wms').execute(i)

    #添加库存
    def add_wares(self):
        self.other_add()
        self.other_upper()

    #获取仓库信息
    def get_warehouse_info(self, wareshouse_code):
        warehouse_info = read_ever.GetData().get_wareshouse_info(wareshouse_code)
        return warehouse_info

    #创建调拨需求-备货
    def add_demand(self, delivery_warehouse_code, receive_warehouse_code, sku_code, qty, num):
        url_add_demand = 'https://test-scms.popicorns.com/api/ec-oms-api/demand/create'

        delivery_warehouse_info = self.get_warehouse_info(delivery_warehouse_code)
        receive_warehouse_info = self.get_warehouse_info(receive_warehouse_code)

        data_demand = {
                            "deliveryWarehouseId": delivery_warehouse_info.get("warehouseId"),
                            "deliveryWarehouseName": delivery_warehouse_info.get("warehouseName"),
                            "deliveryWarehouseCode": delivery_warehouse_info.get("warehouseCode"),
                            "receiveWarehouseId": receive_warehouse_info.get("warehouseId"),
                            "receiveWarehouseName": receive_warehouse_info.get("warehouseName"),
                            "receiveWarehouseCode":  receive_warehouse_info.get("warehouseCode"),
                            "remark": "",
                            "details": [
                                {
                                    "itemSkuCode": sku_code,
                                    "itemSkuType": 1,
                                    "quantity": qty,
                                    "itemPicture": "https://img.popicorns.com/dev/file/2021/11/08/8cbba5e1160a48e9bd9b43e54450ab7c.jpg"
                                }
                            ]
                        }
        time.sleep(1)
        for i in range(num):
            res = requests.post(url_add_demand, headers=self.headers, data=json.dumps(data_demand))
            print('备货需求{0}新增:'.format(i) + res.json().get('message'))

    #查询调拨需求
    def search_demand(self):
        url_search_demand = "https://test-scms.popicorns.com/api/ec-wms-api/transferOut/demand/list"
        data_search_demand = {
                                "current":1,
                                "size":2,
                                "states":[

                                ],
                                "receiveWarehouseCode":"",
                                "demandCodeList":None,
                                "goodsSkuCodeList":None,
                                "startCreateTime":"",
                                "endCreateTime":"",
                                "sourceCodeList": None,
                                "customerType":"",
                                "createUserId":10,
                                "demandType":"",
                                "cancelFlag":"",
                                "sortField":[
                                    {
                                        "field":"create_time",
                                        "type":"DESC"
                                    }
                                ],
                                "saleOrderCodes":None
                            }
        res = requests.post(url_search_demand, headers=self.headers, data=json.dumps(data_search_demand))
        demands = res.json().get("data").get("records")
        demands_list = []
        for i in demands:
            demands_list.append({
                "id": i.get("id"),
                "demandCode": i.get("demandCode")
            })
        return demands_list

    #取消调拨需求
    def cancel_demand(self):
        url_cancel_demand = 'https://test-scms.popicorns.com/api/ec-oms-api/demand/cancel'
        data_cancle_demand = {"id": 373}
        res = requests.post(url_cancel_demand, headers=self.headers, data=json.dumps(data_cancle_demand))
        print(res.json())
        print('取消调拨需求:' + res.json().get('message'))

    #创建拣货单
    def create_pick(self):
        info = self.search_demand()
        demand_codes_list = []
        for item in info:
            demand_codes_list.append(str(item.get("demandCode")))
        url_create_pick = 'https://test-scms.popicorns.com/api/ec-wms-api/transferOut/picking/create'
        data_create_demand = {"demandCodes": demand_codes_list, "pickType": 1}
        res = requests.post(url_create_pick, headers=self.headers, data=json.dumps(data_create_demand))
        print("创建拣货单:", res.json().get("message"))

    #查询拣货单
    def search_pick_order(self):
        url_search_pick_order = 'https://test-scms.popicorns.com/api/ec-wms-api/transferOut/picking/list'
        data_search_pick_order = {
                                      "current": 1,
                                      "size": 10,
                                      "pickOrderNo": "",
                                      "createUsername": "",
                                      "pickingUser": "",
                                      "state": 0,
                                      "pickType": "",
                                      "distributeStatus": "",
                                      "type": "",
                                      "payTime": [],
                                      "startPickTime": "",
                                      "endPickTime": "",
                                      "sortField": [
                                        {
                                          "field": "create_time",
                                          "type": "DESC"
                                        }
                                      ],
                                      "saleSkuCodes": [],
                                      "skuCodes": []
                                    }
        res = requests.post(url_search_pick_order, headers=self.headers, data=json.dumps(data_search_pick_order))
        pick_orders = res.json().get("data").get("records")
        pick_orders_list = []
        for i in pick_orders:
            pick_orders_list.append({
                "id": i.get("id"),
                "pickOrderNo": i.get("pickOrderNo")
            })
        return pick_orders_list


    #分配拣货人
    def assign_picker(self):
        info = self.search_pick_order()
        pick_order_no = info[0].get("pickOrderNo")
        url_assign_picker = 'https://test-scms.popicorns.com/api/ec-wms-api/transferOut/picking/assignPickUser'
        data_assign_picker = {"pickOrderNos": [pick_order_no], "pickUsername": "黄乐乐", "pickUserId": "10"}
        res = requests.post(url_assign_picker, headers=self.headers, data=json.dumps(data_assign_picker))
        print("分配拣货人：", res.json().get("message"))
        return pick_order_no

    #查询拣货单详情
    def picking_detail(self):
        info = self.search_pick_order()
        pick_order_no = info[0].get("pickOrderNo")
        url_pciking_detail = "https://test-scms.popicorns.com/api/ec-wms-api/transferOut/picking/detail/{0}?t=1642684741035)".format(pick_order_no)
        res = requests.get(url_pciking_detail, headers=self.headers)
        picking_detail = res.json().get("data")
        return picking_detail


    #确认拣货
    def do_picking(self):
        info = self.search_pick_order()
        pick_order_no = info[0].get("pickOrderNo")
        picking_detail = self.picking_detail()
        url_do_picking = "https://test-scms.popicorns.com/api/ec-wms-api/transferOut/picking/doPicking"
        data_submit_tray_info = {
                                    "pickOrderNo": pick_order_no,
                                    "details": picking_detail.get("details")
                                }
        print(data_submit_tray_info)
        res = requests.post(url_do_picking, headers=self.headers, data=json.dumps(data_submit_tray_info))
        print("确认拣货：", res.json().get("message"))

    # 按需装托
    def submit_tray_info(self):
        pass




if __name__ == '__main__':

    """
    测试使用仓库：
    533	佛山1号备货仓	CNFS02-BH
    534	佛山2号备货仓	CNFS03-BH
    
    537	佛山1号中转仓	CNFS02-ZZ
    535	佛山2号中转仓	CNFS03-ZZ
    
    539	英国1号仓	UKBH01
    540	法国1号仓	ZY-FOR
    
    532	英国2号仓	UKBH02
    530	休斯顿1号仓	USTX01
    """

    warehouse_info = GetWarehouse().switch_warehouse("FSBH")        #切换到预期仓库
    authorization = read_ever.GetData().get_authorization("config.json")     #获取token


    player = Transfer(authorization)
    # player.del_wares()  # 删除库存
    # player.add_wares()     #添加库存

    # player.add_demand("FSBH", "LA01", "53586714577", 5, 2)     #新增调拨-备货需求
    x = player.search_demand()
    print(x)
    #player.cancel_demand()      #取消调拨需求
    # player.create_pick()      #创建拣货单
    # player.assign_picker()      #分配拣货人
    # player.do_picking()     #确认拣货
