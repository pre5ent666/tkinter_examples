"""
Create a basic to-do list
We will learn about the following:
- Allowing the user to enter text
- Binding functions to key presses
- Dynamically generatring widgets
- Scrolling an area
- Storing data (with sqlite)

Ref.:
- David Love (2018). Python Tkinter By Example.
"""

import tkinter as tk

class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        # solve None
        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        # window title and size
        self.title("To-Do App v1")
        self.geometry("300x400")
        
        # default hint
        todo1 = tk.Label(self, text="--- Add Items Here ---", bg="lightgrey", fg="black", pady=10)
        self.tasks.append(todo1)

        # task widgets
        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        self.task_create = tk.Text(self, height=3, bg="white", fg="black")

        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        # add task
        self.bind("<Return>", self.add_task)

        # scheme
        self.colour_schemes = [{"bg": "lightgrey", "fg": "black"},{"bg": "grey", "fg": "white"}]

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0,tk.END).strip()

        if len(task_text) > 0:
            new_task = tk.Label(self, text=task_text, pady=10)
            _, task_style_choice = divmod(len(self.tasks), 2)

            my_scheme_choice = self.colour_schemes[task_style_choice]

            new_task.configure(bg=my_scheme_choice["bg"])
            new_task.configure(fg=my_scheme_choice["fg"])

            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task)

        self.task_create.delete(1.0, tk.END)

if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()