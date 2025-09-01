import re
email = input("What's your email?").strip().lower()
if re.search(r"^[a-z0-9_.+-]+@[a-z0-9-]+\.[a-z]{2,6}$", email):
    print("Valid")
else:
    print("Invalid")