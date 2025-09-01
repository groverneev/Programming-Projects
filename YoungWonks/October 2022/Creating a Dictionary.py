myDictionary = {"bob" : "apple", "joe" : "pear", "sally" : "strawberries"}
myDictionary["sam"] = "grapes"
print(myDictionary)
print(myDictionary["joe"])
del myDictionary["bob"]
for a in myDictionary:
    print(a, myDictionary[a])
print(myDictionary.keys())
print(myDictionary.values())
