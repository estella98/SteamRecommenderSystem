import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import urllib.request as req

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#create the output dataframe
outPut= pd.DataFrame(columns=['gameName','gameID','Confidence'])

driver = webdriver.Chrome(ChromeDriverManager().install())
#putting all the distinct game names into a list
gameDF = pd.read_csv("gameList.csv", usecols=[0], dtype= str)
gameList = gameDF['gameName'].values.tolist()

for item in gameList:
    
    urlEncode = req.pathname2url(item)
    #print(urlEncode)
    print(item)
    url = "https://steamdb.info/search/?a=app&q='" + urlEncode + "'"
    driver.get(url)
    p_element = driver.find_element_by_class_name('app')
    print(p_element.text)
    print("---------------")





