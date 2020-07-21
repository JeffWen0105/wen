歡迎使用Line-Bot + Line-Notify，Line群組輸入指令並將爬蟲的即時訊息傳到群組內
使用說明:

	
1. 編輯bdse-conf.txt並輸入正確 Line Notify 權杖
	ex. ~$ nano conf/token.txt

2. 編輯ig_conf.yaml並輸入IG 帳號及密碼
	ex. ~$ nano conf/ig_conf.yaml

3. 編輯authorization.yaml並輸入中央氣象局開放資料平臺授權碼
	ex. ~$ nano conf/authorization.yaml

4. 執行程式方式
	ex. ~/line-bot$ gunicorn -w 3 app:app

注: 
	1. 請確保Web Server具備外部網路及SSL安全認證
	2. 更詳細操作步驟[請參閱HackMD](https://hackmd.io/@JeffWen/line-bot)

該腳本秉持GNU自由軟體精神，鼓勵各位修改程式使符合使用者本身的服務需求!!