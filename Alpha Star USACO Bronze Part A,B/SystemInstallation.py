row, col = map(int, input().split())
array = []
for t in range(row):
    test = input().split()
    for s in range(col):
        test[s] = int(test[s])
    array.append(test)
counter = 0
largest = 0
frow = 0
fcol = 0
for i in range(col - 3):
    counter = 0
    for j in range(row - 3):
        counter = 0
        counter = array[i][j] + array[i][j+1] + array[i][j+2] + array[i+1][j] + array[i+1][j+1] + array[i+1][j+2] + array[i+2][j] + array[i+2][j+1] + array[i+2][j+2]
        if counter > largest:
            largest = counter
            frow = i + 1
            fcol = j + 1
print(largest)
print(frow, end = " ")
print(fcol)