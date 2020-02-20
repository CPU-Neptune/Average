import average as avg
from tkinter import *
from tkinter import messagebox
import tkinter as tk

window=Tk()

window.geometry("400x100")
window.title('Durchschnittsrechner')

#define titles

Note=Label(window, text='Nach jeder Note Leerzeichen; Kommzahlen mit Punkt')
Note.grid(row=0, column=1)

Sontige=Label(window, text='Sonstige Noten')
Sontige.grid(row=1,column=0)

Klausur=Label(window, text='Klausurnoten')
Klausur.grid(row=2,column=0)

#define entries

onele=StringVar()
SontigeE=Entry(window,textvariable=onele)
SontigeE.grid(row=1,column=1)

twole=StringVar()
KlausurE=Entry(window,textvariable=twole)
KlausurE.grid(row=2,column=1)


#define buttons + buttonfunction

SubmitAverage=Button(window, text='Durchschnitt', command=lambda :avg.main(avg.input_onel(onele.get()), avg.input_twol(twole.get())))

SubmitAverage.grid(row=5,column=1)

 #shows as text in the window

#make the SubmitAverage button do something
#show the averages

window.mainloop()