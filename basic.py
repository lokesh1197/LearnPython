from tkinter import *
from random import randint

root = Tk()

myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is Lokesh Mohanty")

# myLabel1.pack()

# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=20)

e = Entry(root, width=35, borderwidth=5)
e.pack()
e.insert(0, "Enter your name...")

def myClick():
    global myButtonLabel
    myButtonLabel = Label(root, text="Hello " + e.get())
    myButtonLabel.pack()
    myButton["state"] = "disabled"

def deleteText():
    if myButtonLabel.winfo_exists():
        myButtonLabel.destroy() # .pack_forget() and .grid_forget() hide the widget
        myButton["state"] = "active"
    else:
        print("myButtonLabel not found")

myButton = Button(root, text="Button", padx=50, command=myClick, fg="yellow",
        bg="green")
myButton.pack()

deleteButton = Button(root, text="Delete", padx=50, command=deleteText)
deleteButton.pack()


# Remove duplicates from a list
entries = [1, 2, 3, 1, 4, 3]
entries_set = set(entries)
unique_entries = list(entries_set)

# Pick a random entry from entries
random_index = randint(0, len(unique_entries) - 1)
entry_label = Label(root, text=unique_entries[random_index])
entry_label.pack()

# 


root.mainloop()
