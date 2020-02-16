#!/bin/bash
echo loading...........
sec=$(grep 'Year' -n performance_small.csv | cut -f 1 -d ":")
ls_sec=$((sec-1))

#head -$ls_sec performance_small.csv > data1.csv

head -$((sec-1)) performance_small.csv > data1.csv
one=$(wc -l performance_small.csv)
set -- $one
ls_one=$(($1-ls_sec))


tail -$ls_one performance_small.csv > data2.csv

read -p "Enter 1 or 2 ...:" answer

case $answer in
	(1) less -N data1.csv ;;
	(2) less -N data2.csv ;;
	(*) echo "try again...." ;;
esac


exit
