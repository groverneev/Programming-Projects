matrix = []
rc = input().split()
row = int(rc[0])
col = int(rc[1])
puddle = 0
for i in range(row):
    matrix.append(list(input()))
for r in range(row):
    for c in range(col):
        if matrix[r][c] == "#":
            puddle = puddle + 1
            if c != col - 1:
                if matrix[r][c + 1] == "#":
                    matrix[r][c + 1] = '1'
            if r != row-1:
                if matrix[r + 1][c] == "#":
                    matrix[r + 1][c] = '1'
print(puddle)