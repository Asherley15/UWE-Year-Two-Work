import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

frame = tk.Frame(root, height=700, width=700, bg="red")
frame.pack()
butt = tk.Button(frame, fg="blue")
butt.place(relheight=0.8, relwidth=0.8,)
root.mainloop()
