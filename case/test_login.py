"""
    目标：完成登录业务实现
"""
#导包 unittest ApiLogin
import unittest
from parameterized import parameterized
from api.api_login import ApiLogin
from tools.read_ever import ReadJson

#读取数据函数
def get_data(filename):
    datas = ReadJson(filename).read_json()
    arrs = []
    for data in datas.values():
        arrs.append((data.get('url'),
                     data.get('username'),
                     data.get('password'),
                     data.get('grant_type'),
                     data.get('expect_result'),
                     data.get('status_code')
                     ))
    return arrs
#新建测试类
class TestLogin(unittest.TestCase):
    #新建测试方法
    @parameterized.expand(get_data("login.json"))
    def test_login(self, url, username, password, grant_type, expect_result, status_code):
        #调用登录方法

        res = ApiLogin().api_post_login(url, username, password, grant_type)
        #print('查看响应结果：', res.json())
        #断言响应信息及状态码
        self.assertEqual(expect_result, res.json()['message'])
        self.assertEqual(status_code, res.status_code)


if __name__ == '__main__':
    unittest.main()
