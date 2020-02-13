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
[[ -z $2 ]] && echo -e "\033[0;31moops,There is no parameter #1 !!\033[0m" && exit 1
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






