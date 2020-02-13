#!/bin/bash
echo "First parameter: $1"
echo "Second parameter: $2"
echo "Third parameter: $3"
echo "four parameter: $4"

	[[ $4 == "all" ]] && read -p "Are you sure ? (yes/NO) " ans &&  \
	[[ "$ans" != "yes" ]] && echo "Terminate program..." && exit  
	if [ $4 != "all" ]
	then
		echo "Loanding........"  
		python ./py_to_sql.py "$1" "$2" "$3" "$4" 
	fi
		[[ "$ans" == "yes" ]] && \
		total=$(ls -l *.csv | wc -l) &&\
		for ((a=1; a <= total ; a++))
		do
			name=$(ls -l *.csv | awk "NR==$a" | fmt -u | cut -f9 -d ' ')
			echo "$name  loanding........" 
			sleep 1.5
			python ./py_to_sql.py "$1" "$2" "$3" $name
			echo "$name is completed"
			sleep 0.5
		done
		
		
