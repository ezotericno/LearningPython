# Files and Exceptions
The ```open()``` function needs one argument: the name of the file you want to open. Python will look in the current dir for it.
The keyword ```with``` closes the file once access to it is no longer need in the program.
```read()``` function

## File Pathing
```with open('text_files/filename.txt') as file_object```
Windows uses \ and not / for file pathing, however you can use either or in your program
Absolute paths are as follows:
```
1. file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
2. with open(file_path) as file_object:
```
- ```readlines()``` method
