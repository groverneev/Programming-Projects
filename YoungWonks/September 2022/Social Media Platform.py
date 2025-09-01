import sys
username = []
counter = 0
while True:
    a = input("Do you want to create a new username or remove an old one (or quit)?")
    if a == "q":
        print("Thank you!")
        sys.exit()
    if a == "r":
        b = input("Enter a username to remove.")
        for c in range(len(username)):
            if username[c] == b:
                counter = 1
                break
        if counter == 0:
            print("Sorry, there is no such username. Please try again.")
        if counter == 1:
            print("You have successfully deleted your old account!")
            username.remove(b)
            counter = 0
    if a == "n":
        b = input("Enter a username to add.")
        for c in range(len(username)):
            if username[c] == b:
                counter = 1
                break
        if counter == 0:
            print("You have successfully created a new username!")
            username.append(b)
        if counter == 1:
            print("Sorry, that username is aldready taken. Please try again.")
            counter = 0
