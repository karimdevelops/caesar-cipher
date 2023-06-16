from pathlib import Path

from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget, 
    QLabel,
    QPushButton, 
    QLineEdit, 
    QVBoxLayout,
    QHBoxLayout
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Caesar Cipher")
        self.setWindowIcon(QIcon("img/logo.png"))

        self.setFixedSize(850, 450)

        widget = QWidget()
        page_layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        heading = QLabel("Caesar Cipher")
        heading.setObjectName("heading")
        heading.setAlignment(Qt.AlignmentFlag.AlignCenter)

        encrypt_button = QPushButton("Encryption")
        decrypt_button = QPushButton("Decryption")

        encrypt_button.setFixedSize(160, 170)
        decrypt_button.setFixedSize(160, 170)

        page_layout.addWidget(heading)
        button_layout.addWidget(encrypt_button)
        button_layout.addWidget(decrypt_button)

        page_layout.addLayout(button_layout)
        widget.setLayout(page_layout)

        self.setCentralWidget(widget)

        encrypt_button.released.connect(self.input_layout)
        decrypt_button.released.connect(self.input_layout)

    def input_layout(self):
        continue_button = QPushButton("Continue")
        user_input = QLineEdit("")
        user_input.setPlaceholderText("Enter your text...")

        layout = QVBoxLayout()
        
        layout.addWidget(user_input)
        layout.addWidget(continue_button)

        self.widget = QWidget()

        self.widget.setLayout(layout)

        self.setCentralWidget(self.widget)

app = QApplication([])
app.setStyleSheet(Path('style.css').read_text())

window = MainWindow()
window.show()

app.exec()
