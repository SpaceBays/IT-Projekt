import tkinter as tk        
from tkinter import messagebox

window = tk.Tk()
window.geometry("1000x500")
window.title("window")
window.configure(background="pink")

def openPulswindow():
    newwindow = tk.Tk()
    newwindow.geometry("990x350+10+150")
    newwindow.title("Puls")
    newwindow.configure(background="red")

    label = tk.Label(newwindow, text="Grænseværdier", font=('Arial', 12))
    label.place(x=20, y=25, heig=20, width=90)

    Grænse1 = tk.Entry(newwindow, background="black")
    Grænse1.place(x=30, y=50, heig=30, width=70)

    Grænse2 = tk.Entry(newwindow, background="black")
    Grænse2.place(x=30, y=100, heig=30, width=70)

    Grænse3 = tk.Entry(newwindow, background="black")
    Grænse3.place(x=30, y=150, heig=30, width=70)

    Grænse4 = tk.Entry(newwindow, background="black")
    Grænse4.place(x=30, y=200, heig=30, width=70)

    Grænse5 = tk.Entry(newwindow, background="black")
    Grænse5.place(x=30, y=250, heig=30, width=70)

    textbox1 = tk.Text(newwindow, font=('Arial', 12))
    textbox1.place(x=200, y=25, heig=300, width=300)

    textbox2 = tk.Text(newwindow, font=('Arial', 12))
    textbox2.place(x=600, y=25, heig=300, width=300)

def openSpO2window():
    newwindow = tk.Tk()
    newwindow.geometry("990x350+10+150")
    newwindow.title("SpO2")
    newwindow.configure(background="blue")

    label = tk.Label(newwindow, text="Grænseværdier", font=('Arial', 12))
    label.place(x=20, y=25, heig=20, width=90)

    Grænse1 = tk.Entry(newwindow, background="black")
    Grænse1.place(x=30, y=50, heig=30, width=70)

    Grænse2 = tk.Entry(newwindow, background="black")
    Grænse2.place(x=30, y=100, heig=30, width=70)

    Grænse3 = tk.Entry(newwindow, background="black")
    Grænse3.place(x=30, y=150, heig=30, width=70)

    Grænse4 = tk.Entry(newwindow, background="black")
    Grænse4.place(x=30, y=200, heig=30, width=70)

    Grænse5 = tk.Entry(newwindow, background="black")
    Grænse5.place(x=30, y=250, heig=30, width=70)

    textbox1 = tk.Text(newwindow, font=('Arial', 12))
    textbox1.place(x=200, y=25, heig=300, width=300)

    textbox2 = tk.Text(newwindow, font=('Arial', 12))
    textbox2.place(x=600, y=25, heig=300, width=300)

def quit():
    message = tk.messagebox.askyesno("Question","Are you sure you want to quit?")

    if message:
        window.destroy()

label = tk.Label(window, text="Patientoplysninger", font=('Arial', 15))
label.place(x=230, y=200, heig=200, width=600)

Puls_button = tk.Button(window, text="Puls", font=('Arial', 25))
Puls_button.place(x=400, y=40, heig=50, width=100)
Puls_button['command'] = openPulswindow

SpO2_button = tk.Button(window, text="SpO2", font=('Arial', 25))
SpO2_button.place(x=550, y=40, heig=50, width=100)
SpO2_button['command'] = openSpO2window

quit_button = tk.Button(window, text="Quit")
quit_button.place(x=930, y=470, heig=30, width=70)
quit_button['command'] = quit

window.mainloop()



hej
