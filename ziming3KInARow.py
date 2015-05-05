__author__ = 'ziming3'
initial_state = []
k = 0
side = ''
opponent = ''
def prepare(initial_state, k, what_side_I_play, opponent_nick_name):
    glob = globals()
    glob['initial_state'] = initial_state
    glob['k'] = k
    glob['side'] = what_side_I_play
    glob['opponent'] = opponent_nick_name


def introduce():



def nickname():
    return "Shintou Hikaru"


def makeMove(CurrentState, currentRemark, timeLimit=10000):



def staticEval(state):
