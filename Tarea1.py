import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)


class FiestraPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exercicio Layouts")
        self.setMinimumSize(500, 350)

        # ==================================================
        # LAYOUT PRINCIPAL HORIZONTAL
        # ==================================================

        caixaH = QHBoxLayout()

        # ==================================================
        # PARTE ESQUERDA
        # ==================================================

        caixaEsquerda = QVBoxLayout()

        cadroVermello1 = QWidget()
        cadroVermello1.setStyleSheet("background-color: red;")

        cadroAmarelo = QWidget()
        cadroAmarelo.setStyleSheet("background-color: yellow;")

        cadroMorado1 = QWidget()
        cadroMorado1.setStyleSheet("background-color: purple;")

        caixaEsquerda.addWidget(cadroVermello1)
        caixaEsquerda.addWidget(cadroAmarelo)
        caixaEsquerda.addWidget(cadroMorado1)

        # ==================================================
        # PARTE CENTRAL
        # ==================================================

        cadroVerde = QWidget()
        cadroVerde.setStyleSheet("background-color: green;")

        # ==================================================
        # PARTE DEREITA
        # ==================================================

        caixaDereita = QVBoxLayout()

        cadroVermello2 = QWidget()
        cadroVermello2.setStyleSheet("background-color: red;")

        cadroMorado2 = QWidget()
        cadroMorado2.setStyleSheet("background-color: purple;")

        caixaDereita.addWidget(cadroVermello2)
        caixaDereita.addWidget(cadroMorado2)

        # ==================================================
        # XUNTAMOS AS TRES PARTES
        # ==================================================

        caixaH.addLayout(caixaEsquerda)
        caixaH.addWidget(cadroVerde)
        caixaH.addLayout(caixaDereita)

        # ==================================================
        # CONTEDOR PRINCIPAL
        # ==================================================

        contedor = QWidget()
        contedor.setLayout(caixaH)

        self.setCentralWidget(contedor)

        self.show()


if __name__ == '__main__':

    aplicacion = QApplication(sys.argv)

    fiestra = FiestraPrincipal()

    aplicacion.exec()