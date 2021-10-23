from tools.read_json import ReadJson
from api.api_login import ApiLogin

def get_data(filepath):

    return ReadJson(filepath).read_json()

class Login(object):

    #获取token
    def get_authorization(self, filepath):
        datas = get_data(filepath)
        data_login_001 = datas["login_001"]
        url = data_login_001.get("url")
        username = data_login_001.get("username")
        password = data_login_001.get("password")
        grant_type = data_login_001.get("grant_type")

        res = ApiLogin().api_post_login(url, username, password, grant_type)
        res_data = res.json()["data"]
        authorization = res_data["tokenHead"] + " " + res_data["token"]
        return authorization


if __name__ == '__main__':
    Login().get_authorization("login.json")