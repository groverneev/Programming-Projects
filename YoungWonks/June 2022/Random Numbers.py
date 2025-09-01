import random
x = int(input("Enter a number between 1 and 6."))
print(random.randint(10**(x - 1), 10**x))
