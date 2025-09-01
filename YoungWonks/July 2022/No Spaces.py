import sys
a = input("What is your first string?").split()
b = input("What is your second string?").split()
c = 0
if a == b:
    sys.exit()
if len(a) > 1:
    c = c + 1
if len(b) > 1:
    c = c + 1
if c == 0:
    print("There are no spaces!")
if c == 1:
    print("There are spaces in one string.")
if c == 2:
    print("There are spaces in both strings.")
