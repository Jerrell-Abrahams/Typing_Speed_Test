import time
from tkinter import *
from tkinter import ttk
from random import choice
import tkinter


start_time = time.time()

def typing_text(filename):
    with open(filename) as file:
        content = file.readlines()
        return content

def get_user_text():
    import time
    user_text = entry_text.get("1.0", "end-1c")
    elapsed_time = max(time.time() - start_time, 1)
    wpm = round((len(user_text) / (elapsed_time / 60)) / 5)
    wpm_label = ttk.Label(root, text=f"WPM: {wpm} ", font=("Verdana", 15), background="#D8B6A4")
    wpm_label.grid(row=2, column=0, pady=20)


def reset():
    main()

def main():
    global entry_text, wpm_label, root
    root = Tk()
    root.title("Typing Speed Test")
    root.configure(bg="#D8B6A4")
    root.geometry("870x600")
    target_label = ttk.Label(root, font=("Verdana", 16), text="Type this text below:", background="#D8B6A4")
    target_label.grid(column=0, row=0, pady=20)
    target_text = ttk.Label(root, font=("arial", 14), background="#D8B6A4", foreground="#630000", text=choice(typing_text("typing text.txt")), wraplength=950)
    target_text.grid(row=1, column=0, pady=20, sticky=W)
    wpm_label = ttk.Label(root, text=f"WPM: ", font=("Verdana", 15), background="#D8B6A4")
    wpm_label.grid(row=2, column=0, pady=20)
    entry_text = tkinter.Text(root,  width=40, height=7, font=("Arial", 14))
    entry_text.grid(column=0, row=3)
    finish_button = tkinter.Button(root, text="Finish", background="#EEEBDD", width=20, command=get_user_text)
    finish_button.grid(row=4, column=0, pady=20)
    reset_button = tkinter.Button(root, text="Reset", background="#EEEBDD", width=20, command=reset)
    reset_button.grid(row=6, column=0, pady=20)


    root.mainloop()


main()


