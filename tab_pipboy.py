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

        layout.addWidget(pc.PipButton("BTN2"))
        layout.addWidget(pc.PipLable("Lable1"))
        layout.addWidget(pc.PipLableInveted("Lable2"))

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

        item1 = QListWidgetItem("Item 1")
        item2 = QListWidgetItem("Item 2")

        list.addItem(item1)
        list.addItem(item2)

        pic = pc.PipLable("Item Name")
        layout.addWidget(list)       
        layout.addWidget(pic)       

        def print_info():
            pic.setText(list.currentItem().text()) 

        list.currentItemChanged.connect(print_info)
        
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
