# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import smtplib
# content = MIMEMultipart()  #建立MIMEMultipart物件
# content["subject"] = "Learn Code With Mike"  #郵件標題
# content["from"] = "a0921789923@gmail.com"  #寄件者
# content["to"] = "a0966603328@gmail.com" #收件者
# content.attach(MIMEText("Demo python send email"))  #郵件內容
#
#
# with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
#     try:
#         smtp.ehlo()  # 驗證SMTP伺服器
#         smtp.starttls()  # 建立加密傳輸
#         smtp.login("a0921789923@gmail.com", "bfwlhwhlekgjtxrl")  # 登入寄件者gmail
#         smtp.send_message(content)  # 寄送郵件
#         print("Complete!")
#     except Exception as e:
#         print("Error message: ", e)


n = int(input("two-digit integer:"))
first = n%10
print(first)
second = (n-first)/10
print(second)
print(first+second)