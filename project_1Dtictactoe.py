board = "--------------------"
player_mark = "x"
computer_mark = "o"
current_mark = None
pos_number = None

# STEP 1

def fun_evaluate(b):
    '''Evaluates the status of the game.'''
    if "xxx" in b:
        return "x" # Player won
    elif "ooo" in b:
        return "o" # Computer won
    elif "-" in b:
        return "-" # Rest, game not finished
    else:
        return "!" # Draw



# STEP 2 # !!! TRACEBACK weil str item assignment ist nicht möglich, muss in Liste verwandeln !!!

def fun_move(b, c, d):
    '''Accepts the strings of the game board, a position number (0-19), and a mark (x or o). Then returns the updated game board.'''
    b[c] = str(d)
    return board

# PLAY

print(board) # prints board
print(len(board)) # prints board length for checking
print("Status: ", fun_evaluate(board)) # prints game status

current_mark = "x" # ACHTUNG hard copy
pos_number = int("4") # ACHTUNG hard copy
board = fun_move(board, pos_number, current_mark)

print(board) # prints board
print(len(board)) # prints board length for checking
print("Status: ", fun_evaluate(board)) # prints game status

