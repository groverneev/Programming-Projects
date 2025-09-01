counter = 0
factors = []
for a in range(100, 121):
    for b in range(1, a + 1):
        if a % b == 0:
            counter = counter + 1
            factors.append(b)
    print("Here are the factors of the number", a, end = "")
    print(":", factors)
    counter = 0
    factors = []
