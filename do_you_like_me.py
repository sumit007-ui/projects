
import tkinter as tk
import random

def show_popup():
    popup = tk.Toplevel(root)
    popup.title("Popup")
    label = tk.Label(popup, text="Thanks for Accepting")
    label.pack(padx=30, pady=30)

def move_button(event):
    x = random.randint(0, 350)
    y = random.randint(0, 350)
    no_button.place(x=x, y=y)

root = tk.Tk()
root.title("Mere Dil ka Raaz")
root.geometry("800x600")

question_label = tk.Label(root, text="I like you and Do you like me?",font=("Helvetica", 18, "italic"), fg='black', bg='cyan')
question_label.pack(pady=30)

yes_button = tk.Button(root, text="Yes", command=show_popup,font=("Helvetica", 10, "italic"), fg='black', bg='light blue')
yes_button.pack(pady=10)

no_button = tk.Button(root, text="No",font=("Helvetica", 10, "italic"), fg='black', bg='light blue')
no_button.pack()

no_button.bind("<Enter>", move_button)

root.mainloop()



