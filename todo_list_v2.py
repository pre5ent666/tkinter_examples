"""
Create a basic to-do list
We will learn about the following:
- Allowing the user to enter text
- Binding functions to key presses
(+) Dynamically generatring widgets
(+) Scrolling an area

Ref.:
- David Love (2018). Python Tkinter By Example.
"""

import tkinter as tk
import tkinter.messagebox as msg

class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks
        
        # define canvas and frame widgets
        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        # define scrollbar
        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.title("To-Do App v2")
        self.geometry("300x400")

        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

        