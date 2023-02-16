from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys #Imports sys, used to end the program later

def trylogin():
    if name_entry.get() == "user" and password_entry.get() == "password": #Checks whether username and password are correct
        window.deiconify() #Unhides the root window
        top.destroy() #Removes the toplevel window
    else:
       messagebox.showwarning("login failed","Please try again" )

def cancel():
    top.destroy() #Removes the toplevel window
    window.destroy() #Removes the hidden root window
    sys.exit() #Ends the script


window=Tk()
top=Toplevel()                #this login ui

top.title("LOGIN-Window")
top.geometry("400x400+400+200")
top.resizable (width=FALSE,height=FALSE)

LABEL_1 = Label(top,text="USER NAME")
LABEL_1.place(x=50,y=100)
LABEL_2 = Label(top,text="PASSWORD")
LABEL_2.place(x=50,y=150)
labelwindow = Label(window, text="This is your main window and you can input anything you want here")

BUTTON_1=ttk. Button(top, text="login",command=trylogin)
BUTTON_1.place(x=50,y=200)
BUTTON_1=ttk. Button(top, text="cancel",command=cancel)
BUTTON_1.place(x=200,y=200)

name_entry=Entry(top,width=30)
name_entry.place(x=150,y=100)
password_entry=ttk. Entry(top,width=30,show="*")
password_entry.place(x=150,y=150)

window.withdraw() #This hides the main window, it's still present it just can't be seen or interacted with
window.mainloop() #Starts the event loop for the main window


