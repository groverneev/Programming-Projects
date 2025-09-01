import random
def myFunction(a):
    myList = []
    for z in range(20):
        myList.append(random.randint(-256, 256))
    if a == "p":
        newList = []
        for z in range(20):
            if myList[z] >= 0:
                newList.append(myList[z])
    else:
        newList = []
        for z in range(20):
            if myList[z] <= 0:
                newList.append(myList[z])
    for z in range(len(newList)):
        print(newList[z])
myFunction(input("Do you want positive or negative numbers?"))