from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("250x310")

emptyText = ""

# label widget
emptyEntry = Entry(root, textvariable=emptyText)

# arranging label widgets
emptyEntry.grid(columnspan=5, ipady=4, ipadx=60)

# StringVar() is the variable class
# we create an instance of this class
equation = StringVar()


def press(num):
    # point out the global expression variable
    global emptyEntry

    # concatenation of string
    emptyEntry = emptyEntry + str(num)

    # update the expression by using set method
    equation.set(emptyEntry)


# button widget
one = Button(root, text="1", command=lambda: press(1), height=3, width=7)
# button1 = Button(root, text=' 1 ', fg='black', bg='red', command=lambda: press(1), height=1, width=7)
two = Button(root, text="2", height=3, width=7)
three = Button(root, text="3", height=3, width=7)
four = Button(root, text="4", height=3, width=7)
five = Button(root, text="5", height=3, width=7)
six = Button(root, text="6", height=3, width=7)
seven = Button(root, text="7", height=3, width=7)
eight = Button(root, text="8", height=3, width=7)
nine = Button(root, text="9", height=3, width=7)
zero = Button(root, text="0", height=3, width=7)

# equations
add = Button(root, text="+", height=3, width=7)
subtract = Button(root, text="-", height=3, width=7)
multiply = Button(root, text="*", height=3, width=7)
divide = Button(root, text="%", height=3, width=7)
enter = Button(root, text="enter", height=3, width=34)
clear = Button(root, text="Clear", height=3, width=7)

# arranging button widgets
one.grid(row=2, column=1, sticky=E)
two.grid(row=2, column=2, sticky=E)
three.grid(row=2, column=3, sticky=E)
four.grid(row=3, column=1, sticky=E)
five.grid(row=3, column=2, sticky=E)
six.grid(row=3, column=3, sticky=E)
seven.grid(row=4, column=1, sticky=E)
eight.grid(row=4, column=2, sticky=E)
nine.grid(row=4, column=3, sticky=E)
zero.grid(row=5, column=2, sticky=E)

# equations
add.grid(row=2, column=4, sticky=E)
subtract.grid(row=3, column=4, sticky=E)
multiply.grid(row=4, column=4, sticky=E)
divide.grid(row=5, column=4, sticky=E)
enter.grid(row=6, columnspan=5, sticky=E)
clear.grid(row=5, column=1, sticky=E)



mainloop()