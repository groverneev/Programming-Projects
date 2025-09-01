n, m = map(int, input().split())
black = []
brown = []
counter = 0
for i in range(n):
    black.append(input())
for j in range(n):
    brown.append(input())
acounter = 0
ccounter = 0
tcounter = 0
gcounter = 0
aacounter = 0
cccounter = 0
ttcounter = 0
ggcounter = 0
for a in range(m):
    acounter = 0
    ccounter = 0
    tcounter = 0
    gcounter = 0
    aacounter = 0
    cccounter = 0
    ttcounter = 0
    ggcounter = 0
    for b in range(n):
        if black[b][a] == "A":
            acounter += 1
        if black[b][a] == "C":
            ccounter += 1
        if black[b][a] == "T":
            tcounter += 1
        if black[b][a] == "G":
            gcounter += 1
    for b in range(n):
        if brown[b][a] == "A":
            aacounter += 1
        if brown[b][a] == "C":
            cccounter += 1
        if brown[b][a] == "T":
            ttcounter += 1
        if brown[b][a] == "G":
            ggcounter += 1
    if (acounter == 0 or aacounter == 0) and (tcounter == 0 or ttcounter == 0) and (ccounter == 0 or cccounter == 0) and (gcounter == 0 or ggcounter == 0):
        counter += 1
print(counter)