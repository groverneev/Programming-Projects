import random
a = int(input("What is your first number?"))
b = int(input("What is your second number?"))
odd_counter = 0
even_counter = 0
for c in range(30):
    d = random.randint(a, b)
    if d%2 == 0:
        even_counter = even_counter + 1
    if d%2 == 1:
        odd_counter = odd_counter + 1
print("There are", even_counter, "even numbers and there are", odd_counter, "odd numbers.")
