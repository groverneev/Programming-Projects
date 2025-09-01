a = int(input("What is the current hour?"))
if a >= 8 and a < 12:
    print("Good morning.")
elif a >= 12 and a < 17:
    print("Good afternoon.")
elif a >= 17 and a < 21:
    print("Good evening.")
else:
    print("Good night.")
