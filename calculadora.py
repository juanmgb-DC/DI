import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QLabel,
    QPushButton,
)
from PyQt6.QtCore import Qt


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora")
        self.setMinimumSize(350, 500)

        caixaPrincipal = QVBoxLayout()

        self.pantalla = QLabel("0")
        self.pantalla.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        self.pantalla.setStyleSheet("""
            background-color: white;
            font-size: 40px;
            padding: 20px;
        """)
        self.pantalla.setMinimumHeight(200)

        caixaPrincipal.addWidget(self.pantalla)





        caixaBotones = QGridLayout()
        caixaBotones.setSpacing(2)

        estilo_gris_claro = "background-color: #e8e8e8;"
        estilo_gris_oscuro = "background-color: #d0d0d0;"
        estilo_naranja = "background-color: #ff8c00; color: white;"

        botones = [
            ("⌫", 0, 0, 1, 1, estilo_gris_claro),
            ("(", 0, 1, 1, 1, estilo_gris_claro),
            (")", 0, 2, 1, 1, estilo_gris_claro),
            ("mod", 0, 3, 1, 1, estilo_gris_claro),
            ("π", 0, 4, 1, 1, estilo_gris_claro),

            ("7", 1, 0, 1, 1, estilo_gris_oscuro),
            ("8", 1, 1, 1, 1, estilo_gris_oscuro),
            ("9", 1, 2, 1, 1, estilo_gris_oscuro),
            ("÷", 1, 3, 1, 1, estilo_gris_claro),
            ("√", 1, 4, 1, 1, estilo_gris_claro),

            ("4", 2, 0, 1, 1, estilo_gris_oscuro),
            ("5", 2, 1, 1, 1, estilo_gris_oscuro),
            ("6", 2, 2, 1, 1, estilo_gris_oscuro),
            ("×", 2, 3, 1, 1, estilo_gris_claro),
            ("x²", 2, 4, 1, 1, estilo_gris_claro),

            ("1", 3, 0, 1, 1, estilo_gris_oscuro),
            ("2", 3, 1, 1, 1, estilo_gris_oscuro),
            ("3", 3, 2, 1, 1, estilo_gris_oscuro),
            ("−", 3, 3, 1, 1, estilo_gris_claro),
            ("=", 3, 4, 2, 1, estilo_naranja),

            ("0", 4, 0, 1, 1, estilo_gris_claro),
            (".", 4, 1, 1, 1, estilo_gris_claro),
            ("%", 4, 2, 1, 1, estilo_gris_claro),
            ("+", 4, 3, 1, 1, estilo_gris_claro),
        ]

        for texto, fila, columna, rowspan, colspan, estilo in botones:
            boton = QPushButton(texto)
            boton.setMinimumSize(60, 60)
            boton.setStyleSheet(estilo)
            caixaBotones.addWidget(boton, fila, columna, rowspan, colspan)

        caixaPrincipal.addLayout(caixaBotones)


        contenedor = QWidget()
        contenedor.setLayout(caixaPrincipal)
        self.setCentralWidget(contenedor)

        self.show()



if __name__ == '__main__':

    aplicacion = QApplication(sys.argv)

    fiestra = FiestraPrincipal()

    aplicacion.exec()