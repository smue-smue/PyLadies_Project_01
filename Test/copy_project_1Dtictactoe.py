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
    input_number = input("Which position from 1 to 20 you would like to play? ") # Options 1-20, easier to understand

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
    rand_number = randrange(0, 20)
    while True:
        if board[rand_number] == "-":
            pos_number = rand_number
            break
        else:
            rand_number = randrange(0, 20)
    
    return fun_move_marker(board, pos_number, current_mark)

def fun_1D_tictactoe(board):
    '''Creates string, alternatively calls player_move and computer_move 
    functions until the end of the game.'''

    result = fun_evaluate_game_status(board)
    while True:
        if result == "!":
            print("\nIt's a draw. \nThis is the final board:", board, "\n")
            break
        elif result == "-":
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

if __name__ == "__main__":
    fun_1D_tictactoe(board)

################################# HOMEWORK #################################
    
# 1. What is a Python module and how does it differ from a Python package?
    # A module is a file containing pre-written code like Python definitions, functions, variables. 
    # Basically every file saved with the ending .py serves as a module, but it only is useful as such if it 
    # contains the right definitions or statements needed by other scripts. 
    # You can use your pre-written custom modules or modules from the pre-installed standard library 
    # through the import statement. Your custom modules have to be stored in the same directory as the scripts 
    # that want to make use of the module, those of the standard library can be accessed automatically.
    # A package is a collection of related modules under a common namespace, that you use to make your code more organized. 
    # Packages can be part of a Library.A library can contain multiple packages and modules.

# 2. What are side effects and give some examples.
    # A side effect happens every time your script interacts with the outside, such as reading user input, 
    # printing something to the screen, writing to a file or modifying given arguments. 
    # Unlike in everyday language, side effects can be intentional and often are an essential part of the script. 
    # It is important though to ensure that the script is behaving as intended and that there are built-in exceptions 
    # to know how to handle wrong user input. Scripts with side effects are harder to test than so-called 
    # “pure functions” which only return a result and have no interaction with the outside.

# 3. What are Exceptions and what to do if third-party code that we use throws them?
    # In everyday language we use the term exception for something that does not follow the usual rules, 
    # in programming it is used as a term for the mechanism of handling those (expected) unexpected situations or errors 
    # through causing a disruption (the Exception). There is a difference in “Errors” and “Exceptions”. 
    # Errors are a broad term for any issues that cause unintentional behavior but not all Exceptions are Errors per se, 
    # but rather a condition that disrupts the script and can be handled.  If an Exception is raised in the script but it 
    # is not handled (like through an try except block), the script will be terminated and a traceback will be printed to 
    # the console with information about the specific Exception that should be handled for the script to run like intended.
    # If third-party code throws Exceptions, we should try to catch and handle them.
    
# 4. Using which keywords can you create, throw and catch your new custom Exception?
    # The keyword "class" is used to create a custom Exception as subclass from the built-in Exception class.
    # The keyword "raise" is used for throwing, meaning triggering, the Exception.
    # The keywords "try" and "except" are used to catch the Exception.

# 5. Give examples of some benefits of testing?
    # Finding unexpected behaviors in code that needs handling with Exceptions.
    # Finding Errors that can't be handled with Exceptions and need to be fixed.

################################# HOMEWORK #################################