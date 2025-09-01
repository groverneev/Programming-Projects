n = int(input())
fj = list(map(int, input().split()))
dr = list(map(int, input().split()))
def comparelist(a, b):
    counter = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            counter += 1
    return counter
def reorder(list1, a, b):
    lst = list1.copy()
    if a == b:
        return lst
    while a < b:
        lst[a], lst[b] = lst[b], lst[a]  
        a += 1
        b -= 1

    return lst
numlist = []
for _ in range(n+1):
    numlist.append(0)
for i in range(n):
    for j in range(n):
        if i <= j:
            newlist = reorder(fj, i, j)
            s = comparelist(newlist, dr)
            numlist[s] += 1
for _ in range(len(numlist)):
    print(numlist[_])

#Efficiency needs to be improved