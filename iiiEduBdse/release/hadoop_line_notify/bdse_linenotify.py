# Copyright (c) IIIedu BDSE.
# BDSE12 Project <contactus@iii.org.tw>
# 指導老師：楊禎文老師


import sys
import requests
import datetime


# 取得Token
def get_conf():
    f = open('bdse-conf.txt', 'r')
    token = f.read()
    token = token.strip('\n')
    f.close()
    return token

# 設定時間日期格式
def time_set():
    iso_time_format = '%Y/%m/%d %H:%M'
    the_time = datetime.datetime.now().strftime(iso_time_format)
    return the_time

# 向Line Notify 請求服務    
def line_notify(state,token,message):
        requests.post(
            url='https://notify-api.line.me/api/notify',
            headers={
                'Authorization': f'Bearer {token}'
            },
            data={
                'message': "{} {}, 發生時間:{}".format(message,state,the_time)
            }
        )


if __name__ == '__main__':
    status = sys.argv[1]
    message = sys.argv[2]
    token = get_conf()
    the_time = time_set()
    if status == 'good' :
        line_notify("恢復",token,message)
    else :
        line_notify("停止",token,message)