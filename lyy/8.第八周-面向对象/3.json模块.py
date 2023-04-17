import json
import requests
"""
json模块：让Python数据与json互相转换，json数据是js语言中的，项目前后端进行数据交互，使用json数据
requests模块：获取里面数据，一般都是json数据
"""
# http://t.weather.sojson.com/api/weather/city/101180101
weather = "http://t.weather.sojson.com/api/weather/city/101180101"
res = requests.get(url=weather)
f = open("郑州天气.json", "w", encoding="utf-8")
f.write(res.text)