import time
from random import randint

hi = 0
wi = 0
forbid = []
k = 0
side = ''
opponent = ''
zobristnum = []
def prepare(initial_state, k, what_side_I_play, opponent_nick_name):
    global zobristnum
    glob = globals()
    glob['k'] = k
    glob['side'] = what_side_I_play
    glob['opponent'] = opponent_nick_name
    board = initial_state[0]
    global hi, wi, forbid
    hi = len(board)
    wi = len(board[0])
    for i in range(hi):
        for j in range(wi):
            if i == "-":
                forbid.append((i, j))
    zinit()
    return "OK"


def zinit():
    global zobristnum, hi, wi, forbid
    zobristnum = [[[0] * 2] * wi] * hi
    for i in range(hi):
        for j in range(wi):
            if (i, j) not in forbid:
                for k in range(2):
                    zobristnum[i][j][k] = randint(0, 4294967296)


def zhash(board):
    global zobristnum, hi, wi, forbid
    val = 0
    for i in range(hi):
        for j in range(wi):
            if (i, j) not in forbid:
                piece = None
                if board[i][j] == "X" : piece = 0
                if board[i][j] == "O" : piece = 1
                if piece != None:
                    val ^= zobristnum[i][j][piece]
    return val


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

def minimax(board, whichSide, playLeft):

def makeMove(CurrentState, currentRemark, timeLimit=10000):
    currentSide = CurrentState[1]
    uttererance = ""

    result = [[], ]
    return result


def staticEval(state):
    board = state[0]
    result = 0
    numberRow = len(board)
    numberCol = len(board[0])
    for i in range(numberRow):





