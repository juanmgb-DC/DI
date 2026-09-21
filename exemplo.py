import sys

from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout,QPushButton,QWidget, QLabel, QLineEdit)

class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("A miña primeira aplicacion Qt")
        self.setMinimumSize(300, 200)
        self.setMaximumSize(600, 600)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("aquamarine"))
        self.setPalette(paleta)
        #print (QColor.colorNames())

        caixaV = QVBoxLayout()

        boton = QPushButton("Pulsame")
        etiqueta = QLabel("Ola a todos")
        cadroTexto = QLineEdit()
        cadroTexto.setPlaceholderText("Introduce o teu nome")

        etiqueta.setText("Otro texto")
        cadroTexto.setText("Tamen o podo modificar")
        print(etiqueta.text())
        print(cadroTexto.text())

        caixaV.addWidget(etiqueta)
        caixaV.addWidget(cadroTexto)
        caixaV.addWidget(boton)


        contedor = QWidget()
        contedor.setLayout(caixaV)
        self.setCentralWidget(contedor)



        self.show()





if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()