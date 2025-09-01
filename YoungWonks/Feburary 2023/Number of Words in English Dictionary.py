def palindrome(a):
    b = a[0:len(a) - 1]
    if (b[::-1] == b) == True:
        print(b)
a = open("/Users/neevgrover/Documents/Python Programs/YoungWonks/Feburary 2023/English_Dictionary.txt", "r")
counter1 = 0
for b in a:
    counter1 = counter1 + 1
a.close()
myDictionary = {}
for z in range(97, 123):
    a = open("/Users/neevgrover/Documents/Python Programs/YoungWonks/Feburary 2023/English_Dictionary.txt", "r")
    counter = 0
    for b in a:
        if b[0] == chr(z):
            counter = counter + 1
    myDictionary[chr(z)] = counter
    a.close()
print(counter1)
print(myDictionary)

a = input("Enter a letter.")
d = open("/Users/neevgrover/Documents/Python Programs/YoungWonks/Feburary 2023/English_Dictionary.txt", "r")
for c in d:
    if c[0] == a:
        print(c)
d.close()
d = open("/Users/neevgrover/Documents/Python Programs/YoungWonks/Feburary 2023/English_Dictionary.txt", "r")
a = input("Enter another letter.")
for c in d:
    if c[len(c) - 2] == a:
        print(c)
d.close()
b = open("/Users/neevgrover/Documents/Python Programs/YoungWonks/Feburary 2023/English_Dictionary.txt", "r")
for c in b:
    palindrome(c)