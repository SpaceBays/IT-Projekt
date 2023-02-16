from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys #Imports sys, used to end the program later

def trylogin():
    if name_entry.get() == "user" and password_entry.get() == "password": #Checks whether username and password are correct
        login.destroy() #Removes the toplevel window
    else:
       messagebox.showwarning("login failed","Please try again" )

def cancel():
    login.destroy() #Removes the toplevel window
    window.destroy() #Removes the hidden root window
    sys.exit() #Ends the script

def trylogin1():
    if cpr_entry.get() == "12345678": #Checks whether username and password are correct
        window.deiconify() #Unhides the root window
        cpr.destroy() #Removes the toplevel window

def cancel1():
    cpr.destroy() #Removes the toplevel window
    window.destroy() #Removes the hidden root window
    sys.exit() #Ends the script


window=Tk()
login=Toplevel()   #this login ui
cpr=Toplevel()

#
login.title("LOGIN-Window")
login.geometry("400x400+400+200")
login.resizable (width=FALSE,height=FALSE)
cpr.title("CPR-Window")
cpr.geometry("400x400+400+200")
cpr.resizable (width=FALSE,height=FALSE)


LABEL_1 = Label(login,text="USER NAME")
LABEL_1.place(x=50,y=100)
LABEL_2 = Label(login,text="PASSWORD")
LABEL_2.place(x=50,y=150)
labelwindow = Label(window, text="This is your main window and you can input anything you want here")
LABEL_1 = Label(cpr,text="CPR-nummer")
LABEL_1.place(x=50,y=100)

BUTTON_1=ttk. Button(login, text="login",command=trylogin)
BUTTON_1.place(x=50,y=200)
BUTTON_1=ttk. Button(login, text="cancel",command=cancel)
BUTTON_1.place(x=200,y=200)
BUTTON_1=ttk. Button(cpr, text="OK",command=trylogin1)
BUTTON_1.place(x=50,y=200)
BUTTON_1=ttk. Button(cpr, text="cancel",command=cancel1)
BUTTON_1.place(x=200,y=200)

name_entry=Entry(login,width=30)
name_entry.place(x=150,y=100)
password_entry=ttk. Entry(login,width=30,show="*")
password_entry.place(x=150,y=150)
cpr_entry=ttk. Entry(cpr,width=30,show="*")
cpr_entry.place(x=150,y=150)


window.withdraw() #This hides the main window, it's still present it just can't be seen or interacted with
window.mainloop() #Starts the event loop for the main window

