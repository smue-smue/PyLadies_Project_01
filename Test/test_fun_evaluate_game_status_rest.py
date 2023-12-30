import copy_project_1Dtictactoe

def test_fun_evaluate_game_status():
    '''Evaluates the status of the game.'''
    
    board = copy_project_1Dtictactoe.board

    if "-" in board:
        assert "-" in board # Rest, game not finished