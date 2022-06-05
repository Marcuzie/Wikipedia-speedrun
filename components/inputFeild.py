from tkinter import Entry, Label


def inputFeild(window, text):
    inputText = Label(window, text=f"{text}", font=("Arial", 25))
    inputText.pack()
    input = Entry(window, fg="#332e2e", font=("Arial", 25))
    input.pack()
    return
