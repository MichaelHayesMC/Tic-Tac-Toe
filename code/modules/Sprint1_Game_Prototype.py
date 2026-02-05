import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tic Tac Toe")
#root.resizable(False, False)
root.geometry("1000x1000")

main_frame = ttk.Frame()
main_frame.pack()

cross_score = ttk.Label(main_frame, text="Crosses: ")
cross_score.grid(row=0, column=0)

circles_score = ttk.Label(main_frame, text="Crosses: ")
circles_score.grid(row=0, column=1)

game_frame = tk.Frame(main_frame, width=220, height=240, bg="Green")
game_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

def ()

button_1 = ttk.Button(game_frame, text="x")
button_1.grid(row=0, column=0, sticky="news")

button_2 = ttk.Button(game_frame, text="x")
button_2.grid(row=0, column=1, sticky="news")

button_3 = ttk.Button(game_frame, text="x")
button_3.grid(row=0, column=2, sticky="news")


restart_button = ttk.Button(main_frame, text="Restart")
restart_button.grid(row=2, column=0, columnspan=2)

root.mainloop()