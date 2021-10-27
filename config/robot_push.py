# -*- coding: utf-8 -*-
import datetime
import time

import fake_useragent
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
    url = "https://d1.weather.com.cn/sk_2d/101010100.html?_=1618886817920"
    r_url = requests.get(url, headers=get_headers())
    print(r_url.json())
    message = json.loads(r_url.text.encode("latin1").decode("utf8").replace("var dataSK = ", ""))
    cityname = message['cityname']
    aqi = int(message['aqi'])
    sd = message['sd']
    wd = message['WD']
    ws = message['WS']
    temp = message['temp']
    weather = message['weather']
    if aqi <= 50:
        airQuality = "优"
    elif aqi <= 100:
        airQuality = "良"
    elif aqi <= 150:
        airQuality = "轻度污染"
    elif aqi <= 200:
        airQuality = "中度污染"
    elif aqi <= 300:
        airQuality = "重度污染"
    else:
        airQuality = "严重污染"
    return cityname + " " + '今日天气：' + weather + ' 温度：' + temp + ' 摄氏度 ' + wd + ws + ' 相对湿度：' + sd + \
        ' 空气质量：' + str(aqi) + "（" + airQuality + "）"
get_weather()

def get_top_list():
    requests_page = requests.get('http://top.baidu.com/buzz?b=1&c=513&fr=topbuzz_b42_c513')
    soup = BeautifulSoup(requests_page.text, "lxml")
    soup_text = soup.find_all("a", class_='list-title')
    i = 0
    top_list = []
    for text in soup_text:
        i += 1
        top_list.append("[" + text.string.encode("latin1").decode("GBK") + "](" + text['href'] + ")")
        if i == 10:
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
    if hour == 6:
        return "各位同学早上好！\n"
    if hour == 12:
        return "各位同学中午好！"
    if hour == 21:
        return "各位同学晚上好！"
    else:
        return "测试信息"

def get_sendContent():
    sendContent = greetings() + "\n" + get_week_day(datetime.date.today()) + "\n\n" + get_weather() + "\n\n" + str(
        get_top_list()).replace("', '", '\n').replace("['", "").replace("']", "") + "\n\n" + get_daily_sentence()
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


