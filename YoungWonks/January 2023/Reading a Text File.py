f = open("/Users/neevgrover/Documents/Python Programs/YoungWonks/January 2023/Reading_Files.txt", "r")
j = f.read()
print(j)
f.close()
f = open("/Users/neevgrover/Documents/Python Programs/YoungWonks/January 2023/Reading_Files.txt", "r")
j = f.readline()
print(j)
f.close()

f = open("/Users/neevgrover/Documents/Python Programs/YoungWonks/January 2023/Reading_Files.txt", "r")
g = open("/Users/neevgrover/Documents/Python Programs/YoungWonks/January 2023/Writing_Files.txt", "w")
for n in f:
    a = n.strip()
    b = a.split()
    d = str(b[0:3])
    print(d.lower())
f.close()
g.close()
f = open("/Users/neevgrover/Documents/Python Programs/YoungWonks/January 2023/Reading_Files.txt", "r")
l = []
for a in f:
    l.append(a)
print(l)