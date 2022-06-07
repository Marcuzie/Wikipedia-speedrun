from tkinter import *
from components.topbar import topbar


def linkValidator():
    if "https://en.wikipedia.org/" in input.get() and input2.get():
        print(f"{input.get()} and {input2.get()}")


window = Tk()
window.geometry("620x620")
window.title("Wikipedia Speedrun")
icon = PhotoImage(file="WikipediaSpeedrunIcon")
window.iconphoto(True, icon)
topbar(window)
inputText = Label(window, text="Enter First Wikipedia Link",
                  font=("Arial", 25))
inputText.pack()
input = Entry(window, fg="#332e2e", font=("Arial", 25))
input.pack()
inputText = Label(window, text="Enter Second Wikipedia Link",
                  font=("Arial", 25))
inputText.pack()
input2 = Entry(window, fg="#332e2e", font=("Arial", 25))
input2.pack()
speedrunButton = Button(window, pady=10, padx=10,
                        text="Speedrun Wikipedia",
                        font=("arial", 25), command=linkValidator)
speedrunButton.pack()


if __name__ == "__main__":
    window.mainloop()
