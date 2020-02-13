#!/bin/bash

# Initial Menu

PS3='Select the feature you would like to use (Enter the corresponding number)'
select fet in "FIXME Log" "Checkout Latest Merge" "File Size List" "File Type Count" "Quit"
do
	case $fet in 
		"FIXME Log")
			# tail -f -n 1 .. | grep -rl "#FIXME" > fixme.log
			;;
		"Checkout Latest Merge")
			
			;;
		"File Size List")
			echo "Sup"
			;;
		"File Type Count")
			echo "4"
			;;
		"Quit")
			break
			;;
		*)
			echo "Please Select a valid option"
			;;
	esac
done
