import tkinter as tk
from tkinter import messagebox
import sys
from tkinter import ttk

class program(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # Sætter størrelse for selve vinduet, angiver en titel, og gør det ujusterbart
        self.geometry("1500x800+100+50")
        self.title("")
        self.resizable(False, False)

        # opretter en tom frame i vores vindue, hvor menuframen efterfølgende placeres i
        self.menucontainer = tk.Frame(self)
        self.menucontainer.place(x=0, y=0, width=1500, height=100)
        self.menu = menuframe(parent=self.menucontainer, controller=self)
        self.menu.place(x=0, y=0, width=1500, height=100)

        # opretter en tom frame, som har til formål via for-loopen at få "stacket" frames oven på hinanden. Den frame, der høre til den knap i menulinjen, der trykkes på, vil blive lagt øverst i stacken, og blive vist på skærmen
        self.framecontainer = tk.Frame(self)
        self.framecontainer.place(x=0, y=100, width=1500, height=800)

        self.frames = {}
        for F in (forsideframe, Graensevaerdierframe, pulsgrafframe, pulsdataframe, SpO2grafframe, SpO2dataframe):
            page_name = F.__name__
            frame = F(parent=self.framecontainer, controller=self)
            self.frames[page_name] = frame
            frame.place(x=0, y=0, width=1500, height=800)

        # funktionen nedenfor angiver "forsideframe" som den første der skal vises (stackes øverst), når programmet åbner. Der bruges her "show_frame"-funktionen
        self.show_frame("Graensevaerdierframe")

    # en funktion, der afhængig af hvilken knap i menulinjen der trykkes på, viser den dertilhørende frame (funktionen benytter iterationen ovenfor, som sørger for at ønskede frame lægger øverst i stacken)
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


# her er menuframeklassen. Den indeholder hele menulinje. menulinjen placeres i "menucontainer"-framen fra "program"-klassen ovenfor
# knapperne referer til frames i andre klasser. måden frames bliver switchet er via "show_frame"-funktionen i "program"-klassen ovenfor. Det er en såkaldt "controller", der sørger for at det kan lade sg gøre, og at klasserne kan kommunikere sammen på tværs
class menuframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.menu_frame = tk.Frame(self, bg="grey", highlightbackground="black", highlightthickness=2)
        self.menu_frame.place(x=0, y=0, width=1500, height=100)

        self.graenseværdier = tk.Button(self.menu_frame, text="Grænser", font=("Arial", 15),
                                        command=lambda: controller.show_frame("Graensevaerdierframe"))
        self.graenseværdier.place(x=200, y=30, width=100, heigh=40)

        self.puls_graf_knap = tk.Button(self.menu_frame, text="Puls graf", font=("Arial", 15),
                                        command=lambda: controller.show_frame("pulsgrafframe"))
        self.puls_graf_knap.place(x=450, y=30, width=100, heigh=40)

        self.puls_data_knap = tk.Button(self.menu_frame, text="Puls data", font=("Arial", 15),
                                        command=lambda: controller.show_frame("pulsdataframe"))
        self.puls_data_knap.place(x=600, y=30, width=100, heigh=40)

        self.SpO2_graf_knap = tk.Button(self.menu_frame, text="SpO2 graf", font=("Arial", 15),
                                        command=lambda: controller.show_frame("SpO2grafframe"))
        self.SpO2_graf_knap.place(x=850, y=30, width=100, heigh=40)

        self.SpO2_data_knap = tk.Button(self.menu_frame, text="SpO2 data", font=("Arial", 15),
                                        command=lambda: controller.show_frame("SpO2dataframe"))
        self.SpO2_data_knap.place(x=1000, y=30, width=100, heigh=40)

        self.quit_button = tk.Button(self.menu_frame, text="Quit", font=("Arial", 15), command=self.quit)
        self.quit_button.place(x=0, y=0)

    def quit(self):
        message = tk.messagebox.askyesno("Question", "Are you sure you want to quit?")

        if message:
            sys.exit()


# resten af klasserne nedenfor er frames, der placeres i "framecontainer"-framen i "program"-klassen ovenfor. Alt afhængig af hvilken menuknap der trykkes på, vil dertilhørende klasse med frame i blive kaldt.
class forsideframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.forside_frame = tk.Frame(self, bg="grey", highlightbackground="black", highlightthickness=2)
        self.forside_frame = tk.Label(self, bg="grey", text="SPACEBABES", font=("Arial#", 100))
        self.forside_frame.place(x=0, y=0, width=1500, height=800)


class Graensevaerdierframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.graensevaerdier_frame = tk.Frame(self, bg="grey", highlightbackground="black", highlightthickness=2)
        self.graensevaerdier_frame.place(x=0, y=0, width=1500, height=800)

        # Puls frame
        self.frame1 = tk.Frame(self.graensevaerdier_frame, width=50, height=50, bg="white", highlightbackground="black",
                               highlightthickness=1)
        self.frame1.pack(expand=True, side=tk.LEFT)

        # minEw puls
        minEw = tk.Label(self.frame1, text="minEw")
        minEw.pack(fill='x', expand=True)

        self.minEw_entry = tk.Entry(self.frame1)
        self.minEw_entry.pack(fill='x', expand=True)
        self.minEw_entry.focus()

        maxEw = tk.Label(self.frame1, text="maxEw")
        maxEw.pack(fill='x', expand=True)

        self.maxEw_entry = tk.Entry(self.frame1)
        self.maxEw_entry.pack(fill='x', expand=True)
        self.maxEw_entry.focus()

        # minKri puls
        minKri = tk.Label(self.frame1, text="minKri")
        minKri.pack(fill='x', expand=True)

        self.minKri_entry = tk.Entry(self.frame1)
        self.minKri_entry.pack(fill='x', expand=True)
        self.minKri_entry.focus()

        # maxKri puls
        maxKri = tk.Label(self.frame1, text="maxKri")
        maxKri.pack(fill='x', expand=True)

        self.maxKri_entry = tk.Entry(self.frame1)
        self.maxKri_entry.pack(fill='x', expand=True)
        self.maxKri_entry.focus()

        # Ilt frame
        self.frame2 = tk.Frame(self.graensevaerdier_frame, width=10, height=100, bg="red", highlightbackground="black",
                               highlightthickness=1)
        self.frame2.pack(padx=1, pady=1, side=tk.RIGHT)

        # EW ilt
        ewIlt = tk.Label(self.frame2, text="Early warning iltmætning")
        ewIlt.pack(fill='x', expand=True)

        self.ewIlt_entry = tk.Entry(self.frame2)
        self.ewIlt_entry.pack(fill='x', expand=True)
        self.ewIlt_entry.focus()

        # Kritisk ilt værdi
        kriIlt = tk.Label(self.frame2, text="Kritisk iltmætning")
        kriIlt.pack(fill='x', expand=True)

        self.kriIlt_entry = tk.Entry(self.frame2)
        self.kriIlt_entry.pack(fill='x', expand=True)
        self.kriIlt_entry.focus()

        # Midten frame
        self.frame3 = tk.Frame(self.graensevaerdier_frame, width=10, height=10, bg="blue")
        self.frame3.pack(expand=True, side=tk.LEFT)

        # enter button
        self.enter_button = tk.Button(self.frame3, text="Enter", command=self.save_grens)
        self.enter_button.grid(row=1, column=3)

        # default button
        self.default_button = tk.Button(self.frame3, text="Default", command=self.default_grens)
        self.default_button.grid(row=1, column=4)

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

        if grens.pop != 0:
            message = tk.messagebox.askyesno("quenstion", "Ønsker du at fortsætte med de valgte værdier?")
            if message:
                program().show_frame("forsideframe")

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

# her kaldes og køres selve programmet. Vinduet og selve programmet er samlet i den klasse der hedder "program", hvorfor det er den der kaldes nedenfor
if __name__ == "__main__":
    Programmet = program()
    Programmet.mainloop()
