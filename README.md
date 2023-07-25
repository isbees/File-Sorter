# File Sorting Script in Python

Simple script to use on your own files. 

I use it on my downloads folder but if you want to run it on your own folder or want to edit the folder options 

## Installation

Clone the repo.
```
git clone 
```
Modify `file_sorter.py` starting with the path. Copy and paste the folder location that you would like to sort

## Adding sorting options

`Line 10 to 17` are the type of files your items will be sorted into. If you want to add another folder, name a variable with a folder name and then set it equal an array with the different types that you want in the folder.

Then add another elif before the else.

## Make it Run Automatically 

To passively sort your folder make sure you use [task scheduler](https://www.jcchouinard.com/python-automation-using-task-scheduler/#:~:text=To%20schedule%20a%20Python%20script%20with%20Task%20scheduler%2C%20create%20an,the%20execution%20of%20your%20script.) 