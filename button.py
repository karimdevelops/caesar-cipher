from pathlib import Path

from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import (
    QWidget, 
    QPushButton,
    QHBoxLayout
)


class Button(QWidget):

    def __init__(self, text, w, h, hover_bool):
        super().__init__()

        self.hover_bool = hover_bool

        self.default_w = w
        self.default_h = h
        self.hover_w = self.default_w + 45
        self.hover_h = self.default_h + 25

        self.setFixedSize(self.hover_w + 10, self.hover_h + 10)

        self.button = QPushButton(text)
        if self.hover_bool == True:
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
        if self.hover_bool == True:
            self.button.setFixedSize(self.default_w, self.default_h)
            self.button.setStyleSheet(f"font-size: 40px")
