import tkinter as tk
from tkinter import ttk
import random

save_file_path = "score_board.txt"

# Class listing all styles for other tkinter widgets to inherit
class styling(ttk.Style):
    def __init__(self, parent):
        super().__init__(parent)

        self.theme_use("clam")
        #style2.map('Custom.TButton', background=[("active", "red")])

        tile_padding_template = [-159, -10, -160, -2]

        self.configure('Crosses.TButton',
                        foreground='Black',
                        font=('Segoe UI Symbol', 50),
                        padding=tile_padding_template,
                        background="#F8CECC",
                        relief="flat")
        self.map("Crosses.TButton", background=[("disabled", "#F8CECC")])

        self.configure('XWin.TButton',
                        foreground='Black',
                        font=('Segoe UI Symbol', 50),
                        padding=tile_padding_template,
                        background="#D5E8D4",
                        relief="flat")
        self.map("XWin.TButton", background=[("disabled", "#D5E8D4")])

        self.configure('Circles.TButton',
                        foreground='Black',
                        font=('Segoe UI Symbol', 50),
                        padding=tile_padding_template,
                        relief="flat")
        self.map("Circles.TButton", background=[("disabled", "#DAE8FC")])

        self.configure('OWin.TButton',
                        foreground='Black',
                        font=('Segoe UI Symbol', 50),
                        padding=tile_padding_template,
                        background="#D5E8D4",
                        relief="flat")
        self.map("OWin.TButton", background=[("disabled", "#D5E8D4")])

        self.configure('Idle.TButton',
                        foreground='Black',
                        background="#f8f5f9",
                        font=('Segoe UI Symbol', 50),
                        padding=tile_padding_template,
                        relief="flat")

        self.configure("Restart.TButton",
                        background="#FFE6CC",
                        font=('Segoe Script', 10),
                        relief="flat",
                        padding=[-10,5,-10,5]
                        )
        self.map(
            "Restart.TButton", 
            background=[("pressed", "#E7CAAA"), ("active", "#F1CCA3")]
            )

        self.configure("Back.TButton",
                        background="#FFE6CC",
                        font=('Segoe Script', 10),
                        relief="flat",
                        padding=[-10,5,-10,5]
                        )
        self.map(
            "Back.TButton", 
            background=[("pressed", "#E7CAAA"), ("active", "#F1CCA3")]
            )

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
        
        self.configure("PVP.TButton",
                       background=("#F8CECC"),
                       font=("Segoe Script", 10),
                       relief="flat",
                       padding=[30, 170, 30, 170]
                       )
        self.map(
            "PVP.TButton", 
            background=[("pressed", "#D38480"), ("active", "#D3ADAC")]
            )
        
        self.configure("PVE.TButton",
                background=("#DAE8FC"),
                font=("Segoe Script", 10),
                relief="flat",
                padding=[30, 85, 30, 85]
                )
        self.map(
            "PVE.TButton", 
            background=[("pressed", "#8CABD6"), ("active", "#B5C0CE")]
            )

        self.configure("Scoreboard.TButton",
                background=("#FFF2CC"),
                font=("Segoe Script", 10),
                relief="flat",
                padding=[30, 48, 30, 48]
                )
        self.map(
            "Scoreboard.TButton", 
            background=[("pressed", "#D6C88C"), ("active", "#CEC8B5")]
            )

        self.configure("Tutorial.TButton",
                background=("#D5E8D4"),
                font=("Segoe Script", 10),
                relief="flat",
                )
        self.map(
            "Tutorial.TButton", 
            background=[("pressed", "#8EAF8C"), ("active", "#99B697")]
            )
        
        self.configure("Title.TLabel",
                       background="#f0eaf3",
                       font=("Segoe Script", 30),
                       relief="flat",
                       padding=[40, 90, 40, 90]
                       )
        
        self.configure("Treeview.Heading",
                       relief="flat",
                       background="#f0eaf3",
                       borderwidth=1,
                       font=("Segoe Script", 8)
                       )
        self.configure("Treeview",
                       background="#f0eaf3",
                       fieldbackground="#f0eaf3",
                       bordercolor="#f0eaf3",
                       borderwidth=1,
                       font=("Segoe Script", 8),
                       foreground="#1C1C1C"
                       )

# Takes tk as a parent to inherit all the tk. properties to make widgets
class main_menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("545x395")
        self.resizable(False, False)

        # Initialises Tkinter Styles
        style = styling(self)

        main_frame = tk.Frame(
            self,
            background=("#E1D5E7"),
            padx=10,
            pady=10
            )
        main_frame.pack()

        title = ttk.Label(
            main_frame, 
            text="Tic Tac Toe",
            wraplength=100,
            style="Title.TLabel"
            )
        title.grid(row=0, column=0)

        widgets_frame = tk.Frame(
            main_frame, 
            padx=3, 
            pady=3, 
            background="#f0eaf3"
            )
        widgets_frame.grid(row=0, column=1)

        pvp_button = ttk.Button(
            widgets_frame, 
            text="PVP ⚔️", 
            command=lambda:playable_game(self, "No_AI"),
            style=("PVP.TButton")
            )
        pvp_button.grid(row=0, column=0, padx=2, pady=2, rowspan=3)

        pve_button = ttk.Button(
            widgets_frame, 
            text="PVE 🤖", 
            style=("PVE.TButton"),
            command=lambda:playable_game(self, "Yes_AI")
            )
        pve_button.grid(row=0, column=1, sticky="n", padx=2, pady=2)

        score_board_button = ttk.Button(
            widgets_frame, 
            text="ScoreBoard 📊",
            style="Scoreboard.TButton",
            command=lambda:scoreboard_page(self)
            )
        score_board_button.grid(row=1, column=1, sticky="nsew", padx=2)

        tutorial_button = ttk.Button(
            widgets_frame, 
            text="Tutorial ⚙️",
            style=("Tutorial.TButton"),
            command=lambda:tutorial_page(self)
            )
        tutorial_button.grid(row=2, column=1, sticky="sew", padx=2, pady=2)

# Class that inherits all tk.Toplevel properties
class playable_game(tk.Toplevel):
    def __init__(self, parent, game_type):
        # Inherits properties of parent which is tkinter
        super().__init__(parent)
        self.parent = parent
        self.game_type = game_type

        # Window properties
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

        # Defined widgets to be placed on the tkinter window
        self.cross_score_board = ttk.Label(
            self.main_frame, 
            textvariable=self.cross_combined, 
            style="Cross_Score.TLabel", 
            padding=11
            )
        self.cross_score_board.grid(row=0, column=0)

        self.tie_score_board = ttk.Label(
            self.main_frame, 
            textvariable=self.tie_combined, 
            style="Tie_Score.TLabel", 
            padding=11
            )
        self.tie_score_board.grid(row=0, column=1)

        self.circles_score_board = ttk.Label(
            self.main_frame, 
            textvariable=self.circles_combined, 
            style="Circles_Score.TLabel", 
            padding=11
            )
        self.circles_score_board.grid(row=0, column=2)

        self.game_frame = tk.Frame(
            self.main_frame, 
            background="#f0eaf3", 
            padx=5, 
            pady=5
            )
        self.game_frame.grid(row=1, column=0, columnspan=3, padx=5, pady=10)

        # Button that allows the player to restart game scores
        self.restart_button = ttk.Button(
            self.main_frame, 
            text="Restart", 
            command=self.game_score_reset, 
            style="Restart.TButton"
            )
        self.restart_button.grid(row=2, column=0, columnspan=2)

        # Button that allows the player to return to main menu
        self.back_button = ttk.Button(
            self.main_frame, 
            text="Back", 
            style="Back.TButton", 
            command=lambda:self.exit("playable_game_button")
            )
        self.back_button.grid(row=2, column=1, columnspan=2)

        # Resets all game property variables
        game_set()

        # Creates the 9x9 grid of buttons
        self.button_grid(self.game_frame, self)
        
        # Updates score to match variables
        self.score_update()

    # Reopen parent widget and delete self
    def exit(self, id):
        if id == "playable_game_button" and self.game_type == "Yes_AI":
            score_confirmation(
                self, 
                self.parent, 
                self.cross_score, 
                self.tie_score, 
                self.circles_score
                )
        else:
            self.parent.deiconify()
        self.destroy()

    # Updates score with the string and integer tkinter variables (Label: Score) with auto updating properties
    def score_update(self):
        self.cross_combined.set(
            f"{self.cross_score_label.get()}{self.cross_score.get()}"
            )
        self.tie_combined.set(
            f"{self.tie_score_label.get()}{self.tie_score.get()}"
            )
        self.circles_combined.set(
            f"{self.circles_score_label.get()}{self.circles_score.get()}"
            )

    # Restart game initiation
    def game_start(self):
        self.back_button.config(state=tk.DISABLED)
        self.restart_button.config(state=tk.DISABLED)

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

        self.back_button.config(state=tk.NORMAL)
        self.restart_button.config(state=tk.NORMAL)

    def game_score_reset(self):
        self.cross_score.set(0)
        self.tie_score.set(0)
        self.circles_score.set(0)

        self.game_start()
        self.score_update()

    # Creates 9 buttons for the 3x3 grid
    def button_grid(self, game_frame, parent):
        id = 0

        for row in range(3):
            for column in range(3):
                id += 1
                button = button_class(id, row, column, parent, self.game_type)
                button.identification(self.game_frame)

# Score popup prompting user to give a input of 3 letters for their score
class score_confirmation(tk.Toplevel):
    def __init__(self, parent, grandparent, cross, tie, circle):
            super().__init__(grandparent)
            self.parent = parent
            self.grandparent = grandparent
            self.cross = cross
            self.tie = tie
            self.circle = circle

            self.title("Save Score Prompt")
            self.geometry("330x265")
            self.resizable(False, False)

            self.main_frame = tk.Frame(self, background="#E1D5E7", padx=10, pady=10)
            self.main_frame.pack()

            self.widget_frame = tk.Frame(
                self.main_frame, 
                background="#f0eaf3", 
                padx=30, 
                pady=30
                )
            self.widget_frame.pack()

            self.score_difference = self.cross.get() - self.circle.get()

            self.score_title = tk.Label(
                self.widget_frame, 
                text=f"Score: {self.score_difference}", 
                background="#f0eaf3", 
                font=('Segoe Script', 15), 
                padx=20, 
                pady=5, 
                width=200
                )
            self.score_title.pack()

            self.insert_name = tk.Label(
                self.widget_frame, 
                text="Please Insert User:", 
                background="#f0eaf3", 
                font=('Segoe Script', 10), 
                padx=20, 
                pady=5, 
                width=200
                )
            self.insert_name.pack()

            self.insert_widget_frame = tk.Frame(self.widget_frame)
            self.insert_widget_frame.pack()

            self.letter1 = ttk.Entry(
                self.insert_widget_frame, 
                width=2, 
                font=('Segoe Script', 20), 
                justify="center"
                )
            self.letter1.grid(column=0, row=1, sticky="e")

            self.letter2 = ttk.Entry(
                self.insert_widget_frame, 
                width=2, 
                font=('Segoe Script', 20), 
                justify="center"
                )
            self.letter2.grid(column=1, row=1, sticky="")

            self.letter3 = ttk.Entry(
                self.insert_widget_frame, 
                width=2, 
                font=('Segoe Script', 20), 
                justify="center"
                )
            self.letter3.grid(column=2, row=1, sticky="w")

            self.letter1.bind("<KeyRelease>", lambda e: self.entry_limit(self.letter1))
            self.letter2.bind("<KeyRelease>", lambda e: self.entry_limit(self.letter2))
            self.letter3.bind("<KeyRelease>", lambda e: self.entry_limit(self.letter3))
            
            self.confirm_button = ttk.Button(
                self.main_frame, 
                text="Confirm", 
                style="Back.TButton", 
                command=self.exit
                )
            self.confirm_button.pack(padx=10, pady=10)
    
    def entry_limit(self, widget):
        widget_func = widget.get()
        if len(widget_func) > 1:
            widget.delete(1, tk.END)

    def exit(self):
        global save_file_path
        user_name = (
            self.letter1.get() + self.letter2.get() + self.letter3.get()
            ).upper()

        if len(user_name) == 3:
            with open(save_file_path, "a") as file:
                file.write(f"{self.score_difference} {user_name}\n")

            self.grandparent.deiconify()
            self.destroy()

# Brief tutorial page
class tutorial_page(tk.Toplevel):
    def __init__(self, parent):
            super().__init__(parent)
            self.parent = parent

            self.parent.withdraw()
            self.title("Tutorial")
            self.geometry("330x230")
            self.resizable(False, False)

            self.main_frame = tk.Frame(self, background="#E1D5E7", padx=10, pady=10)
            self.main_frame.pack()

            self.widget_frame = tk.Frame(
                self.main_frame, 
                background="#f0eaf3", 
                padx=5, 
                pady=5
                )
            self.widget_frame.grid(row=0)

            self.rule_title = tk.Label(
                self.widget_frame, 
                text="Rules:", 
                background="#f0eaf3", 
                font=('Segoe Script', 10)
                )
            self.rule_title.pack()

            self.rule_info = tk.Label(
                self.widget_frame, 
                text=(
                    "Tic-Tac-Toe is a two-player game played on a 3x3 grid. "
                    "Players alternate placing 'X' or 'O' in empty squares, "
                    "with the goal of being the first to get three of their marks in a row "
                    "(horizontally, vertically, or diagonally). "
                    "The first player (often 'X') goes first, and the game ends in a tie if "
                    "all nine squares are filled without three-in-a-row. "
                    ),
                wraplength=300,
                justify="center",
                background="#f0eaf3", 
                font=('Segoe Script', 8)
            )
            self.rule_info.pack()

            self.back_button = ttk.Button(
                self.main_frame, 
                text="Back", 
                style="Back.TButton", 
                command=lambda:playable_game.exit(self)
                )
            self.back_button.grid(row=1, padx=10, pady=10)

# Scoreboard that reads local txt file for scores
class scoreboard_page(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        player_dir = []
        line_max = 0
        placings = [
            "#1st",
            "#2nd",
            "#3rd",
            "#4th",
            "#5th",
            "#6th",
            "#7th",
            "#8th",
            "#9th",
            "#10th"
        ]

        self.parent = parent

        self.parent.withdraw()
        self.title("Scoreboard")
        self.geometry("415x360")
        self.resizable(False, False)

        self.main_frame = tk.Frame(self, background="#E1D5E7", padx=10, pady=10)
        self.main_frame.pack()

        self.widget_frame = tk.Frame(
            self.main_frame, 
            background="#f0eaf3", 
            padx=5, 
            pady=5
            )
        self.widget_frame.grid(row=0)

        self.hscore_title = tk.Label(
            self.widget_frame, 
            text="HIGH SCORES", 
            background="#f0eaf3", 
            font=('Segoe Script', 17), 
            padx=7, 
            pady=5
            )
        self.hscore_title.grid(row=0, sticky="w")

        treeview_headers = ("Rank", "Name", "Score")
        self.score_display = ttk.Treeview(
            self.widget_frame, 
            columns=treeview_headers, 
            show="headings"
            )
        self.score_display.grid(row=1, padx=5, pady=5)

        self.score_display.heading("Rank", text="RANK", anchor="w")
        self.score_display.heading("Name", text="NAME", anchor="w")
        self.score_display.heading("Score", text="SCORE (WINS - LOSSES)", anchor="w")

        self.score_display.column("Rank", minwidth=80, width=80, anchor="w")
        self.score_display.column("Name", minwidth=80, width=80, anchor="w")
        self.score_display.column("Score", minwidth=210, width=210, anchor="w")

        with open(save_file_path, "r") as file:
            for line in file.readlines():
                # Automatically assigns values to the vars in list
                value, key = line.split()
                player_dir.append([int(value), key])

        sorted_player_dir = sorted(player_dir, reverse=True)

        for player_val in sorted_player_dir:
            if line_max <= 9:
                player_data = f"{placings[line_max]} {player_val[1]} {player_val[0]}"
                self.score_display.insert("", "end", values=player_data)
                line_max += 1

        self.back_button = ttk.Button(
            self.main_frame, 
            text="Back", 
            style="Back.TButton", 
            command=lambda:playable_game.exit(self)
            )
        self.back_button.grid(row=1, padx=10, pady=10)

# The necessary blueprint to create each button in a 3x3 grid
class button_class:
    # States id var as self property on initiate class (class startup)
    def __init__(self, id, row, column, parent, game_type):
        self.id = id
        self.row = row
        self.column = column
        self.parent = parent
        self.game_type = game_type

    # Assigns each button with a blank square then follows up to assign each in a 3x3 grid
    def identification(self, game_frame):
        if self.game_type == "Yes_AI":
            self.button = ttk.Button(
                game_frame, 
                command=self.button_func_ai, 
                style="Idle.TButton"
                )
        elif self.game_type == "No_AI":
            self.button = ttk.Button(
                game_frame, 
                command=self.button_func, 
                style="Idle.TButton"
                )
        self.grid_allocation()
        key_name = self.id
        value = self.button
        game_properties.record_list[key_name] = value

    # Allocates each button to create the 3x3 grid in game_frame widget
    def grid_allocation(self):
        self.button.grid(
            row=self.row, 
            column=self.column, 
            padx=3, 
            pady=3
            )

    # Changes the label text of the selected buttons depending on current playing character 'x' or 'o'
    def button_func(self):
        self.parent.back_button.config(state=tk.DISABLED)
        self.parent.restart_button.config(state=tk.DISABLED)

        if game_properties.crosses == True:
            self.button.config(text="✕", state=tk.DISABLED, style="Crosses.TButton")
            game_properties.x_list.append(self.id)
            game_properties.x_list.sort()
            game_properties.crosses = False
        elif game_properties.crosses == False:
            self.button.config(text="⭘", state=tk.DISABLED, style="Circles.TButton")
            game_properties.o_list.append(self.id)
            game_properties.o_list.sort()
            game_properties.crosses = True

        game_properties.disable_count += 1

        self.win_cond()

        # Threshold for all buttons to be occupied till able to reset game
        if game_properties.disable_count == 9 and game_properties.game_won == False:
            self.parent.after(2000, lambda: self.parent.score_add("tie"))

    def button_func_ai(self):
        looking = True
        self.parent.back_button.config(state=tk.DISABLED)
        self.parent.restart_button.config(state=tk.DISABLED)

        game_properties.disable_count += 1

        # User turn record data
        self.button.config(text="✕", state=tk.DISABLED, style="Crosses.TButton")
        game_properties.x_list.append(self.id)
        game_properties.x_list.sort()
        game_properties.possible_moves.remove(self.id)
        
        self.win_cond()

        # Ai process for PVE
        if game_properties.possible_moves != [] and game_properties.game_won == False:
                for win_scenario in game_properties.win_list:
                    if len(set(game_properties.x_list) & set(win_scenario)) >= 2:
                        test = (set(game_properties.x_list) ^ set(win_scenario)).pop()
                        if test in game_properties.possible_moves:
                            game_properties.win_list.remove(win_scenario)
                            game_properties.record_list[test].config(
                                text="⭘", 
                                state=tk.DISABLED, 
                                style="Circles.TButton"
                                )
                            game_properties.o_list.append(test)
                            game_properties.o_list.sort()
                            game_properties.possible_moves.remove(test)
                            game_properties.disable_count += 1
                            self.win_cond()
                            return
                        else:
                            while looking:
                                a = random.randrange(1,9)
                                for move in game_properties.possible_moves:
                                    if a == move:
                                        looking = False
                                        game_properties.record_list[a].config(
                                            text="⭘", 
                                            state=tk.DISABLED, 
                                            style="Circles.TButton"
                                            )
                                        game_properties.o_list.append(a)
                                        game_properties.o_list.sort()
                                        game_properties.possible_moves.remove(move)
                                        game_properties.disable_count += 1
                                        self.win_cond()
                                        return
                else:
                    while looking:
                        a = random.randrange(1,9)
                        for move in game_properties.possible_moves:
                            if a == move:
                                looking = False
                                game_properties.record_list[a].config(
                                    text="⭘", 
                                    state=tk.DISABLED, 
                                    style="Circles.TButton"
                                    )
                                game_properties.o_list.append(a)
                                game_properties.o_list.sort()
                                game_properties.possible_moves.remove(move)
                                game_properties.disable_count += 1
                                self.win_cond()
                                return

        # Threshold for all buttons to be occupied till able to reset game
        if game_properties.disable_count == 9 and game_properties.game_won == False:
            self.parent.after(2000, lambda: self.parent.score_add("tie"))

    # Inherits boolean for while loop checking process (check for moves)
    def ai_opponent(self, looking):
        while looking:
            a = random.randrange(1,9)
            for move in game_properties.possible_moves:
                if a == move:
                    game_properties.record_list[a].config(
                        text="⭘", 
                        state=tk.DISABLED, 
                        style="Circles.TButton"
                        )
                    game_properties.o_list.append(a)
                    game_properties.o_list.sort()
                    game_properties.possible_moves.remove(move)
                    looking = False
                    game_properties.disable_count += 1
                    self.win_cond()
                    return looking

    # All possible win scenarios compared with current player input to find winner
    def win_cond(self):
        # Convert the following if statements dependent on button type to a function
        if self.button.winfo_exists():
            for win_scenario in game_properties.win_list:
                if len(set(game_properties.x_list).intersection(set(win_scenario))) == 3:
                    game_properties.game_won = True
                    for button in set(game_properties.x_list).intersection(set(win_scenario)):
                        game_properties.record_list[button].config(style="XWin.TButton")
                        for button in game_properties.record_list:
                            game_properties.record_list[button].configure(state=tk.DISABLED)
                    self.parent.after(2000, lambda: self.parent.score_add("cross"))

            for win_scenario in game_properties.win_list:
                if len(set(game_properties.o_list).intersection(set(win_scenario))) == 3:
                    game_properties.game_won = True
                    for button in set(game_properties.o_list).intersection(set(win_scenario)):
                        game_properties.record_list[button].config(style="OWin.TButton")
                        for button in game_properties.record_list:
                            game_properties.record_list[button].configure(state=tk.DISABLED)
                    self.parent.after(2000, lambda: self.parent.score_add("circles"))

# Index of game recording components
class game_properties:
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
    game_won = False
    disable_count = 0
    crosses = True
    x_list = []
    o_list = []
    possible_moves = [1,2,3,4,5,6,7,8,9]
    record_list = {}

# Resets all game properties to default state
def game_set():
    game_properties.win_list = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7]
        ]
    game_properties.game_won = False
    game_properties.disable_count = 0
    game_properties.crosses = True
    game_properties.x_list = []
    game_properties.o_list = []
    game_properties.possible_moves = [1,2,3,4,5,6,7,8,9]
    game_properties.record_list = {}

# Creates loop for tkinter interface
if __name__ == "__main__":
    menu = main_menu()
    menu.mainloop()