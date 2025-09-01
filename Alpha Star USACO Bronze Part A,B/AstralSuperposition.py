t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    arr = []
    for _ in range(n):
        t = input()
        u = list(t)
        for v in range(len(u)):
            if u[v] == "W":
                u[v] = 0
            elif u[v] == "G":
                u[v] = 1
            elif u[v] == "B":
                u[v] = 2
        arr.append(u)
    counter = 0
    if a == 0 and b == 0:
        for _ in range(n):
            for __ in range(n):
                if arr[_][__] == 1 or arr[_][__] == 2:
                    counter += 1
        print(counter)









        """
    fp = arr
    sp = arr
    for i in range(n):
        for j in range(a):
            sp[i].pop(0)
    for i in range(b):
        sp.pop(0)
    print(sp)
    """