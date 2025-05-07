grade = []

def add():
    input("Enter Subject Name: ")
    x = input("Enter Score: ")
    if x.isdigit():
        x = float(x)
        grade.append(x)
        print ("Score added")
    else:
        print("Enter valid input.\n")
def avg():
    print ("Average is ",sum(grade)/len(grade))
    

while True:
    print("------------------------------------")
    print("          Grade Calculator")
    print("------------------------------------")
    print ("a. Add Score\nb. Calculate Average\nc. Exit\n")
    i = input("Enter choice: ").lower()
    if i == "a":
        add()
    elif i == "b":
        avg()
    elif i == "c":
        print("Goodbye")
        break
    else:
        print("Please Enter a valid input\n")
    