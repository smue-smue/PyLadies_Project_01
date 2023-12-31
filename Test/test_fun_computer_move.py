import copy_project_1Dtictactoe
from copy_project_1Dtictactoe import fun_move_marker
from random import randrange

def test_fun_computer_move():
    '''
    Original function: Accepts string of the game board, 
    will select position to play, returns the updated board.

    Test function: Test to ensure that the randomly chosen 
    position is correctly reflected on the board.
    '''

    board = copy_project_1Dtictactoe.board

    computer_mark = "o"
    pos_number = randrange(0, 20)
    while board[pos_number] != "-": # This while loop checks if position is already occupied.
        pos_number = randrange(0, 20)

    updated_board = fun_move_marker(board, pos_number, computer_mark)

    assert updated_board[pos_number] == computer_mark # This tests if the move is reflected on the board correctly.

