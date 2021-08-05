from tkinter import *
import tkinter
import tkinter.messagebox
from typing import Counter
import numpy as np
import random
import time

grid = np.empty(shape=(3, 3), dtype=str)
notwon = True
root = Tk()
root.title('Tic Tac Toe')
root.iconbitmap

clicked = True
count = 0

print(grid)
x = False
pctur = False
notwon = True
valid = True
counter = 0


def b_click(i, j, b):
    global pctur, x, selection, buttons, notwon

    if pctur == False:
        if grid[i, j] != "X" and grid[i, j, ] != 'O':
            grid[i, j] = str("X")
            print(grid)
            b["text"] = str('X')
            b["fg"] = "Red"
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
                b["text"] = str('X')
                b["fg"] = "Red"
                tkinter.messagebox.showinfo("winner", "Congrats, you win!")

            counter = 0
            for t in grid:

                for p in t:
                    if p == '':
                        counter += 1

            if counter == 0:
                tkinter.messagebox.showinfo("winner", "Its a draw!")
                exit()
            global buttons
            buttons.remove(b)
            pctur = True

        elif grid[i, j] == 'X' or grid[i, j] == 'O':
            print("Invalid selection, choose another space")

    if pctur == True:
        if x == False:
            selection = random.choice(buttons)
            if selection in (buttons):
                x = True
                selection.invoke()

        if x == True:
            if grid[i, j] != "X" and grid[i, j] != 'O':
                grid[i, j] = "O"
                x = False
                if(grid[0, 0] == 'O' and grid[0, 1] == 'O' and grid[0, 2] == 'O'
                   or grid[0, 0] == 'O' and grid[1, 1] == 'O' and grid[2, 2] == 'O'
                        or grid[0, 0] == 'O' and grid[1, 0] == 'O' and grid[2, 0] == 'O'
                        or grid[0, 1] == 'O' and grid[1, 1] == 'O' and grid[2, 1] == 'O'
                        or grid[0, 2] == 'O' and grid[1, 2] == 'O' and grid[2, 2] == 'O'
                        or grid[0, 2] == 'O' and grid[1, 1] == 'O' and grid[2, 0] == 'O'
                        or grid[1, 0] == 'O' and grid[1, 1] == 'O' and grid[1, 2] == 'O'
                        or grid[2, 0] == 'O' and grid[2, 1] == 'O' and grid[2, 2] == 'O'):
                    b["text"] = 'O'
                    b["fg"] = "Green"
                    tkinter.messagebox.showinfo(
                        "Loser", "You Lose, better luck next time!")
                    notwon = False

            buttons.remove(b)
            print(grid)
            b["text"] = 'O'
            b["fg"] = "Green"
            x = False
            pctur = False


b1 = Button(root, text=" ", font=("Helvetica", 20), height=3,
            width=6, bg="White", fg="Red", command=lambda: b_click(0, 0, b1))
b2 = Button(root, text=" ", font=("Helvetica", 20), height=3,
            width=6, bg="White", command=lambda: b_click(0, 1, b2))
b3 = Button(root, text=" ", font=("Helvetica", 20), height=3,
            width=6, bg="White", command=lambda: b_click(0, 2, b3))
b4 = Button(root, text=" ", font=("Helvetica", 20), height=3,
            width=6, bg="White", command=lambda: b_click(1, 0, b4))
b5 = Button(root, text=" ", font=("Helvetica", 20), height=3,
            width=6, bg="White", command=lambda: b_click(1, 1, b5))
b6 = Button(root, text=" ", font=("Helvetica", 20), height=3,
            width=6, bg="White", command=lambda: b_click(1, 2, b6))
b7 = Button(root, text=" ", font=("Helvetica", 20), height=3,
            width=6, bg="White", command=lambda: b_click(2, 0, b7))
b8 = Button(root, text=" ", font=("Helvetica", 20), height=3,
            width=6, bg="White", command=lambda: b_click(2, 1, b8))
b9 = Button(root, text=" ", font=("Helvetica", 20), height=3,
            width=6, bg="White", command=lambda: b_click(2, 2, b9))

buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]


def pcturn():
    global buttons, selection
    selection = random.choice(buttons)
    if selection in (buttons):
        selection = selection


b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

root.mainloop()
