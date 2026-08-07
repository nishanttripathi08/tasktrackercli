from datetime import datetime

class Task:
    def __init__(self, description, id):
        self.description = description
        self.id = id
        self.status = "todo"
        self.createdAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
