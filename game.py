import sys
import copy
from constants import EMPTY_GRID, BLANK, O, X


INF = sys.maxsize

class Game:
    def __init__(self, init_state):
        self.init_state = init_state

    def __str__(self):
        return "Init_state="+str(self.init_state)

    # placeholder, to be overridden in derived class
    def terminal_test(self, state):
        return True 

    # placeholder, to be overriden in derived class
    def utility(self, state):
        return 0 

    # placeholder, to be overriden in derived class
    def actions(self, state):
        moves = []
        return moves

    # placeholder, to be overriden in derived class
    def result(self, state, action):
        return state


class TicTacToe(Game):
    def __init__(self):
        super().__init__(copy.deepcopy(EMPTY_GRID))
        self.player = "x"

    def terminal_test(self, state):
        # if there is no empty space then it's a terminal state
        if not (BLANK in state[0] or
                BLANK in state[1] or
                BLANK in state[2]):
            return True

        # otherwise, if there's a winner, it's a terminal state
        winner = self.winner(state)
        return winner == X or winner == O

    def winner(self, state):
        # check each row for a winning configuration
        for row in [0, 1, 2]:
            if (state[row][0] != BLANK and
                state[row][0] == state[row][1] and
                state[row][0] == state[row][2]):
                return state[row][0]

        # check each column for a winner configuration
        for col in [0, 1, 2]:
            if (state[0][col] != BLANK and
                state[0][col] == state[1][col] and
                state[0][col] == state[2][col]):
                return state[0][col]

        # check the top left to bottom right diagonal
        if (state[0][0] != BLANK and
            state[0][0] == state[1][1] and
            state[0][0] == state[2][2]):
            return state[0][0]
        
        # check the bottom left to top right diagonal
        if (state[2][0] != BLANK and
            state[2][0] == state[1][1] and
            state[2][0] == state[0][2]):
            return state[2][0]

        return BLANK

    def utility(self, state):
        winner = self.winner(state)
        if winner == X:
            return 1
        elif winner == O:
            return -1
        else:
            return 0
        
    def actions(self, state):
        moves = []
        for row in [0, 1, 2]:
            for col in [0, 1, 2]:
                if state[row][col] == BLANK:
                    moves.append((row,col))
        return moves

    def result(self, state, action, player):
        res_state = copy.deepcopy(state)
        res_state[action[0]][action[1]] = player
        return res_state