import os
import sys
import time
import json
import yaml

import requests


class IG_scraper():
    def __init__(self):
        self.ig = None
        self.Token = None

    def setToken(self,which_token):
        f = open(f'conf/token.txt', 'r')
        token = f.read()
        self.Token = token.split('\n')[which_token]
        f.close()

    def start(self,ig):
        self.ig = ig
        self.get_ig_name_passwd()
        self.get_info()
        print('done..')
        self.send_message()

    def get_ig_name_passwd(self):
        with open('conf/ig_conf.yaml', 'r') as f:
            self.data = yaml.load(f)

    def get_info(self):
        if self.ig:
            command =  f"instagram-scraper {self.ig} --media-metadata -u {self.data['username']} -p {self.data['password']} -d ./IG/{self.ig}/ -m 1 -t none"
            os.system(f"{command}")

    def send_message(self):
        if self.Token and self.ig:
            if os.path.isdir(f'IG/{self.ig}'):
                with open(f"IG/{self.ig}/{self.ig}.json" , 'r') as reader:
                    items = json.loads(reader.read())
                try:
                    massages = items['GraphImages'][0]['edge_media_to_caption']['edges'][0]['node']['text']
                    imgs = items['GraphImages'][0]['urls']
                    try:
                        requests.post(
                        url='https://notify-api.line.me/api/notify',
                        headers={
                            'Authorization': f'Bearer {self.Token}'
                        },
                        data={'message': f"\n {massages}",
                             })
                    except Exception as e:
                        print(e)
                    for _ in range(0,len(imgs)):
                        try:
                            requests.post(
                                url='https://notify-api.line.me/api/notify',
                                headers={
                                    'Authorization': f'Bearer {self.Token}'
                                },
                                data={'message': f"\nIG:{_+1}張圖，總計{len(imgs)}張圖",
                                      'imageThumbnail':f"{imgs[_]}",
                                      'imageFullsize': f"{imgs[_]}",
                                     })
                            time.sleep(0.5)
                        except Exception as e:
                            print(e)
                except Exception as e:
                    print(e)
                os.system(f'rm -r IG/{self.ig}')
            else:
                try:
                    massages = '沒有找到此IG帳號，請重新輸入...'
                    requests.post(
                    url='https://notify-api.line.me/api/notify',
                    headers={
                        'Authorization': f'Bearer {self.Token}'
                    },
                    data={'message': f"\n {massages}",
                         })
                except Exception as e:
                    print(e)
        else:
            print("請輸入Token..")
