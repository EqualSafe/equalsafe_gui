from PyQt5.QtWidgets import QWidget, QVBoxLayout, QStackedWidget, QLabel
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, QSize, pyqtSignal, Qt
from PyQt5.QtGui import QColor, QPalette, QPixmap

class VideoPlayer(QWidget):
    playRequested = pyqtSignal()

    def __init__(self, sdpUrl, parent=None):
        super().__init__(parent)
        self.sdpUrl = '/Users/omarkanj/Desktop/Projects/file1.sdp'#sdpUrl
        self.player = QMediaPlayer(self)
        self.stack = QStackedWidget(self)  # Use a stacked widget to layer the video and background
        self.videoWidget = QVideoWidget(self.stack)
        self.backgroundWidget = QWidget(self.stack)  # Widget to show when the video is not playing
        self.initUI()
        self.playRequested.connect(self.togglePlayback)

    def initUI(self):
        self.setMinimumSize(QSize(460, 280))
        self.setMaximumSize(QSize(460, 280))
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.stack)
        self.setLayout(self.layout)

        # Setup background widget
        self.backgroundWidget.setAutoFillBackground(True)
        self.backgroundWidget.setStyleSheet("""
            QWidget {
                background-color: #444444;
                border-radius: 20px;
            }
            """)

        # Setup label with text and an icon
        self.label = QLabel("Camera playback off\nPress to turn on", self.backgroundWidget)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: white; margin: 15px;font-size: 20px")
        # Set the path to your camera icon PNG file
        self.icon = QLabel('', self.backgroundWidget)
        iconPath = 'images/camera_white_64.png'
        self.icon.setPixmap(QPixmap(iconPath))
        self.icon.setWordWrap(True)

        # Layout for the background widget to center the label
        bgLayout = QVBoxLayout(self.backgroundWidget)
        bgLayout.addWidget(self.icon, alignment=Qt.AlignCenter)
        bgLayout.addWidget(self.label, alignment=Qt.AlignCenter)

        self.backgroundWidget.setLayout(bgLayout)

        self.stack.addWidget(self.backgroundWidget)  # Add background widget to stack
        self.stack.addWidget(self.videoWidget)  # Add video widget to stack

        # Set the video output to the video widget
        self.player.setVideoOutput(self.videoWidget)

        # Load the video
        self.loadVideo()

        self.stack.setCurrentWidget(self.backgroundWidget)  # Set background widget as current


    def loadVideo(self):
        content = QMediaContent(QUrl.fromLocalFile(self.sdpUrl))
        self.player.setMedia(content)
        self.stack.setCurrentWidget(self.videoWidget)  # Switch to video widget when video is loaded

    def mousePressEvent(self, event):
        # Emit a signal when the widget is pressed
        self.playRequested.emit()

    def togglePlayback(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
            self.stack.setCurrentWidget(self.backgroundWidget)  # Show the background widget
        else:
            self.loadVideo()
            self.player.play()
            self.stack.setCurrentWidget(self.videoWidget)  # Show the video widget
