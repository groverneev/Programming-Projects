import time
a = input("Enter a string.")
for b in range(len(a)):
    print(a[b])
    if b != len(a) - 1:
        time.sleep(1)
