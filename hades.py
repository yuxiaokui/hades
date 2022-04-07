import importlib
import requests
import sys
import os
import re

proxy ={"http": "socks5h://127.0.0.1:10808", "https": "socks5h://127.0.0.1:10808"}
version = "1.0.0"


def upgrade():
    print("当前版本" + version)
    url = "https://github.com/yuxiaokui/hades/releases/latest"
    session = requests.session()
    response = session.get(url,timeout=5, proxies=proxy)
    latest_version = response.url.split("/")[-1]
    print("最新版本" + latest_version)
    if latest_version != version:
        print("版本更新....")
        url = "https://github.com/yuxiaokui/hades/releases/download/"+latest_version+"/hades.py"
        session = requests.session()
        response = session.get(url, timeout=5, proxies=proxy)
        with open('hades.py',"wb") as f:
            f.write(response.content)
    
def list_local_pocs():
    print("本地存在poc列表：")
    for poc in os.listdir("./pocs"):
        if poc == "__pycache__":
            continue
        print(poc)
    return os.listdir("./pocs")

def list_remote_pocs():
    local_pocs = os.listdir("./pocs")
    print("远程存在poc列表：")
    url = "https://github.com/yuxiaokui/hades/tree/main/pocs"
    session = requests.session()
    response = session.get(url, timeout=5, proxies=proxy)
    p = r"/yuxiaokui/hades/blob/main/pocs/(.*?).py"
    pocs = re.findall(p,response.text)
    for poc in pocs:
        print(poc + ".py")  
        if poc + ".py" not in local_pocs:
            print(poc + "下载...")
            url = "https://raw.githubusercontent.com/yuxiaokui/hades/main/pocs/"+poc+".py"
            print(url)
            response = session.get(url, timeout=5, proxies=proxy)
            with open("pocs/" + poc + ".py","wb") as f:
                f.write(response.content)

if __name__ == '__main__':
    upgrade()
    list_local_pocs()
    list_remote_pocs()
    poc = sys.argv[1]
    target = sys.argv[2]
    if target[-1] != "/":
        url = target + "/"
    else:
        url = target
    runner = importlib.import_module('pocs.' + poc)
    if runner.poc(url):
        print(url + " ===>  Vuln!")
    else:
        print(url + " ===>  NotVuln!")
