import sys
player1 = input("What is player 1's name?")
player2 = input("What is player 2's name?")
row1 = ["1", "2", "3"]
row2 = ["4", "5", '6']
row3 = ["7", "8", "9"]
def print_board():
    print(row1)
    print(row2)
    print(row3)
print_board()
row1 = ["-", "-", "-"]
row2 = ["-", "-", '-']
row3 = ["-", "-", "-"]
def sysexit(z):
    print_board()
    if z == "X":
        print(player1, "won!")
        sys.exit()
    if z == "O":
        print(player2, "won!")
        sys.exit()
def game_over(xo):
    if row1[0] == xo and row1[1] == xo and row1[2] == xo:
        sysexit(xo)
    if row2[0] == xo and row2[1] == xo and row2[2] == xo:
        sysexit(xo)
    if row3[0] == xo and row3[1] == xo and row3[2] == xo:
        sysexit(xo)
    if row1[0] == xo and row2[0] == xo and row3[0] == xo:
        sysexit(xo)
    if row1[1] == xo and row2[1] == xo and row3[1] == xo:
        sysexit(xo)
    if row1[2] == xo and row2[2] == xo and row3[2] == xo:
        sysexit(xo)
    if row1[0] == xo and row2[1] == xo and row3[2] == xo:
        sysexit(xo)
    if row1[2] == xo and row2[1] == xo and row3[0] == xo:
        sysexit(xo)
def if_statement(a, b):
    if b == 1:
        row1[0] = a
        game_over(a)
    if b == 2:
        row1[1] = a
        game_over(a)
    if b == 3:
        row1[2] = a
        game_over(a)
    if b == 4:
        row2[0] = a
        game_over(a)
    if b == 5:
        row2[1] = a
        game_over(a)
    if b == 6:
        row2[2] = a
        game_over(a)
    if b == 7:
        row3[0] = a
        game_over(a)
    if b == 8:
        row3[1] = a
        game_over(a)
    if b == 9:
        row3[2] = a
        game_over(a)
for a in range(4):
    print(player1, end = "")
    b = int(input(", enter a number from 1 - 9:"))
    if_statement("X", b)
    print_board()
    print(player2, end = "")
    b = int(input(", enter a number from 1 - 9:"))
    if_statement("O", b)
    print_board()
print(player1, end = "")
b = int(input(", enter a number from 1 - 9:"))
if_statement("X", b)
print_board()
print("The game is a draw.")