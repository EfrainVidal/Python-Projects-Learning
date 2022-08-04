from tkinter import *

# creating main tkinter window/toplevel
root = Tk()

# set a title and size for the window
root.title("Window")
root.geometry("400x400")

# this will create a label widget
firstname_lbl = Label(text="First Name: ")
lastname_lbl = Label(text="Last Name: ")

# grid method to arrange labels in respective
# rows and columns as specified
firstname_lbl.grid(row=0, column=0, sticky=W, pady=2)
lastname_lbl.grid(row=1, column=0, sticky=W, pady=2)


# entry widgets, used to take entry from user
firstname_entry = Entry(root)
lastname_entry = Entry(root)

# this will arrange entry widgets
firstname_entry.grid(row=0, column=1, pady=2)
lastname_entry.grid(row=1, column=1, pady=2)

# infinite loop which can be terminated by keyboard
# or mouse interrupt

mainloop()