notprime = 0
while True:
    for a in range(30):
        for z in range (2, a):
            y = a % z
            if y == 0:
                notprime = 1
        if notprime != 1 and a != 0 and a != 2:
            print (a, "is a prime number.")
        notprime = 0
