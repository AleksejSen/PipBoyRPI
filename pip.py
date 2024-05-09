# images from: https://github.com/ultrinnan/PipBoy?tab=readme-ov-file
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
    QButtonGroup,
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
        self.main_layout.setSpacing(0)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        # Set the layout on the central widget
        central_widget.setLayout(self.main_layout)

        # STAT Menue
        mainWindowStyles = """
            border: none;
            border-top : 3px solid green;
        """
        self.movie = QMovie("images/vaultboy.gif")
        valutBoyLable = QLabel(self)
        valutBoyLable.setMovie(self.movie)
        self.movie.start()
        valutBoyLable.setAlignment(Qt.AlignCenter)
        valutBoyLable.setStyleSheet(mainWindowStyles)
        # self.main_layout.insertWidget(0, valutBoyLable)
        self.main_layout.addWidget(valutBoyLable)

        # INV Menue
        # self.anotherLabel = QLabel("Another Label", self)
        # self.anotherLabel.setAlignment(Qt.AlignCenter)
        # self.anotherLabel.setStyleSheet(mainWindowStyles)
        # self.anotherLabel.hide()  # Hide it initially
        # self.main_layout.addWidget(self.anotherLabel)

        btnFontSize = 15
        btnHsize = 40
        btnWsize = 80

        buttonStyleStr = """
        QPushButton
        {
            font-family: Monofonto, serif;
            font-size: 15px;
            color : green;
            border: none;
            border-bottom : 3px solid green;
            margin-bottom: -10px
        }
        QPushButton::checked
        {
            color : green;
            border: none;
            border-top : 3px solid green;
            border-left : 3px solid green;
            border-right : 3px solid green;
            border-top-left-radius: 7px;
            border-top-right-radius: 7px;
            border-bottom : 3px solid green;
            font-weight: bold;
            font-size: 16px;
            margin-bottom: -10px;
            padding-bottom: 5px;
        }
        """

        statBtn = QPushButton(text="STAT", parent=self)
        statBtn.setFixedSize(btnWsize, btnHsize)
        statBtn.setStyleSheet(buttonStyleStr)
        statBtn.setCheckable(True)
        statBtn.setChecked(True)

        invBtn = QPushButton(text="INV", parent=self)
        invBtn.setFixedSize(btnWsize, btnHsize)
        invBtn.setStyleSheet(buttonStyleStr)
        invBtn.setCheckable(True)

        dataBtn = QPushButton(text="DATA", parent=self)
        dataBtn.setFixedSize(btnWsize, btnHsize)
        dataBtn.setStyleSheet(buttonStyleStr)
        dataBtn.setCheckable(True)

        mapBtn = QPushButton(text="MAP", parent=self)
        mapBtn.setFixedSize(btnWsize, btnHsize)
        mapBtn.setStyleSheet(buttonStyleStr)
        mapBtn.setCheckable(True)

        radioBtn = QPushButton(text="RADIO", parent=self)
        radioBtn.setFixedSize(btnWsize, btnHsize)
        radioBtn.setStyleSheet(buttonStyleStr)
        radioBtn.setCheckable(True)

        # button group to chec/unchek buttons
        btn_group = QButtonGroup(self)
        btn_group.addButton(statBtn)
        btn_group.addButton(invBtn)
        btn_group.addButton(dataBtn)
        btn_group.addButton(mapBtn)
        btn_group.addButton(radioBtn)

        self.top_bar.addWidget(statBtn)
        self.top_bar.addWidget(invBtn)
        self.top_bar.addWidget(dataBtn)
        self.top_bar.addWidget(mapBtn)
        self.top_bar.addWidget(radioBtn)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

            # border-top : 3px solid green;
            # border-left : 3px solid green;
            # border-right : 3px solid green;
            # border-top-left-radius: 7px;
