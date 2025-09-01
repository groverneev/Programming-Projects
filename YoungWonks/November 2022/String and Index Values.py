a = input("Enter a string.")
myDictionary = {}
for b in range(len(a)):
    myDictionary[a[b]] = b
print(myDictionary)