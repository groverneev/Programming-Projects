a = input("Enter your full name.")
a.lower()
a = list(a)
b = []
for z in range(97, 113):
    if a.count(chr(z)) == 1:
        b.append(chr(z))
print(b)