def myFunction(a, b):
    if a == "" or b == "":
        a = 10
        b = 10
    a = int(a)
    b = int(b)
    for z in range(a):
        for y in range(b):
            print("•", end = " ")
        print("")
myFunction(input("What is the length of your pattern?"), input("What is the width of your pattern?"))