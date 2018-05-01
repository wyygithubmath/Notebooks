#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.parse
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

import pandas as pd

url_aps = "http://journals.aps.org/search/results?"
jqu = {"page": 1, "date": "custom", "sort": "recent", "per_page": 20, "start_date": "2015", "end_date": "2017", "journal": ["prl", "pra", "rmp"], "clauses": '[{"operator":"AND","field":"all","value":"Gaussian"},{"operator":"AND","field":"title","value":"coherence"}]'}
text = requests.get('http://journals.aps.org/search/results?', params=jqu)
drive = webdriver.PhantomJS()
drive.get(text.url)
bsObjPh = BeautifulSoup(drive.page_source, "lxml")
total_num = int(bsObjPh.findAll("button")[-1].get_text())

for i in range(1, total_num+1):
	

drive.close()
