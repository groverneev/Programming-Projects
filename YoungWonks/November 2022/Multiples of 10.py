myDictionary = {"A": 10, "B": 20, "C": 35, "D": 40, "E": 19, "F": 11}
newDictionary = {}
for a in myDictionary:
    if myDictionary[a]%10 == 0:
        newDictionary[a] = myDictionary[a]
print(newDictionary)