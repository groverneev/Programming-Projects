a = int(input("How big do you want your dot pattern to be?"))
if a%2 == 0:
    a = a - 1
for x in range(1, a + 1):
    if (x) % 2 == 0:
        print("\n\n")
    else:
        for y in range(3):
            for z in range(7):
                print("•", end = " ")
            print("")
