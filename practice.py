from tkinter import *

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
    myButtonLabel = Label(root, text="Hello " + e.get())
    myButtonLabel.pack()

myButton = Button(root, text="Button", padx=50, command=myClick, fg="yellow",
        bg="green")
myButton.pack()


root.mainloop()
