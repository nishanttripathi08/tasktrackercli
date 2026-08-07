import sys, os, json
from task import Task

filename = "data.json"

if not os.path.exists(filename): #
    with open(filename, "w", encoding="utf-8") as file:
        json.dump([], file) # Creates a file with an empty JSON object
with open("data.json", "r") as file:
    data = json.load(file)
if len(sys.argv) < 2:
    print("Error: No command found")
else:
    firstArg = sys.argv[1]
    match firstArg:
        case "add":
            if len(sys.argv) < 3:
                print("Error: Missing task description")
            else:
                ID = max([item["id"] for item in data]) + 1 if len(data) != 0 else 1
                task = Task(sys.argv[2], ID)
                data.append(vars(task))
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
        case "update":
            if len(sys.argv) < 3:
                print("Error: Missing ID number and updated description")
            elif len(sys.argv) < 4:
                print("Error: Missing updated description")
            elif not sys.argv[2].isdigit() or int(sys.argv[2]) > len(data) or int(sys.argv[2]) == 0:
                print("Error: Third argument is not valid ID number")
            else:
                givenID = sys.argv[2]
                updatedDescription = sys.argv[3]
                (data[int(givenID) - 1])["description"] = updatedDescription
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
        #case "delete":

        #case "mark-in-progress":

        #case "mark-done":

        #case "list":

        #case "_":


