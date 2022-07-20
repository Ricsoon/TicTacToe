import random

print("Tic Tac Toe - The Game")
print("You will play against the computer!!")

print("See the board below")
print("_ _ _")
print("_ _ _")
print("_ _ _")

print("Choose a number from 1 to 9 to make your move")
print("1 2 3")
print("4 5 6")
print("7 8 9")

def show_board(board):
    print("The board status is \n")

    for index in range(len(board)):
        print(board[index], end=" ")
        if index == 2 or index == 5 or index == 8:
            print("")

def verify_board(board, player):
    # checking the board lines
    if board[0] == player and board[1] == player and board[2] == player:
        if player == "X":
            return 1
        else:
            return 2
    if board[3] == player and board[4] == player and board[5] == player:
        if player == "X":
            return 1
        else:
            return 2
    if board[6] == player and board[7] == player and board[8] == player:
        if player == "X":
            return 1
        else:
            return 2
    
    # checking the board columns
    if board[0] == player and board[3] == player and board[6] == player:
        if player == "X":
            return 1
        else:
            return 2
    if board[1] == player and board[4] == player and board[7] == player:
        if player == "X":
            return 1
        else:
            return 2
    if board[2] == player and board[5] == player and board[8] == player:
        if player == "X":
            return 1
        else:
            return 2
    
    # checking the diagonals of the board
    if board[0] == player and board[4] == player and board[8] == player:
        if player == "X":
            return 1
        else:
            return 2
    if board[2] == player and board[4] == player and board[6] == player:
        if player == "X":
            return 1
        else:
            return 2
    return 0

pick_numbers = 0

board = ["_"] * 9

while True:
    pick = int(input("Which is your choice?"))

    while board[pick-1] != "_":
        print("invalid move. Look at the board again.")
        show_board(board)
        pick = int(input("Which is your choice?"))
    
    board[pick-1] = "X"
    pick_numbers +=1

    winner = verify_board(board,"X")

    if winner != 0:
        break
    
    if pick_numbers == 9:
        break

    show_board(board)

    computer_choice = random.randint(1,9)
    while board[computer_choice-1] != "_":
        computer_choice = random.randint(1,9)

    board[computer_choice-1] = "O"
    pick_numbers += 1

    winner = verify_board(board, "O")
    if winner != 0:
        break
    show_board(board)

if winner == 1:
    print("Congratz, you won!!")
elif winner == 2:
    print("You lose, computer wins")
else:
    print("Draw!!")

show_board(board)