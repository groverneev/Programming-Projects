def calc_area(array):
    top = array[0][1]
    floor = array[0][1]
    left = array[0][0]
    right = array[0][0]
    for i in range(len(array)):
        if array[i][1] >= top:
            top = array[i][1]
        if array[i][1] <= floor:
            floor = array[i][1]
        if array[i][0] <= left:
            left = array[i][0]
        if array[i][0] >= right:
            right = array[i][0]
    return (top-floor)*(right-left)
n = int(input())
arr = []
for i in range(n):
    a = input().split()
    a[0] = int(a[0])
    a[1] = int(a[1])
    arr.append(a)
arr1 = arr.copy()
arr2 = arr.copy()
arr3 = arr.copy()
arr4 = arr.copy()
arr1.remove(max(arr1, key=lambda x: x[0]))
arr2.remove(min(arr2, key=lambda x: x[0]))
arr3.remove(max(arr3, key=lambda x: x[1]))
arr4.remove(min(arr4, key=lambda x: x[1]))
area1 = calc_area(arr1)
area2 = calc_area(arr2)
area3 = calc_area(arr3)
area4 = calc_area(arr4)
print(min(area1, area2, area3, area4))