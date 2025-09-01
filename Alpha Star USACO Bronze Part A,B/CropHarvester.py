x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
if ((x3 <= x1 and x4 >= x2) and (y4 >= y2 or y3 <= y1)) or ((y3 <= y1 and y4 >= y2) and (x4 >= x2 or x3 <= x1)):
    if x4 >= x2 and x3 <= x1 and y4 >= y2 and y3 <= y1:
        print(0)
    else:
        if x3 >= x1 and x4 >= x2 and y4 >= y2 and y3 <= y1:
            print(abs(x3-x1)*abs(y2-y1))
        if x3 <= x1 and x4 <= x2 and y4 >= y2 and y3 <= y1:
            print(abs(x2-x4)*abs(y2-y1))
        if x3 <= x1 and x4 >= x2 and y4 >= y2 and y3 >= y1:
            print(abs(x2-x1)*abs(y3-y1))
        if x3 >= x1 and x4 >= x2 and y4 <= y2 and y3 >= y1:
            print(abs(x3-x1)*abs(y2-y4))
else:
    print(abs(x2-x1)*abs(y2-y1))