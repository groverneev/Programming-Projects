"""Coin Flipping
[ Memory: 16 MB, CPU: 1 sec ]

Bessie likes laying out her 𝑁2
 coins in a N x N square grid arrangement (1 <= N <= 10), with all heads facing up. Unfortunately, when she lays her coins out randomly, some coins are flipped over as tails. 

Bessie has large hooves, so she can only flip over coins from the "top-left rectangle" of her coin grid, -- a rectangular sub-grid that contains the top-left coin. This way, she can flip all the coins from heads to tails or vice versa

Bessie thinks she will be able to flip all the coins to heads, and wants you to help her find the minimum number of flips she needs to do.

Note that flipping over the same rectangle twice is pointless, because the coins would return to their original side. Consider flipping each top-left rectangle at most once.

INPUT FORMAT

The first line of the input is the integer N.

Each of the N lines that follow contains a string of N characters, each either 0 (representing heads) or 1 (representing tails).

OUTPUT FORMAT

Please output the minimum number of times Bessie needs to flip coins to obtain a grid of coins facing heads up.

SAMPLE INPUT

4
0001
0001
0111
1111
SAMPLE OUTPUT

4
In this example, if Bessie flips over the entire grid of coins from the top-left hand corner, she obtains an arrangement like this: 

1110
1110
1000
0000
Then, if she flips over the top-left 2×3
 rectangle, she gets

0000
0000
1000
0000
Then. if she flips over the top-left 3×1
 rectangle, she gets

1000
1000
0000
0000
All that remains is for Bessie to flip the top-left rectangle containing the two 1s, and she is finished. She takes a total of four flips for this method.

"""

n = int(input())
coins = []
counter = 0
for i in range(n):
    myArray = []
    myVar = input()
    for zed in range(n):
        myArray.append(int(myVar[zed]))
    coins.append(myArray)
for x in range(n-1, -1, -1):
    for y in range(n-1, -1, -1):
        if coins[x][y] == 1:
            counter = counter + 1
            for a in range(x, -1, -1):
                for b in range(y, -1, -1):
                    if coins[a][b] == 0:
                        coins[a][b] = 1
                    else:

                        coins[a][b] = 0
print(counter)