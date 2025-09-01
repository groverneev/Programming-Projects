def animals(a):
    counter = 0
    wild = ["lion", "cheetah"]
    domestic = ["cat", "dog"]
    for z in range(2):
        if a == wild[z]:
            counter = 1
    if counter == 1:
        print("Your animal is wild.")
    else:
        print("Your animal is domestic.")
animals(input("What is your animal?"))