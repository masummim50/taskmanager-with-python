import datetime
import uuid

class Task:
    all_tasks = []
    def __init__(self, task_name):
        self.task = task_name
        self.created_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated_time = None
        self.completed_time = None
        self.task_done = False
        self.id = str(uuid.uuid4())
        self.all_tasks.append(self)
    def update_task(self, task_object, new_task_name):
        for t in self.all_tasks:
            if(t == task_object):
                t.task = new_task_name
                t.updated_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    def complete_task(self, task_object):
        for t in self.all_tasks:
            if(t==task_object):
                t.task_done = True
                t.completed_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def add():
    print("\nEnter task: ", end="")
    text = input()
    task = Task(text)
    print("\nNew Task created Successfullly\n")

def unishow(t):
    ctime = t.completed_time
    if(t.completed_time == None):
        ctime = "N/A"
    utime = t.updated_time
    if(utime == None):
        utime = "N/A"
    print("Id - ", t.id)
    print("Task - ", t.task)
    print("Created Time - ", t.created_time)
    print("Updated Time - ", utime)
    print("Completed - ", t.task_done)
    print("Completed Time- ", ctime)
    print()

def show(type):
    print()
    count = 0
    for i,t in enumerate(Task.all_tasks):
        if(type == "number"):
            print("No - ", i+1)
        unishow(t)
        count+=1
    if(count == 0):
        print("No task added yet\n")
        
def showfiltered(type):
    if(type == "completed"):
        count = 0;
        for i,t in enumerate(Task.all_tasks):
            if(t.task_done):
                count+=1
                unishow(t)
        if(count == 0):
            print()
            print("There is no completed tasks")
            print()
    else:
        count = 0;
        heading = 0;
        for i,t in enumerate(Task.all_tasks):
            if(t.task_done == False):
                if(heading == 0):
                    print("\nPending Tasks:")
                    heading+=1
                unishow(t)
                count+=1
        if(count == 0):
            print()
            print("There is no pending tasks")
            print()
        
choice = 1
while(choice!= 0):
    print("1: to add a new task")
    print("2: to show all tasks")
    print("3: to update a task")
    print("4: to mark a task complete")
    print("5: to show the completed tasks")
    print("6: to show the pending tasks")
    print("0: to stop\n")
    print("Choose option: ", end="")
    choice = input()
    if(choice == "1"):
        add()
    elif(choice == "2"):
        show("")
    elif(choice == "3"):
        if(len(Task.all_tasks) == 0):
            print("\nList is empty, nothing to update\n")
        else:
            show("number")
            print("choose task number: ", end="")
            tn = input()
            if(int(tn)> len(Task.all_tasks) or int(tn)<1):
                print("\nInvalid Selection\n")
            else:
                t = Task.all_tasks[int(tn)-1]
                print("updated task info: ", end="")
                up = input()
                t.update_task(t, str(up))
                print("\nupdated successfully\n")
    elif(choice == "4"):
        if(len(Task.all_tasks) == 0):
            print("\nNo task in the list\n")
        else:
            show("number")
            print("Choose which one to mark complete: ", end="")
            tocomplete = input()
            if(int(tocomplete)> len(Task.all_tasks) or int(tocomplete) < 1):
                print("\nInvalid todo number\n")
            else:
                t = Task.all_tasks[int(tocomplete)-1]
                if(t.task_done):
                    print("\nAlready marked as completed\n")
                else:
                    t.complete_task(t)
                    print("\nMarked as complete\n")
    elif(choice == "5"):
        showfiltered("completed")
    elif(choice == "6"):
        showfiltered("pending")
    elif(choice == "0"):
        break
    else:
        print("\nThat's not a valid choice\n")




