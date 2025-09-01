import sys
myDictionary = {1 : "", 2 : "", 3 : "", 4 : "", 5 : "", 6 : "", 7 : "", 8 : "", 9 : ""}
counter = 2
def aaa():
    print("1:", myDictionary[1], "2:", myDictionary[2], "3:", myDictionary[3])
    print("4:", myDictionary[4], "5:", myDictionary[5], "6:", myDictionary[6])
    print("7:", myDictionary[7], "8:", myDictionary[8], "9:", myDictionary[9])
aaa()
def done():
    print("Player X Won!")
    aaa()
    sys.exit()
def check(letter):
    if myDictionary[1] == letter and myDictionary[2] == letter and myDictionary[3] == letter:
        done()
    if myDictionary[4] == letter and myDictionary[5] == letter and myDictionary[6] == letter:
        done()
    if myDictionary[7] == letter and myDictionary[8] == letter and myDictionary[9] == letter:
        done()
    if myDictionary[1] == letter and myDictionary[4] == letter and myDictionary[7] == letter:
        done()
    if myDictionary[2] == letter and myDictionary[5] == letter and myDictionary[8] == letter:
        done()
    if myDictionary[3] == letter and myDictionary[6] == letter and myDictionary[9] == letter:
        done()
    if myDictionary[1] == letter and myDictionary[5] == letter and myDictionary[9] == letter:
        done()
    if myDictionary[3] == letter and myDictionary[5] == letter and myDictionary[7] == letter:
        done()
while True:
    a = int(input("Enter a number between 1 and 9."))
    if myDictionary[a] == "X" or myDictionary[a] == "O":
        print("Sorry, that space is aldready taken. Please try again.")
    else:
        if counter%2 == 0:
            myDictionary[a] = "X"
        else:
            myDictionary[a] = "O"
        counter = counter + 1
        check("X")
        check("O")
        aaa()
    if myDictionary[1] != "":
        if myDictionary[2] != "":
            if myDictionary[3] != "":
                if myDictionary[4] != "":
                    if myDictionary[5] != "":
                        if myDictionary[6] != "":
                            if myDictionary[7] != "":
                                if myDictionary[8] != "":
                                    if myDictionary[9] != "":
                                        print("The game is a draw.")
                                        sys.exit()