import random

def play_tic_tac_toe():
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]

    current_player = "X"
    winner = None
    game_running = True

    # Print the board
    def print_board():
        print(board[0] + " | " + board[1] + " | " + board[2])
        print("---------")
        print(board[3] + " | " + board[4] + " | " + board[5])
        print("---------")
        print(board[6] + " | " + board[7] + " | " + board[8])
        print()

    # Take input from the player
    def player_input():
        while True:
            move = int(input("Enter a number 1-9: "))
            if move >= 1 and move <= 9 and board[move - 1] == "-":
                board[move - 1] = current_player
                break
            else:
                print("Invalid move. Try again.")

    # Check the win condition
    def check_winner():
        nonlocal winner
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

    # Check the tie condition
    def check_tie():
        nonlocal game_running
        if "-" not in board:
            print_board()
            print("It's a tie!")
            game_running = False

    # Switch players
    def switch_player():
        nonlocal current_player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    # Computer's move
    def computer():
        if game_running and current_player == "O":
            while True:
                position = random.randint(0, 8)
                if board[position] == "-":
                    board[position] = "O"
                    check_winner()  # Check for a winner after the computer's move
                    switch_player()
                    break

    # Print the result
    def result():
        if winner:
            print(f"Winner is {winner}!")
        else:
            print("It's a tie!")

    # Main game loop
    while game_running:
        print_board()
        player_input()
        check_winner()
        if winner:
            print_board()
            result()
            break
        check_tie()
        if not game_running:
            print_board()
            result()
            break
        switch_player()
        computer()
        check_winner()
        if winner:
            print_board()
            result()
            break
        check_tie()
        if not game_running:
            print_board()
            result()
            break
    # Ask the player to restart
    play_again = input("Do you want to play again? (Y/N): ")
    if play_again.lower() != "y":
        return

    play_tic_tac_toe()


if __name__ == "__main__":
    play_tic_tac_toe()
