from random import randint

hi = 0
wi = 0
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
    global hi, wi
    hi = len(initial_state[0])
    wi = len(initial_state[0][0])
    board = initial_state[0]
    blank = 0
    for row in board:
        for i in row:
            if i != "-":
                blank += 1
    zinit(blank)
    return "OK"


def zinit(blank):
    global zobristnum
    zobristnum = [[0] * 2] * blank
    for i in range(blank):
        for j in range(2):
            zobristnum[i][j] = randint(0, 4294967296)


def zhash(s, blank):
    global zobristnum
    val = 0
    for i in range(blank):
        piece = None
        if s[i] == "X" : piece = 0
        if s[i] == "O" : piece = 1
        if piece != None:
            val ^= zobristnum[i][piece]
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


def makeMove(CurrentState, currentRemark, timeLimit=10000):



def staticEval(state):

