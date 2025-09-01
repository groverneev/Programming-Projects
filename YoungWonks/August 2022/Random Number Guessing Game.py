import random
a = random.randint(1, 1000)
guess = None
counter = 0
while guess != a:
    guess = int(input("What is your number?"))
    if a > guess:
        print("Higher.")
        counter = counter + 1
    if a < guess:
        print("Lower.")
        counter = counter + 1
    if a == guess:
        print("You guessed it correctly!")
        print("You took", counter, "tries to guess the number.")
