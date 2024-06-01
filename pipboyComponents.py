from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QTabWidget,
    QVBoxLayout,
    QWidget,
    QLabel,
    QApplication,
    QPushButton,
    QListWidget,
    QListWidgetItem,   
)
from PyQt5.QtGui import QMovie, QPalette, QColor, QPixmap


"""
Button Creation Function
"""
def PipButton(btnText):
    btnStyleStr = """
    QPushButton{ 
        background-color: green; 
        border-radius: 0px;
        font-family: Monofonto, serif;
        font-weight: bold;
        font-size: 15px;
    }
    QPushButton:pressed { 
        background-color: #002f00;
    }
    """
    btn = QPushButton()
    btn.setFixedSize(50, 20)
    btn.setStyleSheet(btnStyleStr)
    btn.setText(btnText)
    return btn


def PipLable(lableTxt):
    lableStyleStr = """
    QLabel{
        background-color: green; 
        font-family: Monofonto, serif;
        font-weight: bold;
        font-size: 15px;
    }
    """
    lable = QLabel()
    lable.setFixedSize(120, 20)
    lable.setStyleSheet(lableStyleStr)
    lable.setText(f" {lableTxt}")
    return lable
    
def PipLableCustom(lableTxt, font_size, h, w):
    lableStyleStr = f"""
    QLabel{{
        background-color: green; 
        font-family: Monofonto, serif;
        font-weight: bold;
        font-size: {font_size};
        text-align: center;
    }}
    """
    lable = QLabel()
    lable.setFixedSize(w, h)
    lable.setStyleSheet(lableStyleStr)
    lable.setText(f" {lableTxt}")
    return lable

def PipLableInveted(lableTxt):
    lableStyleStr = """
    QLabel{
        background-color: black; 
        font-family: Monofonto, serif;
        color: green;
        font-weight: bold;
        font-size: 15px;
    }
    """
    lable = QLabel()
    lable.setFixedSize(120, 20)
    lable.setStyleSheet(lableStyleStr)
    lable.setText(f" {lableTxt}")
    return lable


def PipLableInvetedCustom(lableTxt, font_size, h, w):
    lableStyleStr = f"""
    QLabel{{
        background-color: black; 
        font-family: Monofonto, serif;
        color: green;
        font-weight: bold;
        font-size: {font_size};
    }}
    """
    lable = QLabel()
    lable.setFixedSize(w, h)
    lable.setStyleSheet(lableStyleStr)
    lable.setText(f" {lableTxt}")
    return lable

def PipList():
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
    
    list = QListWidget()
    list.setGeometry(20, 20, 100, 100)
    list.setStyleSheet(listStyleStr)

    return list
