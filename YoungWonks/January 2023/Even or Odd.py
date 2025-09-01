a = input("Enter a string of numbers seperated by spaces.").split()
b = []
for z in range(len(a)):
    a[z] = int(a[z])
    if a[z]%2 == 0:
        b.append(a[z])
print(b)