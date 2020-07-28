使用Flask 製作簡單的登入（出）網頁
使用說明:

0. 下載相關Python套件:

	bcrypt
	flask_mysqldb
	flask

1. 創建MySQL 資料表:

	ex. MySQL:
	create table users ( id int not null auto_increment, name varchar(20) not null, email varchar(20) not null, password char(80) not null, primary key (id) );

2. 修改程式碼內MySQL的登入帳號、密碼、資料庫名稱、資料庫IP:

	ex. Python:
	app.config['MYSQL_HOST'] = 'localhost'          # 登入ip
	app.config['MYSQL_USER'] = 'root'               # 登入帳號
	app.config['MYSQL_PASSWORD'] = 'root'           # 登入密碼
	app.config['MYSQL_DB'] = 'db'                   # 登入資料庫名稱

4. 執行程式方式
	ex. ~/Flask_login$ python3 app.py

注: 
	1. 請確保MySQL可以正常運作
	2. 更詳細操作步驟[請參閱HackMD](https://hackmd.io/@JeffWen/flask)

該腳本秉持GNU自由軟體精神，鼓勵各位修改程式使符合使用者本身的服務需求!!