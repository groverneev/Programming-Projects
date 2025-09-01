a = open("/Users/neevgrover/Documents/Python Programs/YoungWonks/Feburary 2023/Source_File.txt", "r")
c = open("/Users/neevgrover/Documents/Python Programs/YoungWonks/Feburary 2023/Destination_File.txt", "w")
for z in a:
    d = z.split()
    e = str(d[0].upper())
    f = str(d[1].upper())
    g = e + f + "\n"
    c.write(g)