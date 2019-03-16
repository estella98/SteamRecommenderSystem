import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import urllib.request as req
from requests import get
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#create the output dataframe
outPut= pd.DataFrame(columns=['gameName','gameID'])

driver = webdriver.Chrome(ChromeDriverManager().install())
#putting all the distinct game names into a list
gameDF = pd.read_csv("gameList.csv", usecols=[0], dtype= str)
gameList = gameDF['gameName'].values.tolist()


for item in gameList:
    try:
        urlEncode = req.pathname2url(item)
        url = "https://steamdb.info/search/?a=app&q='" + urlEncode + "'"
        print(url)
        driver.get(url)
        class_element = driver.find_element_by_class_name('app')
        # getting the appId for the game
        #print(class_element.text.split(" ")[0])
        gameId = class_element.text.split(" ")[0]
        print(gameId)
        outPut = outPut.append({'gameName': item, 'gameID': gameId}, ignore_index = True)
        print("---------------")
        export_csv = outPut.to_csv ('gameID.csv', index = None, header=True)
    except:
        continue








