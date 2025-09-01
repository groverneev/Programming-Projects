import random
myList = []
counter = 1
for a in range(25):
    myList.append(random.randint(1, 50))
myList.sort()
while True:
    if myList[counter] > 20:
        break
    counter = counter + 1
print("The second smallest number above 20 is", myList[counter + 1], end = "")
print(".")
