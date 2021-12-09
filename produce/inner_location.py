from api.api_ecStockoperation import ApiPdaInnerLocation
from tools.read_ever import GetData

class InnerLocation(object):

    def batch_move(self, url_file, token_file, data_file):
        url = GetData().get_url(url_file)["pda_inner_location"]["batch_move"]
        authorization = GetData().get_data(token_file)["authorization"]
        datas = GetData().get_data(data_file)["batch_move"]
        res = ApiPdaInnerLocation().api_post_single(url, authorization, datas)
        print(res.json())

    def single_move(self, url_file, token_file, data_file):

        url = GetData().get_url(url_file)["pda_inner_location"]["single_move"]
        authorization = GetData().get_token(token_file)["authorization"]
        datas = GetData().get_data(data_file)["single_move"]
        res = ApiPdaInnerLocation().api_post_single(url, authorization, datas)
        print(res.json())

    def move_to_bad_location(self,url_file, token_file, data_file):

        url = GetData().get_data(url_file)["pda_inner_location"]["to_bad"]
        authorization = GetData().get_data(token_file)["authorization"]
        datas = GetData().get_data(data_file)["to_bad"]
        res = ApiPdaInnerLocation().api_post_to_bad(url, authorization, datas)
        print(res.json())

    def move_to_good_location(self, url_file, token_file, data_file):
        url = GetData().get_data(url_file)["pda_inner_location"]["to_good"]
        authorization = GetData().get_data(token_file)["authorization"]
        datas = GetData().get_data(data_file)["to_good"]
        res = ApiPdaInnerLocation().api_post_to_good(url, authorization, datas)
        print(res.json())


if __name__ == '__main__':

    #批量移库
    InnerLocation().batch_move('url.json', 'config.json', 'pda_inner_location.json')

    #逐件移库
    #InnerLocation().single_move('url.json', 'config.json', 'pda_inner_location.json')

    #转次
    #InnerLocation().move_to_bad_location('url.json', 'config.json', 'pda_inner_location.json')

    #转良
    #InnerLocation().move_to_good_location('url.json', 'config.json', 'pda_inner_location.json')