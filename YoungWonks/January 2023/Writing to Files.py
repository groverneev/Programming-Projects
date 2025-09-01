import random
f = open("/Users/neevgrover/Documents/Python Programs/YoungWonks/January 2023/Writing_To_Files.txt", "w")
for a in range(10000000):
    f.write(str(random.randint(1, 1000)))
    f.write("\n")
f.close()
total = 0
f = open("/Users/neevgrover/Documents/Python Programs/YoungWonks/January 2023/Writing_To_Files.txt", "r")
for a in f:
    total = total + int(a)
print(total/10000000)