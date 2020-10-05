from colorpicker import ColorPicker
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

app = QApplication([])

mainWindow = QMainWindow()
mainWindow.resize(QSize(360, 200))
cp = ColorPicker(mainWindow)
#cp.colorChanged.connect(lambda: print(cp.getColor("hsv")))
mainWindow.show()
cp.show()
#mainWindow.addWidget(cp)

app.exec_()
