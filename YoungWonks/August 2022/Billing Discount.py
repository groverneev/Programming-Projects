import random
age = int(input("What is your age?"))
bill = float(input("What is your bill amount?"))
discount = 0
if age < 16:
    discount = 8
    i = random.randint(1, 100)
    j = random.randint(1, 100)
    k = i + j
    print("Solve this math problem:", i, "+", j)
    y = int(input())
    if y == k:
        discount = 10
        print("You got an extra 2% discount!")
elif age > 15 and age < 41:
    discount = 5
    x = input("Enter a code.")
    if x == "YoungWonks":
        discount = 8
elif age > 40:
    discount = 8
print("Your discount is:", discount, end = "")
print("%")
print("Your discount amount is: $", end = "")
print((discount * bill)/100)
print("Your final amount is: $", end = "")
print(bill - ((discount * bill)/100))
