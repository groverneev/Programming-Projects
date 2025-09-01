myDictionary = {"Bob" : 72, "Sam" : 26, "Joe" : 86}
myList = []
for a in myDictionary:
    myDictionary[a] = myDictionary[a] + 5
for b in myDictionary:
    if myDictionary[b] < 60:
        myList.append(b)
for c in myList:
    del myDictionary[c]
for d in myDictionary:
    if int(myDictionary[d]) > 90 and int(myDictionary[d]) < 100:
        myDictionary[d] = "A"
    elif int(myDictionary[d]) > 80 and int(myDictionary[d]) < 90:
        myDictionary[d] = "B"
    elif int(myDictionary[d]) > 70 and int(myDictionary[d]) < 80:
        myDictionary[d] = "C"
    elif int(myDictionary[d]) > 60 and int(myDictionary[d]) < 70:
        myDictionary[d] = "D"
    elif int(myDictionary[d]) < 60:
        myDictionary[d] = "F"
print(myDictionary)
