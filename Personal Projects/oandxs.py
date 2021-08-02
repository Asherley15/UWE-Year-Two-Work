import numpy as np
import random
import time
from numpy.random import rand

grid = np.empty(shape=(3, 3), dtype=str)


def fullboard():
    if np.all((grid != "")):
        print("Board is full, Game over!")


def pcturn():
    pcrow = random.randint(0, 2)
    pccol = random.randint(0, 2)
    if grid[pcrow, pccol] == "":
        grid[pcrow, pccol] = 'O'
    else:
        pcturn()


def userturn():
    row = int(input("Which row do you wish to move X into?"))
    col = int(input("Which column do you wish to move X into?"))
    if grid[row - 1, col - 1] != 'X' or 'O':
        grid[row - 1, col - 1] = 'X'
    else:
        print("That Square is taken, choose a valid option.")
        userturn()


print(grid)


notwon = True
while notwon == True:
    if (fullboard()):
        break
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
