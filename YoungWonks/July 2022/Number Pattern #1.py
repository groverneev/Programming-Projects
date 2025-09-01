d = int(input("How many rows do you want?"))
c = 1
for a in range(d):
    for b in range((2*a) + 1):
        print(c, end = " ")
        c = c + 1
    print("")
