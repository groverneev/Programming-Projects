a, b, c = input().split()
row = int(a)
col = int(b)
mult = int(c)
matrix = []
new = ""
for a in range(row):
    a = input()
    for b in range(len(a)):
        for c in range(mult):
            new = new + a[b]
    matrix.append(new)
    new = ""
for a in range(row):
    for b in range(mult):
        print(matrix[a])