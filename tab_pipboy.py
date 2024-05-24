import sys
import os
import pipboyComponents as pc

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QTabWidget,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QLabel,
    QListWidget,
    QListWidgetItem,   
    QApplication,
    QPushButton,
    QProgressBar,
)
from PyQt5.QtGui import QMovie, QPalette, QColor, QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PiP Boy")
        self.resize(480, 320)
        self.setFixedSize(480, 320)
        self.setStyleSheet("background-color: black;")
        self.setWindowFlags(Qt.FramelessWindowHint)

        tabBarStyle = """
        QTabWidget::pane{
            border: 3px solid green;
            border-radius: 7px;
        }
        QTabBar::tab {
            width: 85px; 
        }
        QTabBar {
            alignment: center; 
            font-family: Monofonto, serif;
            font-size: 15px;
            color : green;
        }
        QTabBar::tab-bar {
            border: 3px solid black;
            border-top : 3px solid black;
            border-bottom : 3px solid black;
        }
        QTabBar::tab:selected {
            color : green;
            font-size: 16px; 
            font-weight: bold;
            font-size: 16px;
            border: none;
            border-top : 3px solid green;
            border-bottom : 3px solid green;
            border-radius: 7px;
        }
        """
        # Create a top-level layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        # Create the tab widget with two tabs
        tabs = QTabWidget()
        tabs.resize(420, 280)
        tabs.setStyleSheet(tabBarStyle)

        tabs.addTab(self.statTabUI(), "STAT")
        tabs.addTab(self.invTabUI(), "INV")
        tabs.addTab(self.dataTabUI(), "DATA")
        tabs.addTab(self.mapTabUI(), "MAP")
        tabs.addTab(self.radioTabUI(), "RADIO")
        layout.addWidget(tabs)

    def statTabUI(self):
        """Create the General page UI."""
        tab = QWidget()
        mainWindowStyles = """
            border: none;
        """
        self.movie = QMovie("images/vaultboy.gif")
        valutBoyLable = QLabel(self)
        valutBoyLable.setMovie(self.movie)
        self.movie.start()
        valutBoyLable.setAlignment(Qt.AlignCenter)
        valutBoyLable.setStyleSheet(mainWindowStyles)

        layout = QVBoxLayout()
        layout.addWidget(valutBoyLable)


        # status bar
        status_layout = QHBoxLayout()
            
        barStyleStr = """
        QProgressBar{
            font-size: 10px;
            font-family: Monofonto, serif;
            font-weight: bold;
            text-align: center;
        }
        QProgressBar::chunk {
            font-size: 10px;
            background-color: green;
        }
        """
        bar = QProgressBar()
        bar.setStyleSheet(barStyleStr)
        bar.setGeometry(80, 10, 80, 10)
        bar.setFixedSize(140, 10)
        bar.setValue(100)
        
        helmet_pic = QPixmap('images/pipboy-helmet2.png')
        helmet = QLabel()
        hekmet_scale = helmet_pic.scaled(30, 30)
        helmet.setPixmap(hekmet_scale) 
        helmet.setFixedSize(50, 50)
        status_layout.addWidget(helmet)
        status_layout.addWidget(bar)
        
        layout.addLayout(status_layout)
        # layout.addWidget(bar)

        tab.setLayout(layout)
        tab.resize(420, 280)
        return tab

    def invTabUI(self):
        """Create the inv page UI."""
        invTab = QWidget()
        invePic = QPixmap('images/inventory.png')
        lable = QLabel()
        lable.setPixmap(invePic)
        lable.setScaledContents(True)
        layout = QVBoxLayout()
        layout.addWidget(lable)
        invTab.setLayout(layout)
        invTab.resize(420, 280)
        return invTab

    def dataTabUI(self):
        """Create the data page UI."""
        dataTab = QWidget()
        # dataPic = QPixmap('images/data.png')
        # lable = QLabel()
        # lable.setPixmap(dataPic)
        # lable.setScaledContents(True)
        # layout = QVBoxLayout()
        # layout.addWidget(lable)

        layout = QHBoxLayout()

        #List
        listStyleStr = """
        QListWidget {
            border : 2px solid green;
            color : green;
            font-family: Monofonto, serif;
            font-weight: bold;
            font-size: 15px;
        }
        QListView::item:selected {
            background-color: green; 
            color : black;
        }
        """
        list = pc.PipList()

        good_item= QListWidgetItem("Good")
        waste_item= QListWidgetItem("Wasteland")
        voice_item= QListWidgetItem("Voice")
        radio_item= QListWidgetItem("Radiation")

        good_pic = QPixmap('images/good.png')
        wasteland_pic = QPixmap('images/wasteland.png')
        voice_pic = QPixmap('images/voice.png')
        radiation_pic = QPixmap('images/radiation.png')

        list.addItem(good_item)
        list.addItem(waste_item)
        list.addItem(voice_item)
        list.addItem(radio_item)

        pic = pc.PipLable("Item Name")
        pic.setPixmap(wasteland_pic)
        pic.setFixedSize(200, 200)
        layout.addWidget(list)       
        layout.addWidget(pic)       

        # pic.setPixmap(pic1)


        def showPicture():
            if(list.currentItem().text() == "Good"):
                pic.setPixmap(good_pic)

            if(list.currentItem().text() == "Wasteland"):
                pic.setPixmap(wasteland_pic)
                
            if(list.currentItem().text() == "Voice"):
                pic.setPixmap(voice_pic)

            if(list.currentItem().text() == "Radiation"):
                pic.setPixmap(radiation_pic)

            
            
            # pic.setText(list.currentItem().text()) 

        list.currentItemChanged.connect(showPicture)
        
        dataTab.setLayout(layout)
        dataTab.resize(420, 280)
        return dataTab

    def mapTabUI(self):
        """Create the map page UI."""
        mapTab = QWidget()
        mapPic = QPixmap('images/map.png')
        lable = QLabel()
        lable.setPixmap(mapPic)
        lable.setScaledContents(True)
        layout = QVBoxLayout()
        layout.addWidget(lable)
        mapTab.setLayout(layout)
        mapTab.resize(420, 280)
        return mapTab

    def radioTabUI(self):
        """Create the radio page UI."""
        radioTab = QWidget()
        radioPic = QPixmap('images/radio.png')
        lable = QLabel()
        lable.setPixmap(radioPic)
        lable.setScaledContents(True)
        layout = QVBoxLayout()
        layout.addWidget(lable)
        radioTab.setLayout(layout)
        radioTab.resize(420, 280)
        return radioTab


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setOverrideCursor(Qt.BlankCursor)  # Set the cursor to blank
    window = Window()
    window.show()
    sys.exit(app.exec_())
