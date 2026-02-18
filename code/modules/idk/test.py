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

one = "I like pizza!"
two = "I like pizza!"
text_data = [one, two]

score_data = [
    "Name1" "100000",
    "Name2" "100000",
    "Name3" "100000", 
    "Name4" "100000", 
    "Name5" "100000", 
]

sample = ["Name Score"] 
# Will have to append placing at the beginning like so: "Placing Name Score" 
## Or may want to transport as vars then convert to str: f"{Placing} {Name} {Score}"

player_data1 = {
    "player1":10000,
    "player2":10,
    "player3":20
}

player_data= {
    10000:"player1",
    10:"player2",
    20:"player3"
}

#player_data["player4"] = 40

newlist = []

for value in player_data:
    newlist.append(value)

newlist.sort(reverse=True)
print(newlist)


with open(file_path, "w") as file:
    for player in score_data:
        file.writelines(f"{player}\n")
    print(f"txt file '{file_path}' was created")




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