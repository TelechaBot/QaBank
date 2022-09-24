# -*- coding: utf-8 -*-
# @Time    : 9/24/22 10:46 PM
# @FileName: idom.py
# @Software: PyCharm
# @Github    ：sudoskys
import json
import requests

host = "https://raw.githubusercontent.com/TelechaBot/QaBank/main/"
proxy_host = "https://raw.fastgit.org/TelechaBot/QaBank/main/"
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

# 请求相关数据
i_url = "https://github.com/masongzhi/Scripts/raw/master/request4word/result.json"
mew = requests.get(i_url, headers=header)
Json_obj = mew.json()

'''json
{
        "answer":"忠言逆耳",
        "confound":"示、问、笑、恶、远、纸、草、笔、天、标、言、分、耳、魔、逆、忠、走、使、路、迷、叉、指、方、说",
        "explain":"诚恳正直的规劝往往刺耳，而不易被人接受。",
        "id":20,
        "pic":"http://twevle.mlxuoy.cn/kantucai/chengyu/172.jpg"
    },
'''


def save_csonfig(_csonfig):
    with open("../Library/Idiom.json", "w", encoding="utf8") as file:
        json.dump(_csonfig, file, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False)


# 清洗数据

New_obj = []
for i in Json_obj:
    i["pic"] = f"{host}Image/idiom/{i['answer']}.jpg"
    i["proxy_pic"] = f"{proxy_host}Image/idiom/{i['answer']}.jpg"
    New_obj.append(i)
save_csonfig(New_obj)

result = json.dumps(New_obj, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False)
print(result)
