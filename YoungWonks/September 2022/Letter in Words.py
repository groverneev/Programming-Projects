words = ["apple", "bannana", "strawberry", "mango", "carrots"]
letter = input("Enter a letter.")
counter1 = 0
for a in range(5):
    for b in range(len(words[a])):
        counter = words[a]
        if counter[b] == letter:
            counter1 = 1
            break
    if counter1 == 1:
        print(counter)
        counter1 = 0
