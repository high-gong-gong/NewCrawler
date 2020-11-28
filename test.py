import threading
import time

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
content = MIMEMultipart()  #建立MIMEMultipart物件
content["subject"] = "Learn Code With Mike"  #郵件標題
content["from"] = "a0921789923@gmail.com"  #寄件者
content["to"] = "a0966603328@gmail.com" #收件者
content.attach(MIMEText("Demo python send email"))  #郵件內容


keyb = 0

class keybo(threading.Thread):
    def newThread(self):
        Thread(target=self.method).start()
    def method(self):
        global keyb
        keyb = 1

class Job(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(Job, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()   # 用於暫停執行緒的標識
        self.__flag.set()    # 設定為True
        self.__running = threading.Event()   # 用於停止執行緒的標識
        self.__running.set()   # 將running設定為True
    def run(self):
        while self.__running.isSet():
            self.__flag.wait()   # 為True時立即返回, 為False時阻塞直到內部的標識位為True後返回
            multifunction()
    def pause(self):
        self.__flag.clear()   # 設定為False, 讓執行緒阻塞
    def resume(self):
        self.__flag.set()  # 設定為True, 讓執行緒停止阻塞
    def stop(self):
        self.__flag.set()    # 將執行緒從暫停狀態恢復, 如何已經暫停的話
        self.__running.clear()    # 設定為False

def main():
    # menu_all = threading.Thread(target = multifunction)
    # menu_all.start()
    a =Job()
    a.start()
    time.sleep(5)
    if keyb == 0:
        updated()
        a.stop()

def multifunction():
    lp = True
    k = keybo()
    while lp == True:
        try:
            print('3秒未執行任何程序則更新，執行:1.程式一 2.程式二 3.離開')
            choose = int(input('請輸入欲使用功能代號:'))
            if choose == 1:
                k.method()
                function1()
            elif choose == 2:
                k.method()
                function2()
            elif choose == 3:
                lp = False
                break
            else:
                print('輸入錯誤')
        except Exception as g:
            pass
            print(g)

def updated():
    try:
        print("\n自動更新程式1和程式2")
        print(abcde)
    except Exception as g:
        pass
        print(g)
        sentmail()

def function1():
    print("程式1")

def function2():
    print("程式2")

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

if __name__ == "__main__":
    main()
