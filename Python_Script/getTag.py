import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import urllib.request as req
from requests import get
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://steamdb.info/app/214560/"
driver.get(url)
class_element = driver.find_elements_by_class_name('btn-tag')
for item in class_element:
    print(item.text)
