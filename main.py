import sys, os, json
from task import Task

FILENAME = "data.json"

def dumpObject(obj):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(obj, file, indent=4)

def findTask(IDnumber):
    for index, item in enumerate(data):
        if item["IDnumber"] == IDnumber:
            return index
    return -1

def printTasks(filter="None"):
    index = 1
    for item in data:
        if filter == "None" or item["status"] == filter:
            print(f"{index}. {item["description"]} [ID = {item["IDnumber"]}, {item["status"]}]. Created at {item["createdAt"]}, and last updated at {item["updatedAt"]}")
            index += 1


if not os.path.exists(FILENAME):
    dumpObject([])
with open(FILENAME, "r") as file:
    data = json.load(file)
if len(sys.argv) < 2:
    print("Error: No command found")
else:
    firstArg = sys.argv[1] # Argument that contains command
    flag = True
    match firstArg:
        case "add": # Adding task
            if len(sys.argv) < 3:
                print("Error: Missing task description")
            else:
                ID = max([item["IDnumber"] for item in data]) + 1 if len(data) != 0 else 1
                task = Task(sys.argv[2], ID)
                data.append(vars(task))
                dumpObject(data)
                print(f"Task added successfully (ID: {ID})")
        case "update": # Updating existing task
            if len(sys.argv) < 3:
                print("Error: Missing ID number and updated description")
            elif len(sys.argv) < 4:
                print("Error: Missing updated description")
            elif not sys.argv[2].isdigit() or int(sys.argv[2]) == 0:
                print("Error: Third argument is not valid ID number")
            else:
                givenID = int(sys.argv[2])
                updatedDescription = sys.argv[3]
                indexOfTask = findTask(givenID)
                if indexOfTask == -1:
                    print(f"Task (ID: {givenID}) not found")
                else:
                    task = data[indexOfTask]
                    task["description"] = updatedDescription
                    task["updatedAt"] = Task.createTimeStamp()
                    print(f"Task (ID: {givenID}) successfully updated")
                    dumpObject(data)
        case "delete": # Deleting existing task
            if len(sys.argv) < 3:
                print("Error: Missing ID number")
            elif not sys.argv[2].isdigit() or int(sys.argv[2]) == 0:
                print("Error: Third argument is not valid ID number")
            else:
                givenID = int(sys.argv[2])
                indexOfTask = findTask(givenID)
                if indexOfTask == -1:
                    print(f"Task (ID: {givenID}) not found")
                else:
                    del data[indexOfTask]
                    print(f"Task (ID: {givenID}) successfully deleted")
                    dumpObject(data)
        case "mark-in-progress" | "mark-done" as command:
            if len(sys.argv) < 3:
                print("Error: Missing ID number")
            elif not sys.argv[2].isdigit() or int(sys.argv[2]) == 0:
                print("Error: Third argument is not valid ID number")
            else:
                givenID = int(sys.argv[2])
                taskOfIndex = findTask(givenID)
                if taskOfIndex == -1:
                    print(f"Task (ID: {givenID}) not found")
                else:
                    task = data[taskOfIndex]
                    if command == "mark-in-progress":
                        task["status"] = "in-progress"
                    else:
                        task["status"] = "done"
                    task["updatedAt"] = Task.createTimeStamp()
                    print(f"Task (ID: {givenID}) successfully marked as \"{task["status"]}\"")
                    dumpObject(data)
        case "list":
            if len(sys.argv) == 2:
                printTasks()
            else:
                match sys.argv[2]:
                    case "todo" | "in-progress" | "done" as command:
                        printTasks(command)
                    case _:
                        print("Error: Invalid command")
        case _:
            print("Error: Invalid command")
