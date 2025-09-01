n, start = map(int, input().split())
whitecounter = 1
currwhite = 1
array = []
counter = start
for z in range(n):
    array.append([])
for i in range(n):
    for j in range(n):
        if currwhite <= 0:
            array[j].append(100)
        else:
            array[j].append(counter)
            counter += 1
        if counter == 10:
            counter = 1
        currwhite -= 1
    whitecounter += 1
    currwhite = whitecounter
for i in range(n):
    for j in range(n):
        if array[i][j] == 100:
            print("  ", end = "")
        else:
            print(array[i][j], end = " ")
    print()