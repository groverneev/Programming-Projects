import random
"""
max_1 = -123456788765432
min_1 = 123456
for a in range(25):
    b = random.randint(1, 100)
    print(b)
    if b > max_1:
        max_1 = b
    if b < min_1:
        min_1 = b
print("The maximum value is:", max_1)
print("The minimum value is:", min_1)
"""

myList = []
max_1 = -123456788765432
min_1 = 123456
for a in range(25):
    myList.append(random.randint(1, 100))
    print(d)
max_1 = max(myList)
min_1 = min(myList)
print("The maximum value is:", max_1)
print("The minimum value is:", min_1)
