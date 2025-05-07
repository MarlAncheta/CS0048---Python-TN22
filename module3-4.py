import random
def play():
    num_guess = random.randint(1, 100)
    attempt = 0
    while True:
        guess = input("Take a guess(1-100): ")
        if guess.lstrip("-").isdigit():
            guess = int(guess)
            attempt += 1
            
            if guess < num_guess:
                print ("Attempt: ",attempt)
                print ("To Low\n")

            elif guess > num_guess:
                print ("Attempt: ",attempt)
                print ("To High\n") 
            
            elif guess == num_guess:
                print ("You guessed right")
                print ("You took Attempts: ",attempt)
                break
        else:
            print("Enter valid number.\n")
            break



while True:
    print("------------------------------")
    print("          To-Do List")
    print("------------------------------")
    print ("a. Play Number Guessing Game\nb. Exit\n")
    i = input("Enter choice: ").lower()
    if i == "a":
        play()
    elif i == "b":
        print("Goodbye")
        break
    else:
        print("Please Enter a valid input\n")
    