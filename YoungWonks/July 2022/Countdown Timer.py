import time
x = int(input("How many seconds do you want your countdown timer to be?"))
for y in range(x):
    print(x)
    x = x - 1
    time.sleep(1)
print("Blast off!")
