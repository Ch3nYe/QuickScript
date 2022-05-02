import urllib
import requests
import json
import time
import random

def sreplace(string):
    for token in ["?",",","╲","/","*",""",""","<",">","|"]:
        string = string.replace(token,"")
    return string

with open("./urls.txt","r") as f:
    lines = f.readlines()
    job_list = list(map(lambda x: x.strip().split()[1], lines))

prefix = "http://webapi.qtfm.cn/api/mobile"
cookies = {'qingting_id': 'xxx'} # your cookies from www.qtfm.cn

for idx, suffix in enumerate(job_list):
    try:
        jurl = prefix + suffix
        res = requests.get(jurl, cookies=cookies)
        j = json.loads(res.text)
        audioUrl = j["programInfo"]["audioUrl"]
        title = j["programInfo"]["title"]
        filename = "{}_{}.mp3".format(idx+1, title)
        filename = sreplace(filename)
        urllib.request.urlretrieve(
            audioUrl,
            filename,
        )
        print("[-]downloading {}/{} save to {}".format(idx+1, len(job_list), filename))
        time.sleep(random.random()*20)
    except Exception as e:
        print(e)
        print("[!]download failed id={}".format(idx))
        continue

