import tkinter as tk
from tkinter import ttk

class styling(ttk.Style):
    def __init__(self, parent):
        super().__init__(parent)

        self.theme_use("clam")
        #style2.map('Custom.TButton', background=[("active", "red")])

        yippe = [-159, -10, -160, -2]

        self.configure('Crosses.TButton',
                        foreground='Black',
                        font=('Segoe UI Symbol', 50),
                        padding=yippe,
                        background="#F8CECC",
                        relief="flat")

        self.map("Crosses.TButton", background=[("disabled", "#F8CECC")])

        self.configure('XWin.TButton',
                        foreground='Black',
                        font=('Segoe UI Symbol', 50),
                        padding=yippe,
                        background="#D5E8D4",
                        relief="flat")

        self.map("XWin.TButton", background=[("disabled", "#D5E8D4")])

        self.configure('Circles.TButton',
                        foreground='Black',
                        font=('Segoe UI Symbol', 50),
                        padding=yippe,
                        relief="flat")

        self.map("Circles.TButton", background=[("disabled", "#DAE8FC")])

        self.configure('OWin.TButton',
                        foreground='Black',
                        font=('Segoe UI Symbol', 50),
                        padding=yippe,
                        background="#D5E8D4",
                        relief="flat")

        self.map("OWin.TButton", background=[("disabled", "#D5E8D4")])


        self.configure('Idle.TButton',
                        foreground='Black',
                        background="#f8f5f9",
                        font=('Segoe UI Symbol', 50),
                        padding=yippe,
                        relief="flat")

        self.configure("Restart.TButton",
                        background="#FFE6CC",
                        font=('Segoe Script', 10),
                        relief="flat",
                        padding=[-10,5,-10,5]
                        )

        self.map("Restart.TButton", background=[("pressed", "#E7CAAA"), ("active", "#F1CCA3")] )

        self.configure("Back.TButton",
                        background="#FFE6CC",
                        font=('Segoe Script', 10),
                        relief="flat",
                        padding=[-10,5,-10,5]
                        )

        self.map("Back.TButton", background=[("pressed", "#E7CAAA"), ("active", "#F1CCA3")] )

        self.configure("Cross_Score.TLabel",
                        background="#F8CECC",
                        font=('Segoe Script', 10),
                        )

        self.configure("Tie_Score.TLabel",
                        background="#F5F5F5",
                        font=('Segoe Script', 10),
                        )

        self.configure("Circles_Score.TLabel",
                        background="#DAE8FC",
                        font=('Segoe Script', 10),
                        )

# Takes tk as a parent to inherit all the tk. properties to make widgets
class main_menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("580x400")

        style = styling(self)

        menu_frame = tk.Frame(
            self,
            background=("#E1D5E7"),
            padx=10,
            pady=10,
            height=400,
            width=400
        )
        menu_frame.pack()

        pvp_button = ttk.Button(
            menu_frame, 
            text="Player vs Player", 
            command=lambda:playable_game(self),
            style=("Back.TButton")
            )
        pvp_button.grid(row=0, column=0, padx=2, pady=2)

        pve_button = ttk.Button(
            menu_frame, 
            text="Player vs Ai", 
            style=("Back.TButton")
            )
        pve_button.grid(row=0, column=1, padx=2, pady=2)

class playable_game(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.parent.withdraw()
        self.title("Game")
        self.geometry("290x400")
        self.resizable(False, False)

        # Int Variables that automatically change the looks of the GUI when changed
        self.cross_score_label = tk.StringVar(value = "Crosses: ")
        self.cross_score = tk.IntVar(value = 0)
        self.cross_combined = tk.StringVar()

        self.tie_score_label = tk.StringVar(value = "Tie: ")
        self.tie_score = tk.IntVar(value = 0)
        self.tie_combined = tk.StringVar()

        self.circles_score_label = tk.StringVar(value = "Circles: ")
        self.circles_score = tk.IntVar(value = 0)
        self.circles_combined = tk.StringVar()

        self.main_frame = tk.Frame(self, background="#E1D5E7", pady=10)
        self.main_frame.pack()

        # Need .get() for score to get the value rather than the label widget data itself
        self.cross_score_board = ttk.Label(self.main_frame, textvariable=self.cross_combined, style="Cross_Score.TLabel", padding=11)
        self.cross_score_board.grid(row=0, column=0)

        self.tie_score_board = ttk.Label(self.main_frame, textvariable=self.tie_combined, style="Tie_Score.TLabel", padding=11)
        self.tie_score_board.grid(row=0, column=1)

        self.circles_score_board = ttk.Label(self.main_frame, textvariable=self.circles_combined, style="Circles_Score.TLabel", padding=11)
        self.circles_score_board.grid(row=0, column=2)

        self.game_frame = tk.Frame(self.main_frame, background="#f0eaf3", padx=5, pady=5)
        self.game_frame.grid(row=1, column=0, columnspan=3, padx=5, pady=10)

        self.button_grid(self.game_frame, self)

        self.restart_button = ttk.Button(self.main_frame, text="Restart", command=self.game_score_reset, style="Restart.TButton")
        self.restart_button.grid(row=2, column=0, columnspan=2)

        self.back_button = ttk.Button(self.main_frame, text="Back", style="Back.TButton", command=self.exit)
        self.back_button.grid(row=2, column=1, columnspan=2)

        self.score_update()
        game_set()

    def exit(self):
        self.after(1, self.parent.deiconify)
        self.after(1, self.destroy)
    
    # Updates score with the string and integer tkinter variables with auto updating properties
    def score_update(self):
        self.cross_combined.set(f"{self.cross_score_label.get()}{self.cross_score.get()}")
        self.tie_combined.set(f"{self.tie_score_label.get()}{self.tie_score.get()}")
        self.circles_combined.set(f"{self.circles_score_label.get()}{self.circles_score.get()}")

    # Restart game initiation
    def game_start(self):
        # Looks for every game_frame child then deletes them to therefore be replaced
        for button in self.game_frame.winfo_children():
            button.destroy()

        game_set()
        self.button_grid(self.game_frame, self)

    # Adds score for the int value for every won game
    def score_add(self, label_type):
        if label_type == "cross":
            self.cross_score.set(self.cross_score.get() + 1)
        elif label_type == "tie":
            self.tie_score.set(self.tie_score.get() + 1)
        elif label_type == "circles":
            self.circles_score.set(self.circles_score.get() + 1)

        self.game_start()
        self.score_update()

    def game_score_reset(self):
        self.cross_score.set(0)
        self.tie_score.set(0)
        self.circles_score.set(0)

        self.game_start()
        self.score_update()

    # Creates 9 buttons for the 3x3 grid
    def button_grid(self, game_frame, parent):
        global record_list
        record_list = {}
        for id in range(1, 10):
            button = button_class(id, record_list, parent)
            button.identification(self.game_frame)

# The necessary blueprint to create a 3x3 grid with button widgets
class button_class:
    # States id var as self property on initiate class (class startup)
    def __init__(self, id, record_list, parent):
        self.id = id
        self.record_list = record_list
        self.parent = parent

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
        
        self.button.grid(row=game_row, column=game_column, padx=3, pady=3)

    # Changes the label text of the selected buttons depending on current playing character 'x' or 'o'
    def button_func(self):
        global crosses
        global disable_count

        if crosses == True:
            self.button.config(text="✕", state=tk.DISABLED, style="Crosses.TButton")
            crosses = False
        elif crosses == False:
            self.button.config(text="⭘", state=tk.DISABLED, style="Circles.TButton")
            crosses = True

        disable_count += 1

        if disable_count != 9:
            self.parent.after(10, self.win_cond)
        # Threshold for all buttons to be occupied till able to reset game
        else:
            self.parent.after(2000, lambda: self.parent.score_add("tie"))


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
            if self.button.cget("text") == "✕":
                x_list.append(self.id)
                x_list.sort()
                
                for win_scenario in win_list:
                    if len(set(x_list).intersection(set(win_scenario))) == 3:
                        for button in set(x_list).intersection(set(win_scenario)):
                            self.record_list[button].config(style="XWin.TButton")
                            for button in self.record_list:
                                self.record_list[button].configure(state=tk.DISABLED)
                            
                        self.parent.after(2000, lambda: self.parent.score_add("cross"))
                    # Threshold for all buttons to be occupied till able to reset game
                    elif disable_count == 9:
                        self.parent.after(2000, lambda: self.parent.score_add("tie"))
                    
            elif self.button.cget("text") == "⭘":
                o_list.append(self.id)
                o_list.sort()

                for win_scenario in win_list:
                    if len(set(o_list).intersection(set(win_scenario))) == 3:
                        for button in set(o_list).intersection(set(win_scenario)):
                            self.record_list[button].config(style="OWin.TButton")
                            for button in self.record_list:
                                self.record_list[button].configure(state=tk.DISABLED)
                        self.parent.after(2000, lambda: self.parent.score_add("circles"))

    # Assigns each button with a blank square then follows up to assign each in a 3x3 grid
    def identification(self, game_frame):
        self.button = ttk.Button(game_frame, command=self.button_func, style="Idle.TButton")
        self.grid_allocation()
        key_name = self.id
        value = self.button
        self.record_list[key_name] = value

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

# Creates loop for tkinter interface
if __name__ == "__main__":
    menu = main_menu()
    menu.mainloop()