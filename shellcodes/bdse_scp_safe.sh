#!/bin/bash 

#叢集自動複製檔案到每一台電腦
#依據/etc/hosts 名單
#針對名單中的每一台 bdsexx 進行複製
#限定hadoop帳號才能使用

# Copyright (c) IIIedu BDSE.
# BDSE12 Project <contactus@iii.org.tw>
# 指導老師：楊禎文老師



n=$(whoami)
[[ ${n} != "hadoop" ]] && echo "oops, pls return to hadoop" && exit 1
[[ -z $1 ]] && echo -e "\033[0;31moops, There is no parameter #1 !!\033[0m" && exit 1
[[ -z $2 ]] && echo -e "\033[0;31moops,There is no parameter #2 !!\033[0m" && exit 1
B='\033[1;34m'
G='\033[0;32m'
N='\033[0m'
R='\033[0;31m'
echo -e "${B}Checking the environment...${N}"
hadoop_home="/usr/local/hadoop/etc/hadoop/"
awk2='awk NR=="2"'
grep1='grep -A 1'
haCheck=$(cat ${hadoop_home}core-site.xml  | ${grep1} "fs.defaultFS" | ${awk2}| grep 'cluster' )
[[ -n ${haCheck} ]] && echo -e "${B}Your cluster : HA cluster${N}" || echo "${B}Your cluster : Normal cluster${N}"
if [[ -n ${haCheck} ]]
	then
		#HA叢集模式
		#自動檢查檢查XML各服務主機
			nna="dfs.namenode.rpc-address.nncluster.nn"
			rma="yarn.resourcemanager.hostname.rm"
			cut1="cut -d "." -f1"
			hadoop=$(cat ${hadoop_conf}hdfs-site.xml | ${grep1} "${nna}1" | ${awk2} )
			nn1=$(echo ${hadoop#*value>} | ${cut1} )
			hadoop=$(cat ${hadoop_conf}hdfs-site.xml | ${grep1} "${nna}2" | ${awk2} )
			nn2=$(echo ${hadoop#*value>} | ${cut1} )
			hadoop=$(cat ${hadoop_conf}yarn-site.xml | ${grep1} "${rma}1" | ${awk2} )
			rm1=$(echo ${hadoop#*value>} | ${cut1} )	
			hadoop=$(cat ${hadoop_conf}yarn-site.xml | ${grep1} "${rma}2" | ${awk2} )
			rm2=$(echo ${hadoop#*value>} | ${cut1} )
			hadoop=$(cat ${hadoop_conf}mapred-site.xml | ${grep1} "mapreduce.jobhistory.address" | ${awk2} )
		#自動檢查NameNode服務是否運作中
			n=1
			for nn in ${nn1} ${nn2}			
			do
				ssh ${nn} jps &> /tmp/out
				cat /tmp/out | grep 'NameNode' &>/dev/null
				[[ "$?" == "0" ]] && echo -e "{R}oops, pls stop NameNode{N}" \
				&&  exit 1
				n=$((n+1))
			done	
		#自動檢查ResourceManager服務是否運作中
			n=1
			for rm in ${rm1} ${rm2} 
			do
				ssh ${rm} jps &> /tmp/out
				cat /tmp/out | grep 'ResourceManager' &>/dev/null
				[[ "$?" == "0" ]] && echo -e "{R}oops, pls stop ResourceManager{N}" \
				&& exit 1 
				n=$((n+1))
			done			
	else
		#一般叢集
		#自動檢查檢查XML各服務主機
			hadoop=$(cat ${hadoop_home}core-site.xml  | ${grep1} "fs.defaultFS" | ${awk2} )
			nna=$(echo ${hadoop#*://} | ${cut1} )
			hadoop=$(cat ${hadoop_home}yarn-site.xml | ${grep1} "yarn.resourcemanager.hostname" | ${awk2} )
			rma=$(echo ${hadoop#*value>} | ${cut1} )
		#自動檢查NameNode服務是否運作中
			ssh ${nna} jps &> /tmp/out
			echo ""
			cat /tmp/out | grep 'NameNode' &>/dev/null
			[[ "$?" == "0" ]] && echo -e "{R}oops, pls stop NameNode{N}" \
			&&  exit 1
		#自動檢查ResourceManager服務是否運作中
			ssh ${rma} jps &> /tmp/out
			cat /tmp/out | grep 'ResourceManager' &>/dev/null
			[[ "$?" == "0" ]] && echo -e "{R}oops, pls stop ResourceManager{N}"  \
			&& exit 1
fi
	echo -e "{G}All services have been stopped"
	name=$(cat /etc/hosts | grep 'bdse' | cut -d " " -f3)
	n=1
	for nn in $name
	do
		self=$(hostname)
		selfCheck=$(echo $(echo $name | cut -d " " -f${n}))
		[[ $selfCheck != $self ]] && \
		echo " scp $1 $(echo $name | cut -d " " -f${n}):$2 "
		n=$((n+1))
	done






