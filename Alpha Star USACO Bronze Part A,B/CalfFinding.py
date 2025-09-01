import sys
x, y = map(int, input().split())
move = 1
counter = 0
position1 = 0
position2 = x
while True:
    position1 = x + move
    if y > x and position1 >= y:
        print(counter + abs(y - position2))
        sys.exit()
    counter += abs(position1 - position2)
    move *= 2
    position2 = x - move
    if y < x and position2 <= y:
        print(counter + abs(y - position1))
        sys.exit()
    counter += abs(position1 - position2)
    move *= 2