n, m = map(int, input().split())

cowheights = list(map(int, input().split()))
candyheights = list(map(int, input().split()))

for i in range(m):
    grounddist = 0
    for j in range(n):
        if cowheights[j] - grounddist > 0:
            new = cowheights[j] - grounddist
            if candyheights[i] - new <= 0:
                cowheights[j] = cowheights[j] + candyheights[i]
                candyheights[i] = 0
                grounddist = grounddist + new
            else:
                cowheights[j] = cowheights[j] + new
                candyheights[i] = candyheights[i] - new
                grounddist = grounddist + new
for i in range(n):
    print(cowheights[i])