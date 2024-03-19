from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

def afficher():
    N = int(w.N.text())
    if N >= 0:
        f = fact(N)
        w.R.setText(f"Le nombre factoriel de {N} est {f}")
    else:
        w.R.setText("Donner un nombre supérieur strictement à 0")

app = QApplication([])
w = loadUi("factoriel.ui")
w.B.clicked.connect(afficher)  # Connect button click event to the afficher function
w.show()

app.exec_()
