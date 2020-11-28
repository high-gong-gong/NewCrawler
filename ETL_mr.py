# 司博特 目前抓取json ,txt已關閉
import requests, os ,csv, json, time, random
from bs4 import BeautifulSoup
from tools import *


headers = {}
ua = '''Referer: https://www.mr-sport.com.tw/weighttraining/page/2
User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Mobile Safari/537.36'''


def getArticle(pages): ##需要修改
    # 起始page 從1開始
    count = 1  # 流水號
    fileName = 'mr_aerobic-training'  # 路徑名稱
    url_list = loadUrl(fileName)#讀取url_list確認是否已經爬取過
    page = 1
    url = 'https://www.mr-sport.com.tw/weighttraining/page/%s'
    # headers = {}
    # ua = '''Referer: https://www.mr-sport.com.tw/weighttraining/page/2
    # User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Mobile Safari/537.36'''
    for i in ua.split("\n"):
        headers[i.split(": ")[0]] = i.split(": ")[1]
    # 抓取每頁資訊
    for times in range(pages):
        res = requests.get(url%(page), headers=headers)
        # print(res)
        soup = BeautifulSoup(res.text,'html.parser')
        # print(soup)
        title = soup.select('h2')
        # print(title[0].text)
        # 抓取每篇文章
        for t in title:
            title_name = t.findAll('a')[0].text
            print(title_name)
            title_url = t.findAll('a')[0]['href']
            # 判斷是否已抓取過
            if title_url in url_list:  # 如果list裡的urtl已存在print已存在
                print('已存在')
            # 如果list裡的url不存在則爬取網頁
            else:
                # print(title_url)
                url_2 = t.findAll('a')[0]['href']
                res_2 = requests.get(url_2, headers=headers)
                soup_2 = BeautifulSoup(res_2.text,'html.parser')
                article_1 = soup_2.select('div.entry')
                # print(article_1[0].text)
                content = article_1[0].text.split('※')[0]
                # print(article_1[0].text.split('※')[0])
                mr_json = []
                value = {'url': title_url, 'title': title_name, 'lesson': 0, 'lesson_time': 0,
                         'strengh': 0, 'describe': content, 'time': 0,'author': 0}
                #saveMDB(value, 'fitness', fileName) # 執行Mongo
                saveUrl(title_url, fileName) # 將爬完的url存在txt
                saveFile(fileName, title_name, value, count)
                sleeptime=random.randint(3, 5)
                time.sleep(sleeptime)
                count += 1
            page +=1


if __name__ ==  '__main__':
    start = time.time()
    # 填入目標網址 以及 欲抓取頁數
    result = getArticle(2) ##需要修改
    end = time.time()
    print('執行時間:%f 秒'%(end - start))