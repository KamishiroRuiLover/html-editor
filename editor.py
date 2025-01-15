from tkinter import *
from tkinter import simpledialog


# Globals #
open_proj = "none"


# Functions #
def make_proj(name):
    file = open("projects/" + name + ".wpro", "w")
    
    global open_proj
    open_proj = name

    noFileWidget.destroy()

    noFileWidget2 = Label(siteEditor, text="No File Open")
    noFileWidget2.place(relx=0.5, rely=0.5, anchor=CENTER)


def new_proj():
    uinput = simpledialog.askstring("New Project", "Enter Project Name:")
    make_proj(uinput)


def open_frame(frame):
    frame.tkraise()


# Tkinter Initialization #
root = Tk()
root.title("HTML Editor")


# Tkinter Menu #
barMenu = Menu(root)

barMenuFile = Menu(barMenu)
barMenu.add_cascade(label="Project", menu=barMenuFile)
barMenuFile.add_command(label="Open")
barMenuFile.add_command(label="New", command=new_proj)

barMenuEditor = Menu(barMenu)
barMenu.add_cascade(label="Editor")

root.config(menu=barMenu)


## Tkinter Frames ##
# website editor #
siteEditor = Frame(root)
noFileWidget = Label(siteEditor, text="Open Project To Continue")
noFileWidget.place(relx=0.5, rely=0.5, anchor=CENTER)

siteEditor.place(relwidth=1, relheight=1)

# FILE END #
open_frame(siteEditor)

root.mainloop()