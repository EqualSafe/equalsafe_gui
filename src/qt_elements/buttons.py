import sys
from PyQt5.QtWidgets import (QPushButton, QLabel)
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPixmap


class FeatureButton(QPushButton):
    def __init__(self, text, action, status_function, *args, **kwargs):
        super().__init__(text, *args, **kwargs)
        self.status_function = status_function
        self.setFixedSize(QSize(220, 100))
        self.clicked.connect(action)
        self.setStyleSheet("""
            QPushButton {
                background-color: #555555;
                color: white;
                border-radius: 10px;
                text-align: center;
                font-size: 28px;
                font-weight: 600;
            }
            QPushButton:pressed {
                background-color: #333333;
            }
        """)
        self.indicator = QLabel(self)
        self.indicator.setFixedSize(10, 10)
        self.indicator.move(self.width() - 15, 5)
        self.indicator.setStyleSheet("QLabel { background-color: %s; border-radius: 5px; }" % '#ff2222')
        self.update_status_indicator(False)

    def update_status_indicator(self, value):
        color = '#00ff55' if value else '#ff2222'
        self.indicator.setStyleSheet("QLabel { background-color: %s; border-radius: 5px; }" % color)


class SettingButton(QPushButton):
    def __init__(self, text, action, custom_color='#555555', *args, **kwargs):
        super().__init__(text, *args, **kwargs)
        self.color = custom_color
        self.setFixedSize(QSize(460, 100))
        self.clicked.connect(action)
        self.setStyleSheet("""
            QPushButton {
                background-color: %s;
                color: white;
                border-radius: 10px;
                text-align: center;
                font-size: 30px;
                font-weight: 600;
            }
            QPushButton:pressed {
                background-color: #333333;
            }
        """ % self.color)