import random
myList = []
for a in range(25):
    myList.append(random.randint(1, 100))
myList.sort()
print(myList)
