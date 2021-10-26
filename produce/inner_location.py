from api.api_ecStockoperation import ApiPdaInnerLocation
from tools.read_json import ReadJson
from produce.login import Login

def get_url(url_file):
    return ReadJson().read_json(url_file)

def get_token(token_file):
    return Login().get_authorization(token_file)

def get_data(data_file):
    return ReadJson().read_json(data_file)


class InnerLocation(object):

    def batch_move(self):
        pass

    def single_move(self, url_file, token_file, data_file):

        url = get_url(url_file)["pda_inner_location"]["single_move"]
        authorization = get_token(token_file)
        datas = get_data(data_file)["single_move"]
        res = ApiPdaInnerLocation().api_post_single(url, authorization, datas)

        print(res.json())

    def move_to_bad_location(self):
        pass

    def move_to_good_location(self):
        pass

if __name__ == '__main__':
    InnerLocation().single_move('url.json', 'login.json', 'pda_batch_move.json')