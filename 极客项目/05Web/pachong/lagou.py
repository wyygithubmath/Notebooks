#! /usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------
# author: wyy
# date: 20170404
# ---------------------

from wcpackages import *

url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="

html = requests.get(url)

bsObj = BeautifulSoup(html.text, "lxml")
# phantomJS
driver = webdriver.PhantomJS()
driver.implicitly_wait(15)
driver.get(url)
ps = driver.page_source
print(BeautifulSoup(ps, "lxml"))
