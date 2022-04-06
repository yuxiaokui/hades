import requests
import socket
import socks
socks.set_default_proxy(socks.SOCKS5, "localhost", 10808)

socket.socket = socks.socksocket
version = "0.1.0"

def upgrade():
    print("当前版本" + version)
    url = "https://github.com/yuxiaokui/hades/releases/latest"
    r = requests.get(url,timeout=5)
    latest_version = r.url.split("/")[-1]
    print("最新版本" + latest_version)
    if latest_version != version:
        print("版本更新....")
        url = "https://github.com/yuxiaokui/hades/releases/download/"+latest_version+"/hades.py"
        r = requests.get(url,timeout=5)
        with open('hades.py',"wb") as f:
            f.write(r.content)
if __name__ == '__main__':
    upgrade()