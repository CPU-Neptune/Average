from tkinter import messagebox

i=-1

def input_onel(onele):
    onel=list(map(float, onele.split()))
    return onel

def input_twol(twole):
    twol=list(map(float, twole.split()))
    return twol

def main(onel, twol):
    avgel=[]
    if len(onel)==0:
        messagebox.showinfo('Test', 'Keine sonstigen Noten')
    else:
        avone=sum(onel) / len(onel)
        avgel.append(avone)

    if len(twol)==0:
        messagebox.showinfo('Test', 'Keine Klausurnoten')
    else:
        avtwo=sum(twol) / len(twol)
        avgel.append(avtwo)

    avges=sum(avgel) / len(avgel)
    avges=round(avges, 2)
    messagebox.showinfo('Durchschnitte', 'Gesamtdurchschnitt: ' + str(avges))

if __name__=="__main__":
    onel=input_onel(onele)
    twol=input_twol(twole)
    input_onel(onele)
    input_twol(twole)
    main(onel, twol)
    print(onel, twol)
    avges=main(onel, twol)