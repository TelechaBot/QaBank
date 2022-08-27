import ast
import json
import time

import requests

import random


def load_csonfig():
    with open("../Library/Drive.json", encoding="utf-8") as f:
        _csonfig = json.load(f)
    return _csonfig


def save_csonfig(_csonfig):
    with open("../Library/Drive.json", "w", encoding="utf8") as f:
        json.dump(_csonfig, f, indent=4, ensure_ascii=False)


header = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}


def random_sleep(mu=24, sigma=12):
    """正态分布随机睡眠
        :param mu: 平均值
        :param sigma: 标准差，决定波动范围
    """
    secs = random.normalvariate(mu, sigma)
    if secs <= 0:
        secs = mu  # 太小则重置为平均值
    time.sleep(secs)


times = 0
errors = 0
uid = 0000
key = "xxxx"
while times < 88 and errors < 8:
    times += 1
    print(f"执行了{times}，错误发生:{errors}")
    i = f"http://de.ylapi.cn/driverexam/query.u?uid={uid}&appkey={key}&subject=1&sort=2&page={times}&maxSize=15"
    mew = requests.get(i, headers=header)
    dict1 = load_csonfig()
    if mew.status_code == 200 and len(mew.text) > 632:
        data = mew.json()
        if str(data.get("code")) == str(1000):
            kik = data.get("datas")
            dict1["datas"] = dict1.get("datas") + kik
            # result = {name: value for name, value in newer.items() if name in result_key}
            save_csonfig(dict1)
        else:
            errors += 1
            print(data.get("code"))
    else:
        errors += 1
        print(mew.status_code)

    random_sleep()
