import sys
counter = 0
myDictionary = {"Sandeep" : "dad1", "Pallavi" : "mom2", "Vihan" : "brother3", "Neev" : "myself4"}
while True:
    a = input("Enter a username (or q to quit).")
    if a == "q":
        print("Thank you for playing!")
        sys.exit()
    for b in myDictionary:
        if a == b:
            counter = 1
    if counter == 0:
        print("No username found. Please try again.")
    if counter == 1:
        counter = 0
        b = input("What is your password?")
        if b == myDictionary[a]:
            print("You have successfully logged into", a, end = "")
            print("'s account!")
        else:
            print("Your password was incorrect. Please try agian.")