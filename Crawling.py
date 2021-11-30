import selenium
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

def log_in():
    URL = 'https://watcha.com/sign_in'
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    #options.add_argument("--headless")
    options.add_argument("--auto-open-devtools-for-tabs")
    driver = webdriver.Chrome(options=options, executable_path='C:/anaconda/chromedriver')
    driver.implicitly_wait(time_to_wait=10)
    driver.get(url=URL)

    driver.find_element_by_xpath('//*[@id="root"]/div[1]/main/div[1]/main/div/form/div[1]/input').send_keys('id@naver.com')
    driver.find_element_by_xpath('//*[@id="root"]/div[1]/main/div[1]/main/div/form/div[2]/input').send_keys('pw')
    driver.find_element_by_xpath('//*[@id="root"]/div[1]/main/div[1]/main/div/form/div[3]/button').click()
    driver.find_element_by_xpath('//*[@id="root"]/div[1]/main/div[1]/section/ul/li[4]/button/div[2]').click() # 프로필 선택
    driver.find_element_by_xpath('//*[@id="root"]/div[1]/nav/ul[2]/li[2]/div/div/div/a').click() # 탐색하기
    return driver

def crawl(i):
    try:
        movie_title = driver.find_element_by_xpath(f'//*[@id="root"]/div[1]/main/div[1]/section/ul/li[{i}]/div[2]/div/div/div[3]/h1')
    except: # 제목이 img
        try:
            movie_title = driver.find_element_by_xpath(f'// [@id="root"]/div[1]/main/div[1]/section/ul/li[{i}]/div[2]/div/div/div[3]/img').get_attribute('alt')
        except:
            data = {}
            return data
    else: # 제목이 h1
        movie_title = movie_title.text
        

    movie_story = driver.find_element_by_class_name("css-1yoak30").text
    movie_rating = driver.find_element_by_class_name("css-k8ekza").text
    movie_info = driver.find_elements_by_class_name("css-e8h0yq")
    
    try: 
        movie_info = movie_info[2].text
    except: 
        movie_info = movie_info[1].text

    data = {'title':movie_title,
          'story':movie_story,
          'rating':movie_rating,
           'info':movie_info}
    return data


if __name__ == '__main__':
    df = pd.DataFrame(columns=['title', 'story', 'rating', 'info'])

    for k in range(1,202):
        print(k)
        driver = log_in()
        driver.find_element_by_xpath('//*[@id="tags"]').click() # 태그 선택
        driver.find_element_by_xpath(f'//*[@id="root"]/div[1]/main/div[1]/div[1]/div/div[1]/div[3]/div/div[2]/div[{k}]').click() # 태그 선택
        time.sleep(3)
        for i in range(1,50): #한 tag 당 50row 씩 받아 오기
            try:
                driver.find_element_by_class_name("css-wvwa3p")
            except:
                pass
            else:
                driver.quit()
                break

            for j in range(1,5):
                movie = driver.find_element_by_xpath(f'//*[@id="root"]/div[1]/main/div[1]/section/ul/li[{i}]/div[1]/ul/li[{j}]/div/div[1]/div[1]/div[2]')
                ActionChains(driver).move_to_element(movie).pause(1.5).perform()
                try:
                    hidden_button = driver.find_element_by_class_name('css-g373u1-StyledEmbedButton').click()
                except:
                    exit_button = driver.find_element_by_class_name("css-zaijf6").click()
                    time.sleep(1)
                    print(i)
                    continue
                df = df.append(crawl(i),ignore_index=True)
                exit_button = driver.find_element_by_class_name("css-zaijf6").click()
                time.sleep(1)
                print(i)

        driver.quit()

    df.to_csv("watcha_crawling.csv", mode='a', index=False, header=False)

