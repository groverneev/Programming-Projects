import random
d = 0
nd = 0
for counter in range(25):
    a = random.randint(50, 150)
    if a%6 == 0:
        print(a,"is divisible by 6.")
        d = d+1
    else:
        print(a,"is not divisible by 6.")
        nd = nd + 1
print("Out of 25 numbers,", d, "are divisible by 6 and", nd, "are not divisible by 6.")
