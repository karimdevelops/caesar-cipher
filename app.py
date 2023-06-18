from pathlib import Path

from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget, 
    QLabel,
    QPushButton, 
    QLineEdit, 
    QTextEdit,
    QVBoxLayout,
    QHBoxLayout
)
from PyQt6.QtGui import QIcon, QFontDatabase
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

        encryption_button = QPushButton("Encryption")
        encryption_button.setObjectName("encryption_button")

        decryption_button = QPushButton("Decryption")
        decryption_button.setObjectName("decryption_button")

        encryption_button.setFixedSize(160, 170)
        decryption_button.setFixedSize(160, 170)

        page_layout.addWidget(heading)
        button_layout.addWidget(encryption_button)
        button_layout.addWidget(decryption_button)

        page_layout.setContentsMargins(0, 60, 0, 0)
        button_layout.setContentsMargins(110, 0, 130, 30)

        page_layout.addLayout(button_layout)
        widget.setLayout(page_layout)

        self.setCentralWidget(widget)

        encryption_button.released.connect(self.input_layout)
        decryption_button.released.connect(self.input_layout)

    def input_layout(self):
        continue_button = QPushButton("Continue")
        continue_button.setObjectName("continue_button")

        continue_button.setFixedSize(160, 170)

        user_input = QTextEdit("")
        user_input.setObjectName("user_input")
        
        user_input.setPlaceholderText("Enter your text...")
        user_input.setFixedSize(800, 100)

        layout = QVBoxLayout()
        
        layout.addWidget(user_input)
        layout.addWidget(continue_button)

        layout.setContentsMargins(25, 60, 0, 0)

        self.widget = QWidget()

        self.widget.setLayout(layout)

        self.setCentralWidget(self.widget)

        # continue_button.released.connect()

app = QApplication([])

QFontDatabase.addApplicationFont('font/Roboto_Mono/RobotoMono-Bold.ttf')
QFontDatabase.addApplicationFont('font/Roboto/Roboto-Medium.ttf')
QFontDatabase.addApplicationFont('font/Anonymous/AnonymousPro-Regular.ttf')
QFontDatabase.addApplicationFont('font/Roboto_Condensed/RobotoCondensed-Regular.ttf')

app.setStyleSheet(Path('style.css').read_text())

window = MainWindow()
window.show()

app.exec()
