import sys
password = "HelloWorld"
input_1 = input("What is the password?")
if input_1 == password:
    print("Access Granted!")
    sys.exit()
guesses = [input_1]
for a in range(2):
    input_1 = input("What is the password?")
    if input_1 == password:
        print("Access Granted!")
        print("Wrong Passwords Tried:", guesses)
        sys.exit()
    else:
        guesses.append(input_1)
print("Access denied. Too many failed attempts.")
print("Here are your failed attempts:", guesses)
