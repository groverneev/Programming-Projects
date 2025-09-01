import random
a = input("Enter a sentence.").split()
random.shuffle(a)
print(a[len(a) - 1])
