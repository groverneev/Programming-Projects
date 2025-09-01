a = input("Enter a string.")
for b in range(len(a)):
    if a[b] == " ":
        print("[Space] is at position", b)
    else:
        print(a[b], "is at position", b)
