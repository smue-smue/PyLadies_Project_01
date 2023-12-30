import copy_project_1Dtictactoe

def test_fun_evaluate_game_status():
    '''Evaluates the status of the game.'''
    
    board = copy_project_1Dtictactoe.board

    if "xxx" in board:
        assert "x" in board # Player won
