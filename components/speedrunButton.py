from tkinter import Button


from linkValidator import linkValidator


def speedrunButton(window):
    speedrunButton = Button(window, pady=10, padx=10,
                            text="Speedrun Wikipedia",
                            font=("arial", 25), command=linkValidator())
    speedrunButton.pack()
