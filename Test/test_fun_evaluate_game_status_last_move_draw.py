from copy_project_1Dtictactoe import fun_evaluate_game_status

def test_fun_evaluate_game_status_last_move_draw():
    '''Evaluates if the game recognizes a draw.'''

    # Last move results in a draw
    board_last_move_draw = "xoxoxoxoxoxoxoxoxoxo"
    assert fun_evaluate_game_status(board_last_move_draw) == "!"
