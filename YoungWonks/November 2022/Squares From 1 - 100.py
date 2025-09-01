myDictionary = {}
for a in range(100):
    a = a + 1
    myDictionary[a] = a*a
a = input("What is your number?")
myList = []
for b in myDictionary:
    a = int(a)
    if b%a != 0:
        myList.append(b)
for c in range(len(myList)):
    del myDictionary[myList[c]]
print(myDictionary)