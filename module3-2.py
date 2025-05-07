def c2f():
    x = input("Enter temperature in Celsius: ")
    if x.lstrip("-").isdigit():
        x = int(x)
        x = (x*(9/5))+32
        print ("Temperature in Fahrenheit:",x,"\n\n")
    else:
        print("Enter valid input.\n")
def f2c():
    x = input("Enter temperature in Celsius: ")
    if x.lstrip("-").isdigit():
        x = int(x)
        x = (x-32)*(5/9)
        print ("Temperature in Fahrenheit:",x,"\n\n")
    else:
        print("Enter valid input.\n")

while True:
    print("-----------------------------------------")
    print("          Temperature Converter")
    print("-----------------------------------------")
    print ("a. Convert Celsius to Fahrenheit\nb. Convert Fahrenheit to Celsius\nc. Exit")
    i = input("Enter choice: ").lower()
    
    if i == "a":
        c2f()
    elif i == "b":
        f2c()
    elif i == "c":
        break
    else:
        print("Enter valid input.\n")