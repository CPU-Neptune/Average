def input_sonst():
    onel=[]
    print()
    onel=list(map(int, input('Sonstige Noten: ').split()))
    return onel

def input_klau():
    twol=[]
    print()
    twol=list(map(int, input('Klausurnoten: ').split()))
    return twol

def average(onel, twol):
    print(onel, twol)
    avgel=[]
    if onel[0]==0:
        print('Keine sonstigen Noten')
    else:
        avone=sum(onel) / len(onel)
        avgel.append(avone)
        print()
        print(f'Durchschnitt Sonstige: {avone}')

    if twol[0]==0:
        print('Keine Klausurnoten')
    else:
        avtwo=sum(twol) / len(twol)
        avgel.append(avtwo)
        print(f'Durchschnitt Klausur: {avtwo}')

    print()
    print()
    print(f'Gesamtdurchschnitt: {sum(avgel)/len(avgel)}')
    input('Press button to end...')

onel=input_sonst()
twol=input_klau()

average(onel, twol)