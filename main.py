import ast
import json
import time

import requests
import pathlib

HOME = str(pathlib.Path().cwd()) + "/"
Dir = HOME + "Library/"
pathlib.Path(Dir).mkdir(exist_ok=True)

if pathlib.Path(HOME + "index.json").exists():
    with open(HOME + "index.json", 'r') as load_f:
        data = json.load(load_f)
else:
    print("Miss index.json")
    data = {}

header = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}


def well(name):
    """
    github@sudoskys
    :param name:
    :return: able use str
    """
    # import string
    name = name.replace('"', '_')  # 消除目标对路径的干扰
    name = name.replace("'", '_')
    name = name.replace(" ", '')
    # remove = string.punctuation
    table = str.maketrans(r'~!#$%^&,[]{}\/？?', '________________', "")
    return name.translate(table)


def DealData(dls, key):
    if key == "XXQG":
        dls = dls.replace(" ", '_')
        dls = json.loads(dls)
        return dls
    elif key == "LGBao":
        DtaDict = {}
        All = dls.split("]")
        for iss in All:
            if iss:
                item = iss.split("######")
                if len(item) == 2:
                    DtaDict[well(item[0])] = ast.literal_eval(item[1] + "]")
                else:
                    pass
                    print(item)
        return DtaDict


def WriteOut(content, path, key):
    if content:
        if len(content) > 222:
            contents = json.dumps(content, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False)
            print(str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())) + " 写出了:" + key)
            with open(path, 'w+') as fs:
                fs.write(contents)


Useful = {}
for k, i in data.items():
    try:
        mew = requests.get(i, headers=header)
    except Exception as e:
        print("Error Occur:" + k + "\n" + str(e) + "\n")
    else:
        time.sleep(2)
        if mew.status_code == 200:
            Con = DealData(mew.text, k)
            FileN = Dir + k + ".json"
            WriteOut(Con, FileN, k)
            Useful[k] = {
                # "Path": FileN,
                "Name": k,
                # "Time": str(int(time.time())),
                "Domain": "https://raw.githubusercontent.com",
                "Proxy": "https://raw.fastgit.org",
                "Url": "/TelechaBot/QaBank/main/Library/" + k + ".json",
            }

content = json.dumps(Useful, sort_keys=True, indent=4, separators=(',', ':'))
with open("Bank.json", 'w+', encoding="utf8") as f:
    f.write(content)
