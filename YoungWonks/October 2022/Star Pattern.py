counter = 0
counter1 = -1
for a in range(5):
    counter = 4 - a
    for b in range(counter):
        print("-", end = "")
    counter1 = counter1 + 2
    for c in range(counter1):
        print("•", end = "")
    counter = 4 - a
    for d in range(counter):
        print("-", end = "")
    print("")
