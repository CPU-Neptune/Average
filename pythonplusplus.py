from tkinter import *
root=Tk()

root.minsize(width=200,height=50)
root.configure(background='#333333')

durchschnitt="-"

eingabeaufforderung=Entry(root,fg="white",bg='#333333',width=50)
eingabeaufforderung.pack()
eingabeaufforderung.get()

eingabeauffordern=Entry(root,fg="white",bg='#333333',width=50)
eingabeauffordern.pack()
eingabeauffordern.get()
LOOL1=(eingabeauffordern.get())
LOOL2=(eingabeaufforderung.get())
Nom1=list(LOOL1)
Nom2=list(LOOL2)


def danach():
    print(Nom1)
    print(Nom2)
    Num1=Nom1
    Num2=Nom2
    durchschnitt=(sum(Nom1)/len(Nom1)+sum(Nom2)/len(Nom2))/2
    tesxt=Label(root,text=durchschnitt,bg='#333333',fg='white')
    tesxt.pack()
    Tk.title(root,"Durchschnitt: "+durchschnitt)

def update():
    texst=Label(root,text=eingabeaufforderung.get(),bg='#333333',fg='white')
    texst.pack()


eingabebutt=Button(root,text="Ausrechnen",command=danach)
eingabebutt.pack()




Tk.title(root,"Durchschnitt: "+durchschnitt)

root.mainloop()
