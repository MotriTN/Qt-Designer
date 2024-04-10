from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def verif1(N):
    if N.find("  ")==-1:
        return False
    else:
        return True

def verif2(N):
    i=0
    v=True
    while i <len(N) and v==True:
        if not  "a"<=N[i]<="z":
            v=False
        i+=1
    return v
def Miroir(N):
    if N.find(" ")==-1:
        return N[::-1]
    else:
        f=""
        for i in range(len(ch)):
            s=i
            s=N[s:].find(" ")
            ch=N[:s]
            ch=ch[::-1]
            f+=ch
        return f
            
def Play():
    N=w.N.Text()
    if N.isdigit()==True:
        w.R.setText("Veuillez Introduire une chaine")
    elif verif1(N)==False:
        w.R.setText("Entre 2 mots un seul espace est autorisé")
    elif len(N)>=50 or N=="":
        w.R.setText("Veuillez essayer une chaine inf à 50 et non vide")
    elif verif2(N)==False:
        w.R.setText("La Chaine doit étre en minuscule")    
    else:
        w.R.setText(Miroir(N))
app = QApplication([])
w = loadUi ("InterfaceMiroirsMots.ui")
w.show()
w.B.clicked.connect(Play)
app.exec_()