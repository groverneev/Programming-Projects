"""s = []
o = []
m = []
e = []
b = []
i = []
g = []
counter = 0
num = int(input())
for ii in range(num):
    aa, bb = input().split()
    bb = int(bb)
    if aa == "S":
        s.append(bb)
    elif aa == "O":
        o.append(bb)
    elif aa == "M":
        m.append(bb)
    elif aa == "E":
        e.append(bb)
    elif aa == "B":
        b.append(bb)
    elif aa == "I":
        i.append(bb)
    elif aa == "G":
        g.append(bb)

for one in range(len(m)):
    for two in range(len(i)):
        for three in range(len(b)):
            for four in range(len(e)):
                for five in range(len(g)):
                    for six in range(len(o)):
                        for seven in range(len(s)):
                            if ((m[one]) * (i[two] + b[three]) * (e[four] + g[five] + o[six] + s[seven]))%2 == 0:
                                counter += 1


print(counter)
"""



s = [0, 0]
o = [0, 0]
m = [0, 0]
e = [0, 0]
b = [0, 0]
i = [0, 0]
g = [0, 0]
counter = 0
num = int(input())
for ii in range(num):
    aa, bb = input().split()
    bb = int(bb)
    if bb%2 == 1:
        bb = 1
    elif bb%2 == 0:
        bb = 0
    if aa == "S":
        s[bb] += 1
    elif aa == "O":
        o[bb] += 1
    elif aa == "M":
        m[bb] += 1
    elif aa == "E":
        e[bb] += 1
    elif aa == "B":
        b[bb] += 1
    elif aa == "I":
        i[bb] += 1
    elif aa == "G":
        g[bb] += 1
print(s)
print(o)
print(m)
print(e)
print(b)
print(i)
print(g)

for one in range(2):
    for two in range(2):
        for three in range(2):
            for four in range(2):
                for five in range(2):
                    for six in range(2):
                        for seven in range(2):
                            #if s[one] != 0 and o[two] != 0 and m[three] != 0 and e[four] != 0 and b[five] != 0 and i[six] != 0 and g[seven] != 0:
                            #    print("hi")
                            #if ((m[one]) * (i[two] + b[three]) * (e[four] + g[five] + o[six] + s[seven]))%2 == 0:
                            #    counter += s[one]*o[two]*m[three]*e[four]*b[five]*i[six]*g[seven]

                            if s[one] != 0 and o[two] != 0 and m[three] != 0 and e[four] != 0 and b[five] != 0 and i[six] != 0 and g[seven] != 0:

                                if ((o[two] + m[three] + o[two]) * (s[one] + i[six] + s[one] + b[five] + e[four] + e[four]) * (e[four] + g[seven] + o[two] + s[one]))%2 == 0:
                                    counter += 1*s[one]*o[two]*m[three]*e[four]*b[five]*i[six]*g[seven]


print(counter)