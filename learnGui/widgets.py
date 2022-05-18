from tkinter import Tk, LabelFrame, Button, Radiobutton, IntVar, Label, StringVar, W, messagebox, Toplevel, filedialog, Checkbutton, OptionMenu, Scale, HORIZONTAL, Listbox, Scrollbar
from PIL import ImageTk, Image

root = Tk()
root.title('Learn basic widgets')
root.geometry("800x600")

# frame = LabelFrame(root, padx=5, pady=5) # padding inside the frame
radio_frame = LabelFrame(root, text="RadioButton", padx=5, pady=5)
radio_frame.grid(row=0, column=0, padx=10, pady=10) # padding outsie the frame

# r = StringVar()
# r.set('1')

MODES = [
    ("Mango", "Mango"),
    ("Orange", "Orange"),
]

fruit = StringVar()
fruit.set("Mango")

for text, mode in MODES:
    Radiobutton(radio_frame, text=text, variable=fruit, value=mode).pack(anchor=W)

def clicked(frame, text):
    my_label = Label(frame, text=text).pack()

# Radiobutton(frame, text="Option 1", variable=r, value=1, command=lambda: clicked('1')).pack()
# Radiobutton(frame, text="Option 2", variable=r, value=2, command=lambda: clicked('2')).pack()

button = Button(radio_frame, text="Click", command=lambda: clicked(radio_frame, fruit.get()))
button.pack()

message_frame = LabelFrame(root, text="MessageBox", padx=5, pady=5)
message_frame.grid(row=0, column=1, padx=10, pady=10)

def popup():
    # showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
    response = messagebox.askyesno("My Popup", "Hello World")
    if response == 1:
        Label(message_frame, text="You clicked yes").pack()
    else:
        Label(message_frame, text="You clicked no").pack()

Button(message_frame, text="Popup", command=popup).pack()

duration = StringVar()

checkbox_frame = LabelFrame(root, text="CheckBox", padx=5, pady=5)
checkbox_frame.grid(row=0, column=2, padx=10 ,pady=10)
checkbox = Checkbutton(checkbox_frame, text="Weekly", variable=duration, onvalue="Weekly", offvalue="Daily",
        command=lambda: clicked(checkbox_frame, duration.get()))
checkbox.pack()
checkbox.deselect()

selected = StringVar()
selected.set("Sunday")

options = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
dropdown_frame = LabelFrame(root, text="DropDown", padx=5, pady=5)
dropdown_frame.grid(row=0, column=3, padx=10 ,pady=10)
# dropdown = OptionMenu(dropdown_frame, selected, "Monday", "Tuesday", "Wednesday", "Thursday", "Sunday", command=lambda: clicked(dropdown_frame, selected.get()))
dropdown = OptionMenu(dropdown_frame, selected, *options)
dropdown.pack()
Button(dropdown_frame, text="Click", command=lambda: clicked(dropdown_frame, selected.get())).pack()


def slide(var):
    Label(slider_frame, text="(" + str(horizontal.get()) + ", " + str(vertical.get()) + ")").pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

slider_frame = LabelFrame(root, text="Slider", padx=5, pady=5)
slider_frame.grid(row=0, column=4, padx=10, pady=10)
vertical = Scale(slider_frame, from_=200, to=800, command=slide)
horizontal = Scale(slider_frame, from_=400, to=1200, orient=HORIZONTAL)
vertical.pack()
horizontal.pack()
# Button(slider_frame, text="Change dimensions", command=slide).pack()

def open():
    global my_img
    window = Toplevel()
    window.title('My Second Window')
    my_img = ImageTk.PhotoImage(Image.open("/home/lokesh/Pictures/earth.jpg"))
    Label(window, image=my_img).pack()
    Button(window, text="Close", command=window.destroy).pack()

Button(root, text="Open Second Window", command=open).grid(row=1, column=0)

def open_file():
    global my_img
    filename = filedialog.askopenfilename(initialdir="/home/lokesh/Pictures", title="Select an image", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    my_img = ImageTk.PhotoImage(Image.open(filename))
    window = Toplevel()
    window.title(filename)
    Label(window, image=my_img).pack()
    Button(window, text="Close", command=window.destroy).pack()

Button(root, text="Open Image", command=open_file).grid(row=1, column=1)

listbox_frame = LabelFrame(root, text="Listbox")
listbox_frame.grid(row=2, column=0)
listbox_scrollbar = Scrollbar(listbox_frame, orient="vertical")

# SINGLE, MULTIPLE, EXTENDED, BROWSE
listbox = Listbox(listbox_frame, width=50, yscrollcommand=listbox_scrollbar)
listbox.pack(pady=15)

listbox_scrollbar.config(command=listbox.yview)
listbox_scrollbar.pack(side="right", fill="y")

listbox_items = ["One", "Two", "Three", "Two", "Three", "Two", "Three", "Two", "Three", "Two", "Three", "Two", "Three", "Two", "Three", "Two", "Three", "Two", "Three", "Two", "Three", "Two", "Three", "Two", "Three", "Two", "Three"]

for item in listbox_items:
    listbox.insert("end", item)



def delete():
    listbox.delete("anchor")
    listbox_label.config(text="")

def select():
    listbox_label.config(text=listbox.get("anchor"))

delete_button = Button(listbox_frame, text="Delete", command=delete)
delete_button.pack(pady=10)
select_button = Button(listbox_frame, text="Select", command=select)
select_button.pack(pady=10)

listbox_label = Label(listbox_frame, text='')
listbox_label.pack(pady=5)

root.mainloop()
