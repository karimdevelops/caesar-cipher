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
    QHBoxLayout,
    QFormLayout
)
from PyQt6.QtGui import (
    QIcon, 
    QFontDatabase, 
    QColor
)
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Caesar Cipher")
        self.setWindowIcon(QIcon("img/logo.png"))

        self.setFixedSize(960, 540)

        self.initUI()

    def initUI(self):

        widget = QWidget()
        page_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        footer_layout = QVBoxLayout()

        heading = QLabel("Caesar Cipher")
        heading.setObjectName("heading")
        heading.setAlignment(Qt.AlignmentFlag.AlignCenter)

        encryption_button = QPushButton("Encryption")
        encryption_button.setObjectName("encryption_button")

        decryption_button = QPushButton("Decryption")
        decryption_button.setObjectName("decryption_button")

        color = QColor("white")

        github_link = QLabel(f"<a href='https://github.com/karimdevelops/caesar-cipher' style='color:{color.name()};'>View Source Code</a>")
        github_link.setOpenExternalLinks(True)
        github_link.setObjectName("github_link")

        encryption_button.setFixedSize(245, 185)
        decryption_button.setFixedSize(245, 185)

        page_layout.addWidget(heading)
        button_layout.addWidget(encryption_button)
        button_layout.addWidget(decryption_button)
        footer_layout.addWidget(github_link)

        page_layout.setContentsMargins(0, 85, 0, 0)   
        button_layout.setContentsMargins(130, 45, 140, 0)
        footer_layout.setContentsMargins(360, 0, 0, 50)

        page_layout.addLayout(button_layout)
        page_layout.addLayout(footer_layout)
        widget.setLayout(page_layout)

        self.setCentralWidget(widget)

        encryption_button.released.connect(self.input_layout)
        decryption_button.released.connect(self.input_layout)

    def input_layout(self):
        submit_button = QPushButton("Submit")
        submit_button.setObjectName("next_button")

        back_button = QPushButton("< Back")
        back_button.setObjectName("back_button")

        submit_button.setFixedSize(145, 175)
        back_button.setFixedSize(145, 175)

        user_input = QTextEdit("")
        user_input.setObjectName("user_input")
        
        user_input.setPlaceholderText("Enter your text...")
        user_input.setFixedSize(800, 175)

        page_layout = QFormLayout()
        button_layout = QHBoxLayout()
        
        page_layout.addRow(user_input)
        button_layout.addWidget(back_button)
        button_layout.addWidget(submit_button)

        page_layout.addRow(button_layout)

        self.widget = QWidget()
        self.widget.setLayout(page_layout)
        self.setCentralWidget(self.widget)

        back_button.clicked.connect(self.initUI)

app = QApplication([])

QFontDatabase.addApplicationFont('font/Roboto_Mono/RobotoMono-Bold.ttf')
QFontDatabase.addApplicationFont('font/Roboto/Roboto-Medium.ttf')
QFontDatabase.addApplicationFont('font/Anonymous/AnonymousPro-Regular.ttf')
QFontDatabase.addApplicationFont('font/Roboto_Condensed/RobotoCondensed-Regular.ttf')
QFontDatabase.addApplicationFont('font/Cubano/Cubano.ttf')
QFontDatabase.addApplicationFont('font/MonomaniacOne/MonomaniacOne-Regular.ttf')

app.setStyleSheet(Path('style.css').read_text())

window = MainWindow()
window.show()

app.exec()
