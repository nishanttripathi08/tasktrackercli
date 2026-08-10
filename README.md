# Task Tracker CLI

A simple command-line tracker built with Python. This project was built following the [Task Tracker project](https://roadmap.sh/projects/task-tracker) from roadmap.sh

### Features

+ Add, update, and delete tasks
+ Mark tasks as todo, in-progress, or done
+ List all tasks
+ Filter tasks by status
+ Store tasks in a JSON file
+ Handle invalid commands and inputs

### How to Run

Clone the repository and run:
```bash
python3 main.py <command>
```

### Commands

#### Add a task
```bash
python3 main.py add "Buy groceries"
```

#### Update a task
```bash
python3 main.py update 1 "Buy groceries and cook dinner"
```

#### Delete a task
```bash
python3 main.py delete 1
```

#### Change task status
```bash
python3 main.py mark-in-progress 1
python3 main.py mark-done 1
```

#### List tasks
```bash
python3 main.py list
python3 main.py list todo
python3 main.py list in-progress
python3 main.py list done
```



### Technologies
+ Python
+ JSON
+ Command-Line Interface(CLI)
+ File I/O

### What I Learned
+ Working with command-line arguments using sys.argv
+ Reading and writing JSON files
+ Working with classes and objects
+ File system operations
+ Handling user input and edge cases
+ Using Git and Github for version control

