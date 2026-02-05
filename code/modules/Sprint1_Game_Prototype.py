import tkinter as tk
from tkinter import ttk

def button_func(button_id):
    print(f"pressed button-{button_id}")

def button_grid(parent_frame):
    button_count = 1
    game_row = 0
    game_column = 0
    game_list = [
        0, 1, 2,
        3, 4, 5,
        6, 7, 8
    ]
    
    while button_count != 10:
        if button_count <= 3:
            game_row = 0
        elif button_count <= 6:
            game_row = 1
        else:
            game_row = 2

        if button_count == 4:
            game_column = 0
        elif button_count == 5:
            game_column = 1
        elif button_count % 3 == 0:
            game_column = 2
        elif button_count % 2 == 0:
            game_column = 1
        else:
            game_column = 0
        
        button = ttk.Button(parent_frame, text=f"#{button_count}, R{game_row}, C{game_column}", command=lambda:button_func(button_count))
        button.grid(row=game_row, column=game_column)
        game_list.append(f"#{button_count}, R{game_row}, C{game_column}")
        
        button_count += 1

    print(game_list)
    return button

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