myQuiz = {"What is 2 + 2?" : "4", "What is the square root of 25?" : "5", "What is the 5th month of the year?" : "May"}
score = 0
for a in myQuiz:
    b = input(a)
    if b == myQuiz[a]:
        print("You got that question correct!")
        score = score + 1
    else:
        print("You got that question wrong.")
print("Thank you for taking this quiz!")
print("You got", score, "questions correct out of 3 questions total!")