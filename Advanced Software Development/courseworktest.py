import tkinter as tk

window = tk.Tk()

label = tk.Label(text="Yeah Accomodation management, bitch",
                 foreground="red", background="black", width=100, height=10)
label.pack()

button = tk.Button(text="Touch me", width=10, height=5,
                   background="green", fg="orange")
button.pack()
window.mainloop()
