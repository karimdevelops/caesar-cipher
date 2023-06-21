from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QLabel, QHBoxLayout, QWidget
from PyQt6.QtGui import QPixmap


class HyperLink(QWidget):
    def __init__(self, text):
        super().__init__()

        self.text = text
        self.link = "<a href='https://github.com/karimdevelops/caesar-cipher' style='color:#31fe5c; text-decoration: {};'>{}</a>"

        self.default_decor = 'none'
        self.hover_decor = 'underline'

        self.label = QLabel(self.link.format(self.default_decor, self.text))
        self.label.setOpenExternalLinks(True)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        pixmap = QPixmap("img/github_logo_small.png")
        self.img_label = QLabel()
        self.img_label.setPixmap(pixmap)
        self.img_label.resize(25, 25)

        self.layout = QHBoxLayout()

        self.layout.addWidget(self.img_label)
        self.layout.addWidget(self.label)

        self.layout.setContentsMargins(370, 0, 435, 0)

        self.setLayout(self.layout)


    def enterEvent(self, QEnterEvent):
        self.label.setText(self.link.format(self.hover_decor, self.text))

        
    def leaveEvent(self, QEvent):
        self.label.setText(self.link.format(self.default_decor, self.text))
