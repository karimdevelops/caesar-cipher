from pathlib import Path

from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import (
    QWidget, 
    QPushButton,
    QHBoxLayout
)


class Button(QWidget):

    def __init__(self, text, hover_bool):
        super().__init__()

        self.setFixedSize(280, 105)

        self.hover_bool = hover_bool

        self.default_w = 245
        self.default_h = 85
        self.hover_w = 270
        self.hover_h = 95

        self.button = QPushButton(text)
        self.button.setObjectName("button")
        self.button.setFixedSize(self.default_w, self.default_h)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)


    def enterEvent(self, QEnterEven):
        if self.hover_bool == True:
            self.button.setFixedSize(self.hover_w, self.hover_h)
            self.button.setStyleSheet("font-size: 45px")

    def leaveEvent(self, QEvent):
        self.button.setFixedSize(self.default_w, self.default_h)
        self.button.setStyleSheet("font-size: 40px")
