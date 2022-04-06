def poc(target):
  if target[-1] != "/"
    url = target + "/"
  else:
    url = target
    r = requests.get( url + "robots.txt")
  if "Disallow:" in r.text:
    return True
  
