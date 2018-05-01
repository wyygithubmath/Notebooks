import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://www.lagou.com/jobs/list_Python?city=上海'
driver = webdriver.PhantomJS(executable_path='../../CS1_Collection/phantomjs/bin/phantomjs.exe')
driver.get(url)

bs4 = BeautifulSoup(driver.page_source, 'lxml')
