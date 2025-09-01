# Horn beats Shears
# Shears beats Grass
# Grass beats Horn

counter = 0
myCounter = []

def myFunction():
    global counter
    for i in range(n):
        x = array[i]
        if x[0] == h and x[1] == s:
            counter = counter + 1
        if x[0] == g and x[1] == h:
            counter = counter + 1
        if x[0] == s and x[1] == g:
            counter = counter + 1
    myCounter.append(counter)
    counter = 0

n = int(input())
array = []

for hi in range(n):
    bob = input().split()
    bob[0] = int(bob[0])
    bob[1] = int(bob[1])
    array.append(bob)

h = 1
s = 2
g = 3
myFunction()
h = 1
g = 2
s = 3
myFunction()
s = 1
g = 2
h = 3
myFunction()
s = 1
h = 2
g = 3
myFunction()
g = 1
h = 2
s = 3
myFunction()
g = 1
s = 2
h = 3
myFunction()
print(max(myCounter))