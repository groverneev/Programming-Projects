key = "a"
counter = 0
while key == "a":
    key = input("What is your key?")
    if key != "a":
        print("You pressed the correct key", counter, "times.")
    counter = counter + 1
