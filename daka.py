import requests
import json
import ast
import time

with open("zuizhongjieguo", "r") as f:
    a = f.read()
    h = ast.literal_eval(a) #转换为字典类型
proxies = {'http': '//192.168.1.9:8080'}
urlds = "http://reportedh5.17wanxiao.com/sass/api/epmpics"
header = h
datas = json.dumps(
    """
    
    请求体  格式 python 字典
    """

)
r = requests.post(urlds, data=datas, headers=header)

respo = json.loads(r.text)

tim = time.strftime("%Y-%m-%d %H:%M:%S %A", time.localtime())

if respo["code"] == "10000" and respo["msg"] == "成功" and respo["data"] == 1:

    with open("Log/记录", "a") as fi:
        fi.write(tim + "打卡成功" + "\n")
else:
    with open("Log/记录", "a") as fi:
        fi.write(tim + "打卡失败" + "\n")
        print("response结果:" + r.text)

with open("Log/记录", "r") as fp:
    fankui = fp.read()
    print(fankui)
