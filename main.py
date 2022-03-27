from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

xpos = 0
ypos = 0

diff = 20

def runApp():
    app = QApplication(sys.argv)
    screenRes = app.desktop().screenGeometry()
    width = screenRes.width()
    height = screenRes.height()
    win = QMainWindow()
    win.setStyleSheet("QMainWindow {background : white;}")
    win.setGeometry(xpos, ypos, width, height)
    win.setWindowTitle("FEC tool")
    
    headerHeight = int(0.1 * height)

    label = QtWidgets.QLabel(win)
    label.setGeometry(0, 0, width, headerHeight)
    label.setText("ING FEC Tool")
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet("QLabel { background-color : rgb(255, 0, 0); color : white; font-size : 24px; font-family: Arial}")

    boxHeight = 50

    txtbox = QtWidgets.QLineEdit(win, placeholderText="Please insert value")
    txtbox.setGeometry(50, headerHeight + diff, 200, boxHeight)
    txtbox.setStyleSheet("QLineEdit { background-color : white; color : black; font-size : 18px; }")

    addButton = QtWidgets.QPushButton(win)
    addButton.setGeometry(300, headerHeight + diff, 80, boxHeight)
    addButton.setText("Add")
    addButton.setStyleSheet("QPushButton { background-color : rgb(255, 0, 0); color : white; border-radius : 10px;}")

    uploadButton = QtWidgets.QPushButton(win)
    uploadButton.setGeometry(400, headerHeight + diff, 80, boxHeight)
    uploadButton.setText("Upload")
    uploadButton.setStyleSheet("QPushButton { background-color : rgb(255, 0, 0); color : white; border-radius : 10px;}")

    buttsHeight = headerHeight + boxHeight + diff
    buttHeight = 20
    rowWidth = 100

    rdButt1 = QtWidgets.QRadioButton("Option1", win)
    rdButt1.setGeometry(50, buttsHeight + diff, rowWidth, buttHeight)
    rdButt1.setStyleSheet("QRadioButton { color : black; }")

    rdButt2 = QtWidgets.QRadioButton("Option2", win)
    rdButt2.setGeometry(50, buttsHeight + 2 * diff, rowWidth, buttHeight)
    rdButt2.setStyleSheet("QRadioButton { color : black; }")

    rdButt3 = QtWidgets.QRadioButton("Option3", win)
    rdButt3.setGeometry(50, buttsHeight + 3 * diff, rowWidth, buttHeight)
    rdButt3.setStyleSheet("QRadioButton { color : black; }")

    rdButt1 = QtWidgets.QRadioButton("Option4", win)
    rdButt1.setGeometry(50 + rowWidth + diff, buttsHeight + diff, rowWidth, buttHeight)
    rdButt1.setStyleSheet("QRadioButton { color : black; }")

    rdButt2 = QtWidgets.QRadioButton("Option5", win)
    rdButt2.setGeometry(50 + rowWidth + diff, buttsHeight + 2 * diff, rowWidth, buttHeight)
    rdButt2.setStyleSheet("QRadioButton { color : black; }")

    rdButt3 = QtWidgets.QRadioButton("Option6", win)
    rdButt3.setGeometry(50 + rowWidth + diff, buttsHeight + 3 * diff, rowWidth, buttHeight)
    rdButt3.setStyleSheet("QRadioButton { color : black; }")
    
    win.show()
    sys.exit(app.exec_())


runApp()
