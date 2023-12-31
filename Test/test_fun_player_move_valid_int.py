import copy_project_1Dtictactoe
from copy_project_1Dtictactoe import fun_move_marker
from random import randrange

def test_fun_player_move():
    '''
    Original function: Accepts string of the game board, asks player which position 
    to play, returns updated board.

    Test function: Test to ensure that a correctly chosen 
    position number is correctly reflected on the board after being placed by the 
    function fun_move_marker.
    '''

    board = copy_project_1Dtictactoe.board

    player_mark = "x"
    pos_number = randrange(0, 20) # removed user input, exchanged for a certainly valid random number

    while board[pos_number] != "-": # This while loop checks if position is already occupied.
        pos_number= randrange (0, 20)

    # The function fun_move_marker places the marker.
    updated_board = fun_move_marker(board, pos_number, player_mark) 
    
    # Expected Outcome: After this function is called, the mark at pos_number 
    # on the returned board (updated_board) should be player_mark.
    assert updated_board[pos_number] == player_mark # This tests if the move is reflected on the board correctly.
