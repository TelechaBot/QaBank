# -*- coding: utf-8 -*-
# @Time    : 8/30/22 12:15 AM
# @FileName: CCCC.py
# @Software: PyCharm
# @Github    ：sudoskys
import ast
import json
import random, time

import requests


def random_sleep(mu=3, sigma=2.8):
    """正态分布随机睡眠
        :param mu: 平均值
        :param sigma: 标准差，决定波动范围
    """
    secs = random.normalvariate(mu, sigma)
    if secs <= 0:
        secs = mu  # 太小则重置为平均值
    time.sleep(secs)


header = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}
# https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/13469825/JSON/?heading=Molecular+Formula
# https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/13469826/JSON/
# 题库生产器


cid = 13469826
TIKU = {}
for i in range(90):
    random_sleep()
    cid += 1
    Json = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{cid}/JSON/?heading=Molecular+Formula"
    Pic = f"https://pubchem.ncbi.nlm.nih.gov/image/imgsrv.fcgi?cid={cid}&t=l"
    mew = requests.get(Json, headers=header)
    if mew.status_code == 200 and len(mew.text) > 632:
        TIKU[str(cid)] = {}
        TIKU[str(cid)]["Formula"] = (
            mew.json()["Record"]["Section"][0]["Section"][0]["Information"][0]["Value"]["StringWithMarkup"][0].get(
                "String"))
        TIKU[str(cid)]["Picture"] = Pic
        print(TIKU[str(cid)])

# content = json.dumps(TIKU, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False)
content = TIKU
Timu = {}
for i, k in content.items():
    import random

    key_list = []
    keys_list = ["A", "B", "C", "D"]
    some_key = random.sample(content.keys(), 1)[0]
    A = content[some_key].get("Formula")
    some_keyS = random.sample(content.keys(), 1)[0]
    B = content[some_keyS].get("Formula")
    some_keySS = random.sample(content.keys(), 1)[0]
    C = content[some_keySS].get("Formula")
    key_list.append(A)
    key_list.append(B)
    key_list.append(C)
    key_list.append(k.get("Formula"))
    random.shuffle(key_list)
    dictionary = dict(zip(keys_list, key_list))

    print(dictionary)
    suf = f"请看这个结构式选择正确的分子式！ \n A " + dictionary["A"] + "\n B " + dictionary["B"] + "\n C " + dictionary[
        "C"] + "\n D " + \
          dictionary["D"]
    Timu[suf] = {}
    Timu[suf]['Pic'] = k.get("Picture")
    for iss, kss in dictionary.items():
        if kss == k.get("Formula"):
            Timu[suf]['Answer'] = iss

with open("../Library/PubChems.json", "w", encoding="utf8") as f:
    json.dump(Timu, f, indent=4, ensure_ascii=False)
