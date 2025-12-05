from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("Enter Title Here")

#Set size of window
root.geometry("300x150")

# Create buttons
red_button = Button(root, text="Red", background='red')
red_button = Button(root, text="Yellow", background='yellow')
red_button = Button(root, text="Green", background='Green')

#Add a label
label = Label(root, text="This is a spotlight")

# Place widgets in window (with pack function!)
label.pack()
red_button.pack()

Text(root, height = 5, width = 52)

# Start the GUI event loop
root.mainloop()