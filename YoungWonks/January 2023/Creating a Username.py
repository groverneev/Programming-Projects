a = input("Enter your full name.").split()
b = ""
for z in range(len(a)):
    b = b + a[z]
print(b.lower())