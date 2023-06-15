from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Caesar Cipher")

app = QApplication([])

window = MainWindow()
window.show()

app.exec()