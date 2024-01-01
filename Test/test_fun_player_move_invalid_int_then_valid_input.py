from unittest.mock import patch
import copy_project_1Dtictactoe

def test_fun_player_move_invalid_int_then_valid_input():
    '''
    Original function: Accepts string of the game board, asks player which position 
    to play, returns updated board.

    Test function: Mocks the user input first simulating an invalid input 
    and then a valid input, addressing the recursions of fun_player_move.
    '''
    
    board = "--------------------"  # Initial board

    invalid_input_number = "29" # removed user input, exchanged for a certainly invalid number
    valid_input_number = "5" # removed user input, exchanged for a certainly valid number
    
    with patch("builtins.input", side_effect=[invalid_input_number, valid_input_number]): #side_effects simulates both user inputs
        updated_board = copy_project_1Dtictactoe.fun_player_move(board)
        # Expected Outcome: After this function is called, the mark at index 4 (5-1)
        # on the returned board (updated_board) should be player_mark "x".

        assert updated_board == "----x---------------"
        assert len(updated_board) == 20
        # This tests if the move is reflected on the board correctly and if the board still only 
        # 20 possible positions.