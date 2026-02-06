import tkinter as tk
from tkinter import ttk

crosses = True
record_list = {}
x_list = []
o_list = []

class button_class:
    def __init__(self, id):
        self.id = id

    # Fix this with range() for loops
    def grid_allocation(self):
        game_row = 0
        game_column = 0

        if self.id <= 3:
            game_row = 0
        elif self.id <= 6:
            game_row = 1
        else:
            game_row = 2

        if self.id == 4:
            game_column = 0
        elif self.id == 5:
            game_column = 1
        elif self.id % 3 == 0:
            game_column = 2
        elif self.id % 2 == 0:
            game_column = 1
        else:
            game_column = 0
        
        self.button.grid(row=game_row, column=game_column)

    def button_func(self):
        global crosses
        if crosses == True:
            self.button.config(text="x", state=tk.DISABLED)
            crosses = False
        elif crosses == False:
            self.button.config(text="o", state=tk.DISABLED)
            crosses = True

        self.win_cond()

    def win_cond(self):
        global x_list
        global o_list

        win_list = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7]
        ]

        # Convert the following if statements dependent on button type to a function
        if self.button.cget("text") == "x":
            x_list.append(self.id)
            x_list.sort()
            

            for win_scenario in win_list:
                if len(set(x_list).intersection(set(win_scenario))) == 3:
                    print("x wins")
                
        if self.button.cget("text") == "o":
            o_list.append(self.id)
            o_list.sort()

            for win_scenario in win_list:
                if len(set(o_list).intersection(set(win_scenario))) == 3:
                    print("o wins")

                #print(set(x_list))
                #print(set(win_scenario))    
                #print(set(x_list).intersection(set(win_scenario)))


    def identfication(self):
        self.button = ttk.Button(game_frame, text=self.id, command=self.button_func)
        self.grid_allocation()

def button_grid(parent_frame):
    # Probably will replace with a for range() loop
    game_list = [
        1, 2, 3,
        4, 5, 6,
        7, 8, 9
    ]

    for id in game_list:
        global record_list
        key_name = f"button_id_{id}"
        value = id
        record_list[key_name] = value
        button = button_class(id)
        button.identfication()

root = tk.Tk()
root.title("Tic Tac Toe")
#root.resizable(False, False)
root.geometry("400x400")

main_frame = ttk.Frame(root)
main_frame.pack()

cross_score = ttk.Label(main_frame, text="Crosses: ")
cross_score.grid(row=0, column=0)

tie_score = ttk.Label(main_frame, text="Tie: ")
tie_score.grid(row=0, column=1)

circles_score = ttk.Label(main_frame, text="Circles: ")
circles_score.grid(row=0, column=2)

game_frame = ttk.Frame(main_frame)
game_frame.grid(row=1, column=0, columnspan=3)

create_buttons = button_grid(game_frame)

restart_button = ttk.Button(main_frame, text="Restart")
restart_button.grid(row=2, column=0, columnspan=3)

root.mainloop()