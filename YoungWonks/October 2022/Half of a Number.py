a = int(input("what is your number?"))
myList = []
for b in range(a):
    myList.append(b + 1)
c = a//2
for d in range(c):
    print(myList[d], end = " ")
print("")
for e in range(c, a):
    print(myList[e], end = " ")
