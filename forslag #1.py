import tkinter as tk
from tkinter import messagebox
import sys

class program(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("1500x800+100+50")

        self.menucontainer = tk.Frame(self, bg="pink")
        self.menucontainer.place(x=0, y=0, width=1500, height=100)
        self.menucontainer.grid_rowconfigure(0, weight=1)
        self.menucontainer.grid_columnconfigure(0, weight=1)
        menu = menuframe(parent=self.menucontainer, controller=self)
        menu.place(x=0, y=0, width=1500, height=100)

        self.container = tk.Frame(self)
        self.container.place(width=1500, height=800)
        self.container.pack( fill="both", expand=True, padx=0,pady=100)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (forsideframe,Graensevaerdierframe, pulsgrafframe, pulsdataframe, SpO2grafframe, SpO2dataframe):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.place(x=0, y=0, width=1500, height=800)

        self.show_frame("forsideframe")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class menuframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.menu_frame = tk.Frame(self, bg="grey", highlightbackground="black", highlightthickness=2)
        self.menu_frame.place(x=0, y=0, width=1500, height=100)

        self.graenseværdier = tk.Button(self, text="Grænser", font=("Arial", 15), command=lambda: controller.show_frame("Graensevaerdierframe"))
        self.graenseværdier.place(x=200, y=30, width=100, heigh=40)

        self.puls_graf_knap = tk.Button(self, text="Puls graf", font=("Arial", 15), command=lambda: controller.show_frame("pulsgrafframe"))
        self.puls_graf_knap.place(x=450, y=30, width=100, heigh=40)

        self.puls_data_knap = tk.Button(self, text="Puls data", font=("Arial", 15), command=lambda: controller.show_frame("pulsdataframe"))
        self.puls_data_knap.place(x=600, y=30, width=100, heigh=40)

        self.SpO2_graf_knap = tk.Button(self, text="SpO2 graf", font=("Arial", 15), command=lambda: controller.show_frame("SpO2grafframe"))
        self.SpO2_graf_knap.place(x=850, y=30, width=100, heigh=40)

        self.SpO2_data_knap = tk.Button(self, text="SpO2 data", font=("Arial", 15), command=lambda: controller.show_frame("SpO2dataframe"))
        self.SpO2_data_knap.place(x=1000, y=30, width=100, heigh=40)

        self.quit_button = tk.Button(self, text="Quit", font=("Arial", 15), command=self.quit)
        self.quit_button.place(x=0, y=0)

    def quit(self):
        message = tk.messagebox.askyesno("Question", "Are you sure you want to quit?")

        if message:
            sys.exit()

class forsideframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.forside_frame = tk.Frame(self, bg="grey", highlightbackground="black", highlightthickness=2)
        self.forside_frame.place(x=0, y=0, width=1500, height=700)

class Graensevaerdierframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.graensevaerdier_frame = tk.Frame(self, bg="black", highlightbackground="black", highlightthickness=2)
        self.graensevaerdier_frame.place(x=0, y=0, width=1500, height=700)

class pulsgrafframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.puls_graf_frame = tk.Frame(self, bg="pink", highlightbackground="black", highlightthickness=2)
        self.puls_graf_frame.place(x=0, y=0, width=1500, height=700)

class pulsdataframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.puls_data_frame = tk.Frame(self, bg="blue", highlightbackground="black", highlightthickness=2)
        self.puls_data_frame.place(x=0, y=0, width=1500, height=700)

class SpO2grafframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.SpO2_graf_frame = tk.Frame(self, bg="green", highlightbackground="black", highlightthickness=2)
        self.SpO2_graf_frame.place(x=0, y=0, width=1500, height=700)

class SpO2dataframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.SpO2_data_frame = tk.Frame(self, bg="yellow", highlightbackground="black", highlightthickness=2)
        self.SpO2_data_frame.place(x=0, y=0, width=1500, height=700)

if __name__ == "__main__":
    app = program()
    app.mainloop()
