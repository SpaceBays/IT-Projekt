import tkinter as tk
from tkinter import messagebox
import sys
from matplotlib import animation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3
import datetime


class program(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("1000x800+100+50")
        self.title("")
        self.resizable(False, False)

        menucontainer = tk.Frame(self)
        menucontainer.place(x=0, y=0, width=1000, height=100)
        menu = menuframe(parent=menucontainer, controller=self)
        menu.place(x=0, y=0, width=1000, height=100)

        framecontainer = tk.Frame(self)
        framecontainer.place(x=0, y=100, width=1000, height=700)

        self.frames = {}
        for F in (forsideframe, Graensevaerdierframe, pulsgrafframe, pulsdataframe, SpO2grafframe, SpO2dataframe):
            page_name = F.__name__
            frame = F(parent=framecontainer, controller=self)
            self.frames[page_name] = frame
            frame.place(x=0, y=0, width=1000, height=700)

        self.show_frame("forsideframe")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class menuframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        menu_frame = tk.Frame(self, bg="grey", highlightbackground="black", highlightthickness=2)
        menu_frame.place(x=0, y=0, width=1000, height=100)

        graenseværdier = tk.Button(menu_frame, text="Grænser", font=("Arial", 15),
                                   command=lambda: controller.show_frame("Graensevaerdierframe"))
        graenseværdier.place(x=100, y=30, width=100, heigh=40)

        puls_graf_knap = tk.Button(menu_frame, text="Puls graf", font=("Arial", 15),
                                   command=lambda: controller.show_frame("pulsgrafframe"))
        puls_graf_knap.place(x=300, y=30, width=100, heigh=40)

        puls_data_knap = tk.Button(menu_frame, text="Puls data", font=("Arial", 15),
                                   command=lambda: controller.show_frame("pulsdataframe"))
        puls_data_knap.place(x=450, y=30, width=100, heigh=40)

        SpO2_graf_knap = tk.Button(menu_frame, text="SpO2 graf", font=("Arial", 15),
                                   command=lambda: controller.show_frame("SpO2grafframe"))
        SpO2_graf_knap.place(x=650, y=30, width=100, heigh=40)

        SpO2_data_knap = tk.Button(menu_frame, text="SpO2 data", font=("Arial", 15),
                                   command=lambda: controller.show_frame("SpO2dataframe"))
        SpO2_data_knap.place(x=800, y=30, width=100, heigh=40)

        quit_button = tk.Button(menu_frame, text="Quit", font=("Arial", 15), command=self.quit)
        quit_button.place(x=0, y=0)

    def quit(self):
        message = tk.messagebox.askyesno("Question", "Are you sure you want to quit?")

        if message:
            sys.exit()


class forsideframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        forside_frame = tk.Frame(self, bg="grey", highlightbackground="black", highlightthickness=2)
        forside_frame.place(x=0, y=0, width=1000, height=700)


class Graensevaerdierframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        graensevaerdier_frame = tk.Frame(self, bg="grey", highlightbackground="black", highlightthickness=2)
        graensevaerdier_frame.place(x=0, y=0, width=1000, height=700)

        overskrift = tk.Label(graensevaerdier_frame, bg="grey", text="Grænseværdier", font=("Arial#", 50))
        overskrift.place(x=350, y=30)

        # Puls frame
        frame1 = tk.Frame(graensevaerdier_frame, width=50, height=50, bg="white", highlightbackground="black",
                          highlightthickness=1)
        frame1.pack(expand=True, side=tk.LEFT)

        # minEw puls
        minEw = tk.Label(frame1, text="minEw")
        minEw.pack(fill='x', expand=True)

        self.minEw_entry = tk.Entry(frame1)
        self.minEw_entry.pack(fill='x', expand=True)
        self.minEw_entry.focus()

        maxEw = tk.Label(frame1, text="maxEw")
        maxEw.pack(fill='x', expand=True)

        self.maxEw_entry = tk.Entry(frame1)
        self.maxEw_entry.pack(fill='x', expand=True)
        self.maxEw_entry.focus()

        # minKri puls
        minKri = tk.Label(frame1, text="minKri")
        minKri.pack(fill='x', expand=True)

        self.minKri_entry = tk.Entry(frame1)
        self.minKri_entry.pack(fill='x', expand=True)
        self.minKri_entry.focus()

        # maxKri puls
        maxKri = tk.Label(frame1, text="maxKri")
        maxKri.pack(fill='x', expand=True)

        self.maxKri_entry = tk.Entry(frame1)
        self.maxKri_entry.pack(fill='x', expand=True)
        self.maxKri_entry.focus()

        # Ilt frame
        frame2 = tk.Frame(graensevaerdier_frame, width=10, height=100, bg="red", highlightbackground="black",
                          highlightthickness=1)
        frame2.pack(expand=True, side=tk.RIGHT)

        # EW ilt
        ewIlt = tk.Label(frame2, text="Early warning iltmætning")
        ewIlt.pack(fill='x', expand=True)

        self.ewIlt_entry = tk.Entry(frame2)
        self.ewIlt_entry.pack(fill='x', expand=True)
        self.ewIlt_entry.focus()

        # Kritisk ilt værdi
        kriIlt = tk.Label(frame2, text="Kritisk iltmætning")
        kriIlt.pack(fill='x', expand=True)

        self.kriIlt_entry = tk.Entry(frame2)
        self.kriIlt_entry.pack(fill='x', expand=True)
        self.kriIlt_entry.focus()

        # Midten frame
        frame3 = tk.Frame(graensevaerdier_frame, width=10, height=10, bg="blue")
        frame3.pack(expand=True, side=tk.LEFT)

        # enter button
        enter_button = tk.Button(frame3, text="Enter", command=self.save_grens)
        enter_button.grid(row=1, column=3)

        # default button
        default_button = tk.Button(frame3, text="Default", command=self.default_grens)
        default_button.grid(row=1, column=4)

    def save_grens(self):
        minKri = self.minKri_entry.get()
        minEw = self.minEw_entry.get()
        maxEw = self.maxEw_entry.get()
        maxKri = self.maxKri_entry.get()
        ewIlt = self.ewIlt_entry.get()
        kriIlt = self.kriIlt_entry.get()

        grens = {minKri, minEw, maxEw, maxKri, ewIlt, kriIlt}
        for g in grens:
            if len(g) == 0:
                messagebox.showwarning("Warning", "Manglende værdi. Prøv igen")

        for g in grens:
            if len(g) == 0:
                break
            if len(g) != 0:
                message = tk.messagebox.askyesno("quenstion", "Ønsker du at fortsætte med de valgte værdier?")
                if message:
                    program().show_frame("forsideframe")
                    break
                else:
                    break

    def default_grens(self):
        minKri = 40
        minEw = 60
        maxEw = 100
        maxKri = 120

        ewIlt = 95
        kriIlt = 90

        message = tk.messagebox.askyesno("quenstion", "Ønsker du at fortsætte med default?")
        if message:
            program().show_frame("forsideframe")


class pulsgrafframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        puls_graf_frame = tk.Frame(self, bg="pink", highlightbackground="black", highlightthickness=2)
        puls_graf_frame.place(x=0, y=0, width=1000, height=700)


class pulsdataframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        puls_data_frame = tk.Frame(self, bg="blue", highlightbackground="black", highlightthickness=2)
        puls_data_frame.place(x=0, y=0, width=1000, height=700)


class SpO2dataframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        SpO2_data_frame = tk.Frame(self, bg="yellow", highlightbackground="black", highlightthickness=2)
        SpO2_data_frame.place(x=0, y=0, width=1000, height=700)


class Sensor:
    def __init__(self):
        self.index = 0
        self.pullData = open("SpO2.txt", "r").readlines()
        for i in range(len(self.pullData)):
            self.pullData[i] = self.pullData[i].rstrip()

            try:
                currentDateTime = datetime.datetime.now()

                connection = sqlite3.connect('/Users/rebeccatimm/Desktop/Database.db')
                c = connection.cursor()

                c.execute('INSERT INTO Ilt (Måling, Tid) VALUES (?,?)', (self.pullData[i], currentDateTime,))
                connection.commit()

                c.execute('SELECT Nummer, Måling FROM Ilt ORDER BY Nummer  ASC')
                records = c.fetchall()
                connection.commit()

                self.pullData1 = []
                for row in records:
                    self.pullData1.append(row[1])

            except sqlite3.Error as e:
                print("kommunikationsfejl med database:", e)

            finally:
                c.close()
                connection.close()

    def getdata(self):
        q = self.pullData1[self.index]
        self.index = self.index + 1
        return int(q)


class SpO2grafframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        SpO2_graf_frame = FigureCanvasTkAgg(f, self)
        SpO2_graf_frame.get_tk_widget().place(x=0, y=0, width=1000, height=700)


f = Figure(dpi=150)
a = f.add_subplot(111)

sensor = Sensor()
ilt_data = []
x = []
y = []

def tegn_graf(i):
    ilt_data.append(sensor.getdata())
    x.append(len(ilt_data))
    y = ilt_data
    a.grid(True)
    a.plot(x, y, color="black")
    a.set_title('Graf for SpO2-værdi', fontsize=20)
    a.set_xlabel('Tid i sekunder (s)', fontsize=15)
    a.set_ylabel('SpO2-værdi', fontsize=15)


if __name__ == "__main__":
    Programmet = program()
    graf = animation.FuncAnimation(f, tegn_graf, interval=1500)
    Programmet.mainloop()


    
    
 


________________________________________________________________________________________


import tkinter as tk
from tkinter import messagebox
from matplotlib import animation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3
import datetime
import sys


class program(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("1000x800+100+50")
        self.title("")
        self.resizable(False, False)

        menucontainer = tk.Frame(self)
        menucontainer.place(x=0, y=0, width=1000, height=100)
        menu = menuframe(parent=menucontainer, controller=self)
        menu.place(x=0, y=0, width=1000, height=100)

        framecontainer = tk.Frame(self)
        framecontainer.place(x=0, y=100, width=1000, height=700)

        self.frames = {}
        for F in (forsideframe, Graensevaerdierframe, pulsgrafframe, pulsdataframe, SpO2grafframe, SpO2dataframe):
            page_name = F.__name__
            frame = F(parent=framecontainer, controller=self)
            self.frames[page_name] = frame
            frame.place(x=0, y=0, width=1000, height=700)

        self.show_frame("forsideframe")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class menuframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        menu_frame = tk.Frame(self, bg="grey", highlightbackground="black", highlightthickness=2)
        menu_frame.place(x=0, y=0, width=1000, height=100)

        graenseværdier = tk.Button(menu_frame, text="Grænser", font=("Arial", 15),
                                   command=lambda: self.controller.show_frame("Graensevaerdierframe"))
        graenseværdier.place(x=100, y=30, width=100, heigh=40)

        puls_graf_knap = tk.Button(menu_frame, text="Puls graf", font=("Arial", 15),
                                   command=lambda: self.controller.show_frame("pulsgrafframe"))
        puls_graf_knap.place(x=300, y=30, width=100, heigh=40)

        puls_data_knap = tk.Button(menu_frame, text="Puls data", font=("Arial", 15),
                                   command=lambda: self.controller.show_frame("pulsdataframe"))
        puls_data_knap.place(x=450, y=30, width=100, heigh=40)

        SpO2_graf_knap = tk.Button(menu_frame, text="SpO2 graf", font=("Arial", 15),
                                   command=lambda: self.controller.show_frame("SpO2grafframe"))
        SpO2_graf_knap.place(x=650, y=30, width=100, heigh=40)

        SpO2_data_knap = tk.Button(menu_frame, text="SpO2 data", font=("Arial", 15),
                                   command=lambda: self.controller.show_frame("SpO2dataframe"))
        SpO2_data_knap.place(x=800, y=30, width=100, heigh=40)

        quit_button = tk.Button(menu_frame, text="Quit", font=("Arial", 15), command=self.quit)
        quit_button.place(x=0, y=0)

    def quit(self):
        message = tk.messagebox.askyesno("Question", "Are you sure you want to quit?")

        if message:
            sys.exit()


class forsideframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        forside_frame = tk.Frame(self, bg="grey", highlightbackground="black", highlightthickness=2)
        forside_frame.place(x=0, y=0, width=1000, height=700)


class Graensevaerdierframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        graensevaerdier_frame = tk.Frame(self, bg="grey", highlightbackground="black", highlightthickness=2)
        graensevaerdier_frame.place(x=0, y=0, width=1000, height=700)

        overskrift = tk.Label(graensevaerdier_frame, bg="grey", text="Grænseværdier", font=("Arial#", 50))
        overskrift.place(x=350, y=30)

        # Puls frame
        frame1 = tk.Frame(graensevaerdier_frame, width=50, height=50, bg="white", highlightbackground="black",
                          highlightthickness=1)
        frame1.pack(expand=True, side=tk.LEFT)

        # minEw puls
        minEw = tk.Label(frame1, text="minEw")
        minEw.pack(fill='x', expand=True)

        self.minEw_entry = tk.Entry(frame1)
        self.minEw_entry.pack(fill='x', expand=True)
        self.minEw_entry.focus()

        maxEw = tk.Label(frame1, text="maxEw")
        maxEw.pack(fill='x', expand=True)

        self.maxEw_entry = tk.Entry(frame1)
        self.maxEw_entry.pack(fill='x', expand=True)
        self.maxEw_entry.focus()

        # minKri puls
        minKri = tk.Label(frame1, text="minKri")
        minKri.pack(fill='x', expand=True)

        self.minKri_entry = tk.Entry(frame1)
        self.minKri_entry.pack(fill='x', expand=True)
        self.minKri_entry.focus()

        # maxKri puls
        maxKri = tk.Label(frame1, text="maxKri")
        maxKri.pack(fill='x', expand=True)

        self.maxKri_entry = tk.Entry(frame1)
        self.maxKri_entry.pack(fill='x', expand=True)
        self.maxKri_entry.focus()

        # Ilt frame
        frame2 = tk.Frame(graensevaerdier_frame, width=10, height=100, bg="red", highlightbackground="black",
                          highlightthickness=1)
        frame2.pack(expand=True, side=tk.RIGHT)

        # EW ilt
        ewIlt = tk.Label(frame2, text="Early warning iltmætning")
        ewIlt.pack(fill='x', expand=True)

        self.ewIlt_entry = tk.Entry(frame2)
        self.ewIlt_entry.pack(fill='x', expand=True)
        self.ewIlt_entry.focus()

        # Kritisk ilt værdi
        kriIlt = tk.Label(frame2, text="Kritisk iltmætning")
        kriIlt.pack(fill='x', expand=True)

        self.kriIlt_entry = tk.Entry(frame2)
        self.kriIlt_entry.pack(fill='x', expand=True)
        self.kriIlt_entry.focus()

        # Midten frame
        frame3 = tk.Frame(graensevaerdier_frame, width=10, height=10, bg="blue")
        frame3.pack(expand=True, side=tk.LEFT)

        # enter button
        enter_button = tk.Button(frame3, text="Enter", command=self.save_grens)
        enter_button.grid(row=1, column=3)

        # default button
        default_button = tk.Button(frame3, text="Default", command=self.default_grens)
        default_button.grid(row=1, column=4)

    def save_grens(self):
        minKri = self.minKri_entry.get()
        minEw = self.minEw_entry.get()
        maxEw = self.maxEw_entry.get()
        maxKri = self.maxKri_entry.get()
        ewIlt = self.ewIlt_entry.get()
        kriIlt = self.kriIlt_entry.get()

        grens = {minKri, minEw, maxEw, maxKri, ewIlt, kriIlt}
        for g in grens:
            if len(g) == 0:
                messagebox.showwarning("Warning", "Manglende værdi. Prøv igen")

        for g in grens:
            if len(g) == 0:
                break
            if len(g) != 0:
                message = tk.messagebox.askyesno("quenstion", "Ønsker du at fortsætte med de valgte værdier?")
                if message:
                    self.controller.show_frame("forsideframe")
                    break
                else:
                    break

    def default_grens(self):
        minKri = 40
        minEw = 60
        maxEw = 100
        maxKri = 120

        ewIlt = 95
        kriIlt = 90

        message = tk.messagebox.askyesno("quenstion", "Ønsker du at fortsætte med default?")
        if message:
           self.controller.show_frame("forsideframe")


class pulsgrafframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        puls_graf_frame = tk.Frame(self, bg="pink", highlightbackground="black", highlightthickness=2)
        puls_graf_frame.place(x=0, y=0, width=1000, height=700)


class pulsdataframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        puls_data_frame = tk.Frame(self, bg="blue", highlightbackground="black", highlightthickness=2)
        puls_data_frame.place(x=0, y=0, width=1000, height=700)


class SpO2dataframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        SpO2_data_frame = tk.Frame(self, bg="yellow", highlightbackground="black", highlightthickness=2)
        SpO2_data_frame.place(x=0, y=0, width=1000, height=700)


class Sensor:
    def __init__(self):
        self.index = 0
        self.pullData = open("SpO2.txt", "r").readlines()
        for i in range(len(self.pullData)):
            self.pullData[i] = self.pullData[i].rstrip()

            try:
                currentDateTime = datetime.datetime.now()

                connection = sqlite3.connect('/Users/rebeccatimm/Desktop/Database.db')
                c = connection.cursor()

                c.execute('INSERT INTO Ilt (Måling, Tid) VALUES (?,?)', (self.pullData[i], currentDateTime,))
                connection.commit()

                c.execute('SELECT ID, Måling FROM Ilt ORDER BY ID DESC LIMIT 100')
                records = c.fetchall()
                connection.commit()

                self.pullData1 = []
                for row in reversed(records):
                    self.pullData1.append(row[1])

            except sqlite3.Error as error:
                print("Kommunikationsfejl med databasen:", error)

            finally:
                c.close()
                connection.close()

    def getdata(self):
        q = self.pullData1[self.index]
        self.index = self.index + 1
        return int(q)


class SpO2grafframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        SpO2_graf_frame = FigureCanvasTkAgg(f, self)
        SpO2_graf_frame.get_tk_widget().place(x=0, y=0, width=1000, height=700)


f = Figure(dpi=150)
a = f.add_subplot(111)

sensor = Sensor()
ilt_data = []
x = []
y = []


def tegn_graf(i):
    ilt_data.append(sensor.getdata())
    x.append(len(ilt_data))
    y = ilt_data
    a.grid(True)
    a.plot(x, y, color="black")
    a.set_title('Graf for SpO2-værdi', fontsize=20)
    a.set_xlabel('Tid i sekunder (s)', fontsize=15)
    a.set_ylabel('SpO2-værdi', fontsize=15)


if __name__ == "__main__":
    Programmet = program()
    graf = animation.FuncAnimation(f, tegn_graf, interval=1500)
    Programmet.mainloop()
