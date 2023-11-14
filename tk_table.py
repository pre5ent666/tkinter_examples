import tkinter as tk
import pandas as pd

root = tk.Tk()
root.geometry("980x650")

df = pd.read_excel("C:\\Users\\Yvonne\\Downloads\\W33_Manual_List.xlsx")
n_rows = df.shape[0]
n_cols = df.shape[1]
col_names = df.columns
i = 0
for j, col in enumerate(col_names):
    text = tk.Text(root, width=40, height=1, bg = "#9BC2E6")
    text.grid(row=i, column=j, pady=(10,0))
    text.insert(tk.INSERT, col)

for i in range(n_rows):
    for j in range(n_cols):
        text = tk.Text(root, width=40, height=1)
        text.grid(row=i+1, column=j)
        text.insert(tk.INSERT, df.loc[i][j])

root.mainloop()