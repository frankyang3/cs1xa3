# CS 1XA3 Project01 - <MyMacId>
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

Menu Reference: Code was used from https://linuxhint.com/bash_select_command/ and https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_07_03.html


....
## FIXME Log
Description: This feature finds every file inside the repo that contains #FIXME in the last line. It then prints the file names into a file fixme.log. This will either create a new file or overwrite the old file. 
Execution: Type 1 in the menu. This will run this feature
Reference: Some code was taken from https://unix.stackexchange.com/questions/213610/find-last-line-of-a-file-for-matching-string

## Checkout Latest Merge
Description: This feature finds the latest commit with 'merge' inside the commit message. It then checks out to the commit. Note that this does not create a new branch.
Execution: Type 2 in the menu. This will run this feature
Reference: This feature was made with help from https://unix.stackexchange.com/questions/191122/how-to-split-the-string-after-and-before-the-space-in-shell-script

## File Size list
Description: This feature lists all files, not directories, and sizes in KB. ALl files are sorted from largest to smallest by size.
Execution: Type 3 in the menu. This will run this feature
Reference: This feature was made with help from https://unix.stackexchange.com/questions/64148/how-do-i-make-ls-show-file-sizes-in-megabytes

## File Type Count
Description: This feature counts all files inside the repo with a user inputted extension (without .)
Execution: Type 4 in the menu. This will show a prompt, type in the file extension such as txt, pdf. 
Reference: This feature was made with help from https://unix.stackexchange.com/questions/64148/how-do-i-make-ls-show-file-sizes-in-megabytes

## Custom Feature 
Description: This feature counts all files inside the repo with a user inputted extension (without .)
Execution: Type 4 in the menu. This will show a prompt, type in the file extension such as txt, pdf. 
Reference: This feature was made with help from https://unix.stackexchange.com/questions/64148/how-do-i-make-ls-show-file-sizes-in-megabytes

## Custom Feature 
Description: This feature counts all files inside the repo with a user inputted extension (without .)
Execution: Type 4 in the menu. This will show a prompt, type in the file extension such as txt, pdf.
Reference: This feature was made with help from https://unix.stackexchange.com/questions/64148/how-do-i-make-ls-show-file-sizes-in-megabytes
