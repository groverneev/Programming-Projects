a = input().split()
b = input().split()
a0 = int(a[0])
a1 = int(a[1])
b0 = int(b[0])
b1 = int(b[1])
if a0 < b0:
    x = a0
else:
    x = b0
if a1 > b1:
    y = a1
else:
    y = b1
print(y-x)