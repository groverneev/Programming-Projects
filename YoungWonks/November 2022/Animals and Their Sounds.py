myDictionary = {"Dog" : "", "Cat" : "", "Horse" : ""}
newDictionary = {}
for a in myDictionary:
    print("What sound does a", a, "make?")
    b = input()
    newDictionary[a] = b
print(newDictionary)
