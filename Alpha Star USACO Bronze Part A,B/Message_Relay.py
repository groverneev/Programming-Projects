n = int(input())
arr = input().split()
for j in range(n):
    arr[j] = int(arr[j])
arr.sort()
print(arr)
dir = []
#true = left, false = right
counter = 0
fr = []
#0 = none, 1 = 1, 2 = 2
for i in range(n):
    if i == 0:
        dir.append(False)
    elif i == n-1:
        dir.append(True)
    else:
        if arr[i] - arr[i-1] <= arr[i+1] - arr[i]:
            dir.append(True)
        else:
            dir.append(False)
for k in range(n):
    if k == 0:
        if dir[k+1] == False:
            counter += 1
            print("a", k)
    elif k == n-1:
        if dir[k-1] == True:
            counter += 1
            print("b", k)
    else:
        if dir[k-1] == True and dir[k+1] == False:
            counter += 1
            print("c", k)
print(counter)