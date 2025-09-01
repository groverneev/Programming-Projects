a = int(input("Enter a number."))
b = input("Do you want binary, hexadecimal, or octal representation?")
if b == "b":
    a = bin(a)
if b == "h":
    a = hex(a)
if b == "o":
    a = oct(a)
print(a)
