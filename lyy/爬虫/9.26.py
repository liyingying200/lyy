import urllib.request

response = urllib.request.urlopen('https://www.baidu.com/')
html = response.read().decode('utf-8')
print(html)
#print(type(response))