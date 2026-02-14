# https://usaco.org/index.php?page=viewproblem2&cpid=1563

t, k = map(int, input().split())
for i in range(t):  # ::1
    n = int(input())
    output = ""
    flip = False
    str = input()
    print("YES")
    if k == 1:
        for i in range(len(str) - 1, -1, -1):
            character = True # O = false and M = true
            if (str[i] == "O"):
                character = False
            if (flip == True):
                character = not character
            if character == True:
                output += "M"
            else:
                output += "O"
                flip = not flip
        print(output[::-1])
