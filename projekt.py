
from tkinter import * #Imports Tkinter
import sys #Imports sys, used to end the program later

root=Tk() #Declares root as the tkinter main window
top = Toplevel() #Creates the toplevel window

entry1 = Entry(top) #Username entry
entry2 = Entry(top) #Password entry
button1 = Button(top, text="Login", command=lambda:command1()) #Login button
button2 = Button(top, text="Cancel", command=lambda:command2()) #Cancel button
label1 = Label(root, text="This is your main window and you can input anything you want here")

def command1():
    if entry1.get() == "ida" and entry2.get() == "1234": #Checks whether username and password are correct
        root.deiconify() #Unhides the root window
        top.destroy() #Removes the toplevel window

def command2():
    top.destroy() #Removes the toplevel window
    root.destroy() #Removes the hidden root window
    sys.exit() #Ends the script


Main_window.geometry("600x500+300+100")

MENU_1 = Menu(Main_window)
Main_window.config(menu=MENU_1)

SETTINGS_1 = Menu(MENU_1,tearoff=0)
MENU_1.add_cascade(label="SETTINGS",menu=SETTINGS_1,underline=0)
SETTINGS_1.add_command(label="Change Password")

Main_window. mainloop()


root.withdraw() #This hides the main window, it's still present it just can't be seen or interacted with
root.mainloop() #Starts the event loop for the main window


