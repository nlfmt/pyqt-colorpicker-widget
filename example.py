from PyQt5.QtWidgets import *

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
        # Use rgb, hsv and hex arguments to set initial color
        self.colorpicker = ColorPicker(self.ui.colorpicker_frame, hsv=(50,50,50))

        # the colorpicker handle is a bit dark and blends in with the bg, let's change it:
        self.colorpicker.ui.hue_selector.setStyleSheet("background-color: #aaa")

        # connect custom Button to display currently selected color
        self.ui.pushButton.clicked.connect(self.selectColor)

        # using ColorPicker's colorChanged signal:
        self.colorpicker.colorChanged.connect(self.onColorChange)


    def selectColor(self):

        # get current color wit getColor() method
        r,g,b = self.colorpicker.getRGB()
        h,s,v = self.colorpicker.getHSV()

        hsv = self.colorpicker.getHSV(360, 1)  # hue in degrees, saturation & value from 0 to 1
        rgb = self.colorpicker.getRGB(100)     # rgb with white = (100,100,100)
        hex = self.colorpicker.getHex(True)    # output with hashtag in string

        self.ui.selected_color_frame.setStyleSheet(f"background-color: rgb({r},{g},{b})")


    def onColorChange(self):
        hex = self.colorpicker.getHex(True)
        self.ui.hex_label.setText(hex)



if __name__=="__main__":
    app = QApplication([])
    window = My_Window()
    window.show()
    app.exec_()
