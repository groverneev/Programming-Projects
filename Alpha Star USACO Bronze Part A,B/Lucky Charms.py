x, y, z = input().split()
l = int(x)
num_charm = int(y)
nail = int(z)
length = []
position = []
for z in range(num_charm):
    x, y = input().split()
    length.append(int(x))
    position.append(int(y))
for z in range(num_charm):
    print(abs(position[z] - nail) + length[z])