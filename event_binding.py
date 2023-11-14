import tkinter as tk
from tkinter import ttk

def return_pressed(event=None):
    print('Return key pressed.')

def log(event):
    print(event)

root = tk.Tk()
root.geometry("980x650")

btn = ttk.Button(root, text='Save', command=return_pressed)
btn.bind('<Return>', return_pressed)
btn.bind('<Return>', log, add='+')

btn.focus()
btn.pack(expand=True)

root.mainloop()