n = int(input())
acorns = []
acorns2 = []
for i in range(n):
    a, b = map(int, input().split())
    test = []
    test.append(a)
    test.append(b)
    acorns.append(test)
    acorns2.append(a/b)
ans = []
ans2 = []
for j in range(3):
    a = max(acorns2)
    index = acorns2.index(a)
    ans.append(index + 1)
    acorns2[index] = 0.0
    ans2.append(acorns[index])
print(ans2[0][1] + ans2[1][1] + ans2[2][1])
print(ans[0])
print(ans[1])
print(ans[2])