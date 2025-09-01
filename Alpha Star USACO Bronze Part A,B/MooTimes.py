m = 7
b = 7
e = 7
counter = 0
num = int(input())
instructions = []
for i in range(num):
    test1, test2, test3 = input().split()
    instructions.append([int(test1), test2, int(test3)])
instructions = sorted(instructions, key=lambda x: x[0])
curr_winn = ["m", "b", "e"]
for i in range(num):
    thing = 0
    test = instructions[i]
    if test[1] == "Mildred":
        m += test[2]
    if test[1] == "Bessie":
        b += test[2]
    if test[1] == "Elsie":
        e += test[2]
    prev_winner = curr_winn
    if m == b and b == e:
        curr_winn = ["m", "b", "e"]
    if m == b and b > e:
        curr_winn = ["m", "b"]
    if m == e and e > b:
        curr_winn = ["m", "e"]
    if e == b and b > m:
        curr_winn = ["b", "e"]
    if e > b and e > m:
        curr_winn = ["e"]
    if b > e and b > m:
        curr_winn = ["b"]
    if m > b and m > e:
        curr_winn = ["m"]
    if prev_winner != curr_winn:
        counter += 1
print(counter)