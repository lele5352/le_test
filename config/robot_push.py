# -*- coding: utf-8 -*-
import datetime
import time
import random
import requests
import simplejson as json
from bs4 import BeautifulSoup



def get_headers():
    #location = './fake_useragent_0.1.11.json'
    ua_lsit = [
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36"
        ]
    ua = random.choice(ua_lsit)
    headers = {
        'user-agent': ua
    }

    return headers

def get_week_day(date):
    week_day_dict = {
        0: '星期一',
        1: '星期二',
        2: '星期三',
        3: '星期四',
        4: '星期五',
        5: '星期六',
        6: '星期天',
    }
    day = date.weekday()
    res = "今天日期为：" + str(datetime.date.today()) + ' ' + week_day_dict[day]
    return res


def get_weather():
    url = "http://www.nmc.cn/rest/weather?stationid=59287&_=1638428068253"
    r_url = requests.get(url, headers=get_headers())
    data = r_url.json()['data']
    air = data['air']
    real = data['real']
    station = data['predict']['station']
    city = station['city']
    aqi = air['aqi']
    humidity = str(data['real']['weather']['humidity'])
    wind_direct = real['wind']['direct']
    wind_power = real['wind']['power']
    temp = real['weather']['temperature']
    weather = real['weather']['info']
    airQuality = air['text']
    comfort_dict = {9999: ' ', 4: '很热，极不适应', 3: '热，很不舒适', 2: '暖，不舒适', 1: '温暖，较舒适', 0: '舒适，最可接受', -1: '凉爽，较舒适',\
                    -2: '凉，不舒适', -3: '冷，很不舒适', -4: '很冷，极不适应'}
    icomfort_no = real['weather']['icomfort']
    icomfort = comfort_dict[icomfort_no]

    return city + " " + '今日天气：' + weather + ' 当前温度：' + str(temp) + ' ℃ ' +'舒适度：' + icomfort +' '+ wind_direct +' ' + wind_power + \
           ' 当前相对湿度：' + humidity + "%" + ' 空气质量：' + str(aqi) + "（" + airQuality + "）"

def get_top_list():
    requests_page = requests.get('http://top.baidu.com/buzz?b=1&c=513&fr=topbuzz_b42_c513')
    soup = BeautifulSoup(requests_page.text, "lxml")
    soup_text = soup.find_all(class_='content_1YWBm')
    i = 0
    top_list = []
    for text in soup_text:
        i += 1
        top_list.append("[" + text.div.string + "](" + text.a['href'] + ")")
        #print(text.div.string)
        #print(text.a['href'])
        if i == 9:
            break
    return top_list

def get_daily_sentence():
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url, headers=get_headers())
    r = json.loads(r.text)
    content = r["content"]
    note = r["note"]
    daily_sentence = "> " + content + "\n" + "> " + note
    return daily_sentence

def greetings():
    hour = int(time.strftime('%H', time.localtime(time.time())))
    if 5 <= hour <= 10:
        return "各位同学早上好！\n"
    elif hour == 11 or hour == 12:
        return "各位同学中午好！\n"
    elif 13 <= hour <= 18:
        return "各位同学下午好！\n"
    elif 19 <= hour <= 24:
        return "各位同学晚上好！\n"
    else:
        return "夜深了，早点睡觉咯~"

def get_sendContent():
    sendContent ="# " + greetings() + "\n" + \
                 '<font color=\"warning\">'+ get_week_day(datetime.date.today()) + '</font>' + "\n\n" + \
                 get_weather() + "\n\n" + \
                 str(get_top_list()).replace("', '", '\n').replace("['", "").replace("']", "") + "\n\n" + \
                 get_daily_sentence()
    print(sendContent)
    return sendContent

def send(content):
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=2c0ee031-c1a7-4217-a532-99ec013e436c" #填写你自己的机器人配置链接
    headers = {"Content-Type": "text/plain"}
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": content,
        }
    }
    requests_url = requests.post(url, headers=headers, data=json.dumps(data))
    if requests_url.text == '{"errcode":0,"errmsg":"ok"}':
        return "发送成功"
    else:
        return "发送失败" + requests_url.text

if __name__ == '__main__':

    #send(get_sendContent())
    #get_sendContent()
    #greetings()
    t1 = time.time() + 8*60*60
    print(t1)