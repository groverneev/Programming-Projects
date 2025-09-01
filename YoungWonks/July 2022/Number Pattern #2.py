d = int(input("How many rows do you want?"))
e = 0
c = 1
for a in range(d + 1):
    e = e + a
    f = e
    for b in range(a):
        print(f, end = " ")
        c = c + 1
        f = f - 1
    print("")
