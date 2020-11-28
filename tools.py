#import pymongo, os
import os





def saveUrl(url, txtName):
    """
    將已經爬完的網頁放入tet檔
    url: 已經爬完的網頁
    txtName:存檔檔名
    """

    path = './list/%s' % txtName

    with open('%s.txt' % (path), 'a+', encoding='utf-8') as w:

        w.write(str(url)+'\n')






def loadUrl(txtName):
    """
    讀取tet檔裡的urk
    txtName:存檔檔名
    return:url_list
    """

    path = './list/%s' % txtName

    #如果有檔案將url存進list裡
    try:
        with open('%s.txt' % (path), 'r', encoding='utf-8') as w:

            url_list = []

            url_list1 = w.readlines()

            for i in url_list1:

                i = str(i).rstrip('\n')

                url_list.append(i)

            return url_list

    #如果沒有檔案回傳一個空的list
    except:

        url_list = []

        return url_list






def saveMDB(article_json, base, col):
    '''
    將爬到的文章存入mongoDB
    article_json:爬到的字典
    base:要存到的資料庫
    col:要存到的集合
    return:回復存檔成功
    '''

    myclient = pymongo.MongoClient("mongodb://192.168.1.120:27017/")

    # print(article_json)

    mydb = myclient['%s'% base]

    mycol = mydb['%s' % col]

    mylist = article_json

    mycol.insert_one(mylist)

    return print('insert成功')





def loadMDB(base, col):

    myclient = pymongo.MongoClient("mongodb://192.168.1.120:27017/")

    # print(article_json)

    mydb = myclient['%s'% base]

    mycol = mydb['%s' % col]

    data = pd.DataFrame(list(mycol.find()))






def saveFile(fileName, fileTitle, article_json, count):
    '''
    爬完網頁後以JASON格式存成text檔
    fileName:路徑名稱
    fileTiile:Jason的title當檔名
    article_json:要存的JASON
    count:如果檔名不符合格式以路徑名稱+流水號 流水號起始
    return:新的流水序號
    '''

    path = './%s' % fileName

    if not os.path.exists(path):

        os.mkdir(path)

    try:

        with open('%s/%s.txt' % (path, fileTitle), 'w', encoding='utf-8') as w:

            w.write(str(article_json))

    except:

        # 如果title有特殊字元改以網頁名稱+流水號方式儲存
        with open('%s/%s%s.txt' % (path, fileName, count), 'w', encoding='utf-8') as w:

            w.write(str(article_json))
