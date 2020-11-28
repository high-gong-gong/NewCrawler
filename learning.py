import requests
requests.request():構造一個請求，支撐以下各方法的基礎方法
requests.get():獲取HTML網頁的主要方法，對應於HTTP的GET
requests.head():獲取HTML網頁頭訊息的方法，對應於HTTP的HEAD
requests.post():向HTML網頁提交POST請求的方法，應用於HTTP的POST
requests.put():向HTML網頁提交PUT請求的方法，應用於HTTP的PUT
requests.patch():向HTML網頁提交局部修改請求，應用於HTTP的PATCH
requests.delete():向HTML頁面提交刪除請求，應用於HTTP的DELETE


requests.request(method, url, **kwargs):
    method: 請求方式, 對應get/put/post..等七種:
        requests.request('GET', url, **kwargs)
        requests.request('HEAD', url, **kwargs)
        requests.request('POST', url, **kwargs)
        requests.request('PUT', url, **kwargs)
        requests.request('PATCH', url, **kwargs)
        requests.request('delete', url, **kwargs)
        requests.request('OPTIOINS', url, **kwargs)
requests.get(url, params=None, **kwargs):
    url:擬獲取頁面的url連結
    params:url中的額外參數，字典或字節流格式，可選
    **kwargs:12個控制訪問的參數
requests.head(url, **Kwargs)
requests.post(url, data=None, json=None, **Kwargs)
requests.put(url, data=None, **Kwargs)
requests.patch(url, data=None, **Kwargs)
requests.delete(url, **Kwargs)


**kwargs:控制訪問的參數，共13個:
    params:字典或字節序列，作為參數增加到url中
    data:字典、字節序列或文件對象，作為Request的內容
    json:JSON格式的數據，作為Request的內容
    headers:字典，HTTP訂製頭(例如'user-agent':'Chrome/10'仿製Chrome第10個版本的瀏覽器)
    cookies:字典或CookieJar, Request中的cookie
    auth:元組，支持HTTP認證功能
    files:字典類型，傳輸文件
    timeout:設定超時時間，秒為單位
    proxies:字典類型，設定訪問代理服務器，可以增加登入認證
    allow_redirects: True/False，默認為True，重定向開關
    stream: True/False，默認為True，獲取內容立即下載開關
    verify: True/False，默認為True，認證SSL證書開關
    cert:本地SSL證書路徑




Response:
    r.status_code:HTTP請求的返回狀態,200表示連接成功,404表示失敗
    r.text:HTTP響應內容的字符串形式,即url對應的頁面內容
    r.encoding:從HTTP header中猜測的響應內容編碼方式
    r.apparent_encoding:從內容中分析出的響應內容編碼方式(被選編碼方式)
    r.content:HTTP響應內容的二進位形式


HTTP協議:
    URL格式 http://host[:port][path]
        host:合法的Internet主機域名或IP地址
        port:端口號，缺省端口為80
        path:請求資源的路徑