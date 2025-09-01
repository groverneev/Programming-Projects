import random
import sys
words = ["apple", "bannana", "strawberry", "mango", "carrots"]
a = random.choice(words)
counter = []
lives = 1
for b in range(len(a)):
    counter.append(a[b])
random.shuffle(counter)
print("Here are your words:", words)
print("Here are your letters:", counter)
print("What word do these letters make?")
while True:
    c = input()
    if c == a:
        print("You guessed correctly!")
        print("You took", lives, "tries to guess the word!")
        sys.exit()
    if c != a:
        print("Try again.")
        lives = lives + 1
