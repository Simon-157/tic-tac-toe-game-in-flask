# Importing the necessary libraries for the program to run.
import random
import sys
import copy
from constants import EMPTY_GRID, BLANK, O, X


# A global variable that is used to store the maximum value of the integer.
INF = sys.maxsize
n_levels = 0
n_states = 0
n_terminal_states = 0
states = dict()
terminal_states = set()

def minimax_decision(game, state):
    """
    > The minimax_decision function returns the best action for the current state of the game
    
    :param game: the game object
    :param state: the current state of the game
    :return: The best action for the current state.
    """
    global n_levels, n_states, n_terminal_states, states, terminal_states
    n_levels = n_states = n_terminal_states = 0
    states = dict()
    terminal_states = set()
    
    value = -INF
    best_action = BLANK
    actions = game.actions(state)
    if(len(actions) == 9):
        best_action = random.choice(actions)

    else:
        for i in range(len(actions)):
            result_state = game.result(state, actions[i], X)
            statestr = grid_to_str(result_state)
            if statestr in states:
                next_state_value = states[statestr]
            else:
                n_states += 1
                next_state_value = min_value(game,result_state,1)
                states[statestr] = next_state_value
            if (next_state_value > value):
                value = next_state_value
            
                best_action = actions[i]
                print(actions)
        print(best_action)
    return best_action
 


def max_value(game, state, level):
    """
    > For each possible action, find the minimum value of the next state, and return the maximum of
    those values
    
    :param game: the game object
    :param state: the current state of the game
    :param level: the current level of the tree
    :return: The maximum value of the next state.
    """
    
    global n_levels, n_states, n_terminal_states, states
    n_levels = max(n_levels, level)
    if game.terminal_test(state):
        util = game.utility(state)
        #print_grid("Reached terminal state with utility "+str(util)+":",state)
        n_terminal_states += 1
        terminal_states.add(grid_to_str(state))
        return util
    value = -INF
    actions = game.actions(state)
    for action in actions:
        next_state = game.result(state, action, X)
        statestr = grid_to_str(next_state)
        if statestr in states:
            next_state_value = states[statestr]
        else:
            n_states += 1
            next_state_value = min_value(game,next_state,level+1)
            states[grid_to_str(next_state)] = next_state_value
        value = max(value, next_state_value)
    return value



def min_value(game, state, level):
    """
    It returns the minimum utility of all the states that can be reached from the given state, assuming
    that the opponent plays optimally
    :param game: the game object
    :param state: the current state of the game
    :param level: the current level of the tree
    :return: The minimum value of the next state.
    """
    global n_levels, n_states, n_terminal_states, states
    n_levels = max(n_levels, level)
    if game.terminal_test(state):
        util = game.utility(state)
        #print_grid("Reached terminal state with utility "+str(util)+":",state)
        n_terminal_states += 1
        terminal_states.add(grid_to_str(state))
        return util
    value = INF
    actions = game.actions(state)
    for action in actions:
        next_state = game.result(state, action, O)
        statestr = grid_to_str(next_state)
        if statestr in states:
            next_state_value = states[statestr]
        else:
            n_states += 1
            next_state_value = max_value(game,next_state,level+1)
            states[grid_to_str(next_state)] = next_state_value
        value = min(value, next_state_value)
    return value

def grid_to_str(grid):
    """
    It takes a list of lists of strings and returns a string
    :param grid: a list of lists of strings, representing the current state of the game
    :return: A string of the grid
    """
    return "".join(grid[0])+"".join(grid[1])+"".join(grid[2])

