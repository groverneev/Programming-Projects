a = int(input("What is your temprature?"))
b = input("What is your unit(f/c)?")
if b == "f":
    c = a - 32
    d = c * (5/9)
    print("The temprature in celsius is:", d)
if b == "c":
    c = a * (9/5)
    d = c + 32
    print("The temprature in fahrenheit is:", d)
