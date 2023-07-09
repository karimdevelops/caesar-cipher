from pathlib import Path

from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget, 
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
    QDialog,
    QMessageBox,
    QSpinBox
)
from PyQt6.QtGui import (
    QIcon, 
    QFontDatabase,
    QPixmap
)
from PyQt6.QtCore import Qt

from hyperlink import HyperLink
from button import Button

from caesar_cipher import caesar_cipher

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Caesar Cipher")
        self.setWindowIcon(QIcon("img/logo.png"))

        self.setFixedSize(960, 540)

        self.initUI()


    def initUI(self):

        self.button_w = 245
        self.button_h = 71

        widget = QWidget()
        page_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        footer_layout = QVBoxLayout()

        heading = QLabel("Caesar Cipher")
        heading.setObjectName("heading")
        heading.setAlignment(Qt.AlignmentFlag.AlignCenter)

        encryption_button = Button("Encryption", self.button_w, self.button_h, True)
        encryption_button.setStyleSheet("color: #4285F4")

        decryption_button = Button("Decryption", self.button_w, self.button_h, True)
        decryption_button.setStyleSheet("color: #ec5352")

        github_link = HyperLink('View Source Code on Github')
        github_link.setObjectName("github_link")

        page_layout.addWidget(heading)
        button_layout.addWidget(encryption_button)
        button_layout.addWidget(decryption_button)
        footer_layout.addWidget(github_link)

        page_layout.setContentsMargins(0, 40, 0, 0)   
        button_layout.setContentsMargins(130, 0, 140, 100)
        footer_layout.setContentsMargins(280, 0, 0, 40)

        page_layout.addLayout(button_layout)
        page_layout.addLayout(footer_layout)
        widget.setLayout(page_layout)

        self.setCentralWidget(widget)

        encryption_button.button.clicked.connect(self.inputUI)
        decryption_button.button.clicked.connect(self.inputUI)

    def clearUI(self):
        self.setCentralWidget(None)


    def inputUI(self):
        self.button_w = 155
        self. button_h = 70

        submit_button = Button("Submit", self.button_w, self.button_h, False)

        back_button = Button("< Back", self.button_w, self.button_h, False)

        self.user_input = QTextEdit("")
        self.user_input.setAcceptRichText(False)

        self.mode = self.sender().text()

        if  self.mode == 'Encryption':
            self.user_input.setObjectName("encryption")
        elif self.mode == 'Decryption':
            self.user_input.setObjectName("decryption")

        self.user_input.setPlaceholderText("Enter your text...")
        self.user_input.setFixedSize(800, 175)

        self.shift_num = QSpinBox()
        self.shift_num.setFixedSize(50, 22)

        self.shift_num.setMinimum(1)
        self.shift_num.setMaximum(20)

        input_prompt = QLabel("Message:")
        input_prompt.setObjectName('prompt')
        shift_prompt = QLabel("Shift number (1-20):")
        shift_prompt.setObjectName('prompt')

        page_layout = QFormLayout()
        text_layout = QVBoxLayout()
        shift_num_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        
        text_layout.addWidget(input_prompt)
        text_layout.addWidget(self.user_input)
        shift_num_layout.addWidget(shift_prompt)
        shift_num_layout.addWidget(self.shift_num)
        button_layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignLeft)
        button_layout.addWidget(submit_button, alignment=Qt.AlignmentFlag.AlignRight)

        text_layout.setContentsMargins(50, 0, 0, 40)
        shift_num_layout.setContentsMargins(50, 0, 0, 10)
        page_layout.setContentsMargins(0, 70, 0, 0)
        button_layout.setContentsMargins(0, 50, 0, 0)

        page_layout.addRow(text_layout)
        page_layout.addRow(shift_num_layout)
        page_layout.addRow(button_layout)

        self.widget = QWidget()
        self.widget.setLayout(page_layout)
        self.setCentralWidget(self.widget)

        back_button.button.clicked.connect(self.initUI)
        submit_button.button.clicked.connect(self.clearUI)
        submit_button.button.clicked.connect(self.cipherUI)

    def cipherUI(self):
        msg = self.user_input.toPlainText()
        shift_num = int(self.shift_num.text())
        mode = self.mode

        dialog_layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        cipher_dialog = QDialog(self)
        
        cipher_dialog.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.CustomizeWindowHint)

        self.cipher_text = QTextEdit(caesar_cipher(msg, shift_num, mode))
        self.cipher_text.setReadOnly(True)
        self.cipher_text.setObjectName('cipher_text')

        copy_button = QPushButton('Copy')
        close_button = QPushButton('Close')

        copy_button.clicked.connect(self.copytext)
        close_button.clicked.connect(self.initUI)
        close_button.clicked.connect(cipher_dialog.close)

        dialog_layout.addWidget(self.cipher_text)
        button_layout.addWidget(copy_button)
        button_layout.addWidget(close_button)
        dialog_layout.addLayout(button_layout)

        cipher_dialog.setLayout(dialog_layout)
        cipher_dialog.exec()

    def copytext(self):
        self.cipher_text.selectAll()
        self.cipher_text.copy()

        copy_info = QMessageBox()
        copy_info.setText("Copied to Clipboard")

        copy_info.exec()

if __name__ == '__main__':

    app = QApplication([])

    QFontDatabase.addApplicationFont(str(Path('font/Roboto_Mono/RobotoMono-Bold.ttf')))
    QFontDatabase.addApplicationFont(str(Path('font/Roboto/Roboto-Medium.ttf')))
    QFontDatabase.addApplicationFont(str(Path('font/AnonymousPro/AnonymousPro-Regular.ttf')))
    QFontDatabase.addApplicationFont(str(Path('font/Roboto_Condensed/RobotoCondensed-Regular.ttf')))
    QFontDatabase.addApplicationFont(str(Path('font/Cubano/Cubano.ttf')))
    QFontDatabase.addApplicationFont(str(Path('font/MonomaniacOne/MonomaniacOne-Regular.ttf')))

    app.setStyleSheet(Path('style.css').read_text())

    window = MainWindow()
    window.show()

    app.exec()
