import sys
a, b = input().split()
row = int(a)
col = int(b)
counter = 0
counter2 = 1
while True:
    if row % 2 == 1 and col % 2 == 1:
        counter = counter + counter2
        counter2 = counter2 * 4
        row = int(row/2)
        col = int(col/2)
    else:
        print(counter)
        sys.exit()