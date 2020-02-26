#!/bin/bash

# Initial Menu

PS3='Select the feature you would like to use (Enter the corresponding number)'
select fet in "FIXME Log" "Checkout Latest Merge" "File Size List" "File Type Count" "Switch to Executable" "Backup and Delete" "Quit" 
do
	case $fet in
		"FIXME Log")
			#find all files in repo, grep the tails for FIXME
			for i in `find .. -type f`; do  tail -1 $i |grep -q "#FIXME"  && echo $i; done > fixme.log
			;;
		"Checkout Latest Merge")
			#checkout the last commit greped that has merge in message
			git checkout $(echo $(git log -n 1 --all --pretty=oneline --grep='merge' -i) | cut -d' ' -f1)
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
		"Switch to Executable")
			echo "Please type in either change or restore: "
			>  permissions.log
			read;
			if [ "$REPLY" == 'change' ]; then
				find .. -type f -name "*.sh" | [ -w xargs ] && xargs chmod u+x
		        elif ["$REPLY" == 'restore' ]; then
				echo "restore"
			else
				echo "Wrong Input"
			fi		
			;;
		"Backup and Delete")
			echo "Please type in either backup or restore"
			[ -d "backup" ] && rm -r backup; mkdir backup || mkdir backup
			read;
			if [ "$REPLY" == 'backup' ]; then
                                cp `find .. -type f -name "*.tmp"` backup
				rm `find .. -type f -name "*.tmp" -not -path "./backup/*"`
                        elif ["$REPLY" == 'restore' ]; then
                                echo "restore"
                        else
                                echo "Wrong Input"
                        fi

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
