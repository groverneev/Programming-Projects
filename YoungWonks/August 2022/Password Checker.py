password = "Python"
guess = None
while guess != password:
    guess = input("What is your guess?")
    if guess != password:
        print("Access denied.")
print("Access granted!")
