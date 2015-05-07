import time
from random import randint, choice
import copy

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
winRemarkList = ["I win, you lose", "Let's have another round", "Don't give up. Try Again."]
prewinRemarkList = ["Attentation! I am going to win.", "Be Cautious!", "Do think twice before you move"]
normalRemarkList = ["I still need more practice. ", "I can beat you. ", "I will never give up. ", "If I lose, I will come back. "]
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
    Hi, My name is Shindou Hikaru, I am a sim Go player.
    I am from anime "Hikaru no go", I am very good at Go,
    and I am certainly sure I will be good at K-In-a-Row game.
    My creators are Ziming Guo, UWNetID: ziming3
    and Weiyou Dai, UWNetID: weiyou16
    '''


def nickname():
    return "Shindou Hikaru"

def successors(state, whoseMove):
    board = state[0]
    stateList = []
    for Rows in range(hi):
        for Cols in range(wi):
            if board[Rows][Cols] == ' ':
                tempBoard = copy.deepcopy(board)
                tempBoard[Rows][Cols] = whoseMove
                newState = [tempBoard, other(whoseMove)]
                stateList.append(newState)
    return stateList


def minimax(state, whichSide, timeLimit, timeStart, playLeft):
    if (time.time() - timeStart >= timeLimit * 0.9): return [staticEval(state), state]
    nextState = []
    if (playLeft == 0): return [staticEval(state), state]
    if whichSide == side: provisional = -900000000
    else: provisional = 900000000
    for everyState in successors(state, whichSide):
        everyResult = minimax(everyState, other(whichSide), timeLimit, timeStart, playLeft - 1)
        newVal = everyResult[0]
        if (whichSide == side and newVal > provisional) or (whichSide == other(side) and newVal < provisional):
            provisional = newVal
            nextState = everyState
    return [provisional, nextState]


def makeMove(CurrentState, currentRemark, timeLimit=10000):
    timeWhenStart = time.time()
    values = minimax(CurrentState, CurrentState[1], timeLimit, timeWhenStart, 2)
    newState = values[1]
    score = values[0]
    if (score > 950):
        newRemark = choice(winRemarkList)
    elif (score > 800 and score <= 950):
        newRemark = choice(prewinRemarkList)
    elif (score <= 800 and score > 100):
        newRemark = choice(normalRemarkList)
    uttererance = ""
    for row in range(hi):
        for col in range(wi):
            if CurrentState[0][row][col] != newState[0][row][col]:
                addedrow = row
                addedcol = col
                break
        else:
            continue
        break
    move = "At (" + str(addedrow) + ", " + str(addedcol) + ") place an " + side
    result = [[move, newState], newRemark]
    return result


def staticEval(state):
    global hi, wi, side, k, rows, cols, lslant, rslant
    board = state[0]
    score = 0
    mine = [0] * k
    oppo = [0] * k
    for i in rows:
        row = board[i[0]]
        count(row, mine, oppo)
    for i in cols:
        col = []
        for j in range(hi):
            col.append(board[j][i[1]])
        count(col, mine, oppo)
    for i in lslant:
        diag = []
        while True:
            try:
                diag.append(board[i[0]+1][i[1]+1])
            except:
                break
        count(diag, mine, oppo)
    for i in rslant:
        diag = []
        while True:
            try:
                diag.append(board[i[0]+1][i[1]-1])
            except:
                break
        count(diag, mine, oppo)
    for i in range(k):
        score += 10 ** i * (mine[i] - oppo[i])
    return score


def count(list, mine, oppo):
    oppside = other(side)
    mycount = 0
    opcount = 0
    maxmine = 0
    maxoppo = 0
    for j in range(len(list)):
        if list[j] == side:
            mycount += 1
            if maxoppo < opcount:
                maxoppo = opcount
            opcount = 0
        elif list[j] == oppside:
            opcount += 1
            if maxmine < mycount:
                maxmine = mycount
            mycount = 0
    for i in range(maxmine):
        mine[i] += 1
    for i in range(maxoppo):
        oppo[i] += 1


def other(side):
    if side == "X":
        return "O"
    elif side == "O":
        return "X"
    else:
        raise Exception("Illegal argument for function other()")