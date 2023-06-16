from pathlib import Path
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QGridLayout
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Caesar Cipher")
        self.setWindowIcon(QIcon("img/logo.png"))

        self.setFixedSize(850, 150)

        heading = QLabel("Caesar Cipher")

        layout = QGridLayout()
        widget = QWidget()

        layout.addWidget(heading, 0, 1)

        widget.setLayout(layout)

        self.setCentralWidget(widget)

app = QApplication([])
app.setStyleSheet(Path('style.css').read_text())

window = MainWindow()
window.show()

app.exec()
