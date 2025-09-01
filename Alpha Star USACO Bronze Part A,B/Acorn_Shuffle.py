n = int(input())
instructions = input().split()
for i in range(len(instructions)):
    instructions[i] = int(instructions[i])
id = input().split()
for i in range(len(id)):
    id[i] = int(id[i])
id2 = []
for a in range(3):
    for b in range(n):
        id2.append(id[instructions[b] - 1])
    id = id2
    id2 = []
for b in range(len(id)):
    print(id[b])