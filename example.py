from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize

from example_window import Ui_MainWindow
from colorpicker import ColorPicker



# Basic Window class using QtDesigner & pyuic5
class My_Window(QMainWindow):


    def __init__(self, *args, **kwargs):
        super(My_Window, self).__init__(*args, **kwargs)

        # set up your custom UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create the colorpicker widget inside the colorpicker_frame in your ui
        self.colorpicker = ColorPicker(self.ui.colorpicker_frame)

        # the colorpicker handle is a bit dark and blends in with the bg, let's change it:
        self.colorpicker.ui.hue_selector.setStyleSheet("background-color: #aaa")

        # connect custom Button to display currently selected color
        self.ui.pushButton.clicked.connect(self.selectColor)

        # using ColorPicker's colorChanged signal:
        self.colorpicker.colorChanged.connect(self.onColorChange)

        print(self.colorpicker.hex2rgb("dd3322"))
        #self.colorpicker.ui.editfields.close()
        self.colorpicker.ui.color_view.close()
        self.colorpicker.ui.hue_frame.close()
        #self.ui.colorpicker_frame.resize(QSize(120,200))
        self.ui.colorpicker_frame.setStyleSheet("background-color: red;")


    def selectColor(self):

        # get current color wit getColor() method
        r,g,b = self.colorpicker.getRGB()
        h,s,v = self.colorpicker.getHSV()

        hsv = self.colorpicker.getHSV(hrange=360, svrange=1)  # hue in degrees, saturation & value from 0 to 1
        rgb = self.colorpicker.getRGB(100)              # rgb in percent
        hex = self.colorpicker.getHex(True)                # use hashtag in string

        print(hsv)
        print(rgb)
        print(hex)
        self.ui.selected_color_frame.setStyleSheet(f"background-color: rgb({r},{g},{b})")


    def onColorChange(self):
        hex = self.colorpicker.getHex(1)
        self.ui.hex_label.setText(hex)



if __name__=="__main__":
    app = QApplication([])
    window = My_Window()
    window.show()
    app.exec_()
