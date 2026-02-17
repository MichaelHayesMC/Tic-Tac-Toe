import tkinter as tk
from tkinter import ttk

def testing():
    with open(file_path, "r") as file:
        for line in file.readlines():
            table.insert("", "end", values=line)
        print(file.readlines())
        #table.insert("", "end", values=file.readlines())
    
    # with open(file_path, "w") as file:
    #     file.write

one = "I like pizza!"
two = "I like pizza!"
text_data = [one, two]

file_path = "output.txt"

with open(file_path, "a") as file:
    file.writelines(f"{text_data}\nhi\n")
    print(f"txt file '{file_path}' was created")

root = tk.Tk()
    
title = ("RANK", "NAME", "SCORE")

table = ttk.Treeview(root, show="headings", columns=title)
table.pack()

table.heading("RANK", text="RANK")
table.heading("NAME", text="RANK")
table.heading("SCORE", text="RANK")

save_but = tk.Button(root, text="save", command=testing)
save_but.pack()

root.mainloop()