import time
from random import randint

hi = 0
wi = 0
forbid = []
k = 0
side = ''
opponent = ''
zobristnum = []
rows = []
cols = []
lslant = []
rslant = []

def prepare(initial_state, k, what_side_I_play, opponent_nick_name):
    glob = globals()
    glob['k'] = k
    glob['side'] = what_side_I_play
    glob['opponent'] = opponent_nick_name
    board = initial_state[0]
    global hi, wi, forbid, rows, cols, lslant, rslant
    hi = len(board)
    wi = len(board[0])
    for i in range(hi):
        for j in range(wi):
            if i == "-":
                forbid.append((i, j))
    zinit()
    if k <= wi:
        for i in range(hi):
            '''
            for l in range(wi - k + 1):
                rows.append((i, l))'''
            rows.append((i, 0))
    if k <= hi:
        for i in range(wi):
            '''
            for l in range(hi - k + 1):
                cols.append((l, i))'''
            cols.append((0, i))
    if k <= wi and k <= hi:
        '''
        for i in range(hi - k + 1):
            for l in range(wi - k + 1):
                lslant.append(i, l)
        for i in range(hi - k + 1):
            for l in range(wi - k, wi):
                rslant.append(i, l)'''
        for i in range(hi - k + 1):
            lslant.append((i, 0))
            rslant.append((i, wi - 1))
        for i in range(wi - k + 1):
            lslant.append((0, i))
        for i in range(wi - k, wi):
            rslant.append((0, i))
    return "OK"

def other(thisSide):
    if thisSide == 'X':
        return 'O'
    else:
        return 'X'
        
def zinit():
    global zobristnum, hi, wi
    zobristnum = [[[0] * 2] * wi] * hi
    for i in range(hi):
        for j in range(wi):
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
    for successors in range():
        return ''
    return provisional


def makeMove(CurrentState, currentRemark, timeLimit=10000):
    currentSide = CurrentState[1]
    uttererance = ""

    result = [[], ]
    return result


def staticEval(state):
    global hi, wi, side, k, rows, cols, lslant, rslant
    board = state[0]
    score = 0
    check = False
    cur = 0
    mine = [0] * k
    oppo = [0] * k
    for i in rows:
        row = board[i[0]]
        mycount = 0
        opcount = 0
        maxmine = 0
        maxoppo = 0
        for j in range(wi):
            if row[j] == side:
                mycount += 1
                if maxoppo < opcount:
                    maxoppo = opcount
                opcount = 0
            else:
                opcount += 1
                if maxmine < mycount:
                    maxmine = mycount
                mycount = 0


def count(list, side):
    first = list.index(side)
    opp = other(side)



def other(side):
    if side == "X":
        return "O"
    elif side == "O":
        return "X"
    else:
        raise Exception("Illegal argument for function other()")
