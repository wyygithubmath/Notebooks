# -*- coding: utf-8 -*-
#---------------------------------------
#   Programming：QiuShiBaiKe
#   version：0.1
#   author：wyy
#   data：2017-01-06
#   language：Python 3.5.2
#   tools : urllib
#   function：get text
#---------------------------------------

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import time

url = "http://www.qiushibaike.com/"
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
headers = {'User-agent': user_agent}
req = urllib.request.Request(url, headers=headers)
html_response = urllib.request.urlopen(req)
bsObj = BeautifulSoup(html_response, "lxml")
qsbk = bsObj.findAll("div",{"class": "content"})
for item in qsbk:
    print(item.text)

page_url = bsObj.find("ul",{"class": "pagination"}).find("a",{"rel": "nofollow"}).attrs["href"]
urllib.parse.urlparse(page_url)


for i in range(2,36):
    mypath = "text/page/" + str(i) + "/"
    myquery = urllib.parse.urlparse(page_url)[4]
    url_all = url + mypath + myquery
    req = urllib.request.Request(url_all, headers=headers)
    html = urllib.request.urlopen(req)
    bsObj = BeautifulSoup(html, "lxml")
    qsbk = bsObj.findAll("div",{"class": "content"})
    print(' ' * 30 + str(i) + ' ' * 30)
    for item in qsbk:
        print(item.text)
        print('-' * 60 + '\n')
    time.sleep(3)
