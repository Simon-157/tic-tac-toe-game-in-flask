# Importing the necessary modules.
from copy import deepcopy
from game import TicTacToe
from minimaxalgo import minimax_decision
from constants import EMPTY_GRID, O, X
from constants import BLANK

def read_grid(prompt, grid):
    """
    It reads a 3x3 grid of numbers from the user and stores them in the grid parameter
    
    :param prompt: The prompt to display to the user
    :param grid: a 3x3 list of lists
    """
    print(prompt)
    for row in range(3):
        vals = input()
        grid[row] = vals.split()


def print_grid(title,grid):
    """
    It prints the grid in a nice format.
    :param title: The title of the grid
    :param grid: a list of lists of strings
    """
    print(title)
    for row in [0, 1, 2]:
        for col in [0, 1, 2]:
            print(grid[row][col],end = " ")
        print()


def validate_input():
    """
    It asks the user to enter a row and column number, and then it checks to make sure that the row and
    column number are valid. 
    If the row and column number are valid, then it returns the row and column number. 
    If the row and column number are not valid, then it asks the user to enter a row and column number
    again.
    :return: the row and col that the player entered.
    """
    flag = True
    while flag ==True:
        ans = input("Enter the row and col to play: ")
        rowStr, colStr = ans.split()
        row, col = int(rowStr), int(colStr)
        print("Player entered ", row, col)
        if row <= 2 and col <= 2:
            flag = False
        else:
            print("You entered a wrong position!! try again")
            
    return row, col


def play_with_comp():
    """
    It's a function that plays a game of tic-tac-toe against the computer. 
    The computer is the X player and the human is the O player. 
    The computer uses the minimax algorithm to decide its next move. 
    The human player can choose to play first or second. 
    The human player can choose to play again or not. 
    The human player can choose to play against the computer or against another human. 
    
    """
    game = TicTacToe()
    test_again = "Y"
    grid = deepcopy(EMPTY_GRID)
    # grid = main_screen()
    global player
    print_grid("Current game board:", grid )
    print("\n" + "-" *50)
    start = input("Do you want to play first: ")
    if start == "Y" or start == "y":
        player = O
    else:
        player = X
    while (not game.terminal_test(grid)):
        print("Current player is",player)
        
        if player == X:
           comp_ans =  minimax_decision(game, grid)
           row, col = comp_ans[0], comp_ans[1]
           print("Computer chosed ", row, col)
           if (grid[row][col] == BLANK):
                grid[row][col] = player
                player = O
                print_grid("Current game board:", grid )

        elif player == O:
            choice = validate_input()
            row, col = choice[0], choice[1]
            if (grid[row][col] == BLANK):
                grid[row][col] = player
                player = X
                print_grid("Current game board:", grid )


# Checking if the game is over and if it is, it prints the winner.
    winner = game.winner(grid)
    if (winner != BLANK):
        print("Congratulations",winner,"!")
    else:
        print("It was a draw.")

# A way to tell Python that the code in this file is the main code.
if __name__ == "__main__":
    play_with_comp()
