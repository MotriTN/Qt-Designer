from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def verif(N):
    i=0
    v=True
    while i <len(N) and v==True:
        if not  ("a"<=N[i]<="z" or N[i]==" "):
            v=False
        i+=1
    return v
def Miroir(ch):
    ph=""
    ch=ch+" "
    while ch.find(" ")!=-1:
        p=ch.find(" ")
        ph+=inverse(ch[:p])+" "
        ch=ch[p+1:]
       
    return ph
def inverse(ch):
    ph=""
    for i in range(0,len(ch),-1):
        ph+=ch[i]
    return ph
def Play():
    N=w.N.text()
    if N=="":
        w.R.setText("Veuillez Introduire une chaine")
    elif N.find("  ")!=-1:
        w.R.setText("Entre 2 mots un seul espace est autorisé")
    elif len(N)>=50 or verif(N)==False:
        w.R.setText("Veuillez essayer une chaine valide")
    else:
        w.R.setText(Miroir(N))
        
app = QApplication([])
w = loadUi ("InterfaceMiroirsMots.ui")
w.show()
w.B.clicked.connect(Play)
app.exec_()

