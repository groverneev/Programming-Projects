names = []
with open("/Users/neevgrover/Documents/Python Programs/Harvard Intro to Python/names.txt", "r") as file:
    # The "r" stands for read
    for line in file:
        #The rstrip method removes the stuff at the end of the thing
        names.append((line.rstrip()))

for name in sorted(names, reverse=True):
    print("hello,", name)