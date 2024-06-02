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
        #Inventor Tab
        self.weapons_btn = pc.PipButton("WEAPONS", 15, 100, 20)
        tabs.addTab(self.invTabUI(), "INV")
        tabs.currentChanged.connect(self.set_focus_on_weapons)

        tabs.addTab(self.dataTabUI(), "DATA")
        tabs.addTab(self.mapTabUI(), "MAP")
        tabs.addTab(self.radioTabUI(), "RADIO")
        layout.addWidget(tabs)


    def set_focus_on_weapons(self):
        self.weapons_btn.setFocus()
    
    def statTabUI(self):
        """Create the General page UI."""
        tab = QWidget()
        mainWindowStyles = """
            border: none;
        """
        vaultboy_pic = os.path.join(os.path.dirname(__file__), 'images/vaultboy.gif')
        self.movie = QMovie(vaultboy_pic)
        valutBoyLable = QLabel(self)
        valutBoyLable.setMovie(self.movie)
        self.movie.start()
        valutBoyLable.setAlignment(Qt.AlignCenter)
        valutBoyLable.setStyleSheet(mainWindowStyles)

        layout = QVBoxLayout()
        layout.addWidget(valutBoyLable)


        # status bar
        status_layout = QHBoxLayout()
            
        healthBarsStylStr = """
        QProgressBar{
            border : 2px solid green;
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
        #healt bar
        bar = QProgressBar()
        bar.setStyleSheet(healthBarsStylStr)
        bar.setGeometry(80, 10, 80, 10)
        bar.setFixedSize(140, 15)
        bar.setValue(94)

        #Armor element
        helmet_pic = os.path.join(os.path.dirname(__file__), 'images/pipboy-helmet2.png')
        helmet_pic = QPixmap(helmet_pic)
        helmet = QLabel()
        hekmet_scale = helmet_pic.scaled(36, 25)
        helmet.setPixmap(hekmet_scale) 
        helmet.setFixedSize(36, 25)
        armor_lable = pc.PipLableInvetedCustom("45", 10, 12, 30)
        armor_layout = QVBoxLayout()
        armor_layout.addWidget(helmet)
        armor_layout.addWidget(armor_lable)
        armor_layout.setAlignment(Qt.AlignVCenter)

        #gun
        gun_pic = os.path.join(os.path.dirname(__file__), 'images/pipboy-gun2.png')
        gun_pic = QPixmap(gun_pic)
        gun = QLabel()
        hekmet_scale = gun_pic.scaled(36, 25)
        gun.setPixmap(hekmet_scale) 
        gun.setFixedSize(36, 25)
        gun_lable = pc.PipLableInvetedCustom("84", 10, 12, 30)
        gun_layout = QVBoxLayout()
        gun_layout.addWidget(gun)
        gun_layout.addWidget(gun_lable)

        
        #Add components to status bar
        status_layout.addLayout(armor_layout) 
        status_layout.addWidget(bar)
        status_layout.addLayout(gun_layout) 
        status_layout.setSpacing(0)
        
        layout.addLayout(status_layout)

        tab.setLayout(layout)
        tab.resize(420, 280)
        return tab

    
    def invTabUI(self):
        main_layout = QVBoxLayout()
        # Create a vertical layout
        top_layout = QHBoxLayout()
        
        apeal_btn = pc.PipButton("APEAL", 15, 100, 20)
        aid_btn = pc.PipButton("AID", 15, 100, 20)

        apeal_btn.setFocusPolicy(Qt.StrongFocus)
        aid_btn.setFocusPolicy(Qt.StrongFocus)


        # Add buttons for each item in the list
        #wapon button is creted in the Window class to fix auto focus when this tab is active
        top_layout.addWidget(self.weapons_btn)
        top_layout.addWidget(apeal_btn)
        top_layout.addWidget(aid_btn)

        #Lists
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

        pisotl_item= QListWidgetItem("10mm Pistol")
        fatman_item= QListWidgetItem("Fat Man")
        shotgun_item= QListWidgetItem("Shotgun")
        minigun_item= QListWidgetItem("Minigun")

        list.addItem(pisotl_item)
        list.addItem(fatman_item)
        list.addItem(shotgun_item)
        list.addItem(minigun_item)

        #Gun viewer layout
        gun10mm_pic = QPixmap(os.path.join(os.path.dirname(__file__), 'images/10mmgreen.png'))
        gun10mm_pic = gun10mm_pic.scaled(150, 104)
        pic = pc.PipLableInveted("Item Name")
        pic.setPixmap(gun10mm_pic)
        pic.setFixedSize(200, 200)
        gun_view_layout = QVBoxLayout()
        gun_view_layout.addWidget(pic)
        #TODO: add gun description lable here

        inventory_layout = QHBoxLayout()
        invTab = QWidget()
        # Set the layout for the main widget
        main_layout.addLayout(top_layout)
        inventory_layout.addWidget(list)
        inventory_layout.addWidget(pic)
        main_layout.addLayout(inventory_layout)
        invTab.setLayout(main_layout)


        # Set window properties
        invTab.setWindowTitle("Vertical List Example")
        invTab.setGeometry(100, 100, 300, 200)

        return invTab

    def dataTabUI(self):
        """Create the data page UI."""
        dataTab = QWidget()
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

        good_pic = QPixmap(os.path.join(os.path.dirname(__file__), 'images/good.png'))
        wasteland_pic = QPixmap(os.path.join(os.path.dirname(__file__), 'images/wasteland.png'))
        voice_pic = QPixmap(os.path.join(os.path.dirname(__file__), 'images/voice.png'))
        radiation_pic = QPixmap(os.path.join(os.path.dirname(__file__), 'images/radiation.png'))

        list.addItem(good_item)
        list.addItem(waste_item)
        list.addItem(voice_item)
        list.addItem(radio_item)

        pic = pc.PipLable("Item Name")
        pic.setPixmap(wasteland_pic)
        pic.setFixedSize(200, 200)
        layout.addWidget(list)       
        layout.addWidget(pic)       

        def showPicture():
            if(list.currentItem().text() == "Good"):
                pic.setPixmap(good_pic)

            if(list.currentItem().text() == "Wasteland"):
                pic.setPixmap(wasteland_pic)
                
            if(list.currentItem().text() == "Voice"):
                pic.setPixmap(voice_pic)

            if(list.currentItem().text() == "Radiation"):
                pic.setPixmap(radiation_pic)

        list.currentItemChanged.connect(showPicture)
        
        dataTab.setLayout(layout)
        dataTab.resize(420, 280)
        return dataTab

    def mapTabUI(self):
        """Create the map page UI."""
        
        mapTab = QWidget()
        mapPic = QPixmap(os.path.join(os.path.dirname(__file__), 'images/map.png'))
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
        radioPic = QPixmap(os.path.join(os.path.dirname(__file__), 'images/radio.png' ))
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
