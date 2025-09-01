import random
a = random.randint(1, 100)
b = random.randint(1, 100)
c = random.randint(1, 100)
large = 0
if a > b and a > c:
    large = a
elif b > a and b > c:
    large = b
elif c > a and c > b:
    large = c
elif c == b and b > a:
    large = c
elif c == a and a > b:
    large = a
elif a == b and b > c:
    large = b
print(large)
