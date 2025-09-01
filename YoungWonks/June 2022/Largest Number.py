import random
a = random.randint(1, 100)
b = random.randint(1, 100)
c = random.randint(1, 100)
print(a, b, c)
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > b and c > a:
    print(c)
elif a == b and a > c:
    print(a)
elif a == b and a < c:
    print(c)
elif a == c and a > b:
    print(a)
elif a == c and a < b:
    print(b)
elif b == c and b > a:
    print(b)
elif b == c and b < a:
    print(a)
elif a == b == c:
    print(a)
