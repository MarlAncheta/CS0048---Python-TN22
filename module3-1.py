def num():
    x = int(input("Enter value for x: "))
    y = int(input("Enter value for y: "))
    return x,y
    
def add():
    x,y = num()
    z = x + y
    a = "+"
    print ("Result of",x,a,y,"=",z,"\n\n")
def sub():
    x,y = num()
    z = x - y
    a = "-"
    print ("Result of",x,a,y,"=",z,"\n\n")
def mul():
    x,y = num()
    z = x * y
    a = "*"
    print ("Result of",x,a,y,"=",z,"\n\n")
def div():
    x,y = num()
    z = x / y
    a = "/"
    print ("Result of",x,a,y,"=",z,"\n\n")


while True:
    print("------------------------------")
    print("          Calculator")
    print("------------------------------")
    print ("a. Add\nb. Subtract\nc. Multiply\nd. Divide\ne.Exit")
    i = input("Enter choice: ").lower()
    if i == "a":
        add()
    elif i == "b":
        sub()
    elif i == "c":
        mul()
    elif i == "d":
        div()
    elif i == "e":
        break
    else:
        print("Please Enter a valid input\n")
    