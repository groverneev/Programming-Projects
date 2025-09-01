"""

Acorn Stockpile
[ Memory: 16 MB, CPU: 1 sec ]

Harry the squirrel is storing N (N <= 1000) acorns for winter. He likes his acorns to be similar in size, so he will not include two acorns if their size difference is more than X (he will keep them if the difference is equal to X). Given X, calculate the maximum number of acorns that Harry can store in his nest. 

INPUT FORMAT

The first line of the input file contains N and X (0 <= X <= 10,000). The next N lines each contain an integer giving the size of one of the acorns. All sizes are positive and not bigger than 10,000.

OUTPUT FORMAT

Output a single positive integer that indicates the maximum number of acorns that Harry will have in his nest for winter. 

SAMPLE INPUT

6 2
2
6
3
4
1
4
SAMPLE OUTPUT
4
Harry can store at most 4 acorns with the sizes 2, 3, 4, 4. In this case notice that the size difference is at most 2.

"""

n, x = input().split()
n = int(n)
x = int(x)
acorns = []
myArray = []
myVar = 0
myVar2 = 0
myArray2 = []
for hi in range(n):
    acorns.append(int(input()))
for i in range(n):
    test = acorns[i]
    for j in range(n):
        if test + x >= acorns[j] and test + x <= acorns[j] + x:
            myVar = myVar + 1
            #print(test + x, acorns[j])
        elif test - x <= acorns[j] and test - x >= acorns[j] - x:
            myVar2 = myVar2 + 1
            #print(test - x, acorns[j])
    myArray.append(myVar)
    myArray2.append(myVar2)
    myVar = 0
    myVar2 = 0
#print(myArray)
a = max(myArray)
b = max(myArray2)
if a > b:
    print(a)
if b > a:
    print(b)
if b == a:
    print(b)
#print(myArray)
#print(myArray2)