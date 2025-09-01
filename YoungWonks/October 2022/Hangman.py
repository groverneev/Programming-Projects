import random
import sys
file1 = open("HangmanWords.txt", "r")
myList = file1.readlines()
word = random.choice(myList)
word = word[:-1]
guess = []
counter = 0
for z in range(len(word)):
    guess.append("_")
for a in range(len(word) + 6):
    print(guess)
    b = input("What is your letter?")
    for c in range(len(word)):
        if b == word[c]:
            guess[c] = b
            counter = counter + 1
    if counter == len(word):
        print("You have won!")
        print("Here is the word:", word)
        print("You have used", a + 1, "lives.")
        sys.exit()
print("You have lost.")
print("Here is the word:", word)
print("You have used", a + 1, "lives.")
#Letters Guessed
#Improve the myList word options
#Do not use lives when you get the letter correct
#Improve the amount of lives given
