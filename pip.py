import sys
import os

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (
   QApplication, 
   QMainWindow, 
   QWidget, 
   QPushButton, 
   QLabel,
   QVBoxLayout, 
   QHBoxLayout,
) 
from PyQt5.QtGui import QMovie, QPalette, QColor


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # os.system('export DISPLAY=:0')

        self.setWindowTitle("PipBoy")
        self.setStyleSheet("background-color: black;") 
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.setFixedSize(QSize(480, 320))
        self.top_bar = QHBoxLayout()
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.top_bar)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        # Set the layout on the central widget
        central_widget.setLayout(self.main_layout)

        #gif animation
        self.movie = QMovie("images/vaultboy.gif")
        valutBoyLable = QLabel(self)
        valutBoyLable.setMovie(self.movie)
        self.movie.start()
        valutBoyLable.setAlignment(Qt.AlignCenter)

        self.main_layout.addWidget(valutBoyLable)

        #Buttons
        btnFontSize = 15
        btnHsize = 40
        btnWsize = 80

        statBtn = QPushButton(text="STAT", parent=self)
        statBtn.setFixedSize(btnWsize, btnHsize)        
        statBtn.setStyleSheet("color : green; border: none; font-weight: bold") 
        statBtn.setFont(QFont('Monofonto', btnFontSize))

        invBtn = QPushButton(text="INV", parent=self)
        invBtn.setFixedSize(btnWsize, btnHsize)        
        invBtn.setStyleSheet("color : green; border: none; font-weight: bold") 
        invBtn.setFont(QFont('Monofonto', btnFontSize))
        
        dataBtn = QPushButton(text="DATA", parent=self)
        dataBtn.setFixedSize(btnWsize, btnHsize)        
        dataBtn.setStyleSheet("color : green; border: none; font-weight: bold") 
        dataBtn.setFont(QFont('Monofonto', btnFontSize))

        mapBtn = QPushButton(text="MAP", parent=self)
        mapBtn.setFixedSize(btnWsize, btnHsize)        
        mapBtn.setStyleSheet("color : green; border: none; font-weight: bold") 
        mapBtn.setFont(QFont('Monofonto', btnFontSize))
        
        radioBtn = QPushButton(text="RADIO", parent=self)
        radioBtn.setFixedSize(btnWsize, btnHsize)        
        radioBtn.setStyleSheet("color : green; border: none; font-weight: bold") 
        radioBtn.setFont(QFont('Monofonto', btnFontSize))

        self.top_bar.addWidget(statBtn)
        self.top_bar.addWidget(invBtn)
        self.top_bar.addWidget(dataBtn)
        self.top_bar.addWidget(mapBtn)
        self.top_bar.addWidget(radioBtn)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
