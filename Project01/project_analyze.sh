#!/bin/bash

# Initial Menu

PS3='Select the feature you would like to use (Enter the corresponding number)'
select fet in "FIXME Log" "Checkout Latest Merge" "File Size List" "File Type Count" "Switch to Executable" "Backup and Delete" "Priority TODO" "Conflict Detector"  "Quit" 
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
			#Switches .sh files to executable and allows all users with write permission to execute, also has an option to revert
			echo "Please type in either change or restore: "
			read;
			if [ "$REPLY" == 'change' ]; then
				find .. -type f -name "*.sh" | xargs getfacl>permissions.log
				cp permissions.log newperms.log
				sed -i 's/rw-/rwx/g' newperms.log
				sed -i 's/-w-/-wx/g' newperms.log
				sed -i 's/r-x/r--/g' newperms.log
				sed -i 's/--x/---/g' newperms.log
				setfacl --restore=newperms.log
				rm newperms.log
			elif [ "$REPLY" == 'restore' ]; then
				test -f permissions.log && setfacl --restore=permissions.log || echo "permissions.log does not exists"		
			else 
				echo "Wrong input"
			fi
			;;
		"Backup and Delete")
			#Creates a backup of all .tmp files, with a restore file containing paths. Also has an option to restore all backed up .tmp files
			echo "Please type in either backup or restore"
			read;
			if [ "$REPLY" == 'backup' ]; then
				[ -d "backup" ] && rm -r backup; mkdir backup || mkdir backup
				if [[ ! -z `find . -type f -name "*.tmp"` ]]; then
                               		cp `find . -type f -name "*.tmp"` backup
					find . -type f -name "*.tmp" -not -path "./backup/*"  > ./backup/restore.log
					rm `find . -type f -name "*.tmp" -not -path "./backup/*"`
				fi
                        elif [ "$REPLY" == 'restore' ]; then
                                if [ -f "./backup/restore.log" ]; then
					file="./backup/restore.log"
					while IFS= read -r line
					do
						d=`echo "$line" | rev | cut -d"/" -f2-  | rev`
						f=`echo "$line" | rev | cut -d"/" -f1  | rev`
						mv "./backup/$f" "$d"
					done<"$file"	
				else
					echo "No backup exists"
				fi
                        else
                                echo "Wrong Input"
                        fi

			;;
		"Priority TODO")
			#Creates a priority TODO List, you may then add or retrieve the list
			echo "Please type in either view or add"
			read;
			if [ "$REPLY" == 'view' ]; then
				test -f todo.txt && cat todo.txt || echo "todo.txt does not exist"
			elif [ "$REPLY" == 'add' ]; then
				test ! -f todo.txt && touch todo.txt
				echo "Please enter priority number, followed by a space then your TODO message"
				read;
				LINE="$REPLY"
				
			else
				echo "Wrong input"
			fi 			
			;;
		"Conflict Detector")
			#Checks two files for differences, the outputs to difflog.txt
			echo "Please input 2 file names with the path starting from the current directory, separated by a space"
			read;
			addr1=`echo "$REPLY" | cut -d" " -f1`
			addr2=`echo "$REPLY" | cut -d" " -f2`
			if [[ -f "$addr1" &&  -f "$addr2" ]]; then
				diff -u  "$addr1"  "$addr2">difflog1.txt
				sed '1,3d' difflog1.txt>difflog.txt
				echo "Differences of $addr1 to $addr2" | cat - difflog.txt > temp && mv temp difflog.txt
			else
				echo "One or more files do not exist"
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
