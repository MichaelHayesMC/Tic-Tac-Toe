import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tic Tac Toe")
root.resizable(False, False)

main_frame = ttk.Frame()
main_frame.pack()

test_button = ttk.Button(main_frame, text="Testing")
test_button.grid(padx=10, pady=10, row=0, column=0)

test_button1 = ttk.Button(main_frame, text="Testing1")
test_button1.grid(padx=10, pady=10, row=1, column=1)

test_button2 = ttk.Button(main_frame, text="Testing2")
test_button2.grid(padx=10, pady=10, row=2, column=2)

root.mainloop()