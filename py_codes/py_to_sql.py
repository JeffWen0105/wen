import sys
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
from sqlalchemy import create_engine     
#必要的套件:sqlalchemy,pandas,pymysql
#pip3 install sqlalchemy
#pip3 install pymysql

def get_data(user = sys.argv[1]          #第一個參數:使用者帳號
            ,password = sys.argv[2]      #第二個參數:使用者密碼
            ,database = sys.argv[3]      #第三個參數:使用的資料庫
            ,data = sys.argv[4]          #第四個參數:csv檔案路徑及名稱
            ,port = 3306 ):              #第五個參數:DB的port,預設3306
    try:
        if len(sys.argv) > 5:
            port =sys.argv[5]
        engine = create_engine(f'mysql+pymysql://{user}:{password}@localhost:{port}/{database}')
        df = pd.read_csv(data)
        df.to_sql(f"{data}", engine, index= False)
        sql = 'show tables;'
        df = pd.read_sql_query(sql, engine)
        print(df)
        print('Successfully!!!!')
    except Exception as e:
        #print(e) #顯示錯誤使用
        print('Expression error!!!Terminate program...')
        exit() 
    

 
if __name__ == "__main__":
    get_data()