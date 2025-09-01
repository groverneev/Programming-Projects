import math
n = int(input())
answer = 0
z = int(math.sqrt(n) + 1)
for a in range(z):
    for b in range(z):
        for c in range(z):
            x = n - ((a*a) + (b*b) + (c*c))
            if x >= 0:
                d = int(math.sqrt(x))
                if (a*a + b*b + c*c + d*d) == n:
                    answer = answer + 1
print(answer)



#Old Inneficient Method:
"""
import math
n = int(input())
answer = 0
z = int(math.sqrt(n) + 1)
for a in range(z):
    for b in range(z):
        for c in range(z):
            for d in range(z):
                if (a*a) + (b*b) + (c*c) + (d*d) == n:
                    answer = answer + 1
print(answer)
"""