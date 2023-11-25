from random import randrange

# DEFINING FUNCTIONS

def fun_evaluate_game_status(board):
    '''Evaluates the status of the game.'''

    if "xxx" in board:
        return "x" # Player won
    elif "ooo" in board:
        return "o" # Computer won
    elif "-" in board:
        return "-" # Rest, game not finished
    else:
        return "!" # Draw

def fun_move_marker(board, pos_number, current_mark):
    '''Accepts string of the game board, a position number (0-19), and a mark (x or o).
    Then returns the updated game board.'''

    list_board = list(board)
    list_board[pos_number] = str(current_mark)
    board = ''.join(list_board)
    return board

def fun_player_move(board):
    '''Accepts string of the game board, asks player which position 
    to play, returns updated board.'''

    player_mark = "x"
    current_mark = player_mark
    print("\n", board)
    input_number = input("Which position from 1 to 20 you would like to play? ") # Options 1-20 easier to understand

    try:
        int_input_number = int(input_number) - 1 # correcting index position
    
    except:
        int_input_number = "no integer"
        print("Please enter a number between 1 and 20, not a word.") 
        return fun_player_move(board)

    if int_input_number >= 0 and int_input_number <= 19:
        if board[int_input_number] == "-":
            pos_number = int_input_number
        else:
            int_input_number = None
            print("This position is not free, please choose another one.")
            return fun_player_move(board)
    else:
        print("Please enter a number between 1 and 20.")
        return fun_player_move(board)
    
    return fun_move_marker(board, pos_number, current_mark)

def fun_computer_move(board):
    '''Accepts string of the game board, will select position to play, 
    returns the updated board.'''

    computer_mark = "o"
    current_mark = computer_mark
    rand_number = randrange(0, 19)
    while True:
        if board[rand_number] == "-":
            pos_number = rand_number
            break
        else:
            rand_number = randrange(0,19)
    
    return fun_move_marker(board, pos_number, current_mark)

def fun_1D_tictactoe(board):
    '''Creates string, alternatively calls player_move and computer_move 
    functions until the end of the game.'''

    result = fun_evaluate_game_status(board)
    while True:
        if result == "-":
            board = fun_player_move(board)
            result = fun_evaluate_game_status(board)
            if result == "-":
                board = fun_computer_move(board)
                result = fun_evaluate_game_status(board)
            else: 
                print("\nCongratulations, you won. \nThis is the final board:", board, "\n")
                break
        else:
            print("\nComputer won. \nThis is the final board:", board, "\n")
            break

# PLAY GAME

board = "--------------------"
fun_1D_tictactoe(board)