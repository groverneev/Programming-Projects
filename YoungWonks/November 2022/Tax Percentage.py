def myFunction(a):
    if a <= 1000:
        c = (a * 90)/100
    elif a > 1000 and a < 2000:
        a = a - 1000
        a = (a * 80)/100
        c = 900 + a
    elif a > 2000 and a < 3000:
        a = a - 2000
        a = (a * 70)/100
        c = 1700 + a
    else:
        a = a - 3000
        a = (a * 60)/100
        c = 2300 + a
    print(c)
myFunction(int(input("What is your monthly salary?")))