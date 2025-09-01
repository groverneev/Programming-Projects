import random
import sys
fruits = ["apple", "bannana", "orange", "pineapple"]
while True:
    a = random.randint(0, 3)
    if "p" in fruits[a] or "P" in fruits[a]:
        print(fruits[a])
        sys.exit()
    else:
        print("P not found.")
