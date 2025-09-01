a, b = input().split()
cows = int(a)
list_ = int(b)
numbers = input().split()
for a in range(list_):
    numbers[a] = int(numbers[a])
circle = []
cowcounter = cows
for a in range(cows):
    circle.append(1)

currentCow = 0
activeCounter = 1

for i in range (cows):
    for moves in range (numbers[activeCounter]):
        currentCow = currentCow + 1
        if currentCow > cows:
            currentCow = 1
#not working