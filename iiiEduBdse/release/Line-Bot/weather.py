import json
import yaml
import urllib.parse as UP

import requests

class SendWR:
    def __init__(self):
        self.Token = none
        self.locationName = none
        self.authorization = none


    def setToken(self,which_token):
        f = open(f'conf/token.txt', 'r')
        token = f.read()
        self.Token = token.split('\n')[which_token]
        f.close()

    def setAuthorization(self):
        with open('conf/authorization.yaml', 'r') as f:
            self.authorization = yaml.load(f)

    def weather_report(self):
        if self.locationName and self.authorization:
            req = f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization={self.authorization}&limit=10&format=JSON&locationName={self.locationName}&sort=time"
            res = requests.get(req)
            data = json.loads(res.text)
            if data['records']['location'] != []:
                describe = data['records']['location'][0]['weatherElement'][0]['time'][0]['parameter']['parameterName']
                min_tmp = data['records']['location'][0]['weatherElement'][2]['time'][0]['parameter']['parameterName']
                max_tmp = data['records']['location'][0]['weatherElement'][4]['time'][0]['parameter']['parameterName']
                pop = data['records']['location'][0]['weatherElement'][1]['time'][0]['parameter']['parameterName']
                mes = f"{UP.unquote(self.locationName)}今日為:{describe}天氣唷～\n降雨機率為:{pop}%\n最低溫:{min_tmp}度,最高溫:{max_tmp}度"
                return mes
            else:
                print("請輸入正確關鍵字唷")
                err = f"親，您輸入的的\" {self.locationName} \"，未查詢到，請輸入正確關鍵字唷"
                return err


    def send_line_message(self,mes):
        if self.Token:
            try:
                requests.post(
                            url='https://notify-api.line.me/api/notify',
                            headers={
                                'Authorization': f'Bearer {self.Token}'
                            },
                            data={
                                  'message': f"\n{mes}",
                            },
                            )
            except Exception as e:
                print(e)

    def start(self):
        mes = self.weather_report()
        self.send_line_message(mes)