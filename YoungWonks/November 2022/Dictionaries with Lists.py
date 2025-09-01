import sys
import random
myDictionary = {"Famous Movies": ["Avengers", "Harry Potter", "Lord of the Rings", "Star Wars"], "Famous TV Shows" : ["Game of Thrones", "The Simpsons", "Friends", "The Office", "The Family Guy"], "Bestselling Novel": ["The Da Vinci Code", "The Little Prince", "Harry Potter", "To Kill a Mockingbird"]}
while True:
    a = input("Enter a category or q to quit.")
    if a == "q":
        print("Thank you for playing!")
        sys.exit()
    print(random.choice(myDictionary[a]))