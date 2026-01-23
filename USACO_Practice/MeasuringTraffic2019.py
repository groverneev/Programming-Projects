# https://usaco.org/index.php?page=viewproblem2&cpid=917

n = int(input())
arr = []
for i in range(n):
    arr.append(list(input().split()))
lowern = 0
uppern = 99999999999999999999999999999999999
for i in range(n): #forward pass
    arr2 = arr[i]
    arr2[1] = int(arr2[1])
    arr2[2] = int(arr2[2])
    print(arr2)
    if (arr2[0] == "on"):
        print("1")
        lowern += arr2[1]
        uppern += arr2[2]
    elif (arr2[0] == "off"):
        print("2")
        lowern -= arr2[1]
        uppern -= arr2[2]
    else:
        print("3")
        lowern = max(lowern, arr2[1])
        uppern = min(uppern, arr2[2])
lower0 = 0
upper0 = 99999999999999999999999999999999999
for i in range(n, 0): #forward pass
    arr2 = arr[i]
    arr2[1] = int(arr2[1])
    arr2[2] = int(arr2[2])

    if (arr2[0] == "off"):
        lower0 += arr2[1]
        upper0 += arr2[2]
    elif (arr2[0] == "on"):
        lower0 -= arr2[1]
        upper0 -= arr2[2]
    else:
        lower0 = max(lower0, arr2[1])
        upper0 = min(upper0, arr2[2])
print([lower0, upper0])
print([lowern, uppern])
