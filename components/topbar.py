from tkinter import PhotoImage


def topbar(window):
    window.title("Wikipedia Speedrun")
    icon = PhotoImage(file="WikipediaSpeedrunIcon.png")
    window.iconphoto(True, icon)
