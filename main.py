import tkinter as tk

class Tegning(tk.Frame):         #Klasse nedarvet fra Frame
    def __init__(self,h,w):      #Konstruktør med dimensioner
        super(). __init__()      #kald af Frame konstruktør

        self.master.title("Tegning")
        self.pack(fill = tk.BOTH, expand = True)

        canvas = tk.Canvas(self)
        canvas.create_line(3,3,3,h-4,w-4,h-4,w-4,3,3,3) #Laver en kant på vinduet
        canvas.create_oval(10,10,10)

window = tk.Tk()                         #Opret vindue
t = Tegning(100,400)                     #Opret tegning
window.geometry("400x400")               #Angiver størrelsen af vinduet
window.configure(background = "purple")  #Angiver farven på vinduet
window.mainloop()                        #Vis vindue



# Tegning af graf

class Graf(tk.Frame):

    def __init__(self,h,w,data):
        ...
        maxx, minx, maxy, miny = 11, -11, 105,-5

        deltax = w / (maxx-minx)        #sætter origo til midten istedt for i venstre hjørne top.
        deltay = h / (maxy-miny)
        oridox = -minx * deltax
        origoy = h + miny * deltay



