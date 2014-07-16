"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided
#import user34_Uc9ea2tRiN_0 as t
# Constants for Monte Carlo simulator
# Change as desired
NTRIALS = 100 # Number of trials to run
MCMATCH = 1.0 # Score for squares played by the machine player
MCOTHER = 1.0 # Score for squares played by the other player
#score = provided.TTTBoard(3)

# Add your functions here.
def is_empty(board):
    """
type:Boolean
a function return True if grid is Empty else False
"""
    for _row in range(board.get_dim()):
        for _col in range(board.get_dim()):
            if board.square(_row,_col) != provided.EMPTY:
                return False
    return True

#def get_player(board,player,rotate=False):
# """
# type:None
# a function return a list of player grid
# """
# if not rotate:
# return [[(_row,_col) for _col in range(board.get_dim()) if board.square(_row,_col) == player]
# for _row in range(board.get_dim())]
# else:
# return [[(_row,_col) for _row in range(board.get_dim()) if board.square(_row,_col) == player]
# for _col in range(board.get_dim())]

def mc_trial(board, player):
    """
This function takes a current board and the next player
to move. The function should play a game starting with
the given player by making random moves,
alternating between players
"""
    #play = random.choice([provided.PLAYERO,provided.PLAYERX])
    play = player
    while board.check_win() is None:
        move = random.choice(board.get_empty_squares())
        #print move
        board.move(move[0],move[1],play)
        play = provided.switch_player(play)
    #while board.check_win():
    # pass
    return board

def mc_update_scores(scores, board, player):
    """
This function takes a grid of scores (a list of lists)
with the same dimensions as the Tic-Tac-Toe board,
a board from a completed game, and which player the
machine player is. The function should score the
completed board and update the scores grid
"""
    # Score for squares played by the machine player
    score = (0,0)
    if board.check_win() == provided.PLAYERX:
        score = (MCMATCH,-MCOTHER)
    elif board.check_win() == provided.PLAYERO:
        score = (-MCMATCH,MCOTHER)
        
    _dic_score = {provided.PLAYERX : score[0],
                  provided.PLAYERO : score[1],
                  provided.EMPTY : 0.0}
    
    _clone = [[ _dic_score[board.square(_row,_col)] for _col in range(board.get_dim())]
     for _row in range(board.get_dim())]
    for _row in range(len(_clone)):
        for _col in range(len(_clone)):
            scores[_row][_col] += _clone[_row][_col]
    return scores

def get_best_move(board, scores):
    """
This function takes a current board and a grid of scores.
The function should find all of the empty squares with
the maximum score and randomly return one of them as a
(row, column) tuple. It is an error to call this function
with a board that has no empty squares (there is no possible next move)
"""
    _sets = set([])
    _sets.add(board.get_empty_squares()[0])
    best = scores[0][0]
    for _index in board.get_empty_squares():
        if best < scores[_index[0]][_index[1]]:
            _sets.pop()
            _sets.add(_index)
            best = scores[_index[0]][_index[1]]
    return _sets.pop()

def mc_move(board, player, trials):
    """
his function takes a current board, which player the
machine player is, and the number of trials to run.
The function should use the Monte Carlo simulation described above to
return a move for the machine player in the form of a (row, column) tuple
"""
    _index = 0
    _dim = board.get_dim()
    _scores = [[0]*_dim for _index in range(_dim)]
    #return random.choice(board.get_empty_squares())
    while _index < trials:
        _index +=1
        _boards = mc_trial(board.clone(), player)
        mc_update_scores(_scores,_boards, player)
        
    return get_best_move(board,_scores)
    
#import user35_ofAHGrBJ3a_2 as wopr

#wopr.test_mc_move(mc_move)
            
    
        
# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

#provided.play_game(mc_move, NTRIALS, False)
#poc_ttt_gui.run_gui(4, provided.PLAYERX, mc_move, NTRIALS, False)
#mc_trial(board,random.choice([provided.PLAYERO,provided.PLAYERX]))
#print get_best_move(provided.TTTBoard(2, False, [[provided.EMPTY, provided.EMPTY], [provided.EMPTY, provided.EMPTY]]),
# [[0, 0], [3, 0]])
#print get_best_move(provided.TTTBoard(3, False, [[provided.EMPTY,provided.EMPTY, provided.EMPTY], [provided.EMPTY,provided.EMPTY, provided.EMPTY],[provided.EMPTY,provided.EMPTY, provided.EMPTY]]), [[1, 2, 3], [7, 8, 9], [4, 5, 6]])
#print mc_update_scores([[0, 0, 0], [0, 0, 0], [0, 0, 0]], provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO],
# [provided.PLAYERO, provided.PLAYERX, provided.EMPTY],
# [provided.EMPTY, provided.PLAYERX, provided.PLAYERO]]), 2)
#t.test_update_scores(mc_update_scores,MCMATCH,MCOTHER)
#mc_update_scores([[0, 0, 0], [0, 0, 0], [0, 0, 0]], provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.PLAYERO, provided.PLAYERX, provided.EMPTY], [provided.EMPTY, provided.PLAYERX, provided.PLAYERO]]), 2)
#score = provided.TTTBoard(3, False,
# [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO],
# [provided.PLAYERO, provided.PLAYERX, provided.EMPTY],
# [provided.EMPTY, provided.EMPTY, provided.PLAYERO]])
#print "E",getPlayer(score,provided.EMPTY)
#print "O",getPlayer(score,provided.PLAYERO)
#print "X",getPlayer(score,provided.PLAYERX)
#print score

