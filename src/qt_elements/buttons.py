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
                border-radius: 20px;
                text-align: center;
                font-size: 28px;
                font-weight: 600;
            }
            QPushButton:pressed {
                background-color: #333333;
            }
            QPushButton:focus {
                outline: none;
            }
        """)
        self.indicator = QLabel(self)
        self.indicator.setFixedSize(20, 20)
        self.indicator.move(self.width() - 30, 10)
        self.indicator.setStyleSheet("QLabel { background-color: %s; border-radius: 10px; }" % '#ff2222')
        self.update_status_indicator(False)

    def update_status_indicator(self, value):
        color = '#00ff55' if value else '#ff2222'
        self.indicator.setStyleSheet("QLabel { background-color: %s; border-radius: 10px; }" % color)


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
                border-radius: 20px;
                text-align: center;
                font-size: 28px;
                font-weight: 600;
            }
            QPushButton:pressed {
                background-color: #333333;
            }
            QPushButton:focus {
                outline: none;
            }
        """ % self.color)

class ListButton(QPushButton):
    def __init__(self, icon_path, text, info, action, *args, **kwargs):
        super().__init__(text, *args, **kwargs)
        self.setFixedSize(QSize(440, 100))
        self.clicked.connect(self.callback)
        self.action = action
        self.icon_path = icon_path
        self.info = info
        self.setup_button_style()

    def setup_button_style(self):
        self.setStyleSheet("""
            QPushButton {
                color: white;
                text-align: left;
                padding-left: 20px;
                font-size: 28px;
                font-weight: 600;
            }
            QPushButton:pressed {
                background-color: #333333;
            }
            QPushButton:focus {
                outline: none;
            }
        """)
        self.setIcon(QIcon(self.icon_path))
        self.setIconSize(QSize(50, 50))
        self.setLayoutDirection(Qt.RightToLeft)  # Icon on the right

    def callback(self):
        self.action(self.info)

class AddButton(ListButton):
    def __init__(self, text, info, action, *args, **kwargs):
        # Assuming the add icon is located at 'icons/add_icon.png' within the application's directory structure.
        super().__init__('images/plus_icon_green.png', text, info, action, *args, **kwargs)

class RemoveButton(ListButton):
    def __init__(self, text, info, action, *args, **kwargs):
        # Assuming the remove icon is located at 'icons/remove_icon.png' within the application's directory structure.
        super().__init__('images/minus_icon_red.png', text, info, action, *args, **kwargs)
