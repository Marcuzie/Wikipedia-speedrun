from tkinter import *
from components import topbar, inputFeild, speedrunButton


window = Tk()
window.geometry("620x620")
topbar(window)
inputFeild(window, "Enter First Wikipedia Link")
inputFeild(window, "Enter Second Wikipedia Link")
speedrunButton(window)


if __name__ == "__main__":
    window.mainloop()
