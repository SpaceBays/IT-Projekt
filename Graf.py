import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import tkinter as tk
from tkinter import ttk
import datetime
from time import sleep

LARGE_FONT= ("Verdana", 12)
style.use("ggplot")

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

def animate(i):
    pullData = open("SpO2.txt","r").read()
    dataList = pullData.split('\n')
    xList = [datetime.datetime.now() + datetime.timedelta(seconds=i)for i in range(100)]
    yList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            y = eachLine
            yList.append(int(y))
    a.clear()
    a.plot(xList, yList)
            
class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Sea of BTC client")
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (StartPage, PageThree):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button3 = ttk.Button(self, text="Graph Page", command=lambda: controller.show_frame(PageThree))
        button3.pack()

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = SeaofBTCapp()
ani = animation.FuncAnimation(f, animate)
app.mainloop()




______________________________________________________________

class Sensor:
    def __init__(self):

        self.pullData = open("SpO2.txt", "r").readlines()
        for i in range(len(self.pullData)):
            self.pullData[i] = self.pullData[i].rstrip()

    def getdata(self):
        for i in self.pullData:
            while len(self.pullData) != 0:
                q = self.pullData.pop(0)
                print(q)

Sensor().getdata()

_________________________________________________________________________________________________________

import matplotlib.pyplot as plt
from matplotlib import animation


class Sensor:
    def __init__(self):
        self.pullData = open("SpO2.txt", "r").readlines()
        for i in range(len(self.pullData)):
            self.pullData[i] = self.pullData[i].rstrip()

    def getdata(self):
        q=self.pullData
        return q

count =0
ilt_data = Sensor().getdata()
x=[]
y=[]

def tegn_graf(i):
    global count
    count +=1
    x.append(count)
    y.append(ilt_data[count])
    plt.grid()
    plt.cla()
    plt.plot(x,y)
    plt.xlabel("Tid i sekunder (s)")
    plt.ylabel("SpO2-værdi")
    plt.title("Graf for SpO2-værdi")

        
graf = animation.FuncAnimation(plt.gcf(),tegn_graf,interval=1500)
plt.show()  

_______________________________________________________________________________________________________________
import matplotlib.pyplot as plt
from matplotlib import animation


class Sensor:
    def __init__(self):
        self.index = 0
        self.pullData = open("SpO2.txt", "r").readlines()
        for i in range(len(self.pullData)):
            self.pullData[i] = self.pullData[i].rstrip()
        #print(self.pullData)

    def getdata(self):
        q=self.pullData[self.index]
        self.index = self.index +1 
        return int(q)

sensor = Sensor()
ilt_data =[]
#ilt_data.append(sensor.getdata())

#print(ilt_data)
x=[]
y=[]

def tegn_graf(i):
    ilt_data.append(sensor.getdata())
    x.append(len(ilt_data))
    y=ilt_data
    plt.grid()
    plt.plot(x,y)
    #print(x,y)
    plt.xlabel("Tid i sekunder (s)")
    plt.ylabel("SpO2-værdi")
    plt.title("Graf for SpO2-værdi")

#print(ilt_data)
graf = animation.FuncAnimation(plt.gcf(),tegn_graf,interval=1500)
plt.show()  




        
        
