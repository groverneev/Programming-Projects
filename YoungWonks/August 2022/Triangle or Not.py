import random
import sys
a = random.randint(5, 15)
b = random.randint(5, 15)
c = random.randint(5, 15)
print(a, b, c)
if a + b <= c:
    print("Not a triangle.")
    sys.exit()
if b + c <= a:
    print("Not a triangle.")
    sys.exit()
if c + a <= b:
    print("Not a triangle.")
    sys.exit()
print("The numbers make a triangle!")
