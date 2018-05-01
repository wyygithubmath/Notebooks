# -*- coding: utf-8 -*-
#---------------------------------------
#   Programming：QiuShiBaiKe
#   version：0.1
#   author：wyy
#   data：2017-01-06
#   language：Python 3.5.2
#   tools : requests
#   function：get text
#---------------------------------------

import urllib.parse
import requests
from bs4 import BeautifulSoup
import time


url = "http://www.qiushibaike.com/text/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

flag = True
i = 1
while flag:
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')

    # get text
    qsbkText = soup.findAll('div', {'class': 'content'})
    with open('./Data/qsbkReq.txt', 'a+', encoding='utf-8') as textFile:
        textFile.write('\n' + str(i) + '\n')
        for item in qsbkText:
            textFile.write(item.text)
            textFile.write('\n' + '---' * 30 + '\n')
    time.sleep(3)

    # exist next url
    if soup.find('span', {'class': 'next'}) == None:
        flag = False

    # get link
    qsbkIndex = soup.find('ul', {'class': 'pagination'}).findAll('a')
    linkList = []
    for link in qsbkIndex:
        linkList.append(link['href'])
    url = 'http://' + urllib.parse.urlparse(url)[1] + linkList[-1]

    i = i + 1
    print(flag)
