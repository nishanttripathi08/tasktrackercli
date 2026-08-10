from datetime import datetime

class Task:
    def __init__(self, description, IDnumber):
        self.description = description
        self.IDnumber = IDnumber
        self.status = "todo"
        self.createdAt = self.createTimeStamp()
        self.updatedAt = self.createTimeStamp()

    @staticmethod
    def createTimeStamp():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")