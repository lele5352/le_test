import requests
from api import

class FrozenReceipt(object):

    #冻结单
    def add_frozen_receipt(self, frozenCount, frozenReason, remark, storageLocationCode, waresSkuCode):
        self.frozenCount = frozenCount  #冻结数量
        self.frozenReason = frozenReason    #冻结原因
        self.remark = remark    #备注
        self.storageLocationCode = storageLocationCode  #库位编码
        self.waresSkuCode = waresSkuCode    #仓库sku编码







    #解冻/批量解冻单
    def batch_defrost(self):
        pass

    #冻结单列表查询
    def page(self):
        pass