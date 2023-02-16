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





#__________________________________________________________

# forslag til forbedring af ovenstående program

import tkinter as tk
from tkinter import messagebox
import sys

def trylogin():
    if username_entry.get() == "user" and password_entry.get() == "password":
        login.destroy() #lukker login-vinduet
        cpr.deiconify() #åbner cpr-vinduet, som indstil nu var skjult i baggrunden
    else:
       messagebox.showwarning("login failed","Please try again" )

def tryCPR():
    if cpr_entry.get() == "12345678": #Checks whether username and password are correct
        cpr.destroy()       # lukker cpr-vinduet
        window.deiconify()  # åbner hovedprogrammet, som indtil nu var skjult i baggrunden
    else:
       messagebox.showwarning("Unknown CPR","Please try again" )

def quit():
    message = tk.messagebox.askyesno("Question","Are you sure you want to quit?")

    if message:
        sys.exit()  #lukker systeemet hvis der svares "ja" til ovenstående besked

        
# Opretter og skjuler hovedprogram i baggrunden
window=tk.Tk()
window.withdraw()


# opretter loginvindue, som bliver vist som det første
login=tk.Toplevel()
login.title("Login")
login.geometry("340x440+400+200")
login.configure(bg="#333333")
login.resizable (width=False,height=False)

login_frame = tk.Frame(login, bg="#333333")

login_label=tk.Label(login_frame,text="Login", bg="#333333", fg="white", font=("Arial",30))
login_label.grid(row=0,column=0,columnspan=2, sticky="news", pady=40)

username_label = tk.Label(login_frame, text="USER NAME", bg="#333333", fg="white", font=("Arial",15))
username_label.grid(row=1,column=0)
username_entry = tk.Entry(login_frame, font=("Arial",15))
username_entry.grid(row=1,column=1,pady=10)

password_label=tk.Label(login_frame,text="PASSWORD", bg="#333333", fg="white", font=("Arial",15))
password_label.grid(row=2,column=0)
password_entry=tk.Entry(login_frame, show="*", font=("Arial",15))
password_entry.grid(row=2,column=1,pady=10)

login_button = tk.Button(login_frame, text="Login", font=("Arial",15),command=trylogin)
login_button.grid(row=3,column=0,columnspan=2, pady=30)
quit_button = tk.Button(login_frame, text="Quit", font=("Arial",15),command=quit)
quit_button.grid(row=3,column=1,columnspan=2, pady=30, padx=30)

login_frame.pack()


# opretter CPR-vindue - bliver vist efter login
cpr=tk.Toplevel()
cpr.withdraw()      #denne skuler cpr-vinduet (det vil kun åbne, hvis login er en succes, se deflogin)
cpr.title("CPR")
cpr.geometry("340x440+400+200")
cpr.configure(bg="#333333")
cpr.resizable (width=False,height=False)

cpr_frame = tk.Frame(cpr, bg="#333333")

cpr_label=tk.Label(cpr_frame,text="CPR", bg="#333333", fg="white", font=("Arial",30))
cpr_label.grid(row=0,column=0,columnspan=2, sticky="news", pady=40)

cpr_label = tk.Label(cpr_frame, text="CPR-nummer", bg="#333333", fg="white", font=("Arial",15))
cpr_label.grid(row=1,column=0)
cpr_entry = tk.Entry(cpr_frame,show="*", font=("Arial",15))
cpr_entry.grid(row=1,column=1,pady=10)

cpr_button = tk.Button(cpr_frame, text="OK", font=("Arial",15),command=tryCPR)
cpr_button.grid(row=3,column=0,columnspan=2, pady=30, padx=30)
quit_button = tk.Button(cpr_frame, text="Quit", font=("Arial",15),command=quit)
quit_button.grid(row=3,column=1,columnspan=2, pady=30, padx=30)

cpr_frame.pack()


# åbner hovedprogram, hvor man først kommer ind til grænseværdier
window.geometry("1500x800+100+50")

window.mainloop() #Starts the event loop for the main window


