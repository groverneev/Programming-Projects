import sys
t, n = map(int, input().split())
positions = []
for z in range(n):
    positions.append(int(input()))
current_time = 0
current_picked = 0
new_pos = 0
while current_time < t:
    minimum = 999999998999999999
    min_index = 0
    for i in range(len(positions)):
        if abs(positions[i]) < abs(minimum):
            minimum = positions[i]
            index=i
    current_time = current_time + abs(minimum - new_pos)
    if current_time > t:
        print(current_picked)
        sys.exit()
    new_pos = minimum
    current_picked = current_picked + 1
    del positions[index]
print(current_picked)