a = int(input("How many times do you want to print the pattern?"))
counter = 0
while counter != a:
    counter = counter + 1
    if counter%2 == 1:
        print("xoxoxo")
    if counter%2 == 0:
        print("oxoxox")
