N, M = map(int, input().split())
clue = []
for f in range(N):
    test = input()
    s = []
    for j in range(M):
        s.append(test[j])
    clue.append(s)
    s = []

counter = 0
for i in range(len(clue)):
    for j in range(len(clue[0])):
        if clue[i][j] == ".":
            if i + 2 < N:
                if i != 0:
                    if clue[i-1][j] == "#":
                        if clue[i + 1][j] == "." or clue[i + 1][j] == "!":
                            if clue[i + 2][j] == "." or clue[i + 2][j] == "!":
                                clue[i][j] = "!"
                                counter = counter + 1

                if i == 0:
                    if clue[i + 1][j] == "." or clue[i + 1][j] == "!":
                        if clue[i + 2][j] == "." or clue[i + 2][j] == "!":
                            clue[i][j] = "!"
                            counter = counter + 1


        if clue[i][j] == ".":
            if j + 2 < M:
                if j != 0:
                    if clue[i][j - 1] == "#":
                        if clue[i][j + 1] == "." or clue[i][j + 1] == "!":
                            if clue[i][j + 2] == "." or clue[i][j + 2] == "!":
                                clue[i][j] = "!"
                                counter = counter + 1

                if j == 0:
                    if clue[i][j + 1] == "." or clue[i][j + 1] == "!":
                        if clue[i][j + 2] == "." or clue[i][j + 2] == "!":
                            clue[i][j] = "!"
                            counter = counter + 1
print(counter)
for a in range(N):
    for b in range(M):
        if clue[a][b] == "!":
            print(a + 1, end = " ")
            print(b + 1)