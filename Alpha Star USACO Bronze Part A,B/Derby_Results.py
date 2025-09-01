n = int(input())
times = []
for z in range(n):
    x = []
    a, b, c = map(int, input().split())
    x.append(a)
    x.append(b)
    x.append(c)
    times.append(x)
times_2 = {}
count=0
for h,m,s in times:
    times_2[s + m*60 + h*3600] = count
    count+=1

times_2 = dict(sorted(times_2.items(), key= lambda x: x[0]))

ans=[]
for key, value in times_2.items():
    ans.append(times[value])

for a in range(n):
    print(ans[a][0], end = " ")
    print(ans[a][1], end = " ")
    print(ans[a][2])