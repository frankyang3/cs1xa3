#!/bin/bash

# Initial Menu

PS3='Select the feature you would like to use (Enter the corresponding number)'
select fet in "FIXME Log" "Checkout Latest Merge" "File Size List" "File Type Count" "Quit"
do
	case $fet in 
		"FIXME Log")
			#find all files in repo, grep the tails for FIXME
			 tail -f -n 1 .. | grep -rl "#FIXME" > fixme.log
			;;
		"Checkout Latest Merge")
			#checkout the last commit greped that has merge in message
			git checkout $(echo $(git log -n 1 --all --pretty=oneline --grep='merge') | cut -d' ' -f1)
			;;
		"File Size List")
			#lists in human readable file size, removes directories
			cd ..
			ls -RlhSp --block-size=KB | grep -v / | grep -v "total"
			;;
		"File Type Count")
			#Prints all grepped files with the extension
			echo "Please input an extension (no . in front), this will output files with that extension"
			read;
			echo "There are $(ls -l | grep ".*\.${REPLY}$" | wc -l) .${REPLY} files in the repo"
			;;
		"Quit")
			#Breaks the select, quits
			break
			;;
		*)
			#Error catching
			echo "Please Select a valid option"
			;;
	esac
done
