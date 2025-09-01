import random
hours1 = random.randint(1, 24)
minutes1 = random.randint(1, 59)
seconds1 = random.randint(1, 59)
hours2 = random.randint(1, 24)
minutes2 = random.randint(1, 59)
seconds2 = random.randint(1, 59)
final1 = 3600*hours1 + 60*minutes1 + seconds1
final2 = 3600*hours2 + 60*minutes2 + seconds2
print(abs(final1 - final2))
