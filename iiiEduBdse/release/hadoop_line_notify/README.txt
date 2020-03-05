歡迎使用hadoop自動檢查HA狀態腳本，並將即時訊息傳到Line裡
使用說明:

1. 將 bdseHadoopNotify 整份資料夾放置家目錄並修改執行權限
 	ex. 使用FileZilla等相關軟體匯入資料夾至 hadoop 帳號的家目錄內
	ex. ~$ chmod 770 bdseHadoopNotify/bdseHadoopNotify  #第一個為目錄 #第二個才是腳本

2. 執行方式(也可以CD 至 bdseHadoopNotify 目錄在執行，依個人喜好修改執行方式)	
	ex. ~$ bash bdseHadoopNotify/bdseHadoopNotify  # .bdseHadoopNotify/ bdseHadoopNotify 

3. 停止方式
	(1). Ctrl-Z 將程式丟入背景
    (2). 正常模式停止程序
		ex. ~$ kill -15 %1  # %後面帶程序工作號碼(數字)
    (3). 檢查程序是否關閉
		ex. ~$ jobs
		ex. ~$ jobs  #要使用兩次確認


注: 請先確定上述檔案均為Unix換行格式!!

該腳本秉持GNU自由軟體精神，鼓勵各位修改程式使符合使用者本身的服務需求!!

