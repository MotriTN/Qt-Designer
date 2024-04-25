from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from numpy import *
def tri(ch):
    tr=False
def Trier(ch):
    l=nbmots(ch)
    T=array([int]*l)
    s1=0
    for i in range(l-1):
        s2=ch.find(" ")
        T[i]=s2-s1
        s1=s2
    T[-1]=ch.find(".")-s2
    
def nbmots(ch):
    l=1
    for i in range(len(ch)):
        if ch[i]==" ":
            l+=1
    return l
def Play():
    N=w.N.text()
    R=w.R
    if len(N)>=50:
        R.setText("Veuillez saisir une chaine inferieur à 50 charactéres")
    elif nbmots(N)>15:
        R.setText("Le maximum des mots dans la phrase est 15")
    elif not("a"<=N[0]<="z" or "A"<=N[0]<="Z"):
        R.setText("La phrase doit commence par un charactére alphabétique")
    elif len(N)==0:
        R.setText("Veuillez introduire une phrase")
    elif N.find("  ")!=-1:
        R.setText("Entre 2 mots un seul espace est autorisé")
    elif N.find(".")!=len(N)-1:
        R.setText("La chaine doit se terminer par un point")
    else:
        R.setText(Trier(N))
    
        


app=QApplication([])

w=loadUi("InterfaceTriage.ui")
w.show()
w.B.clicked.connect(Play)
app.exec_()
