import tkinter as tk
from tkinter import ttk


def return_pressed(event):
    print(event.keysym)


def log(event):
    print(event)


root = tk.Tk()

btn = ttk.Button(root, text='Save')
btn.bind('<Right>', return_pressed)
btn.bind('<Left>', return_pressed)
btn.bind('<Up>', return_pressed)
btn.bind('<Down>', return_pressed)



btn.focus()
btn.pack(expand=True)

root.mainloop()