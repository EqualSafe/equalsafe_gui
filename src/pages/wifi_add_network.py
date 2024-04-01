
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QLineEdit, QApplication, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt
from src.qt_elements.buttons import (FeatureButton, SettingButton)
from src.qt_elements.keyboard import QwertyKeyboard

stylesheet = f"""
QLabel {{
    color: white;
    font-size: 28px;
}}
"""
line_edit_stylesheet = """
QLineEdit {
    color: white;
    font-size: 28px;
    border: 1px solid #aaa;
    border-radius: 10px;
    padding: 1ex;
}
"""

class WifiAddNetworkPage:
    def __init__(self, app):
        self.widget = QWidget()
        self.layout = QVBoxLayout(self.widget)
        self.app = app

    def setup(self):
        # Label and input for SSID
        ssid_label = QLabel("SSID:", self.widget)
        self.layout.addWidget(ssid_label)

        self.ssid_input = QLineEdit(self.widget)
        self.layout.addWidget(self.ssid_input)

        # Label and input for Password
        password_label = QLabel("Password:", self.widget)
        self.layout.addWidget(password_label)

        self.password_visibility_action = QAction(QIcon('images/hide_icon.png'), 'toggle_visibility')
        self.password_visibility_action.triggered.connect(self.toggle_hide_show_password)
        self.password_visibility_action

        self.password_input = QLineEdit(self.widget)
        self.password_hidden = True
        self.password_input.setEchoMode(QLineEdit.Password)  # Hide password text
        self.password_input.addAction(self.password_visibility_action, QLineEdit.TrailingPosition)
        self.layout.addWidget(self.password_input)

        # set styles
        ssid_label.setStyleSheet(stylesheet)
        self.ssid_input.setStyleSheet(line_edit_stylesheet)
        password_label.setStyleSheet(stylesheet)
        self.password_input.setStyleSheet(line_edit_stylesheet)

        # Add Network Button
        add_network_button = SettingButton("Add", self.add_network)
        # Back to wifi networks button
        back_button = SettingButton("Wifi Settings", self.app.show_wifi_settings_page)
        self.layout.addWidget(add_network_button, alignment=Qt.AlignBottom | Qt.AlignCenter)
        self.layout.addWidget(back_button, alignment=Qt.AlignBottom | Qt.AlignCenter)

        # keyboard
        self.keyboard = QwertyKeyboard()
        self.keyboard.keyPressed.connect(self.handleKeyPress)
        self.layout.addWidget(self.keyboard)

    def toggle_hide_show_password(self):
        self.password_hidden = not self.password_hidden
        self.password_input.setEchoMode(QLineEdit.Password if self.password_hidden else QLineEdit.Normal)  # Hide password text
        self.password_visibility_action.setIcon(QIcon('images/hide_icon.png' if self.password_hidden else 'images/show_icon.png'))  # Icon for hidden password


    def handleKeyPress(self, key):
        # Determine which QLineEdit is currently focused
        focusedWidget = QApplication.focusWidget()
        if isinstance(focusedWidget, QLineEdit):
            # If the key is special like Enter, you might want to handle it differently
            if key == '\n':
                # do something when Enter is pressed
                pass
            elif key == '⌫':  # Backspace key
                # Emit a special signal or handle the backspace action directly
                focusedWidget = QApplication.focusWidget()
                if isinstance(focusedWidget, QLineEdit):
                    currentText = focusedWidget.text()
                    # Remove the last character
                    focusedWidget.setText(currentText[:-1])
            else:
                # Insert the key press into the focused QLineEdit
                focusedWidget.insert(key)

    def set_params(self, ssid, password):
        self.ssid_input.setText(ssid)
        self.password_input.setText(password)

    def add_network(self):
        print({
            'ssid': self.ssid_input.text(),
            'password': self.password_input.text()
        })
        self.app.show_wifi_settings_page()
