# IT-Projekt

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from matplotlib import animation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3
import datetime
import sys

class Program(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("1000x800+100+50")
        self.title("")
        self.resizable(False, False)

        menucontainer = tk.Frame(self)
        menucontainer.place(x=0, y=0, width=1000, height=100)
        menu = menuframe(parent=menucontainer, controller=self)
        menu.place(x=0, y=0, width=1000, height=100)

        framescontainer = tk.Frame(self)
        framescontainer.place(x=0, y=100, width=1000, height=700)

        self.frames = {}
        for Frame in (frontpageframe, limitsframe, pulsegraphframe, pulsedataframe, SpO2graphframe, SpO2dataframe):
            page_name = Frame.__name__
            frame = Frame(parent=framescontainer, controller=self)
            self.frames[page_name] = frame
            frame.place(x=0, y=0, width=1000, height=700)

        self.show_frame("frontpageframe")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class menuframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        menu_frame = tk.Frame(self, bg="grey", highlightbackground="black", highlightthickness=2)
        menu_frame.place(x=0, y=0, width=1000, height=100)

        limits_button = tk.Button(menu_frame, text="Limits", font=("Arial", 15), command=lambda: self.controller.show_frame("limitsframe"))
        limits_button.place(x=100, y=30, width=100, heigh=40)

        pulse_graph_button = tk.Button(menu_frame, text="Pulse Graph", font=("Arial", 15), command=lambda: self.controller.show_frame("pulsegraphframe"))
        pulse_graph_button.place(x=300, y=30, width=100, heigh=40)

        pulse_data_button = tk.Button(menu_frame, text="Pulse Data", font=("Arial", 15), command=lambda: self.controller.show_frame("pulsedataframe"))
        pulse_data_button.place(x=450, y=30, width=100, heigh=40)

        SpO2_graph_button = tk.Button(menu_frame, text="SpO2 Graph", font=("Arial", 15), command=lambda: self.controller.show_frame("SpO2graphframe"))
        SpO2_graph_button.place(x=650, y=30, width=100, heigh=40)

        SpO2_data_button = tk.Button(menu_frame, text="SpO2 Data", font=("Arial", 15), command=lambda: self.controller.show_frame("SpO2dataframe"))
        SpO2_data_button.place(x=800, y=30, width=100, heigh=40)

        quit_button = tk.Button(menu_frame, text="Quit", font=("Arial", 15), command=self.quit)
        quit_button.place(x=0, y=0)

    def quit(self):
        message = tk.messagebox.askyesno("Question", "Are you sure you want to quit?")

        if message:
            sys.exit()


class frontpageframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frontpage_frame = tk.Frame(self, bg="grey", highlightbackground="black", highlightthickness=2)
        frontpage_frame.place(x=0, y=0, width=1000, height=700)


class limitsframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        limits_frame = tk.Frame(self, bg="grey", highlightbackground="black", highlightthickness=2)
        limits_frame.place(x=0, y=0, width=1000, height=700)
        heading_label = tk.Label(limits_frame, bg="grey", text="Limits", font=("Arial#", 50))
        heading_label.place(x=430, y=30)

        # Pulse frame
        pulse_limits_frame = tk.Frame(limits_frame, width=50, height=50, highlightbackground="black",highlightthickness=1)
        pulse_limits_frame .pack(expand=True, side=tk.LEFT)

        pulse_minearlywarning_label = tk.Label(pulse_limits_frame, text="Pulse - Min Early Warning")
        pulse_minearlywarning_label.pack(fill='x', expand=True)
        self.pulse_minearlywarning_entry = tk.Entry(pulse_limits_frame)
        self.pulse_minearlywarning_entry.pack(fill='x', expand=True)
        self.pulse_minearlywarning_entry.focus()

        pulse_maxearlywarning_label = tk.Label(pulse_limits_frame , text="Pulse - Max Early Warning")
        pulse_maxearlywarning_label.pack(fill='x', expand=True)
        self.pulse_maxearlywarning_entry = tk.Entry(pulse_limits_frame)
        self.pulse_maxearlywarning_entry.pack(fill='x', expand=True)
        self.pulse_maxearlywarning_entry.focus()

        pulse_mincritical_label = tk.Label(pulse_limits_frame , text="Pulse - Min Critical")
        pulse_mincritical_label.pack(fill='x', expand=True)
        self.pulse_mincritical_entry = tk.Entry(pulse_limits_frame )
        self.pulse_mincritical_entry.pack(fill='x', expand=True)
        self.pulse_mincritical_entry.focus()

        pulse_maxcritical_label = tk.Label(pulse_limits_frame , text="SpO2 - Max Critical")
        pulse_maxcritical_label.pack(fill='x', expand=True)
        self.pulse_maxcritical_entry = tk.Entry(pulse_limits_frame)
        self.pulse_maxcritical_entry.pack(fill='x', expand=True)
        self.pulse_maxcritical_entry.focus()

        # SpO2 frame
        SpO2_limits_frame = tk.Frame(limits_frame, width=10, height=100, highlightbackground="black", highlightthickness=1)
        SpO2_limits_frame.pack(expand=True, side=tk.RIGHT)

        SpO2_earlywarning_label = tk.Label(SpO2_limits_frame, text="SpO2 - Early warning")
        SpO2_earlywarning_label.pack(fill='x', expand=True)
        self.SpO2_earlywarning_entry = tk.Entry(SpO2_limits_frame)
        self.SpO2_earlywarning_entry.pack(fill='x', expand=True)
        self.SpO2_earlywarning_entry.focus()

        SpO2_critical_label = tk.Label(SpO2_limits_frame, text="SpO2 - Critical")
        SpO2_critical_label.pack(fill='x', expand=True)
        self.SpO2_critical_entry = tk.Entry(SpO2_limits_frame)
        self.SpO2_critical_entry.pack(fill='x', expand=True)
        self.SpO2_critical_entry.focus()

        # Middle frame
        middle_frame = tk.Frame(limits_frame, width=10, height=10, bg="blue")
        middle_frame.pack(expand=True, side=tk.LEFT)
        enter_button = tk.Button(middle_frame, text="Enter", command=self.save_limits)
        enter_button.grid(row=1, column=3)
        default_button = tk.Button(middle_frame, text="Default", command=self.default_limits)
        default_button.grid(row=1, column=4)

    def save_limits(self):
        Pulse_mincritical = self.pulse_mincritical_entry.get()
        Pulse_minearlywarning = self.pulse_minearlywarning_entry.get()
        Pulse_maxearlywarning = self.pulse_maxearlywarning_entry.get()
        Pulse_maxcritical = self.pulse_maxcritical_entry.get()
        SpO2_earlywarning = self.SpO2_earlywarning_entry.get()
        SpO2_critical = self.SpO2_critical_entry.get()

        limits = {Pulse_mincritical, Pulse_minearlywarning, Pulse_maxearlywarning, Pulse_maxcritical, SpO2_earlywarning, SpO2_critical}
        for l in limits:
            if len(l) == 0:
                messagebox.showwarning("Warning", "Missing limit(s). Try again")

        for l in limits:
            if len(l) == 0:
                break
            if len(l) != 0:
                message = tk.messagebox.askyesno("quenstion", "Do you want to continue?")
                if message:
                    self.controller.show_frame("frontpageframe")
                    break
                else:
                    break

    def default_limits(self):
        Pulse_mincritical = 40
        Pulse_minearlywarning = 60
        Pulse_maxearlywarning = 100
        Pulse_maxcritical = 120

        SpO2_earlywarning = 95
        SpO2_critical = 90

        message = tk.messagebox.askyesno("quenstion", "Do you want to continue with default?")
        if message:
           self.controller.show_frame("frontpageframe")


class SpO2Sensor:
    def __init__(self):
        self.index = 0
        self.pullData = open("SpO2.txt", "r").readlines()
        for i in range(len(self.pullData)):
            self.pullData[i] = self.pullData[i].rstrip()

            try:
                currentDateTime = datetime.datetime.now()

                connection = sqlite3.connect('/Users/rebeccatimm/Desktop/Database.db')
                c = connection.cursor()

                c.execute('INSERT INTO SpO2 (Data, Time) VALUES (?,?)', (self.pullData[i], currentDateTime,))
                connection.commit()

                c.execute('SELECT ID, Data FROM SpO2 ORDER BY ID DESC LIMIT 20')
                records = c.fetchall()
                connection.commit()

                self.pullData1 = []
                for row in reversed(records):
                    self.pullData1.append(row[1])

            except sqlite3.Error as error:
                print("Communicationerror with Database:", error)

            finally:
                c.close()
                connection.close()

    def getdata(self):
        q = self.pullData1[self.index]
        self.index = self.index + 1
        return int(q)

class SpO2graphframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        SpO2_graph_frame = FigureCanvasTkAgg(SpO2graph, self)
        SpO2_graph_frame.get_tk_widget().place(x=0, y=0, width=1000, height=700)

SpO2graph = Figure(dpi=150)
a = SpO2graph.add_subplot(111)

SpO2Sensor = SpO2Sensor()
SpO2_data = []
x = []
y = []

def draw_SpO2_graph(i):
    SpO2_data.append(SpO2Sensor.getdata())
    x.append(len(SpO2_data))
    y = SpO2_data
    a.grid(True)
    a.plot(x, y, color="black")
    a.set_title('SpO2 Graph', fontsize=20)
    a.set_xlabel('Time in seconds (s)', fontsize=15)
    a.set_ylabel('SpO2-Data', fontsize=15)


class SpO2dataframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        try:
            connection = sqlite3.connect('/Users/rebeccatimm/Desktop/Database.db')
            c = connection.cursor()

            c.execute("SELECT Data FROM SpO2 ORDER BY ID DESC LIMIT 20")
            records = c.fetchall()
            connection.commit()

            SpO2_Data_label = Label(self, width=60, text='SpO2 Data', borderwidth=5, relief='flat', anchor='w')
            SpO2_Data_label.grid(row=0, column=0)

            i = 1
            for data in reversed(records):
                for j in range(len(data)):
                    x = Entry(self, width=60)
                    x.grid(row=i, column=j)
                    x.insert(END, data[j])
                    x.configure(state='disabled')
                i = i + 1

        except sqlite3.Error as error:
            print("Communicationerror with Database:", error)

        finally:
            c.close()
            connection.close()


class PulseSensor:
    def __init__(self):
        self.index = 0
        self.pullData = open("Puls.txt", "r").readlines()
        for i in range(len(self.pullData)):
            self.pullData[i] = self.pullData[i].rstrip()

            try:
                currentDateTime = datetime.datetime.now()

                connection = sqlite3.connect('/Users/rebeccatimm/Desktop/Database.db')
                c = connection.cursor()

                c.execute('INSERT INTO Pulse (Data, Time) VALUES (?,?)', (self.pullData[i], currentDateTime,))
                connection.commit()

                c.execute('SELECT ID, Data FROM Pulse ORDER BY ID DESC LIMIT 20')
                records = c.fetchall()
                connection.commit()

                self.pullData1 = []
                for row in reversed(records):
                    self.pullData1.append(row[1])

            except sqlite3.Error as error:
                print("Communicationerror with Database:", error)

            finally:
                c.close()
                connection.close()

    def getdata(self):
        q = self.pullData1[self.index]
        self.index = self.index + 1
        return int(q)


class pulsegraphframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        pulse_graph_frame = FigureCanvasTkAgg(Pulsegraph, self)
        pulse_graph_frame.get_tk_widget().place(x=0, y=0, width=1000, height=700)

Pulsegraph = Figure(dpi=150)
b = Pulsegraph.add_subplot(111)

PulseSensor = PulseSensor()
Pulse_data = []
x1 = []
y1 = []

def draw_pulse_graph(i):
    juhuu = PulseSensor.getdata()
    Pulse_data.append(juhuu)
    x1.append(len(Pulse_data))
    y1 = Pulse_data
    b.grid(True)
    if juhuu > 60 and juhuu <= 100:
        b.plot(x1, y1, color="green")
    elif juhuu > 100 and juhuu <= 120 or juhuu > 40 and juhuu <= 60:
        b.plot(x1, y1, color="yellow")
    else:
        b.plot(x1, y1, color="red")
    b.set_title('Pulse Graph', fontsize=20)
    b.set_xlabel('Time in seconds (s)', fontsize=15)
    b.set_ylabel('SpO2-Data', fontsize=15)


#Pulse_mincritical = 40
#Pulse_minearlywarning = 60
#Pulse_maxearlywarning = 100
#Pulse_maxcritical = 120


class pulsedataframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        try:
            connection = sqlite3.connect('/Users/rebeccatimm/Desktop/Database.db')
            c = connection.cursor()

            c.execute("SELECT Data FROM Pulse ORDER BY ID DESC LIMIT 20")
            records = c.fetchall()
            connection.commit()

            Pulse_Data_label = Label(self, width=60, text='Puls Data', borderwidth=5, relief='flat', anchor='w')
            Pulse_Data_label.grid(row=0, column=0)

            i = 1
            for data in reversed(records):
                for j in range(len(data)):
                    x = Entry(self, width=60)
                    x.grid(row=i, column=j)
                    x.insert(END, data[j])
                    x.configure(state='disabled')
                i = i + 1

        except sqlite3.Error as error:
            print("Communicationerror with Database:", error)

        finally:
            c.close()
            connection.close()



if __name__ == "__main__":
    TheProgram = Program()
    SpO2graph = animation.FuncAnimation(SpO2graph, draw_SpO2_graph, interval=1500)
    Pulsegraph = animation.FuncAnimation(Pulsegraph, draw_pulse_graph, interval=1500)
    TheProgram.mainloop()
    
    ___________________________________________________________________________________________________________________________________________________________
    
    def get_pulse_mincrit(self):
        self.pulse_mincritical = self.pulse_mincritical_entry.get()
        return self.pulse_mincritical
    
    def get_pulse_minearlywarning(self):
        self.pulse_minearlywarning = self.pulse_minearlywarning_entry.get()
        return self.pulse_minearlywarning

    def get_pulse_maxcritical(self):
        self.pulse_maxcritical = self.pulse_maxcritical_entry.get()
        return self.pulse_maxcritical

    def get_SpO2_earlywarning(self):
        self.SpO2_earlywarning = self.SpO2_earlywarning_entry.get()
        return self.SpO2_earlywarning
    
    def get_SpO2_critical(self):
        self.SpO2_critical = self.SpO2_critical_entry.get()
        return self.SpO2_critical
