import random
a = ["bob", "is", "an", "alien"]
b = "•••".join(a)
print(b)
print(b[-3])
print(b[-2:0:-1])
print(ord(b[16]))
c = b[random.randint(1, 20)]
print(c)
if ord(c) > 65 and ord(c) <= 91:
    print (c, "is a letter.")
else:
    if ord(c) > 97 and ord(c) <= 123:
        print(c, "is a letter.")
    else:
        print(c, "is not a letter.")