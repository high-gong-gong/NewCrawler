#KC_Wang
import allrecipes_scraping
import cookpad_scraping
import icookweb_scraping
#Tyler
import ETL_dcard_fitness
import ETL_dcard_weightloss
import ETL_ptt_fitness
import ETL_mr
import ETL_hiyd
#Kuo
import businessweekly
import eagersport
import edh
import i_fit
import jo_fitness
import joiiup
import on1
import peeta
import pixnet
import sportsplanetmag
import trouble_care
import trueterral
import worldGym
#james
import Yahoo_Pic_Crawer         #防蟲覆爬
import Sougou_Pic_Crawer        #防蟲覆爬
#DaFu
import Youtube_txt

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
import threading
import time

keyb = 0

#寄送mail之參數
content = MIMEMultipart()  #建立MIMEMultipart物件
content["subject"] = "Bug!!"  #郵件標題
content["from"] = "a0921789923@gmail.com"  #寄件者
content["to"] = "a0966603328@gmail.com" #收件者
content.attach(MIMEText("There is an error in the program"))  #郵件內容

class waiting(threading.Thread):
    def newThread(self):
        Thread(target=self.method).start()
    def method(self):
        global keyb
        keyb = 1
        #print(keyb)

def main():
    menu_all = threading.Thread(target = multifunction)
    menu_all.start()
    time.sleep(10)
    if keyb == 0:
        updated()
        #print("update")

def multifunction():
    lp = True
    k = waiting()
    while lp == True:
        try:
            print('3秒未輸入任何指令則執行爬蟲程式更新')
            print('可執行功能:1.進入食譜爬蟲 2.進入健身爬蟲 3.離開')
            choose = int(input('請輸入欲使用功能代號:'))
            if choose == 1:
                k.method()
                cooking()
                os.system("cls");
            elif choose == 2:
                k.method()
                exercise()
            elif choose == 3:
                lp = False
            else:
                print('輸入錯誤')
        except Exception as g:
            pass
            print(g)

def updated():
    try:
        Yahoo_Pic_Crawer.main()
        ETL_mr.getArticle(1)
        print('\n')
        print(abcde)

    except Exception as g:
        pass
        print(g)
        sentmail()

def sentmail():
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login("a0921789923@gmail.com", "bfwlhwhlekgjtxrl")  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            print("Complete!")
        except Exception as e:
            print("Error message: ", e)

def cooking():
    lp = True
    item = []
    while lp == True:
        try:
            print('可執行功能:1.爬allrecipes 2.爬cookpad 3.爬icookweb 4.離開')
            choose = int(input('請輸入欲使用功能代號:'))
            if choose == 1:
                item = input("請輸入查詢食材:")
                page = int(input("請輸入爬取頁數:"))
                result_dict = allrecipes_scraping.getRecipeList(item, page)
                allrecipes_scraping.getRecipeIngredient(item, result_dict)
            elif choose == 2:
                item = input("請輸入查詢食材:")
                page = int(input("請輸入爬取頁數:"))
                result_dict = allrecipes_scraping.getRecipeList(item, page)
                cookpad_scraping.getRecipeContent(item,result_dict)
            elif choose == 3:
                item = input("請輸入查詢食材:")
                page = int(input("請輸入爬取頁數:"))
                result_dict = allrecipes_scraping.getRecipeList(item, page)
                icookweb_scraping.getRecipeContent(item,result_dict)

            elif choose == 4:
                lp = False
            else:
                print('輸入錯誤')
        except Exception as g:
            pass
            print(g)

def exercise():
    lp = True
    while lp == True:
        try:
            print('可執行功能:1.爬司博特 2.爬PTT 3.爬Hi運動 4.爬低卡健身版 5.爬低卡減重版 6.爬worldGym 7.爬良醫 8.爬伊格 9.爬早安健康 10.爬愛瘦身 11.爬滾去健身吧 12.爬揪健康 13.爬1on1 14.爬Petta 15.爬愛學習 16.爬運動星球 '
                  '17.爬Care 18.爬蔬羅特 19.爬Yahoo照片 20.爬Sougou照片 21.爬Youtube 22.離開')
            choose = int(input('請輸入欲使用功能代號:'))
            if choose == 1:
                page = int(input("請輸入爬取頁數:"))
                ETL_mr.getArticle(page)
            elif choose == 2:
                page = int(input("請輸入爬取頁數:"))
                ETL_ptt_fitness.getArticle(page)
            elif choose == 3:
                page = int(input("請輸入爬取頁數:"))
                ETL_hiyd.getArticle(page)
            elif choose == 4:
                before = int(input("請輸入爬取頁數:"))
                ETL_dcard_fitness.getArticle(before)
            elif choose == 5:
                before = int(input("請輸入爬取頁數:"))
                ETL_dcard_weightloss.getArticle(before)
            elif choose == 6:
                worldGym.worldGym(1)
            elif choose == 7:
                endPage = int(input("請輸入爬取頁數:"))
                businessweekly.businessweekiy(endPage)
            elif choose == 8:
                endPage = int(input("請輸入爬取頁數:"))
                eagersport.eagersport(endPage)
            elif choose == 9:
                count = int(input("請輸入爬取頁數:"))
                edh.edh(count)
            elif choose == 10:
                endPage = int(input("請輸入爬取頁數:"))
                i_fit.ifit(endPage)
            elif choose == 11:
                endPage = int(input("請輸入爬取頁數:"))
                jo_fitness.joFitness(endPage)
            elif choose == 12:
                endPage = int(input("請輸入爬取頁數:"))
                joiiup.joiiup(endPage)
            elif choose == 13:
                print('have bug')
            elif choose == 14:
                endPage = int(input("請輸入爬取頁數:"))
                peeta.peeta(endPage)
            elif choose == 15:
                count = int(input("請輸入爬取頁數:"))
                pixnet.pixnet(count)
            elif choose == 16:
                print('have bug')
                count = int(input("請輸入爬取頁數:"))
                sportsplanetmag.sportsplanetmag(count)
            elif choose == 17:
                endPage = int(input("請輸入爬取頁數:"))
                trouble_care.troubleCare(endPage)
            elif choose == 18:
                endPage = int(input("請輸入爬取頁數:"))
                trueterral.trueterral(endPage)
            elif choose == 19:
                print('尚未完成')
                #Yahoo_Pic_Crawer.GetYahooImag()
            elif choose == 20:
                print('尚未完成')
                #Sougou_Pic_Crawer.GetSougouImag()
            elif choose == 21:
                Youtube_txt.web_crawler()
            elif choose == 22:
                lp = False
            else:
                print('輸入錯誤')
        except Exception as g:
            pass
            print(g)

if __name__ == "__main__":
    main()