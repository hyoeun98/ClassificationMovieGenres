import selenium
import pandas as pd
import pickle

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


URL = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%81%ED%99%94+%EB%B0%94%EB%9E%8C+%EC%B6%9C%EC%97%B0%EC%A7%84'
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
#options.add_argument("--headless")
options.add_argument("--auto-open-devtools-for-tabs")
driver = webdriver.Chrome(options=options, executable_path='C:/anaconda/chromedriver')
driver.implicitly_wait(time_to_wait=3)
driver.get(url=URL)
df = pd.read_csv('movies.csv')
title = df['title']
user_dic = []
require= []

for i in range(1, len(title)):
    search_box = driver.find_element_by_xpath('//*[@id="nx_query"]')
    search_box.clear()
    search_box.send_keys("영화 " + title[i] + " 출연진")
    search_box.submit()

    try:
        characters = driver.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div[2]/div/ul/li[2]/div/ul')
    except:
        require.append(title[i])
    else:
        try:
            characters_names = characters.find_elements_by_css_selector('a > div > div.title_box > span > span')
        except:
            continue
        else:
            for c in characters_names:
                user_dic.append(c.text)

character_names = 'CharacterNames.txt'
require_title = 'RequireTitle.txt'
with open(character_names, 'ab') as lf:
    pickle.dump(user_dic, lf)
    
with open(require_title, 'ab') as lf:
    pickle.dump(require, lf)

