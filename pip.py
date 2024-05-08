import sys
import os

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QMovie


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # os.system('export DISPLAY=:0')

        self.setWindowTitle("PipBoy")
        self.setStyleSheet("background-color: black;") 
        self.setWindowFlags(Qt.FramelessWindowHint)

        # button = QPushButton("Press Me!")

        self.setFixedSize(QSize(480, 320))

        #gif animation
        self.movie = QMovie("images/vaultboy.gif")
        label = QLabel(self)
        label.setMovie(self.movie)
        self.movie.start()
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        #Buttons
        statBtn = QPushButton(text="STAT", parent=self)
        statBtn.setFixedSize(100, 60)        
        statBtn.setStyleSheet("color : green; border: none; font-weight: bold") 
        statBtn.setFont(QFont('Monofonto', 17))

        # invBtn = QPushButton(text="INV", parent=self)
        # invBtn.setFixedSize(100, 60)        
        # invBtn.setStyleSheet("color : green; border: none; font-weight: bold") 
        # invBtn.setFont(QFont('Monofonto', 17))

        #static image
        # pixmap = QPixmap('images/vaultboy.gif')
        # label = QLabel(self)
        # label.setPixmap(pixmap)
        # label.setAlignment(Qt.AlignCenter)
        
        # self.setCentralWidget(label)
        # self.resize(pixmap.width(), pixmap.height())

        # Set the central widget of the Window.
        # self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
