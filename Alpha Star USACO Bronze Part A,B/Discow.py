a = input()
counter = 0
for i in range(len(a) - 1):
    if (a[i] == a[i+1]):
        a = a[0:i-1] + a[i+2:]
        counter += 1
print(a)