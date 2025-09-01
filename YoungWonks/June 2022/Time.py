repeat = True
while repeat == True:
    time = int(input("What is the time in HHMM format?"))
    if time >= 400 and time <= 1159:
        print("Morning")
    elif time > 2400 or time < 0:
        print("Please enter a valid time.")
    elif time == 1200:
        print("Noon")
    elif time >= 1201 and time <= 1700:
        print("Afternoon")
    elif time >= 1701 and time <= 2000:
        print("Evening")
    else:
        print("Night")
    x = input("Keep going? y/n")
    if x == "n":
        repeat = False
print("Thank you for playing!")
