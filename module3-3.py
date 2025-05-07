tasks = {}
task_id = 1

def add():
    global task_id
    task = input("Enter task description: ")
    tasks[task_id] = task
    print(f"Task added with ID {task_id}")
    task_id += 1

def rem():
    remove_id = input("Enter task ID to remove: ")
    if remove_id.isdigit() and int(remove_id) in tasks:
        del tasks[int(remove_id)]
        print(f"Task {remove_id} removed.")
    else: print("Invalid task ID.")

def veiw():
    if not tasks:
        print("No tasks.")
    else:
        for id, task in tasks.items():
            print(f"{id}: {task}")

while True:
    print("------------------------------")
    print("          To-Do List")
    print("------------------------------")
    print ("a. Add Task\nb. Remove Task\nc. View Tasks\nd. Exit\n")
    i = input("Enter choice: ").lower()
    if i == "a":
        add()
    elif i == "b":
        rem()
    elif i == "c":
        veiw()
    elif i == "d":
        print("Goodbye")
        break
    else:
        print("Please Enter a valid input\n")
    