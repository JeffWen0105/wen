import time
import json
import yaml

import requests
from weather import SendWR
from ig_app import IG_scraper
from line_message import Message as mes
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *



app = Flask(__name__)



# Channel Access Token
line_bot_api = LineBotApi(<Your Channel Access Token>)
# Channel Secret
handler = WebhookHandler(<Your Channel Secret>)

@app.route("/")
def hello():
    return "Hi , This is a Line bot server..."


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    print(body)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)

    # 初始化 Line Notify
    line_mes = mes()
    line_mes.setToken(-1)

    if event.message.text.replace(' ','') == "IG":
        line_mes.send(messages= f"歡迎使用IG自動爬取系統，請輸入想要爬取IG帳號..EX: IG-帳號 ")
    try:
        if len(event.message.text.split('-')) == 2:
            if event.message.text.split('-')[0].replace(' ','') == "IG" and event.message.text.split('-')[-1] != None:
                ig_usr = event.message.text.split('-')[-1]
                print(f"開始爬取IG-{ig_usr}帳號...")
                line_mes.send(messages= f"開始爬取: {ig_usr} 帳號的最新一篇文章中，請稍候.....")
                # 初始化 IG 爬蟲
                ig_crawer = IG_scraper()
                ig_crawer.setToken(-1)
                ig_crawer.start(ig_usr)
    except Exception as _:
        print(_)

    if event.message.text.replace(' ','') == "氣象":
        line_mes.send(messages= f"歡迎使用氣象查詢系統，請輸入想要查詢縣市..EX: 氣象-臺北市")
    try:
        if len(event.message.text.split('-')) == 2:
            if event.message.text.split('-')[0].replace(' ','') == "氣象" and event.message.text.split('-')[-1] != None:
                # 初始化 氣象 爬蟲
                weather = SendWR()
                weather.setToken(-1)
                weather.locationName = event.message.text.split('-')[-1]
                weather.start()
    except Exception as _:
        print(_)

if __name__ == "__main__":
    app.run()
