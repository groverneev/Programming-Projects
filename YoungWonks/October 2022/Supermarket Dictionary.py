import sys
fruits = {"apple" : "$5", "bannana" : "$2", "cherry" : "$7", "watermellon" : "$9"}
veggies = {"carrots" : "$8", "spinach" : "$6", "broccoli" : "$5"}
myDictionary = {"fruits" : fruits, "veggies" : veggies}
cart = dict()
print(myDictionary)
counter = 0
price = 0
while True:
    a = input("Do you want to purchase an item (p) or check out (c) or view your cart (v) or quit (q)?")
    if a == "q":
        print("Thank you for visiting our supermarket!")
        sys.exit()
    if a == "v":
        print("Here is your cart:", cart)
    if a == "c":
        print("Here is your cart:", cart)
        d = input("Do you want to check out (y/n)?")
        if d == "n":
            print("Ok.")
        if d == "y":
            print("Your items have been successfully checked out!")
            print("You spent", price, "dollars today.")
            print("Thank you for visiting this supermarket! We hope to see you next time!")
            sys.exit()
    if a == "p":
        a = input("What is your category?")
        for b in myDictionary:
            if b == a:
                counter = 1
                break
        if counter == 0:
            print("Sorry, but we do not have that category of items. Please try again.")
        if counter == 1:
            counter = 0
            a = input("What item do you want to buy?")
            for b in fruits:
                if b == a:
                    counter = 1
                    break
            if counter == 1:
                print("That item is in stock! Here is the price:", fruits[a])
                c = input("Do you want to add the item to your cart (y/n)?")
                if c == "n":
                    print("Ok.")
                if c == "y":
                    print("Your item has been successfully added to your cart!")
                    cart[a] = fruits[a]
                    price = price + int(fruits[a])
            if counter == 0:
                print("Sorry, but that item is not currently in stock. Please try again.")
        counter = 0
