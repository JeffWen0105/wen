#!/bin/bash

echo " 0 -------創建一個spark容器"
echo " 1 -------將spark容器重啟喚起運作"
echo " 2 -------停止正在運作的spark容器"
echo " 3 -------查看spark容器的log"
echo " 4 -------查看正在運作的容器"
echo " 5 -------顯示虛擬機IP"
echo " 6 -------刪除spark容器"
echo " 7 -------關閉Docker伺服器(請先停止所有的container)=>for Windows"
echo "=======================CHOSE ONE======================="

read -p "Please enter a value: " answer 
	case "$answer" in
		q*|exit|bye ) echo "Terminate program...!" ; exit ;;
		0) 
			docker-machine ip 
			docker container run --name pyspark_exercise -v $HOME/share/pyspark:/home/jovyan/work -p 8800:8888 -p4040:4040 jupyter/pyspark-notebook ;;
		1) 
			docker container restart pyspark_exercise 
			docker container ls ;;
		2) 
			docker container stop pyspark_exercise 
			docker container ls ;;
		3) 
			docker container logs pyspark_exercise;;
		4)
			docker container ls ;;
		5)
			docker-machine ip ;;
		6)
			docker container stop pyspark_exercise
			docker container rm pyspark_exercise 
			docker container ls -a;;
                7) read -p "Are you sure ? (y/N) " ans
                        if [[ "$ans" == "y" ]]
                                then
                                        docker-machine stop  &>/dev/null
                                        echo "bye bye~~"
                        fi
                        ;;
		*) echo "Only choices 0, 1, 2, 3, 4, 5, 6, 7" ;;
	esac

exit

		
		
