# pip3 install beautifulsoup4
# pip install selenium
# pip install lxml
import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlretrieve

#設定使用的瀏覽器，並且將網頁設定在Google圖片搜尋(chromedriver要放在桌面)
driver = webdriver.Chrome('C:/Users/Big data/Desktop/chromedriver.exe')
url = 'https://www.youtube.com/?hl=zh-TW&gl=TW'
driver.get(url)

#輸入想搜尋的東西，並且使用Google圖片搜尋此物品
input_str = input("請輸入想搜尋的東西: ")
#input_str = "JoJos Bizarre Adventure"
driver.find_element_by_name('search_query').send_keys(input_str)
driver.find_element_by_id('search-icon-legacy').click()

time.sleep(5)

EE_BS=BeautifulSoup(driver.page_source,'lxml')
total_img=EE_BS.find_all('a',{"id":"video-title"})
#url = driver.current_url
#print(url)

#print(total_img[0])
for i in range(len(total_img)):
   if(total_img[i].get('title')):
       #driver.get(total_img[i].get('title'))
       title = total_img[i].get('title')
       url = total_img[i].get('href')
       url = "https://www.youtube.com/" + url
       print(title)
       print(url)