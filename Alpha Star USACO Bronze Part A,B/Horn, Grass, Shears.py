num = int(input())
n = []
for i in range(num):
    test = input().split()
    test[0] = int(test[0])
    test[1] = int(test[1])
    n.append(test)
counter1 = 0
counter2 = 0
counter3 = 0
for j in range(num):
    #1 is Rock, 2 is Paper, 3 is Scissors
    if (n[j][0] == 1 and n[j][1] == 3) or (n[j][0] == 2 and n[j][1] == 1) or (n[j][0] == 3 and n[j][1] == 2):
        counter1 += 1
    #1 is Rock, 3 is Paper, 2 is Scissors
    if (n[j][0] == 1 and n[j][1] == 2) or (n[j][0] == 2 and n[j][1] == 3) or (n[j][0] == 3 and n[j][1] == 1):
        counter2 += 1
    #2 is Rock, 1 is Paper, 3 is Scissors
    if (n[j][0] == 1 and n[j][1] == 2) or (n[j][0] == 2 and n[j][1] == 3) or (n[j][0] == 3 and n[j][1] == 1):
        counter3 += 1
print(max([counter1, counter2, counter3]))