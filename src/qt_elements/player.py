import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl

class VideoPlayer(QWidget):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle("PyQt Video Stream Player")
        self.setGeometry(100, 100, 420, 360)

        # Create instances of QMediaPlayer and QVideoWidget
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoWidget = QVideoWidget()

        # Layout and buttons
        self.playButton = QPushButton('Play')
        self.stopButton = QPushButton('Stop')
        self.playButton.clicked.connect(self.playVideo)
        self.stopButton.clicked.connect(self.stopVideo)

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.videoWidget)
        layout.addWidget(self.playButton)
        layout.addWidget(self.stopButton)
        self.setLayout(layout)

        # Set the video output to the video widget
        self.mediaPlayer.setVideoOutput(self.videoWidget)

    def playVideo(self):
        # Set the media content to a stream URL
        # Example: Replace 'your_stream_url_here' with your actual stream URL
        streamUrl = 'udp://@localhost:8000'
        self.mediaPlayer.setMedia(QMediaContent(QUrl(streamUrl)))
        self.mediaPlayer.play()

    def stopVideo(self):
        self.mediaPlayer.stop()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     player = VideoPlayer()
#     player.show()
#     sys.exit(app.exec_())
