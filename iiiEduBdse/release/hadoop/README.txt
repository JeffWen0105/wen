歡迎使用hadoop自動啟動腳本，簡化複雜指令操作
使用說明:

1.腳本修改執行權限，並將腳本放入/usr/local/bin 內，
 
ex. ~$ sudo chmod 777 hadoopStartBdse12
ex. ~$ sudo mv hadoopStartBdse12 /usr/local/bin

2.執行方式(除"scpBdse12"，其餘腳本僅限Hadoop帳號執行):
	
	(1) hadoopStartBdse12
		ex. ~$ hadoopStartBdse12
	(2) hadoopStopBdse12
		ex. ~$ hadoopStopBdse12
	(3) nodecheckBdse12
		ex. ~$ nodecheckBdse12
	(4) safeScpBdse12 (檢查叢集是否在正運行)
		ex. /usr/loacl/hadoop/etc/hadoop/$ safeScpBdse12 core-site.xml  /usr/loacl/hadoop/etc/hadoop/ 
		# 第一個參數為欲複製之檔案 ， 第二個參數為複製到其它電腦的路徑
	(5) scpBdse12
		ex. /usr/loacl/hadoop/etc/hadoop/$ scpBdse12 core-site.xml  /usr/loacl/hadoop/etc/hadoop/ 
		# 第一個參數為欲複製之檔案 ， 第二個參數為複製到其它電腦的路徑

注: 請先確定上述檔案均為Unix換行格式!!

該腳本秉持GNU自由軟體精神，鼓勵各位修改程式使符合使用者本身的服務需求!!

