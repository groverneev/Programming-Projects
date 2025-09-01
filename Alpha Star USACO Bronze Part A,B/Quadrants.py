n, b = map(int, input().split())
arr = []
for ee in range(n):
    test = input().split()
    test[0] = int(test[0])
    test[1] = int(test[1])
    arr.append(test)
minMaxReg = 45676545676567865676
for i in range(n):
    fx = arr[i][0] + 1
    for j in range(n):
        fy = arr[j][1] + 1
        reg1 = 0
        reg2 = 0
        reg3 = 0
        reg4 = 0
        for k in range(n):
            cow = arr[k]
            if cow[0] < fx and cow[1] < fy:
                reg1 += 1
            elif cow[0] > fx and cow[1] > fy:
                reg3 += 1
            elif cow[0] > fx and cow[1] < fy:
                reg2 += 1
            elif cow[0] < fx and cow[1] > fy:
                reg4 += 1
            maxReg = max(reg1, reg2, reg3, reg4)
        if maxReg < minMaxReg:
            minMaxReg = maxReg
print(minMaxReg)