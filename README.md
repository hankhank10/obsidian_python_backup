# obsidian_python_backup
 
 Very simple Python script to backup your Obsidian vault to a zip file and then optionally also upload it to Dropbox

 Good if you're using Obsidian sync as it is a one-way backup


## Scheduling

You can schedule this script to run automatically using cron on Linux or Mac, or Task Scheduler on Windows

### Linux/Mac

1. Open a terminal window
2. Type `crontab -e`
3. Add the following line to the bottom of the file, replacing the path with the path to your script, for instance the below will run every hour

```
0 * * * * python3 /path/to/obsidian_python_backup.py
```

### Windows

1. Open Task Scheduler
2. Click "Create Task"
3. Give it a name
4. Click the "Triggers" tab
5. Click "New"
6. Set the schedule to "Daily" and set the time you want it to run
7. Click the "Actions" tab
8. Click "New"
9. Set the action to "Start a program"
10. Set the path to your Python executable (e.g. `C:\Users\username\AppData\Local\Programs\Python\Python39\python.exe`)
11. Set the arguments to the path to your script (e.g. `C:\Users\username\Documents\obsidian_python_backup.py`)
12. Click "OK"