from tkinter import Tk, Button, Label, DISABLED, W, E, SUNKEN, PhotoImage
from PIL import ImageTk, Image
import sys, os

program_directory = sys.path[0]


root = Tk()
root.title('Images')
root.iconphoto(True, PhotoImage(file=os.path.join(program_directory, "dragon.gif")))
# icon = Image.open('dragon.gif')
# photo = ImageTk.PhotoImage(icon)
# root.wm_iconphoto(False, photo)
# root.iconbitmap('dragon.ico')
# root.iconphoto(False, PhotoImage(file='/home/lokesh/Repositories/Learn/python/gui/firstGui/images/laptop.ico'))
# root.tk.call('wm', 'iconphoto', root._w, ImageTk.PhotoImage(file='dragon.gif'))

my_image1 = ImageTk.PhotoImage(Image.open("images/random.bmp"))
my_image2 = ImageTk.PhotoImage(Image.open("images/laptop.ico"))

image_list = [my_image1, my_image2]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_image1)
my_label.grid(row=0, column=0, columnspan=3)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 0:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=1)

    # Update status bar
    status = Label(root, text="Image " + str(image_number + 1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == len(image_list) - 1:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=1)

    # Update status bar
    status = Label(root, text="Image " + str(image_number + 1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

button_back = Button(root, text="<<", command=lambda: back())
button_forward = Button(root, text=">>", command=lambda: forward(1))
button_quit = Button(root, text="Exit Program", command=root.quit)

button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=1)
button_quit.grid(row=1, column=2, pady=3)
status.grid(row=2, column=0, columnspan=3, sticky=W+E) # sticky -> stretch, W+E -> west to east

root.mainloop()
