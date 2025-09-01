counter = 1
duplicate = counter
myArray = []
while counter != 100:
    duplicate = str(counter)
    for a in range(len(duplicate)):
        myArray.append(duplicate[a])
    if myArray[len(duplicate) - 1] == "2":
        print(counter)
    myArray = []
    counter = counter + 1
