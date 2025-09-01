import sys
import random
def random_function():  
    y = 0
    while y != 1:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        d = random.randint(0, 9)
        e = random.randint(0, 9)
        f = random.randint(0, 9)
        if a != b and a != c and a != d and a != e and a != f:
            if b != c and b != d and b != e and b != f:
                if c != d and c != e and c != f:
                    if d != e and d != f:
                        if e != f:
                            y = 1
    a = str(a)
    b = str(b)
    c = str(c)
    d = str(d)
    e = str(e)
    f = str(f)
    return a+b+c+d+e+f
def real_account(x):
    counter = 0
    for k in myDictionary:
        if x == k:
            counter = 1
    return counter
myDictionary = {"123456" : 10}
while True:
    a = input("Do you want to get a new account, view an account, delete an account, add money, withdraw money, or quit?")
    if a == "q":
        print("Thank you for playing!")
        sys.exit()
    elif a == "n":
        b = random_function()
        print("Here is your password:", b)
        c = int(input("What is your starting balance?"))
        myDictionary[b] = c
        print("You have successfully created a new account!")
    elif a == "v":
        b = input("Enter a password for the account you want to view.")
        ra = real_account(b)
        if ra == 0:
            print("Your account does not exist.")
        else:
            print("Here is your account balance:", myDictionary[b])
    elif a == "d":
        z = input("What is the password for the account you want to delete?")
        ra = real_account(z)
        if ra == 0:
            print("Your account does not exist.")
        else:
            del myDictionary[z]
        print("Your account has been successfully deleted!")
    elif a == "a":
        y = input("What is your password?")
        ra = real_account(b)
        if ra == 0:
            print("That account does not exist.")
        else:
            z = int(input("How much money do you want to add to your account?"))
            myDictionary[y] = myDictionary[y] + z
            print("Your money has been successfully added!")
    elif a == "w":
        y = input("What is your password?")
        ra = real_account(b)
        if ra == 0:
            print("That account does not exist.")
        else:
            z = int(input("How much money do you want to withdraw to your account?"))
            myDictionary[y] = myDictionary[y] - z
            print("Your money has been successfully withdrawn!")