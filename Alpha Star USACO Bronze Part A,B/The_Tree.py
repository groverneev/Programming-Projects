import sys
n, b = map(int, input().split())
mylist = []
for a in range(n):
    mylist.append(int(input()))
test = 0
counter = 0
mylist = sorted(mylist, reverse=True)
for x in range(n):
    test = mylist[x] + test
    if test >= b:
        print(counter + 1)
        sys.exit()
    counter = counter + 1