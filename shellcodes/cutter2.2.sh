#!/bin/bash
#2.2優化版
echo "--------歡迎使用cutter2.2版--------"
mkdir files_cutter 2>/dev/null  #如果沒有cuter目錄就建立
ls -lh  *.csv  #顯示當前目錄全部的csv檔
total=$(ls -l *.csv | wc -l) #統計csv檔數量
echo "總計$total個csv檔案.."
echo "=======================CHOSE ONE======================="
read -p "enter number: " number    #選擇第幾個檔案
	[[ "$number" != [[:digit:]]* ]]&& echo "請輸入數字" && echo "程式終止" &&exit 1
	(("$number" > $total))&& echo "目錄只有$total個csv檔案" && echo "程式終止" &&exit 1  
ls -l *.csv | awk "NR==$number" | fmt -u | cut -f9 -d ' ' #篩選出檔案名稱
ans=$(ls -l *.csv | awk "NR==$number" | fmt -u | cut -f9 -d ' ')	
echo "==================show how many row==================="
read -p "Are you sure ? (yes/NO) " anns  #如果要顯示欄位打yes
   [[ "$anns" == "yes" ]]&& echo "loanding........" &&  wcs=$(cat $ans | wc -l) && echo "總計$wcs行"
echo "======================CUT============================"
read -p "min: " min  #切割的第一個位置
read -p "max: " max  #切割的第二個位置
#echo $min
#echo $max
	(($min > $max))&& echo "輸入錯誤" && echo "程式終止" &&exit 1
names=${ans%.*}  #刪除.csv只取檔案名稱
#將裁減的檔案輸出到files_cutter資料夾，檔名:原檔案名稱-cutter-(切割第一個位置)-(切割第二個位置).csv
sed -n "${min},${max}p" $ans > files_cutter/"$names-cutter-$min-$max".csv #輸出裁切的檔案
name="$names-cutter-$min-$max".csv 
echo "=================COMPLETE======================="
echo "檔案名稱:$name"
echo "檔案路徑:"
pwd | awk '{print $1"/files_cutter/"}'
# 輸出切割完的檔案名稱及路徑
