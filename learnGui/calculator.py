from tkinter import Tk, Entry, Label, Button, StringVar, DoubleVar, END

root = Tk()
root.title("Simple Calculator")

firstNumber = DoubleVar()
:qa

operation = StringVar()

operations = { 'add': '+', 'subtract': '-', 'multiply': '*', 'divide': '/', 'none': '' }

display = Entry(root, width=45)
display.grid(row=0, columnspan=4, ipady=20, ipadx=5)

def buttonClickfn(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, str(current) + str(number))

def buttonClrfn():
    display.delete(0, END)

def buttonAddfn(operation, firstNumber):
    if operation.get() != "":
        buttonEqfn(operation, firstNumber)

    firstNumber.set(float(display.get()))
    operation.set(operations['add'])
    display.delete(0, END)
    return

def buttonSubfn(operation, firstNumber):
    if operation.get() != "":
        buttonEqfn(operation, firstNumber)

    firstNumber.set(float(display.get()))
    operation.set(operations['subtract'])
    display.delete(0, END)
    return

def buttonMulfn(operation, firstNumber):
    if operation.get() != "":
        buttonEqfn(operation, firstNumber)

    firstNumber.set(float(display.get()))
    operation.set(operations['multiply'])
    display.delete(0, END)
    return

def buttonDivfn(operation, firstNumber):
    if operation.get() != "":
        buttonEqfn(operation, firstNumber)

    firstNumber.set(float(display.get()))
    operation.set(operations['divide'])
    display.delete(0, END)
    return

def buttonEqfn(operation, firstNumber):
    if operation.get() != "":
        secondNumber = float(display.get())
        display.delete(0, END)
        result = 0
        if operation.get() == operations['add']:
            result = firstNumber.get() + secondNumber
        if operation.get() == operations['subtract']:
            result = firstNumber.get() - secondNumber
        if operation.get() == operations['multiply']:
            result = firstNumber.get() * secondNumber
        if operation.get() == operations['divide']:
            result = firstNumber.get() / secondNumber
        display.insert(0, str(result))
        operation.set('')
        firstNumber.set(0)
    return

def buttonDotfn():
    return

button00 = Button(root, text="00", padx=40, pady=20, command=lambda: buttonClickfn('00'))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonClickfn(0))
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonClickfn(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonClickfn(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonClickfn(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonClickfn(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonClickfn(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonClickfn(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonClickfn(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonClickfn(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonClickfn(9))
buttonDot = Button(root, text=".", padx=40, pady=20, command=lambda: buttonDotfn())
buttonAdd = Button(root, text="+", padx=40, pady=20, command=lambda: buttonAddfn(operation, firstNumber))
buttonSub = Button(root, text="-", padx=40, pady=20, command=lambda: buttonSubfn(operation, firstNumber))
buttonDiv = Button(root, text="/", padx=40, pady=20, command=lambda: buttonDivfn(operation, firstNumber))
buttonMul = Button(root, text="x", padx=40, pady=20, command=lambda: buttonMulfn(operation, firstNumber))
buttonClr = Button(root, text="Clear", padx=80, pady=20, command=buttonClrfn)
buttonEq = Button(root, text="=", padx=80, pady=20, command=lambda: buttonEqfn(operation, firstNumber))


button00.grid(row=4, column=1)
button0.grid(row=4, column=0)
button1.grid(row=3, column=2)
button2.grid(row=3, column=1)
button3.grid(row=3, column=0)
button4.grid(row=2, column=2)
button5.grid(row=2, column=1)
button6.grid(row=2, column=0)
button7.grid(row=1, column=2)
button8.grid(row=1, column=1)
button9.grid(row=1, column=0)
buttonDot.grid(row=4, column=2)
buttonAdd.grid(row=1, column=3)
buttonSub.grid(row=2, column=3)
buttonDiv.grid(row=3, column=3)
buttonMul.grid(row=4, column=3)
buttonClr.grid(row=5, column=0, columnspan=2)
buttonEq.grid(row=5, column=2, columnspan=2)

root.mainloop()
