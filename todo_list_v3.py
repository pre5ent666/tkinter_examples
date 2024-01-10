"""
Create a basic to-do list
We will learn about the following:
- Allowing the user to enter text
- Binding functions to key presses
- Dynamically generatring widgets
- Scrolling an area
(+) Storing data with sqlite

Ref.:
- David Love (2018). Python Tkinter By Example.
"""

import tkinter as tk
import tkinter.messagebox as msg
import os
import sqlite3

class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        # solve None
        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks
        
        # define canvas and frames
        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        # define scrollbar
        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        # define title and size of window
        self.title("To-Do App v3")
        self.geometry("300x400")

        #
        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_frame = self.tasks_canvas.create_window((0,0), window=self.tasks_frame, anchor="n")

        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        # default hint
        todo1 = tk.Label(self, text="--- Add Items Here ---", bg="lightgrey", fg="black", pady=10)
        # todo1.bind("<Button-1>", self.remove_task)
        self.tasks.append(todo1)

        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

        # define scheme
        self.colour_schemes = [{"bg": "lightgrey", "fg": "black"},{"bg": "grey", "fg": "white"}]

        current_tasks = self.load_tasks()
        for task in current_tasks:
            task_text = task[0]
            self.add_task(None, task_text, True)

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
            self.tasks.remove(event.widget)
            delete_task_query = "DELETE FROM tasks WHERE task=?"
            delete_atsk_data = (task.cget("text"),)
            self.runQuery(delete_task_query, delete_atsk_data)

            event.widget.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def add_task(self, event=None, task_text=None, from_db=False):
        if not task_text:
            task_text = self.task_create.get(1.0,tk.END).strip()

        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10) # the master here is different from v1
            self.set_task_colour(len(self.tasks), new_task)

            new_task.bind("<Button-1>", self.remove_task)
            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task)

            if not from_db:
                self.save_task(task_text)

        self.task_create.delete(1.0, tk.END)

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        else:
            if event.num == 5:
                move = 1
            else:
                move = -1

            self.tasks_canvas.yview_scroll(move, "units")

    def task_width(self, event=None):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)

    def set_task_colour(self, position, task):
        _, task_style_choice = divmod(position, 2)

        my_scheme_choice = self.colour_schemes[task_style_choice]

        task.configure(bg=my_scheme_choice["bg"])
        task.configure(fg=my_scheme_choice["fg"])

if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()