import requests
import math

import pandas as pd
import munch


def get_json(frequency=1): 
    '''連線至kaggle的討論區，如果連線狀態不正常（非200）將離開程式'''
    if frequency < 1:
        print(f'(您輸入的參數為:{frequency},請輸入大於0以上的正整數)')
        exit()
    page = math.ceil( (frequency*6)/16 )
    json_list = []
    for page in range(1 ,page+1 ):
        response = requests.get(
                    url=f'https://www.kaggle.com/forums/35355/topics.json?sortBy=top&group=all&page={page}&pageSize=20&category=all',
                    headers={
                        'Referer': 'https://www.kaggle.com/c/home-credit-default-risk/discussion?sortBy=top&group=all&page=1&pageSize=20&category=all',
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
                    },
                    timeout=3
                )
        if response.status_code != 200:    #如果網路回應不是200就離開程式。
            print(f'response status is not 200 ({response.status_code})')
            exit()
        json_list.append(response.json())
    data = combine(json_list,frequency)
    return data


def combine(json_list,frequency): 
    '''分析下載下來的Json檔並分類排序組成DataFrame'''
    classmate = ['軍皓','裕鈞','浩祖','詠茹','索先','冠穎']*frequency
    kaggle_url = 'https://www.kaggle.com'
    title = []
    url = []
    for num in range (0,len(json_list)):
        for topic in json_list[num]['topics']:   #將Json解析並取值。
            topic = munch.munchify(topic)
            title.append(topic.title)             #取出要的欄位擺入list內。 
            url.append(kaggle_url+topic.topicUrl)

    #依據classmate list長度去除多餘主題。
    zip_name = list(zip(classmate,title[4:]))   #去除前4項沒有意義的討論主題
    zip_web = list(zip(classmate,url[4:]))
    get_name = list(zip(*zip_name))
    get_web = list(zip(*zip_web))

    #組合成DataFrame。
    data = pd.DataFrame(
            { 'title':get_name[1],'url':get_web[1],'charge': get_name[0]} 
            , index = range( 1 ,(len(get_name[0])+1) )
            )
    return data



if __name__ == '__main__':

    data = get_json(4)  #  參數每個人各別需要看文件的次數，預設為1。 
    data.to_csv('discussion.csv', encoding= 'utf_8_sig') 
    #輸出檔名為discussion的CSV檔。


