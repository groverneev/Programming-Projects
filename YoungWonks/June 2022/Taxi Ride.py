import time
d = int(input("How far would you like to go in km?"))
s = int(input("How fast would you like to go in km/hour?"))
t = d/s
t = t*3600
print("Now driving...")
time.sleep(t)
print("We've reached the destination.")
