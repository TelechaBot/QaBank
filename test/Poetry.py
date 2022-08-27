# -*- coding: utf-8 -*-
# @Time    : 8/27/22 10:11 PM
# @FileName: Poetry.py
# @Software: PyCharm
# @Github    ：sudoskys

import json
import time

import requests

import random


def load_csonfig():
    with open("../Library/Poetry.json", encoding="utf-8") as f:
        _csonfig = json.load(f)
    return _csonfig


def save_csonfig(_csonfig):
    with open("../Library/Poetry.json", "w", encoding="utf8") as f:
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


import random

with open("../Library/Songci.json", encoding="utf-8") as f:
    _csonfig = json.load(f)


with open("../Library/Poem.json", encoding="utf-8") as f:
    Timu = json.load(f)

for i in _csonfig:
    some = i["paragraphs"]
    author = i["author"]
    title = i["rhythmic"]
    keys = random.randint(1, len(some) - 2)
    guess_up = some[keys - 1]
    guess = some[keys]
    guess_down = some[keys + 1]

    if len(guess) > 15:
        question1 = (f"在 {author} 的诗《{title}》中，有这样一句: {guess}\n请问它的下面一句是？")
        question2 = (f"在 {author} 的诗《{title}》中，有这样一句: {guess}\n请问它的上面一句是？")
        Timu[question1] = guess_down
        Timu[question2] = guess_up
Timu = json.dumps(Timu, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False)
print(Timu)

# i = f"http://de.ylapi.cn/driverexam/query.u?uid={uid}&appkey={key}&subject=1&sort=2&page={times}&maxSize=15"
# mew = requests.get(i, headers=header)
# dict1 = load_csonfig()
# if mew.status_code == 200 and len(mew.text) > 632:
#     data = mew.json()
#     if str(data.get("code")) == str(1000):
#         kik = data.get("datas")
#         dict1["datas"] = dict1.get("datas") + kik
#         # result = {name: value for name, value in newer.items() if name in result_key}
#         save_csonfig(dict1)
#     else:
#         print(data.get("code"))
# else:
#     print(mew.status_code)
#
# random_sleep()
