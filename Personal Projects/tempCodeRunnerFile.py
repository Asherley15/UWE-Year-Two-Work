import numpy as np
import random
import time
from numpy.random import f, rand

grid = np.empty(shape=(3, 3), dtype=str)

notwon = True


def fullboard():
    check = ''
    if check in grid:
        global notwon
        notwon = True
    else:
        print("Board is full, its a draw!")
        print(grid)
        notwon = False
        exit()


def pcturn():
    pcrow = random.randint(0, 2)
    pccol = random.randint(0, 2)
    if grid[pcrow, pccol] == "":
        grid[pcrow, pccol] = 'O'
    else:
        pcturn()


def userturn():
    valid = True
    while valid:
        try:
            row = int(input("Which row do you wish to move X into?"))
            if 0 > row or row > 3:
                print("Please enter a valid input.")
            else:
                valid = False
        except ValueError:
            print("Please enter a valid number")
            continue

    col = int(input("Which column do you wish to move X into?"))

    if grid[row - 1, col - 1] != 'X' or 'O':
        grid[row - 1, col - 1] = 'X'
    else:
        print("That Square is taken, choose a valid option.")
        userturn()


while notwon == True:
    fullboard()
    userturn()
    if (grid[0, 0] == 'X' and grid[0, 1] == 'X' and grid[0, 2] == 'X'
        or grid[0, 0] == 'X' and grid[1, 1] == 'X' and grid[2, 2] == 'X'
        or grid[0, 0] == 'X' and grid[1, 0] == 'X' and grid[2, 0] == 'X'
        or grid[0, 1] == 'X' and grid[1, 1] == 'X' and grid[2, 1] == 'X'
        or grid[0, 2] == 'X' and grid[1, 2] == 'X' and grid[2, 2] == 'X'
        or grid[0, 2] == 'X' and grid[1, 1] == 'X' and grid[2, 0] == 'X'
        or grid[1, 0] == 'X' and grid[1, 1] == 'X' and grid[1, 2] == 'X'
            or grid[2, 0] == 'X' and grid[2, 1] == 'X' and grid[2, 2] == 'X'):
        print(grid)
        print("You win!")
        notwon = False
        break
    else:
        fullboard()
        print(grid)
        print("Robot is thinking...")
        # time.sleep(2)
        pcturn()
        if(grid[0, 0] == 'O' and grid[0, 1] == 'O' and grid[0, 2] == 'O'
           or grid[0, 0] == 'O' and grid[1, 1] == 'O' and grid[2, 2] == 'O'
           or grid[0, 0] == 'O' and grid[1, 0] == 'O' and grid[2, 0] == 'O'
           or grid[0, 1] == 'O' and grid[1, 1] == 'O' and grid[2, 1] == 'O'
           or grid[0, 2] == 'O' and grid[1, 2] == 'O' and grid[2, 2] == 'O'
           or grid[0, 2] == 'O' and grid[1, 1] == 'O' and grid[2, 0] == 'O'
           or grid[1, 0] == 'O' and grid[1, 1] == 'O' and grid[1, 2] == 'O'
           or grid[2, 0] == 'O' and grid[2, 1] == 'O' and grid[2, 2] == 'O'):
            print("You lose!")
            print(grid)
            notwon = False
        else:
            print(grid)
