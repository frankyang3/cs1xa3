# CS 1XA3 Project01 - yangf51


## Usage
Execute this script from project root with:
```bash
chmod +x CS1XA3/Project01/project_analyze.sh
./CS1XA3/Project01/project_analyze
```

This will then prompt a user input menu.
Select the feature by typing in a digit between 1-9
Typing 9 will exit the program

1. FIXME Log
2. Checkout Latest Merge
3. File Size list
4. File Type Count
5. Switch to Executable
6. Backup and Delete
7. Priority TODO
8. Conflict Detector
9. Quit Program

Menu Reference: Code was used from *https://linuxhint.com/bash_select_command/* and *https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_07_03.html*


....
## FIXME Log
**Description:** This feature finds every file inside the repo that contains #FIXME in the last line. It then prints the file names into a file fixme.log. This will either create a new file or overwrite the old file. </br> 
**Execution:** Type 1 in the menu. This will run this feature</br> 
**Reference:** Some code was taken from *https://unix.stackexchange.com/questions/213610/find-last-line-of-a-file-for-matching-string*</br> 

## Checkout Latest Merge
**Description:** This feature finds the latest commit with 'merge' inside the commit message. It then checks out to the commit. Note that this does not create a new branch.</br> 
**Execution:** Type 2 in the menu. This will run this feature</br> 
**Reference:** This feature was made with help from *https://unix.stackexchange.com/questions/191122/how-to-split-the-string-after-and-before-the-space-in-shell-script*</br> 

## File Size list
**Description:** This feature lists all files, not directories, and sizes in KB. ALl files are sorted from largest to smallest by size </br> 
**Execution:** Type 3 in the menu. This will run this feature</br> 
**Reference:** This feature was made with help from *https://unix.stackexchange.com/questions/64148/how-do-i-make-ls-show-file-sizes-in-megabytes*</br> 

## File Type Count
**Description:** This feature counts all files inside the repo with a user inputted extension (without .) </br> 
**Execution:** Type 4 in the menu. This will show a prompt, type in the file extension such as txt, pdf. </br> 
**Reference:** This feature was made with help from *https://unix.stackexchange.com/questions/64148/how-do-i-make-ls-show-file-sizes-in-megabytes*  </br> 

## Switch To Executable
**Description:** This feature changes all .sh files to executable format, only allowing users with write permission to execute. Additionally, this feature allows users to restore the original permissions on the .sh files </br> 
**Execution:** Type 5 in the menu. Then enter either ```change``` or ```restore```, depending on the user input, the program will either change all .sh files to executable form (for user with write permission), or restore original permissions. </br> 
**Reference:** This feature was made with help from *https://linux.die.net/man/1/setfacl* and *https://linux.die.net/man/1/getfacl* and *https://unix.stackexchange.com/questions/189104/back-up-and-restore-file-permissions*  </br> 

## Backup and Delete
**Description:** This feature creates a backup of all .tmp files and stores them inside a backup folder, deleting them everywhere else. When the user chooses to restore these files, they files will be moved from the backup folder to their original locations </br> 
**Execution:** Type 6 in the menu. Then enter either ```backup``` or ```restore```, depending on the user input, the program will either backup files or restore them from the backup folder. </br> 
**Reference:** This feature was made with help from *https://unix.stackexchange.com/questions/64148/how-do-i-make-ls-show-file-sizes-in-megabytes*  </br> 

## Custom Feature - Priority TODO List 
**Description:** When selected, this feature will prompt for the user to retrieve the todo list or input a new item. If the user chooses to retrieve the list, the todo list will get printed. If the user chooses to input a new item, the todo list will prompt for a priority and item. The list then sorts the item into the existing list according to priority.  </br> 
**Execution:** Type 7 in the menu. Then enter either ```view``` or ```add```. If you entered ```add```, input a priority (higher is higher on list), then input the TODO item separated by a space. The TODO list will be updated </br> 
**Reference:** This feature was made with help from *https://stackoverflow.com/questions/6438896/sorting-data-based-on-second-column-of-a-file*   </br> 

## Custom Feature - Conflict Detector  
**Description:** This feature will take two file paths, and compare the inside of the files. Any differences will get printed into a separate difflog.txt file. Each difference will show the line number, and both versions of that line.  </br> 
**Execution:** Type 8 in the menu, then you will be prompted to enter 2 file paths, one after the other. The feature will create or overwrite the difflog.txt file showing the differences of the two files.  </br> 
**Reference:** This feature was made with help from *https://unix.stackexchange.com/questions/81998/understanding-of-diff-output* </br> 


