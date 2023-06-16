from pathlib import Path
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QGridLayout, QPushButton
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Caesar Cipher")
        self.setWindowIcon(QIcon("img/logo.png"))

        self.setFixedSize(850, 450)

        heading = QLabel("Caesar Cipher")
        heading.setObjectName("heading")

        encrypt_button = QPushButton("Encryption")
        decrypt_button = QPushButton("Decryption")

        layout = QGridLayout()
        widget = QWidget()

        layout.addWidget(heading, 0, 0)
        layout.addWidget(encrypt_button, 1, 0)
        layout.addWidget(decrypt_button, 1, 1)

        widget.setLayout(layout)

        self.setCentralWidget(widget)

app = QApplication([])
app.setStyleSheet(Path('style.css').read_text())

window = MainWindow()
window.show()

app.exec()
