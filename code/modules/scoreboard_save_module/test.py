import tkinter as tk
from tkinter import ttk

file_path = "output.txt"

# def testing():
#     with open(file_path, "r") as file:
#         for line in file.readlines():
#             table.insert("", "end", values=line)
#         print(file.readlines())
        #table.insert("", "end", values=file.readlines())
    
    # with open(file_path, "w") as file:
    #     file.write

sample = ["Name Score"] 
# Will have to append placing at the beginning like so: "Placing Name Score" 
## Or may want to transport as vars then convert to str: f"{Placing} {Name} {Score}"

player_data= {
    10000:"player1",
    10:"player2",
    20:"player3"
}

player_data[40] = "player4"

newlist = []

for value in player_data:
    newlist.append(value)

#newlist.sort(reverse=True)
#print(newlist)

newerlist = {}

# with open(file_path, "w") as file: 
#     for i in newlist:
#         file.write(f"{i} {player_data[i]}\n")

with open(file_path, "r") as file:
    for line in file.readlines():
        print(f"Line Split: {line.split()}")
        # Automatically assigns values to the vars in list
        value, key = line.split()
        newerlist[key] = value

newernewlist = []

for value in newerlist:
    newernewlist.append(value)

for i in newernewlist:
    print(f"{i} {newerlist[i]}")


# root = tk.Tk()
    
# title = ("RANK", "NAME", "SCORE")

# table = ttk.Treeview(root, show="headings", columns=title)
# table.pack()

# table.heading("RANK", text="RANK")
# table.heading("NAME", text="RANK")
# table.heading("SCORE", text="RANK")

# save_but = tk.Button(root, text="save", command=testing)
# save_but.pack()

# root.mainloop()