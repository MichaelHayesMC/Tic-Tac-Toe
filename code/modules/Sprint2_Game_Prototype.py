import tkinter as tk
from tkinter import ttk

# Index of game recording components
def game_set():
    global crosses
    global record_list
    global x_list
    global o_list
    global disable_count
    disable_count = 0
    crosses = True
    record_list = {}
    x_list = []
    o_list = []

# The necessary blueprint to create a 3x3 grid with button widgets
class button_class:
    # States id var as self property on initiate class (class startup)
    def __init__(self, id):
        self.id = id

    # Allocates each button to create the 3x3 grid in game_frame widget
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

    # Changes the label text of the selected buttons depending on current playing character 'x' or 'o'
    def button_func(self):
        global crosses
        global disable_count

        if crosses == True:
            self.button.config(text="x", state=tk.DISABLED)
            crosses = False
        elif crosses == False:
            self.button.config(text="o", state=tk.DISABLED)
            crosses = True

        disable_count += 1

        # Threshold for all buttons to be occupied till able to reset game
        if disable_count == 9:
            score_add("tie")
            game_start()

        self.win_cond()

    # All possible win scenarios compared with current player input to find winner
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
        if self.button.winfo_exists():
            if self.button.cget("text") == "x":
                x_list.append(self.id)
                x_list.sort()
                
                for win_scenario in win_list:
                    if len(set(x_list).intersection(set(win_scenario))) == 3:
                        score_add("cross")
                    
            elif self.button.cget("text") == "o":
                o_list.append(self.id)
                o_list.sort()

                for win_scenario in win_list:
                    if len(set(o_list).intersection(set(win_scenario))) == 3:
                        score_add("circles")

    # Assigns each button with a blank square then follows up to assign each in a 3x3 grid
    def identification(self):
        self.button = ttk.Button(game_frame, text="⬜", command=self.button_func)
        self.grid_allocation()

# Creates 9 buttons for the 3x3 grid
def button_grid(parent_frame):
    global record_list
    record_list = {}
    for id in range(1, 10):
        key_name = f"button_id_{id}"
        value = id
        record_list[key_name] = value
        button = button_class(id)
        button.identification()

# All tkinter widgets instantiated
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("400x400")

# Updates score with the string and integer tkinter variables with auto updating properties
def score_update():
    cross_combined.set(f"{cross_score_label.get()}{cross_score.get()}")
    tie_combined.set(f"{tie_score_label.get()}{tie_score.get()}")
    circles_combined.set(f"{circles_score_label.get()}{circles_score.get()}")

# Restart game initiation
def game_start():
    # Looks for every game_frame child then deletes them to therefore be replaced
    for button in game_frame.winfo_children():
        button.destroy()

    game_set()
    button_grid(game_frame)

# Adds score for the int value for every won game
def score_add(label_type):
    if label_type == "cross":
        cross_score.set(cross_score.get() + 1)
    elif label_type == "tie":
        tie_score.set(tie_score.get() + 1)
    elif label_type == "circles":
        circles_score.set(circles_score.get() + 1)
    
    game_start()
    score_update()

# Int Variables that automatically change the looks of the GUI when changed
cross_score_label = tk.StringVar(value = "Crosses: ")
cross_score = tk.IntVar(value = 0)
cross_combined = tk.StringVar()

tie_score_label = tk.StringVar(value = "Tie: ")
tie_score = tk.IntVar(value = 0)
tie_combined = tk.StringVar()

circles_score_label = tk.StringVar(value = "Circles: ")
circles_score = tk.IntVar(value = 0)
circles_combined = tk.StringVar()

main_frame = ttk.Frame(root)
main_frame.pack()

# Need .get() for score to get the value rather than the label widget data itself
cross_score_board = ttk.Label(main_frame, textvariable=cross_combined)
cross_score_board.grid(row=0, column=0)

tie_score_board = ttk.Label(main_frame, textvariable=tie_combined)
tie_score_board.grid(row=0, column=1)

circles_score_board = ttk.Label(main_frame, textvariable=circles_combined)
circles_score_board.grid(row=0, column=2)

game_frame = ttk.Frame(main_frame)
game_frame.grid(row=1, column=0, columnspan=3)

create_buttons = button_grid(game_frame)

restart_button = ttk.Button(main_frame, text="Restart", command=game_start)
restart_button.grid(row=2, column=0, columnspan=3)

score_update()
game_set()


own_frame = tk.Frame(background="blue")
own_frame.pack()

style = ttk.Style()
style2 = ttk.Style()

style2.theme_use("clam")
#style2.map('Custom.TButton', background=[("active", "red")])


yippe = [-159, -10, -160, -2]

style2.configure('Custom.TButton',
                foreground='Black',
                background="#F8CECC",
                font=('Segoe UI Symbol', 50),
                padding=yippe,
                bg=0,
                relief="flat")

button = ttk.Button(own_frame, text="✕", style="Custom.TButton")
button.grid(row=0,column=0)

#button2 = tk.Button(own_frame, 
                    #text="✕", 
                    #bg='#F8CECC',
                    #relief='flat',
                    #height=-5, 
                    #width=4, 
                    #font=('Segoe UI Symbol', 50),
                    #bd=0)

#button3 = tk.Button(root, 
                    #text="◯", 
                    #bg='#F8CECC',
                    #relief='flat',
                    #height=-500000, 
                    #width=4, 
                    #font=('Segoe UI Symbol', 50),
                    #bd=0,)

#button2.grid(row=0,column=1, padx=2.5,pady=5)
#button3.grid(row=0, column=2, padx=2.5,pady=5)
#button3.config(relief='flat')


# Creates loop for tkinter interface
root.mainloop()