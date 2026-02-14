# https://usaco.org/index.php?page=viewproblem2&cpid=1565

n, q = map(int, input().split()) # n = #deals, q = #queries
deals = list(map(int, input().split()))

for i in range(1, n):
    deals[i] = min(deals[i], 2 * deals[i - 1]) # removes all the bad deals

queries = [int(input()) for i in range(q)]
max_x = max(queries)

sizes = []
prices = []

cur = 1
for i in range(n):
    if cur > max_x * 2:
        break
    sizes.append(cur)
    prices.append(deals[i])
    cur = cur * 2
m = len(sizes)

for x in queries:
    leftover_need = x
    cost = 0
    best = 10**25

    for i in range(m - 1, -1, -1):
        if sizes[i] <= leftover_need:
            counter = leftover_need // sizes[i]
            cost += counter * prices[i]
            leftover_need -= counter * sizes[i]
        if leftover_need > 0:
            best = min(best, cost + prices[i])

    print(min(cost, best))
