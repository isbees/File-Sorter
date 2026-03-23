# File Sorting Script in Python

This script organizes files in a specified directory by sorting them into categorized folders based on their file types. It is particularly useful for managing clutter in your Downloads folder.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/isbees/File-Sorter.git
   ```
2. Open `file_sorter.py` and modify the `path` variable to point to the folder you want to sort.

## Adding Sorting Categories

The script categorizes files based on their extensions. You can customize these categories by editing the lists defined in `file_sorter.py` (e.g., `videos`, `audio`, `images`, etc.).

To add a new category:
1. Define a new list variable with the folder name and include the desired file extensions.
2. Add a corresponding `elif` block in the sorting logic to handle the new category.

## Automating the Script

To run the script automatically, use [Task Scheduler](https://www.jcchouinard.com/python-automation-using-task-scheduler/#:~:text=To%20schedule%20a%20Python%20script%20with%20Task%20scheduler%2C%20create%20an,the%20execution%20of%20your%20script.). This allows you to schedule the script to execute at regular intervals, keeping your folder organized without manual intervention.
