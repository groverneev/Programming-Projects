def myFunction(a):
    b = ""
    for c in range(len(a) - 1, -1, -1):
        b = b + a[c]
    print(b)
myFunction(input("What is your string?"))