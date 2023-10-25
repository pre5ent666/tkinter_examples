import tkinter as tk
import tkinter.ttk as ttk
root = tk.Tk()
root.title("Hello")
root.geometry("350x200+200+300") # wxh+x+y

def button_event():
    print(mycombobox.current(), mycombobox.get())

comboboxList = ['apple','banana','orange','lemon','tomato']
mycombobox = ttk.Combobox(root, state='readonly')
mycombobox['values'] = comboboxList

mycombobox.pack(pady=10) # the distance from top of window
mycombobox.current(0) # default value of combobox, 0 is index of values

buttonText = tk.StringVar()
buttonText.set('button')
tk.Button(root, textvariable=buttonText, command=button_event).pack()

root.mainloop() # to keep the tk window

