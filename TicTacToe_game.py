#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Initialize the game board
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

# Function to print the board
def print_board(board):
    for row in range(3):
        print(" %c | %c | %c " % (board[row][0], board[row][1], board[row][2]))
        if row < 2:
            print("---|---|---")

# Function to check for a win
def check_win(board, player):
    # Check rows and columns
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Function to make a move
def make_move(board, player):
    while True:
        try:
            move = int(input(f'{player}, where do you want to play? (1-9): '))
            if move < 1 or move > 9:
                print("Invalid move. Please choose a number between 1 and 9.")
                continue

            row, col = divmod(move - 1, 3)
            if board[row][col] != " ":
                print("This position is already taken. Try again.")
            else:
                board[row][col] = player
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

# Main game loop
def play_game():
    turn = 0
    while True:
        player = 'X' if turn % 2 == 0 else 'O'
        print_board(board)
        make_move(board, player)
        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        if turn == 8:  # All 9 cells are filled
            print_board(board)
            print("It's a tie!")
            break
        turn += 1


# In[ ]:


# Start the game
play_game()

