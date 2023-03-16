import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# root window
window = tk.Tk()
window.geometry("600x400")
window.resizable(False, False)
window.title('Grænseværdier')

# Gemmer værdier
minEw = tk.StringVar()
maxEw = tk.StringVar()
minKri = tk.StringVar()
maxkri = tk.StringVar()

ewIlt = tk.StringVar()
kriIlt = tk.StringVar()



#Top
frametop = tk.Frame(master=window, height=100, bg="white",highlightbackground="black", highlightthickness=1)
frametop.pack(fill=tk.X,side=tk.TOP)


# Puls frame
frame1 = tk.Frame(master=window, width=50, height=50, bg="white",highlightbackground="black", highlightthickness=1)
frame1.pack(expand=True,side=tk.LEFT)
    
# minEw
minEw = ttk.Label(frame1, text="minEw")
minEw.pack(fill='x', expand=True)

minEw_entry = ttk.Entry(frame1, textvariable=minEw)
minEw_entry.pack(fill='x', expand=True)
minEw_entry.focus()

# maxEw
maxEw = ttk.Label(frame1, text="maxEw")
maxEw.pack(fill='x', expand=True)


maxEw_entry = ttk.Entry(frame1, textvariable=maxEw)
maxEw_entry.pack(fill='x', expand=True)
maxEw_entry.focus()

# minKri
minKri = ttk.Label(frame1, text="minKri")
minKri.pack(fill='x', expand=True)

minKri_entry = ttk.Entry(frame1, textvariable=minKri)
minKri_entry.pack(fill='x', expand=True)
minKri_entry.focus()

# maxKri
maxKri = ttk.Label(frame1, text="maxKri")
maxKri.pack(fill='x', expand=True)

maxKri_entry = ttk.Entry(frame1, textvariable=maxKri)
maxKri_entry.pack(fill='x', expand=True)
maxKri_entry.focus()

#Midten
frame3 = tk.Frame(master=window, width=10, height=10, bg="blue")
frame3.pack(expand=True,side=tk.LEFT)

#Ilt
frame2 = tk.Frame(master=window, width=10, height=100, bg="red",highlightbackground="black", highlightthickness=1)
frame2.pack(padx=1, pady=1,side=tk.RIGHT)

ewIlt = ttk.Label(frame2, text="Early warning iltmætning")
ewIlt.pack(fill='x', expand=True)

ewIlt_entry = ttk.Entry(frame2, textvariable=ewIlt,)
ewIlt_entry.pack(fill='x', expand=True)
ewIlt_entry.focus()

#Kritisk ilt værdi
kriIlt = ttk.Label(frame2, text="Kritisk iltmætning")
kriIlt.pack(fill='x', expand=True)

kriIlt_entry = ttk.Entry(frame2, textvariable=kriIlt,)
kriIlt_entry.pack(fill='x', expand=True)
kriIlt_entry.focus()

# Quit button in the lower right corner
enter_button = ttk.Button(frame3, text="Enter")
enter_button.grid(row=1, column=3)

default_button = ttk.Button(frame3, text="Default")
default_button.grid(row=1, column=4)

quit_button = ttk.Button(frametop, text="Quit", command=window.destroy)
quit_button.grid(row=1, column=1)

window.mainloop()
