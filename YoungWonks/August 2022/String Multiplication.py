a = input("Enter a string of digits.")
counter = None
final = 0
aa = None
bb = None
c = int(a)
for b in range(len(a)):
    aa = a[b - 2]
    bb = a[b - 1]
    aa = int(aa)
    bb = int(bb)
    counter = aa * bb
    final = final + counter
fruit = a[b]
fruit = int(fruit)
print(final - fruit)
