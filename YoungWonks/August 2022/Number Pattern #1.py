a = int(input("How many times do you want to print the pattern?"))
for b in range(a):
    for c in range(5):
        print(c + 1, end = " ")
    print("")
    for d in range(5, 0, -1):
        print(d, end = " ")
    print("")
