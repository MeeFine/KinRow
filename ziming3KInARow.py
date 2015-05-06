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

    return "OK"

def introduce():
    return '''
    Hi, My name is Shintou Hikaru, I am a sim Go player.
    I am from anime "Hikaru no go", I am very good at Go,
    and I am certainly sure I will be good at K-In-a-Row game.
    My creators are Ziming Guo, UWNetID: ziming3
    and Weiyou Dai, UWNetID: weiyou16
    '''


def nickname():
    return "Shintou Hikaru"


def makeMove(CurrentState, currentRemark, timeLimit=10000):

    result = [[], ]
    return result


def staticEval(state):

