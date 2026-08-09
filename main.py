import sys, os, json
from task import Task
from datetime import datetime

if not os.path.exists("data.json"):
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump([], file) # Creates a file with an empty JSON object
with open("data.json", "r") as file:
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
                ID = max([item["id"] for item in data]) + 1 if len(data) != 0 else 1
                task = Task(sys.argv[2], ID)
                data.append(vars(task))
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
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
                for tasks in data:
                    if tasks["id"] == givenID:
                        tasks["description"] = updatedDescription
                        tasks["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        print(f"Task (ID: {givenID}) successfully updated")
                        with open("data.json", "w") as file:
                            json.dump(data, file, indent=4)
                        flag = False
                        break
                if flag:
                    print(f"Task (ID: {givenID}) not found")
        case "delete": # Deleting existing task
            if len(sys.argv) < 3:
                print("Error: Missing ID number")
            elif not sys.argv[2].isdigit() or int(sys.argv[2]) == 0:
                print("Error: Third argument is not valid ID number")
            else:
                givenID = int(sys.argv[2])
                for i in range(len(data)):
                    if (data[i])["id"] == givenID:
                        del data[i]
                        print(f"Task (ID: {givenID}) successfully deleted")
                        with open("data.json", "w") as file:
                            json.dump(data, file, indent=4)
                        flag = False
                        break
                if flag:
                    print(f"Task (ID: {givenID}) not found")
        case "mark-in-progress" | "mark-done" as command:
            if len(sys.argv) < 3:
                print("Error: Missing ID number")
            elif not sys.argv[2].isdigit() or int(sys.argv[2]) == 0:
                print("Error: Third argument is not valid ID number")
            else:
                givenID = int(sys.argv[2])
                for tasks in data:
                    if tasks["id"] == givenID:
                        tasks["status"] = command[5:]
                        tasks["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        print(f"Task (ID: {givenID}) successfully marked as \"{command[5:]}\"")
                        with open("data.json", "w") as file:
                            json.dump(data, file, indent=4)
                        flag = False
                        break
                if flag:
                    print(f"Task (ID: {givenID}) not found")
        case "list":
            if len(sys.argv) == 2:
                for task in data:
                    print(f"Task number {task["id"]} is to \"{task["description"]}\". It is currently \"{task["status"]}\", was created at {task["createdAt"]}, and was last updated at {task["updatedAt"]}")
            else:
                match sys.argv[2]:
                    case "todo" | "in-progress" | "done" as command:
                        for task in data:
                            if task["status"] == command:
                                print(f"Task number {task["id"]} is to \"{task["description"]}\". It is currently \"{task["status"]}\", was created at {task["createdAt"]}, and was last updated at {task["updatedAt"]}")
                    case _:
                        print("Error: Invalid command")
        case _:
            print("Error: Invalid command")
