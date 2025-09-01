people = int(input())
row = []
col = []
for i in range(people):
    r, c = input().split()
    r = int(r)
    c = int(c)
    row.append(r)
    col.append(c)
def distance(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2
max = 0
person1 = 0
person2 = 0
for i in range(people):
    for j in range(i + 1, people):
        a = distance(row[i], col[i], row[j], col[j])
        if a > max:
            max = a
            person1 = i
            person2 = j
print(person1 + 1, person2 + 1)