import random
a = 1234567890
final = 1
for b in range(10):
    c = random.randint(1, 100)
    print(c)
    if c < a:
        a = c
for z in range(1, a + 1):
    final = final * z
print("The smallest factorial is:", final)
