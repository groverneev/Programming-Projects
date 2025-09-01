n, u = map(int, input().split())
grid = [input() for _ in range(4)]

def why():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    for col in range(int(n/2)-1):
        for row in range(int(n/2)-1):
            if grid[row][col] != grid[n-1-row][col]:
                print(row, col)
                counter1 += 1
            if grid[row][col] != grid[row][n-1-col]:
                counter1 += 1
                print(row, col)

            if grid[row][col] != grid[n-1-row][n-1-col]:
                counter1 += 1
                print(row, col)
    for col in range(int(n/2)-1):
        for row in range(int(n/2), n-1):
            if grid[row][col] != grid[int(n/2)-1-row][col]:
                counter2 += 1
            if grid[row][col] != grid[row][n-1-col]:
                counter2 += 1
            if grid[row][col] != grid[int(n/2)-1-row][n-1-col]:
                counter2 += 1
    for col in range(int(n/2), n-1):
        for row in range(int(n/2)-1):
            if grid[row][col] != grid[n-1-row][col]:
                counter3 += 1
            if grid[row][col] != grid[row][int(n/2)-1-col]:
                counter3 += 1
            if grid[row][col] != grid[n-1-row][int(n/2)-1-col]:
                counter3 += 1
    for col in range(int(n/2), n-1):
        for row in range(int(n/2), n-1):
            if grid[row][col] != grid[int(n/2)-1-row][col]:
                counter4 += 1
            if grid[row][col] != grid[row][int(n/2)-1-col]:
                counter4 += 1
            if grid[row][col] != grid[int(n/2)-1-row][int(n/2)-1-col]:
                counter4 += 1
    print(counter1, counter2, counter3, counter4)
    return min(counter1, counter2, counter3, counter4)
print(why())

#for i in range(u):
#    task = int(input())
    #do the task and then call why()
