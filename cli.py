import requests as r
from auth import login
from myconfig import ConfigReport
import sys

USE_PROXIES = False  # TODO
proxies = None
if USE_PROXIES:
   proxies = {
      'http': 'http://127.0.0.1:9999',
      'https': 'http://127.0.0.1:9999',
   }

print("本脚本会基于上次打卡记录构造本次打卡数据，并自动提交。")

username = sys.argv[1]
password = sys.argv[2]

print('登录中...')
s = r.Session()
login(s, username, password)

try:
   ConfigReport().default_method(s, proxies=proxies)
   print('打卡成功！')
except Exception as e:
   print('错误！\n', e)
