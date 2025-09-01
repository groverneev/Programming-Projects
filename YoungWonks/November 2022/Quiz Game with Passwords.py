import sys
counter = 0
momQuiz = {"What is 2 + 2?" : "4", "What is the square root of 25?" : "5", "What is the 5th month of the year?" : "May"}
dadQuiz = {"What is 2 + 3?" : "5", "What is the 6th month of the year?" : "June"}
myDictionary = {"Sandeep" : "dad1", "Pallavi" : "mom2"}
while True:
    a = input("Enter a username (or q to quit).")
    z = a
    if a == "q":
        print("Thank you for playing!")
        sys.exit()
    for b in myDictionary:
        if a == b:
            counter = 1
    if counter == 0:
        print("No username found. Please try again.")
    if counter == 1:
        counter = 0
        b = input("What is your password?")
        if b == myDictionary[a]:
            print("You have successfully logged into", a, end = "")
            print("'s account!")
            print("Here is your quiz:")
            if z == "Sandeep":
                print(dadQuiz)
                score = 0
                for a in dadQuiz:
                    b = input(a)
                    if b == dadQuiz[a]:
                        print("You got that question correct!")
                        score = score + 1
                    else:
                        print("You got that question wrong.")
                print("Thank you for taking this quiz!")
                print("You got", score, "questions correct out of 2 questions total!")
            if z == "Pallavi":
                print(momQuiz)
                score = 0
                for a in momQuiz:
                    b = input(a)
                    if b == momQuiz[a]:
                        print("You got that question correct!")
                        score = score + 1
                    else:
                        print("You got that question wrong.")
                print("Thank you for taking this quiz!")
                print("You got", score, "questions correct out of 3 questions total!")
        else:
            print("Your password was incorrect. Please try agian.")