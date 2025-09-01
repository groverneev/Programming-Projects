def myFunction(a, b):
    if len(a) == len(b):
        print("Your strings are equal in length!")
    else:
        print("Your strings are not equal in length.")
myFunction(input("What is your first string?"), input("What is your second string."))