a = input("Enter a sentence.")
counter = 0
counter2 = 0
for b in range(len(a)):
    c = a[b]
    for d in range(len(c)):
        if c[counter2] == "e" or c[counter2] == "E":
            counter = 1
        if counter == 0:
            print(c[counter2], end = "")
        counter = 0
        counter2 = counter2 + 1
    counter2 = 0
