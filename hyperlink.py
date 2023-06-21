from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QColor

class HyperLink(QWidget):
    def __init__(self, text):
        super().__init__()

        self.text = text
        self.link = "<a href='https://github.com/karimdevelops/caesar-cipher' style='color:#31fe5c; text-decoration: {};'>{}</a>"

        self.default_decor = 'none'
        self.hover_decor = 'underline'

        self.label = QLabel(self.link.format(self.default_decor, self.text))

        self.label.setOpenExternalLinks(True)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.addWidget(self.label)

    def enterEvent(self, QEnterEvent):
        self.label.setText(self.link.format(self.hover_decor, self.text))
        
    def leaveEvent(self, QEvent):
        self.label.setText(self.link.format(self.default_decor, self.text))
