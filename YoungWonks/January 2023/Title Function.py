a = input("Enter a string with weird capatalization.").split()
for b in range(len(a)):
    print(a[b].title(), end = " ")