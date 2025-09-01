n = int(input())
numbers = list(map(int, input().split()))
counter = 0
list1 = []
for i in range(n):
    list3 = []
    x1 = numbers[i]
    for j in range(i+1, n):
        x2 = numbers[j]
        if x2 not in list3:
            if x1 != x2:
                for k in range(j+1, n):
                    x3 = numbers[k]
                    if x2 == x3:
                        list2 = [x1, x2]
                        if list2 not in list1:
                            counter += 1
                            list1.append([x1, x2])
                            list3.append(x2)
print(counter)