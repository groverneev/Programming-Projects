a = input("Enter the musical notes seperated by spaces.").lower().split()
final = []
counter = []
for b in range(len(a)):
    counter1 = a[b]
    for d in range(len(counter1)):
        counter.append(ord(counter1[d]))
    final.append(counter)
    counter = []
    counter1 = ""
print(final)