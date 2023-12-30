import copy_project_1Dtictactoe

def test_fun_evaluate_game_status():
    '''Evaluates the status of the game.'''
    
    board = copy_project_1Dtictactoe.board

    if "xxx" in board:
        assert "x" in board # Player won
    elif "ooo" in board:
        assert "o"in board # Computer won
    elif "-" in board:
        assert "-" in board # Rest, game not finished
    else:
        assert "-" not in board and "xxx" not in board and "ooo" not in board # Draw
    
