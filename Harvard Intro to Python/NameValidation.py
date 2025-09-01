import re
name = input("Please enter your first and last name?").strip()
if re.search(r"[a-zA-Z+] [a-zA-zN+]", name):
    print("Hello,", name, end = "")
    print("!")
else:
    print("Please enter a valid first and last name.")