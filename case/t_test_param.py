#导包
import unittest
from parameterized import parameterized

#新建测试类
class TestParam(unittest.TestCase):
    #参数化-列表里面套元祖
    @parameterized.expand([('admin','123456'),('user01','654321')])
    def test_param(self,username,password):
        print('用户名：',username)
        print('密码：',password)

if __name__ == "__main__":
    unittest.main()