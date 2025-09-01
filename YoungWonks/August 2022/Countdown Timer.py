import time
a = int(input("How many seconds do you want your timer to last?"))
while a != 0:
    print(a)
    a = a - 1
    time.sleep(1)
print("Blast off!")
