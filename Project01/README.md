# CS 1XA3 Project01 - yangf51


## Usage
Execute this script from project root with:
```bash
chmod +x CS1XA3/Project01/project_analyze.sh
./CS1XA3/Project01/project_analyze
```

This will then prompt a user input menu.
Select the feature by typing in a digit between 1-5

1. FIXME Log
2. Checkout Latest Merge
3. File Size list
4. File Type Count
5. Quit Program

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

## Custom Feature - Priority TODO List 
**Description:** When selected, this feature will prompt for the user to retrieve the todo list or input a new item. If the user chooses to retrieve the list, the todo list will get printed. If the user chooses to input a new item, the todo list will prompt for a priority and item. The list then sorts the item into the existing list according to priority.  </br> 
**Execution:** Type 5 in the menu. This will show a prompt to either retrieve the list or input a new item. To see the list, type 2. To input a new item, type 1. Then input a priority (higher is higher on list), then input the TODO item. The TODO list will be updated </br> 
**Reference:** NOT BUILT YET   </br> 

## Custom Feature - Conflict Detector  
**Description:** This feature will take two file paths, and compare the inside of the files. Any differences will get printed into a separate difflog.txt file. Each difference will show the line number, and both versions of that line.  </br> 
**Execution:** Type 6 in the menu, then you will be prompted to enter 2 file paths, one after the other. The feature will create or overwrite the difflog.txt file showing the differenes of the two files.  </br> 
**Reference:** NOT BUILT YET  </br> 




