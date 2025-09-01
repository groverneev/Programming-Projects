questions = open("/Users/neevgrover/Documents/Python Programs/YoungWonks/Feburary 2023/Questions.txt", "r")
answers = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
score = open("/Users/neevgrover/Documents/Python Programs/YoungWonks/Feburary 2023/Score.txt", "r")
for z in score:
    highscore = z
score.close()
score = open("/Users/neevgrover/Documents/Python Programs/YoungWonks/Feburary 2023/Score.txt", "w")
counter = 0
scorecounter = 0
for b in questions:
    print(b)
    c = int(input())
    if answers[counter] == c:
        print("Your answer is correct!")
        scorecounter = scorecounter + 1
    else:
        print("Your answer is wrong.")
        print("The correct answer is", answers[counter])
    counter = counter + 1
print("You got", scorecounter, "questions correct!")
scorecounter = int(scorecounter)
highscore = int(highscore)
if highscore == scorecounter:
    print("Your score is equal to the current high score!")
if highscore < scorecounter:
    print("You made a new high score! The previous high score is only", highscore, "but your score is", scorecounter, end = "")
    print("!")
    highscore = scorecounter
    score.write(str(highscore))
if highscore > scorecounter:
    print("The high score is", highscore, end = "")
    print(", however your score is only", scorecounter, end = "")
    print(".")
questions.close()
score.close()