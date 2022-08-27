import ast
import json
import random
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
    elif key == "Drive":
        # with open(Dir + "Drive.json", 'r') as drivef:
        #     data = json.load(drivef)
        return {}
    elif key == "Bili":
        return {}
    elif key == "Songci":
        dls = json.loads(dls)
        Timu = {}
        for i in range(6):
            for i in dls:
                some = i["paragraphs"]
                author = i["author"]
                title = i["rhythmic"]
                keys = random.randint(2, len(some) - 2)
                guess_up = some[keys - 1]
                guess = some[keys]
                guess_down = some[keys + 1]
                s = dls[random.randint(2, 60)]["paragraphs"]
                a = dls[random.randint(2, 60)]["paragraphs"]
                ganrao1 = random.sample(s, 1)[0]
                ganrao2 = random.sample(a, 1)[0]
                if len(guess) > 15:
                    some = [
                        (f"在 {author} 的诗《{title}》中，有这样一句: {guess}\n请问它的下面一句是？ |A:{guess_down}|B:{ganrao1}|C:{ganrao2}\n\n请回答大写字母",
                         "A"),
                        (f"在 {author} 的诗《{title}》中，有这样一句: {guess}\n请问它的下面一句是？ |A:{ganrao1}|B:{guess_down}|C:{ganrao2}\n\n请回答大写字母",
                         "B"),
                        (f"在 {author} 的诗《{title}》中，有这样一句: {guess}\n请问它的下面一句是？ |A:{ganrao2}|B:{ganrao1}|C:{guess_down}\n\n请回答大写字母",
                         "C"),
                    ]
                    question1 = random.sample(some, 1)[0]
                    # question2 = f"在 {author} 的诗《{title}》中，有这样一句: {guess}\n请问它的上面一句是？"
                    if len(question1[0] + question1[1]) < 3500:
                        Timu[question1[0]] = question1[1]
                else:
                    some = [
                        (f"在 {author} 的诗《{title}》中，有这样一句: {guess}\n请问它的上面一句是？ |A:{guess_up}|B:{ganrao1}|C:{ganrao2}\n\n请回答大写字母",
                         "A"),
                        (f"在 {author} 的诗《{title}》中，有这样一句: {guess}\n请问它的上面一句是？ |A:{ganrao1}|B:{guess_up}|C:{ganrao2}\n\n请回答大写字母",
                         "B"),
                        (f"在 {author} 的诗《{title}》中，有这样一句: {guess}\n请问它的上面一句是？ |A:{ganrao2}|B:{ganrao1}|C:{guess_up}\n\n请回答大写字母",
                         "C"),
                    ]
                    question2 = random.sample(some, 1)[0]
                    # question2 = f"在 {author} 的诗《{title}》中，有这样一句: {guess}\n请问它的上面一句是？"
                    if len(question2[0] + question2[1]) < 3500:
                        Timu[question2[0]] = question2[1]

                # Timu[question2] = guess_up
                Timu = json.dumps(Timu, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False)
                Timu = json.loads(Timu)
        return Timu
    elif key == "Lunyu":
        dls = json.loads(dls)
        Timus = {}
        for isa in range(6):
            for iss in dls:
                some = iss["paragraphs"]
                chapter = iss["chapter"]
                keys = random.randint(1, len(some) - 2)
                # guess_up = some[keys - 1]
                guess = some[keys]
                guess_down = some[keys + 1]
                s = random.sample(dls, 1)[0]["paragraphs"]
                a = random.choice(dls)["paragraphs"]
                ganrao1 = random.sample(s, 1)[0]
                ganrao2 = random.sample(a, 1)[0]
                if len(guess) > 15:
                    some = [
                        (
                        f"在论语 {chapter} 中，有这样一句对话: {guess}\n请问它的下面一句是？ \n|A:{guess_down}\n\n|B:{ganrao1}\n\n|C:{ganrao2}\n\n请回答大写字母",
                        "A"),
                        (
                        f"在论语 {chapter} 中，有这样一句对话: {guess}\n请问它的下面一句是？ \n|A:{ganrao1}\n\n|B:{guess_down}\n\n|C:{ganrao2}\n\n请回答大写字母",
                        "B"),
                        (
                        f"在论语 {chapter} 中，有这样一句对话: {guess}\n请问它的下面一句是？ \n|A:{ganrao2}\n\n|B:{ganrao1}\n\n|C:{guess_down}\n\n请回答大写字母",
                        "C"),
                    ]
                    question1 = random.sample(some, 1)[0]
                    # question2 = f"在 {author} 的诗《{title}》中，有这样一句: {guess}\n请问它的上面一句是？"
                    if len(question1[0] + question1[1]) < 3500:
                        Timus[question1[0]] = question1[1]
                # Timu[question2] = guess_up
                Timus = json.dumps(Timus, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False)
                Timus = json.loads(Timus)
        return Timus


def WriteOut(content, path, key):
    if content:
        if len(str(content)) > 333:
            contents = json.dumps(content, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False)
            print(str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())) + " 写出了:" + key)
            with open(path, 'w+') as fs:
                fs.write(contents)
        else:
            # print(len(content))
            print(str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())) + " 跳过了:" + key)
    else:
        print(str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())) + " 复用了:" + key)


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
                "FullUrl": "https://raw.githubusercontent.com" + "/TelechaBot/QaBank/main/Library/" + k + ".json",
            }

content = json.dumps(Useful, sort_keys=True, indent=4, separators=(',', ':'))
with open("Bank.json", 'w+', encoding="utf8") as f:
    f.write(content)
