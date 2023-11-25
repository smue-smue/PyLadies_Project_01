from random import randrange

board = "--------------------"
player_mark = "x"
computer_mark = "o"
current_mark = None
pos_number = None
rand_number = None
result = None

# STEP 1

def fun_evaluate(board):
    '''Evaluates the status of the game.'''

    if "xxx" in board:
        return "x" # Player won
    elif "ooo" in board:
        return "o" # Computer won
    elif "-" in board:
        return "-" # Rest, game not finished
    else:
        return "!" # Draw

# STEP 2

def fun_move(board, pos_number, current_mark):
    '''Accepts string of the game board, a position number (0-19), and a mark (x or o). /n
    Then returns the updated game board.'''

    list_board = list(board)
    list_board[pos_number] = str(current_mark)
    board = ''.join(list_board)
    return board

# STEP 3

def fun_player_move(current_mark, pos_number, board):
    '''Accepts string of the game board, asks player which position /n 
    to play, returns updated board.'''

    current_mark = player_mark
    print(board)
    pos_number = int(input("Which position you would like to play? "))
    return fun_move(board, pos_number, current_mark)

# STEP 4

def fun_pc_move(current_mark, pos_number, board, rand_number):
    '''Accepts string of the game board, will select position to play, returns the updated board.'''

    current_mark = computer_mark
    rand_number = randrange(0,19)
    while True:
        if board[rand_number] == "-":
            pos_number = rand_number
            break
        else:
            rand_number = randrange(0,19)
    return fun_move(board, pos_number, current_mark)

# STEP 5

def fun_1D_tictactoe(current_mark, pos_number, board, rand_number, result):
    '''Creates string, alternatively calls player_move and pc_move functions until the end of the game.'''
    
    while True:
        result = fun_evaluate(board)
        if result == "-":
            board = fun_player_move(current_mark, pos_number, board)
            board = fun_pc_move(current_mark, pos_number, board, rand_number)
            fun_1D_tictactoe(current_mark, pos_number, board, rand_number, result)
        else:
            print("The game ends. \nThis is the final board:", board, "\n")
        break

# PLAY

#print(board) # prints board
#print(len(board)) # prints board length for checking
#print("Status: ", fun_evaluate(board)) # prints game status

#board = fun_player_move(current_mark, pos_number, board)
#print(board)
#print(len(board)) # prints board length for checking
#print("Status: ", fun_evaluate(board)) # prints game status

#board = fun_pc_move(current_mark, pos_number, board, rand_number)
#print(board)
#print(len(board)) # prints board length for checking
#print("Status: ", fun_evaluate(board)) # prints game status

board = fun_1D_tictactoe(current_mark, pos_number, board, rand_number, result)