from copy import deepcopy
from minimax.minimax import MiniMax


def heuristic(state):
    X2 = 0
    X1 = 0
    O1 = 0
    O2 = 0

    for row in range(0, 3):
        if state[row][0] == state[row][1] == state[row][2]:
            if state[row][0] == 'X':
                return 15
            else:
                return -15
        # check same columns
    for column in range(0, 3):
        if state[0][column] == state[1][column] == state[2][column]:
            if state[0][column] == 'X':
                return 15
            else:
                return -15

        # check two diagnols
    if state[0][0] == state[1][1] == state[2][2]:
        if state[0][0] == 'X':
            return 15
        else:
            return -15

    if state[0][2] == state[1][1] == state[2][0]:
        if state[0][2] == 'X':
            return 15
        else:
            return -15


    # check for 2 consecutive Xs
    for i in range(0, 3):
        if state[i][0] == state[i][1] == 'X' and state[i][2] == '':
            X2 += 1
        elif state[i][1] == state[i][2] == 'X' and state[i][0] == '':
            X2 += 1
        elif state[i][0] == state[i][2] == 'X' and state[i][1] == '':
            X2 += 1
    for j in range(0, 3):
        if state[0][j] == state[1][j] == 'X' and state[2][j] == '':
            X2 += 1
        elif state[0][j] == state[2][j] == 'X' and state[1][j] == '':
            X2 += 1
        elif state[2][j] == state[1][j] == 'X' and state[0][j] == '':
            X2 += 1
    if state[0][0] == state[1][1] == 'X' and state[2][2] == '':
        X2 += 1
    elif state[0][0] == state[2][2] == 'X' and state[1][1] == '':
        X2 += 1
    elif state[2][2] == state[1][1] == 'X' and state[0][0] == '':
        X2 += 1
    if state[2][0] == state[1][1] == 'X' and state[0][2] == '':
        X2 += 1
    elif state[2][0] == state[0][2] == 'X' and state[1][1] == '':
        X2 += 1
    elif state[0][2] == state[1][1] == 'X' and state[2][0] == '':
        X2 += 1

    # check for single Xs
    for i in range(0, 3):
        if state[i][0] == state[i][1] == '' and state[i][2] == 'X':
            X1 += 1
        elif state[i][1] == state[i][2] == '' and state[i][0] == 'X':
            X1 += 1
        elif state[i][0] == state[i][2] == '' and state[i][1] == 'X':
            X1 += 1
    for j in range(0, 3):
        if state[0][j] == state[1][j] == '' and state[2][j] == 'X':
            X1 += 1
        elif state[0][j] == state[2][j] == '' and state[1][j] == 'X':
            X1 += 1
        elif state[2][j] == state[1][j] == '' and state[0][j] == 'X':
            X1 += 1
    if state[0][0] == state[1][1] == '' and state[2][2] == 'X':
        X1 += 1
    elif state[0][0] == state[2][2] == '' and state[1][1] == 'X':
        X1 += 1
    elif state[2][2] == state[1][1] == '' and state[0][0] == 'X':
        X1 += 1
    if state[2][0] == state[1][1] == '' and state[0][2] == 'X':
        X1 += 1
    elif state[2][0] == state[0][2] == '' and state[1][1] == 'X':
        X1 += 1
    elif state[0][2] == state[1][1] == '' and state[2][0] == 'X':
        X1 += 1

    # check for double Os
    for i in range(0, 3):
        if state[i][0] == state[i][1] == 'O' and state[i][2] == '':
            O2 += 1
        elif state[i][1] == state[i][2] == 'O' and state[i][0] == '':
            O2 += 1
        elif state[i][0] == state[i][2] == 'O' and state[i][1] == '':
            O2 += 1
    for j in range(0, 3):
        if state[0][j] == state[1][j] == 'O' and state[2][j] == '':
            O2 += 1
        elif state[0][j] == state[2][j] == 'O' and state[1][j] == '':
            O2 += 1
        elif state[2][j] == state[1][j] == 'O' and state[0][j] == '':
            O2 += 1
    if state[0][0] == state[1][1] == 'O' and state[2][2] == '':
        O2 += 1
    elif state[0][0] == state[2][2] == 'O' and state[1][1] == '':
        O2 += 1
    elif state[2][2] == state[1][1] == 'O' and state[0][0] == '':
        O2 += 1
    if state[2][0] == state[1][1] == 'O' and state[0][2] == '':
        O2 += 1
    elif state[2][0] == state[0][2] == 'O' and state[1][1] == '':
        O2 += 1
    elif state[0][2] == state[1][1] == 'O' and state[2][0] == '':
        O2 += 1

    # check for single Os
    for i in range(0, 3):
        if state[i][0] == state[i][1] == '' and state[i][2] == 'O':
            O1 += 1
        elif state[i][1] == state[i][2] == '' and state[i][0] == 'O':
            O1 += 1
        elif state[i][0] == state[i][2] == '' and state[i][1] == 'O':
            O1 += 1
    for j in range(0, 3):
        if state[0][j] == state[1][j] == '' and state[2][j] == 'O':
            O1 += 1
        elif state[0][j] == state[2][j] == '' and state[1][j] == 'O':
            O1 += 1
        elif state[2][j] == state[1][j] == '' and state[0][j] == 'O':
            O1 += 1
    if state[0][0] == state[1][1] == '' and state[2][2] == 'O':
        O1 += 1
    elif state[0][0] == state[2][2] == '' and state[1][1] == 'O':
        O1 += 1
    elif state[2][2] == state[1][1] == '' and state[0][0] == 'O':
        O1 += 1
    if state[2][0] == state[1][1] == '' and state[0][2] == 'O':
        O1 += 1
    elif state[2][0] == state[0][2] == '' and state[1][1] == 'O':
        O1 += 1
    elif state[0][2] == state[1][1] == '' and state[2][0] == 'O':
        O1 += 1
    return 3 * X2 + X1 - (3 * O2 + O1)   


def is_terminal(state):

    moves = ['X', 'O']

    for move in moves:
        # check same rows
        for row in range(0, 3):
            if state[row][0] == state[row][1] == state[row][2] == move:
                return True
        # check same columns
        for column in range(0, 3):
            if state[0][column] == state[1][column] == state[2][column] == move:
                return True
        # check two diagnols
        if state[0][0] == state[1][1] == state[2][2] == move:
            return True
        if state[0][2] == state[1][1] == state[2][0] == move:
            return True

    for i in range(0, 3):
        for j in range(0, 3):
            if state[i][j] == '':
                return False
    return True


def get_next_states(state, is_maximizing):
    expanded_nodes = []
    for i in range(0, 3):
        for j in range(0, 3):
            if state[i][j] == '':
                next_state = deepcopy(state)
                if is_maximizing:
                    next_state[i][j] = 'X'
                else:
                    next_state[i][j] = 'O'
                expanded_nodes.append(next_state)
    return expanded_nodes


if __name__ == '__main__':
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    max_depth = 3

    minimax = MiniMax()

    best_move, best_value = minimax.solve(board, max_depth, True, heuristic, is_terminal, get_next_states)

    print(best_move)
    print(best_value)