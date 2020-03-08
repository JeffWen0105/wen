# Copyright (c) IIIedu BDSE.
歡迎使用Hadoop偽叢集式伺服器版:
	要求程式: Vmware player等級以上
	預設系統配置: 8 G, 4 Cores
	最低系統配置: 4 G, 2 Cores (運行較大資料，可能會程式崩潰)
	Python : 3.6.9
	Hadoop生態系版本:
		hadoop:3.2.1      
		spark:2.4.5
		zookeeper:3.5.7
		kafka:2.4.0
	Hadoop主要設定檔: hadoop-env.sh、core-site.xml、mapred-site.xml、
			 yarn-site.xml、hdfs-site.xml、workers
	Spark主要設定檔:  spark-env.sh、spark-defaults.conf
使用說明:
	0.  bdse.7z 解壓縮後進入bdse資料夾，並對 bdse.vmx 案右鍵，
		執行Open with VMware Player，並選擇 " I copied it "，
		產生新的網卡MAC地址
	
	注  1. 第一次使用進入系統或是更換網域，請務必執行下方指令:
			bdse@bdse:~$ sudo bdseChangHosts 
			# 依據DHCP取得浮動IP 修訂Hosts清單IP
			# 查詢浮動IP方式: hostname -I
			
		2. 可以使用Putty、GitBash、ConEmu、等終端機登入操作:
			ex. ssh bdse@192.168.1.45   浮動IP請先查詢

	1. 登入帳號: bdse，密碼: bdse
	
	2. 切換hadoop帳號，帳號密碼均為: hadoop

	3. 啟動叢集:		
		(1) start-dfs.sh 						# 啟動HDFS
		(2) start-yarn.sh						# 啟動Yarn
		(3) mapred --daemon start historyserver				# 啟動HistoryServer
	
	4. 啟動筆記本:
		(1) jupyter notebook 			# jupyter lab
		(2) 到瀏覽器輸入該虛擬機取得的浮動IP，並加上8591 port埠號
			# ex. 192.168.1.45:8591 	# 浮動IP請先查詢
		(3) 進入筆記本密碼為空字串，直接點Log in 即可使用
			
	5. 關閉叢集:
		(1) mapred --daemon stop historyserver				# 關閉HistoryServer
		(2) stop-yarn.sh						# 關閉HDFS
		(3) stop-dfs.sh 						# 關閉Yarn
	
	*. 懶人開(關)叢集:
		(1) bdseStartAll
		(2) bdseStopAll
	*. 節點自動檢查:
		bdseNodeCheck
		
	*. Java程式網頁UI的port埠號:
		叢集啟動後，於瀏覽器輸入該虛擬機取得的浮動IP，並加上port埠號
		ex. 192.168.1.45:port number		# 浮動IP請先查詢
		1. NameNode : 9870
		2. ResourceManager : 8088
		3. HistoryServer : 19888
		4. Spark : 8080				# Spark Standalon
	

該虛擬機秉持GNU自由軟體精神，鼓勵各位修改程式碼使符合使用者本身的服務需求!!

-------------------------------------------------------------------------------

附錄:
	筆記本取得SparkSession:
		# Import pyspark套件
		1.  from pyspark.sql import SparkSession
		# 建立parkSession
		2. 	spark = SparkSession.builder \
			.appName('bdse12') \
			.master("yarn")\
			.getOrCreate()
			
	使用Spark Standalon方式:
		# 切換Spark目錄
		1.  cd $SPARK_HOME
		# 啟動Master 及 Worker
		2.  ./sbin/start-all.sh
		# PI測試
		3.  ./bin/spark-submit \
			--class org.apache.spark.examples.SparkPi \
			--master spark://bdse.example.org:7077 \
			/usr/local/spark/bin/examples/jars/spark-examples*.jar \
			10
		
	使用kafka 方法:
		# 啟動Zookeeper
		1.	zkServer.sh start
		# 啟動Kafka
		2.	kafka-server-start.sh -daemon \
			/usr/local/kafka/config/server.properties
		# 創建kafka主題
		3.  kafka-topics.sh --create --zookeeper localhost:2181 \
			--replication-factor 1 \
			--partitions 1 --topic test
		# 建立生產者並輸入測試文字
		4.	kafka-console-producer.sh --broker-list localhost:9092 --topic test
		# 建立接收者並檢查測試文字
		5.	kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning

