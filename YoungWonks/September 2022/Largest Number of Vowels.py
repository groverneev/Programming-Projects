largest = "hi"
large_counter = -22
counter = 0
a = input("Enter a list of words.").split()
for b in range(len(a)):
    c = a[b]
    for d in range(len(c)):
        if c[d] == "A" or c[d] == "a" or c[d] == "E" or c[d] == "e" or c[d] == "I" or c[d] == "i" or c[d] == "O" or c[d] == "o" or c[d] == "U" or c[d] == "u":
            counter = counter + 1
    if counter > large_counter:
        large_counter = counter
        largest = c
    counter = 0
print(largest)
