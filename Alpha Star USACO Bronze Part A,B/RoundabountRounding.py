"""
sss = input()
def agree(n):
    n = str(n)
    nn = list(n)
    if int(n) >= 10:
        for _ in range(len(nn)):
            nn[_] = int(nn[_]) #integer list of digits
        for i in range(2, len(nn)):
            nn[i] = 0
        if nn[1] >= 5:
            nn[0] = nn[0] + 1
        nn[1] = 0
        bessy = "s"
        for j in range(len(nn)):
            nn[j] = str(nn[j])
            bessy += nn[j]
        bessy = bessy[1:]
    else:
        if int(n) >= 5:
            bessy = 10
        elif int(n) < 5:
            bessy = 0

    l = len(n)
    elsie = int(n)

    elsie = round(elsie, -(1))
    print(bessy,elsie)
    if elsie == bessy:
        return True
    else:
        return False

c = 0
for t in range(int(sss)):
    if agree(t) == False:
        c += 1
print(c)

"""






























"""



def elsie(n, p):

    for i in range((p)):
        if n == 5 or n == 50 or n == 500 or n == 5000 or n == 50000 or n == 500000:
            n = n + 1
        n = round(n, -(i+1))
        #print(n)
    return n
n = int(input())
c = 0
for i in range(len(str(n))):
    for j in range(n):
        k = j
        if j == 5 or j == 50 or j == 500 or j == 5000 or j == 50000 or j == 500000:
            k = j + 1

        b = round(k, -i)
        e = elsie(j, i)
        print(j, b ,e)
        if b != e:
            c+= 1
            print("hi")

print(c)

"""


def count_different_roundings(T, test_cases):
    results = []
    for N in test_cases:
        count = 0
        for x in range(2, N + 1):
            # Chain rounding
            chain_rounded = x
            power = 10
            while power <= x:
                if (chain_rounded % power) >= (power // 2):
                    chain_rounded = (chain_rounded // power + 1) * power
                else:
                    chain_rounded = (chain_rounded // power) * power
                power *= 10
            
            # Regular rounding directly to the nearest 10^P
            P = 1
            while P <= x:
                P *= 10
            regular_rounded = (x + (P // 2)) // P * P
            
            # Compare the two results
            if chain_rounded != regular_rounded:
                count += 1
        
        results.append(count)
    
    return results

# Testing the function with the sample input from the image
T = 4
test_cases = [1, 100, 4567, 3366]
print(count_different_roundings(T, test_cases))
