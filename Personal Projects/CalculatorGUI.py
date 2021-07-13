import tkinter as tk
from tkinter import Label, filedialog, Text
import os

root = tk.Tk()

frame = tk.Frame(root, height=700, width=700, bg="grey")


title = Label(root, text="Calculator Test", fg="blue")
frame.grid(row="2", column="1")
title.grid(row="1", column="1")
root.mainloop()
