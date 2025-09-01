def myFunction(p, n, d, q):
    a = p + 5*n + 10*d + 25*q
    a = a/100
    print(a)
myFunction(int(input("How many pennies do you have?")), int(input("How many nickels do you have?")), int(input("How many dimes do you have?")), int(input("How many quarters do you have?")))