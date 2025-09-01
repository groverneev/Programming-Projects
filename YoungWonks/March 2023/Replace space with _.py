a = open("/Users/neevgrover/Documents/Python Programs/YoungWonks/March 2023/replace_space.txt", "r+")
b = a.read()
b = list(b)
counter = 0
for x in b:
    if x == " ":
        b[counter] = "•"
    counter = counter + 1
d = "".join(b)
a.write(d)