a = int(input("How long do you want your fibonacci tringle to be?"))
close_number = 0
far_number = 0
current = 0
for b in range(a):
    for c in range(b + 1):
        if c == 1:
            far_number = far_number + 1
        current = close_number + far_number
        print(current, end = " ")
        far_number = close_number
        close_number = current
    print("")
    current = 0
    close_number = 0
    far_number = 0
