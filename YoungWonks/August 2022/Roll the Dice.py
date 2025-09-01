import random
import time
account = 5
while True:
    b = input("Do you want to roll the dice or not? y/n")
    if b == "n":
        print("Thank you for playing!")
        break
    if b == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print("Wait for 1 second.")
        time.sleep(1)
        if dice1 == dice2:
            print("You won!")
            account = account + 5
        if dice1 != dice2:
            print("You lost.")
            account = account - 1
        print("Your account has $", end = "")
        print(account)
        if account == 0:
            print("Thank you for playing.")
            break
