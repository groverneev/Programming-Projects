import os
a = input("Enter a filename.")
exists = os.path.isfile(a)
if exists == False:
    print("Your filename does not exist.")
else:
    print("Your filename exists.")