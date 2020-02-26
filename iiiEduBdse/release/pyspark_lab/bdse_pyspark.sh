#!/bin/bash

# Copyright (c) IIIedu BDSE.
# BDSE12 Project
# "指導老師：楊禎文老師"

echo "環境檢查中..."
images=$(docker image ls  | grep 'iiiedu/bdse_pyspark')
image=$(echo $images)
if [[ -z $image ]]
then
	echo -e "\x1b[;31;1mUnable to find main image\x1b[;37;0m.."
	sleep 0.5
	echo -e "\x1b[;32;1mDownloading\x1b[;37;0m.."
	docker build -t "iiiedu/bdse_pyspark" main/
	sleep 0.5
	clear
	images=$(docker image ls  | grep 'iiiedu/bdse_pyspark')
	image=$(echo $images)
	[[ -n $image ]] && echo -e "\x1b[;32;1mImage installed complete..\x1b[;37;0m" || echo -e "\x1b[;31;1moops!! Can't install image..\x1b[;37;0m"
fi	
[[ -n $image ]] && echo  -e "環境正確,歡迎使用Pyspark of docker環境" || exit 1

while true
do
	echo " 0 -------創建一個Pyspark容器"
	echo " 1 -------將Pyspark容器重啟喚起運作"
	echo " 2 -------停止正在運作的Pyspark容器"
	echo " 3 -------顯示Pyspark容器的IP及Port埠號"
	echo " 4 -------查看Pyspark容器的token"
	echo " 5 -------進入Pyspark容器內"
	echo " 6 -------刪除Pyspark容器"
	echo " 7 -------查看(輸出)Pyspark容器的logs"
	echo " 8 -------查看Pyspark容器掛載本機目錄路徑"
	echo " 9 -------查看Pyspark容器系統使用狀態"
	echo " S -------列出目前所有正運行中的容器"
	echo " T -------關閉Docker伺服器"
	echo " d -------刪除Pyspark image檔"
	echo " q -------離開程式"
	echo "=======================CHOSE ONE======================="

	read -p "please choose one of the above options: " answer 
		case "$answer" in
			exit|bye ) echo "Terminate program...!" ; exit ;;		
			0) 
				exists=$(docker container ls -a | grep 'pyspark_exercise')
				exist=$(echo $exists)
				[[ -n $exist ]] && echo -e "\x1b[;31;1mThe container is already exists..\x1b[;37;0m \nTerminate program...! \n" && exit 1	
				#檢查是否已經建立container
					adv=$(echo -e "\x1b[;31;1mAdvanced option (y/N)\x1b[;37;0m \n\n")
					read -p "$adv" ans
					#進階設定
					if [[ "$ans" == "y" ]]
					then
								read -p "Create a shared storage volume in the container. $HOME/" homePath 
									[[ ! $homePath || $homePath == [[:space:]] ]] && echo "Input error" && \
									exit 1 || [[ $homePath == "q" ]] && echo "Terminate program...!" && exit 1 
								#掛載於本機目錄路徑	
								read -p "Publish a container port to the host:" portNumber
									[[  $portNumber != [[:digit:]]* ]] && echo -e "Input error \n" &&  exit 1
								#映射Port號	
								echo -e "\n-------------------------------------------------------------"
								printf "\x1b[;31;1mWarning: CPU scheduling and prioritization are advanced kernel-level features."
								printf "Most users do not need to change these values from their defaults."
								printf "Setting these values incorrectly can cause your host system to become unstable or unusable. \x1b[;37;0m \n" 
								echo -e "-------------------------------------------------------------\n"
								read -p "How many cores do you need(Default value as a blank space)?:" core					
									[[ ! $core ]] && echo "with as many threads as logical cores on your machine "
								#限制多少核心
								read -p "How much RAM do you need(Default value as a blank space)?:" ram
								#限制多少記憶體
									[[ ! $ram ]] && echo "The maximum amount of memory the container can use"
									if [[ ! $core ]] && [[ ! $ram ]]
									then
										docker container run -d --name pyspark_exercise -v $HOME/${homePath}:/home/jovyan/work -p ${portNumber}:8888\
										-p4040:4040 iiiedu/bdse_pyspark &>/dev/null
									elif [[ ! $core ]]
									then
										docker container run -d --name pyspark_exercise -m ${ram}m -v $HOME/${homePath}:/home/jovyan/work\
										-p ${portNumber}:8888 -p4040:4040 iiiedu/bdse_pyspark &>/dev/null
									elif [[ ! $ram ]]
									then
										docker container run -d --name pyspark_exercise --cpus=${core} -v $HOME/${homePath}:/home/jovyan/work\
										-p ${portNumber}:8888 -p4040:4040 iiiedu/bdse_pyspark &>/dev/null
									else
										docker container run -d --name pyspark_exercise -m ${ram}m --cpus=${core} -v $HOME/${homePath}:/home/jovyan/work\
										-p ${portNumber}:8888 -p4040:4040 iiiedu/bdse_pyspark &>/dev/null
									fi
					else
						docker container run -d --name pyspark_exercise -v $HOME/share/pyspark:/home/jovyan/work -p 8820:8888 -p4040:4040 iiiedu/bdse_pyspark &>/dev/null
						#預設狀態
					fi 
				echo -e "Container is building.."
				sleep 0.5
				exists=$(docker container ls | grep 'pyspark_exercise')
				exist=$(echo $exists) #檢查是否建立容器
				[[ ! $exist ]] && echo -e "\x1b[;31;1mPyspark容器建立失敗!!\n\n\x1b[;37;0m" || echo -e "\x1b[;32;1mPyspark容器已建立\n\n\x1b[;37;0m"
				;;
			1) 
				echo "Restatring Pyspark container..."
				docker container restart pyspark_exercise &>/dev/null
				#重新啟動容器
				exists=$(docker container ls | grep 'pyspark_exercise')
				exist=$(echo $exists) 
				[[ ! $exist ]] && echo -e "\x1b[;31;1m請先建立Pyspark容器\n\n\x1b[;37;0m" || echo -e "\x1b[;32;1mPyspark容器已啟動..\n\n\x1b[;37;0m "
				;;
			2) 
				echo "Stoping Pyspark container..."
				sleep 0.5
				docker container stop pyspark_exercise &>/dev/null
				#停止容器
				exists=$(docker container ls | grep 'pyspark_exercise')
				exist=$(echo $exists)
				[[ ! $exist ]] && echo -e "\x1b[;32;1mPyspark容器已停止..\n\n\x1b[;37;0m" || echo -e "\x1b[;31;1mPyspark容器尚未停止\n\n\x1b[;37;0m"
				;;
			3) 
				exists=$(docker container ls | grep 'pyspark_exercise')
				exist=$(echo $exists)
				[[ ! $exist ]] && echo -e "\x1b[;31;1mPyspark容器尚未啟動!!\x1b[;37;0m" \
				&& echo -e "\x1b[;31;1mTerminate program...!" && exit 1
					getIp=$(docker-machine ip)
					#取得IP
					port=$(docker container ls --format "table {{.Names}}\t{{.Ports}}" | grep 'pyspark_exercise')
					#取得與port相關所有資訊
					getports=$(echo ${port#*/*:} | cut -d "/" -f1 | cut -d "-" -f1)
					#限定條件過濾port
					echo "Your container IP: ${getIp}:${getports}"
					echo -e "\x1b[;32;1mIP and port are on clipboard!!\x1b[;37;0m"
					echo ${getIp}:${getports} | clip 
					echo -e "\n\n"
					#clip 為Windows剪貼簿
				
				;;
			4)
				exists=$(docker container ls | grep 'pyspark_exercise')
				exist=$(echo $exists)
				[[ ! $exist ]] && echo -e "\x1b[;31;1mPyspark容器尚未啟動!!\x1b[;37;0m" \
				&& echo -e "\x1b[;31;1mTerminate program...!" && exit 1
					docker container logs pyspark_exercise >& pyspark_exercise.txt
					#將logs相關資訊輸出暫存
					tokens=$(cat pyspark_exercise.txt | grep -n 'token')
					rm pyspark_exercise.txt
					#取得logs資訊並刪除暫存
					token=$(echo ${tokens##?*?:} |  cut -d "=" -f2)
					#限定條件只過濾token
					echo "Your token : ${token}"
					echo -e "\x1b[;32;1mToken is on clipboard!!\x1b[;37;0m"
					echo ${token} | clip 
					echo -e "\n\n"
					#clip 為Windows剪貼簿
				
				;;
			5)
				
				exists=$(docker container ls | grep 'pyspark_exercise')
				exist=$(echo $exists)
				[[ ! $exist ]] && echo -e "\x1b[;31;1mPyspark容器尚未啟動!!\x1b[;37;0m" \
				&& echo -e "\x1b[;31;1mTerminate program...!" && exit 1
					read -p "Log In As root User (y/N) " ans
					if [[ "$ans" == "y" ]]
					then
						docker container exec -it --user root pyspark_exercise /bin/bash 
						#管理員身分進入容器
					else
						docker container exec -it pyspark_exercise /bin/bash 
						#一般身分進入容器
					fi
				;;
			6)	
				ask=$(echo -e "\x1b[;31;1mAre you sure ? (y/N)\x1b[;37;0m \n")
				read -p "$ask " ans
				if [[ "$ans" == "y" ]]
				then
					echo "Removing Pyspark container..."
					sleep 0.5
					docker container stop pyspark_exercise &>/dev/null
					#停止容器
					sleep 0.5
					docker container rm -f pyspark_exercise  &>/dev/null
					#刪除容器
					exists=$(docker container ls -a | grep 'pyspark_exercise')
					exist=$(echo $exists)
					[[ ! $exist ]] && echo -e "\x1b[;32;1mPyspark容器已刪除\n\n\x1b[;37;0m" || echo -e "\x1b[;31;1mPyspark容器尚未刪除\n\n\x1b[;37;0m"
					#檢查容器是否被刪除
				fi
				;;
			7)
				exists=$(docker container ls | grep 'pyspark_exercise')
				exist=$(echo $exists)
				[[ ! $exist ]] && echo -e "\x1b[;31;1mPyspark容器尚未啟動!!\x1b[;37;0m" \
				&& echo -e "\x1b[;31;1mTerminate program...!" && exit 1
				read -p "Output logs to a text file. (y/N)" ans
				if [[ "$ans" == "y" ]]
					then
					docker container logs pyspark_exercise >& pyspark_logs.txt
					#輸出logs
					where=$(pwd)
					echo -e "\x1b[;32;1mOutput to: $where/pyspark_logs.txt..\n\n\x1b[;37;0m"
					#顯示logs存放位置
					else
					docker container logs pyspark_exercise
					echo -e "\n"
					fi
				;;
			8)	
				exists=$(docker container ls -a | grep 'pyspark_exercise')
				exist=$(echo $exists)
				[[ ! $exist ]] && echo -e "\x1b[;31;1mPyspark容器尚未建立!!\x1b[;37;0m"  \
				&& echo -e "\x1b[;31;1mTerminate program...!" && exit 1							
				path=$(docker inspect pyspark_exercise  --format "{{.Mounts}}" | fmt -u | cut -d " " -f2 | awk "NR==1")
				#顯示容器掛載於本機目錄路徑
				echo -e "The share path to the directory on the host: ${path}"
				echo -e "\x1b[;32;1mThe path is on clipboard!!\x1b[;37;0m"
				echo ${path} | clip 
				echo -e "\n"
				;;
				
			9)	
				exists=$(docker container ls | grep 'pyspark_exercise')
				exist=$(echo $exists)
				[[ ! $exist ]] && echo -e "\x1b[;31;1mPyspark容器尚未啟動!!\x1b[;37;0m" \
				&& echo -e "\x1b[;31;1mTerminate program...!" && exit 1				
				echo -e '\t\t\t\t\x1b[;32;1mSTATS:\x1b[;37;0m'
				docker stats pyspark_exercise --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.MemPerc}}" --no-stream
				#顯示容器CPU及記憶體使用狀態
				echo -e "\n"
				;;
			S)	
				docker container ls
				;;
				
			T) 
				ask=$(echo -e "\x1b[;31;1mAre you sure ? (y/N)\x1b[;37;0m \n")
				read -p "$ask " ans
				if [[ "$ans" == "y" ]]
				then
					sleep 0.5
					docker container stop $(docker container ls -aq) &>/dev/null
					sleep 0.5
					docker-machine stop  
					#關閉Docker伺服器
					echo "bye bye.." && exit 1
				fi
				;;
			d) 
				ask=$(echo -e "\x1b[;31;1mAre you sure ? (y/N)\x1b[;37;0m \n")
				read -p "$ask " ans
				if [[ "$ans" == "y" ]]
				then
					sleep 0.5
					docker container rm -f pyspark_exercise &>/dev/null
					sleep 0.5
					docker rmi  -f "iiiedu/bdse_pyspark" &>/dev/null
					#刪除映像檔		
					images=$(docker image ls  | grep 'iiiedu/bdse_pyspark')
					image=$(echo $images)
					[[ -z $image ]] && echo -e "\x1b[;32;1mPyspark映像檔已刪除\x1b[;37;0m"  \
					&& echo -e "\x1b[;31;1mTerminate program...!" && exit 1
				fi
				;;
			*) echo "Only choices 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, S, T, d" ;;
		esac

done
