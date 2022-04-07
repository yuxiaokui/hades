import requests
def poc(url):
  r = requests.get(url + "?class.module.classLoader.DefaultAssertionStatus=x")
  if r.status_code == 400:
    return True
  else:
    r = requests.post(url + "?class.module.classLoader.DefaultAssertionStatus=x")
    if r.status_code == 400:
      return True
