def myFunction(a):
    myList = []
    for z in range(a):
        if a%(z + 1) == 0:
            myList.append(z + 1)
    print(myList)
myFunction(int(input("What is your number?")))