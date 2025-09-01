def myFunction(a):
    myList = []
    for z in range(len(a)):
        myList.append(a[z])
    myList.sort()
    b = ""
    for z in range(len(myList)):
        b = b + myList[z]
    print(b)
myFunction(input("Enter a word."))