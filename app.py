from pathlib import Path
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QGridLayout, QPushButton, QLineEdit, QVBoxLayout
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
        self.widget = QWidget()

        layout.addWidget(heading, 0, 0)
        layout.addWidget(encrypt_button, 1, 0)
        layout.addWidget(decrypt_button, 1, 1)

        self.widget.setLayout(layout)

        self.setCentralWidget(self.widget)

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
