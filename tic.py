import random

board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

current_player = "X"
winner = None
game_running = True

#board
def print_board(board):
    print(board[0] +  " | " + board[1] +  " | " + board[2])
    print("---------")
    print(board[3] +  " | " + board[4] +  " | " + board[5])
    print("---------")
    print(board[6] +  " | " + board[7] +  " | " + board[8])

#take input
def player_input(board):
    move = int(input("enter a number 1-9: "))
    if move >= 1 and move <= 9 and board[move-1] == "-":
        board[move-1] = current_player
    else:
        print("error")

#check win condition
def check_winner(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    elif board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    elif board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    else:
        return False
    
#check tie condition
def check_tie(board):
    global game_running
    if "-" not in board:
        print_board(board)
        print("it is a tie")
        game_running = False

#switch

def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"



def computer(board):
    while current_player == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switch_player()

#check

def result(board):
    if check_winner:
        print(f"winner is {winner}")

while game_running:
    print_board(board)
    player_input(board)
    check_winner(board)
    check_tie(board)
    result(board)
    switch_player()
    computer(board)
    player_input(board)
    check_winner(board)
    result(board)