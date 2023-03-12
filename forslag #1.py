import tkinter as tk
from tkinter import messagebox
import sys

class program(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # Sætter størrelse for selve vinduet, og gør det ujusterbart
        self.geometry("1500x800+100+50")
        self.title("")
        self.resizable(False, False)

        # opretter en tom frame, hvor menuframen skal placeres i
        self.menucontainer = tk.Frame(self)
        self.menucontainer.place(x=0, y=0, width=1500, height=100)
        self.menu = menuframe(parent=self.menucontainer, controller=self)
        self.menu.place(x=0, y=0, width=1500, height=100)

        # opretter en tom frame, som via for-loopen får "stacket" frames oven på hinanden. Den frame, der høre til den knap i menulinjen, der trykkes på, vil blive lagt øverst i stacken, og blive vist på skærmen
        self.framecontainer = tk.Frame(self)
        self.framecontainer.place(x=0, y=100, width=1500, height=800)

        self.frames = {}
        for F in (forsideframe,Graensevaerdierframe, pulsgrafframe, pulsdataframe, SpO2grafframe, SpO2dataframe):
            page_name = F.__name__
            frame = F(parent=self.framecontainer, controller=self)
            self.frames[page_name] = frame
            frame.place(x=0, y=0, width=1500, height=800)

        # funktionen nedenfor angiver "forsideframe" som den første der skal lægge, når programmet åbner. der bruges her "show_frame"-funktionen
        self.show_frame("forsideframe")

    # en funktion, der afhængig af hvilken knap i menulinjen der trykkes på, viser den dertilhørende frame (funktionen benytter iterationen ovenfor, som sørger for at ønskede frame lægger øverst i stacken)
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

#her er menuframeklassen. de indeholder hele menulinje. menulinjen placeres i "menucontainer"-framen fra "program"-klassen ovenfor
#knapperne referer til frames i andre klasser. måden frames bliver switchet er via "show_frame"-funktionen i "program"-klassen ovenfor. Det er en såkaldt "controller", der sørger for at det kan lade sg gøre, og at klasserne kan kommunikere sammen på tværs
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

#resten af klasserne nedenfor er frames, der placeres i "framecontainer"-framen i "program"-klassen ovenfor. alt afhngig af hvilken menuknap der trykkes på, vil dertilhørende klasse med frame i blive kaldt.
class forsideframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.forside_frame = tk.Frame(self, bg="grey", highlightbackground="black", highlightthickness=2)
        self.forside_frame = tk.Label(self, bg="grey" ,text="SPACEBABES", font = ("Arial#", 100))
        self.forside_frame.place(x=0, y=0, width=1500, height=800)

class Graensevaerdierframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.graensevaerdier_frame = tk.Frame(self, bg="black", highlightbackground="black", highlightthickness=2)
        self.graensevaerdier_frame.place(x=0, y=0, width=1500, height=800)

class pulsgrafframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.puls_graf_frame = tk.Frame(self, bg="pink", highlightbackground="black", highlightthickness=2)
        self.puls_graf_frame.place(x=0, y=0, width=1500, height=800)

class pulsdataframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.puls_data_frame = tk.Frame(self, bg="blue", highlightbackground="black", highlightthickness=2)
        self.puls_data_frame.place(x=0, y=0, width=1500, height=800)

class SpO2grafframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.SpO2_graf_frame = tk.Frame(self, bg="green", highlightbackground="black", highlightthickness=2)
        self.SpO2_graf_frame.place(x=0, y=0, width=1500, height=800)

class SpO2dataframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.SpO2_data_frame = tk.Frame(self, bg="yellow", highlightbackground="black", highlightthickness=2)
        self.SpO2_data_frame.place(x=0, y=0, width=1500, height=800)

# her kaldes og køres selve programmet. vinduet og programmet er samlet i de klasse der hedder "program", hvorfor det er den der kaldes nedenfor
if __name__ == "__main__":
    Programmet = program()
    Programmet.mainloop()
