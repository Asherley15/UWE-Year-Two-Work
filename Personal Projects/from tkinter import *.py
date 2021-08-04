from tkinter import *
import tkinter
import numpy as np
import random
import time

grid = np.empty(shape=(3, 3), dtype=str)
notwon = True
root = Tk()
root.title('Tic Tac Toe')
root.iconbitmap
l = 1

print(grid)
x = True
for i in range(0, grid.shape[0]):
    for j in range(0, grid.shape[1]):
        l += 1
        num = str(l)
        name = Button(root, text=" ", font=("Helvetica", 20), height=3,
                      width=6, bg="White", command=lambda: b_click(i, j, name))
        name.grid(row=i, column=j)
        print(name, i, j)


def b_click(i, j, name):

    if grid[i, j] != "X" and grid[i, j, ] != 'O':
        grid[i, j] = "X"
        print(grid)
        name["text"] = 'X'
        name["fg"] = "Red"
        print(i, j)
        x = False

    elif grid[i, j] == 'X' or grid[i, j] == 'O':
        print("Invalid selection, choose another space")


root.mainloop()
