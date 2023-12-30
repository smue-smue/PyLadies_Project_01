import copy_project_1Dtictactoe

def test_fun_evaluate_game_status():
    '''Evaluates the status of the game.'''
    
    board = copy_project_1Dtictactoe.board

    if "-" not in board and "xxx" not in board and "ooo" not in board:
        assert "-" not in board and "xxx" not in board and "ooo" not in board # Draw