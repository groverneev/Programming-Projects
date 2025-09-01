a, b = input().split()
dist = int(a)
horse = int(b)
for a in range(horse):
    a, b, c = input().split()
    speed = int(a)
    most = int(b)
    rest = int(c)
    distcounter = 0
    timecounter = 0
    final = 0
    while distcounter < dist:
        if timecounter >= most:
            timecounter = 0
            final = final + rest
        else:
            timecounter = timecounter + 1
            distcounter = distcounter + speed
            final = final + 1
    print(final)