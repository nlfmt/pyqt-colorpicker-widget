# PyQt5 Color Picker

Simple Color Picker Widget created with PyQt5 to easily get color input from the user.

![colorpicker](https://user-images.githubusercontent.com/71983360/95017068-408f8100-0657-11eb-8001-a6788e94abba.png)


## Usage

1. To use the Color Picker Widget in a python project make sure you have the `PyQt5` library:

   ```
   pip install PyQt5
   ```

   then add the `colorpicker` folder into your project folder and import `ColorPicker`

   ```python
   from colorpicker import ColorPicker
   ```

2. To add the widget to your app, create a `360x200` placeholder widget in your ui and add the colorpicker to it:

   ```python
   colorpicker = ColorPicker(my_placeholder)
   ```

   and then run the `getColor` method to get the currently selected color:

   ```python
   current_color = colorpicker.getColor()
   ```


* `getColor` returns either an RGB tuple: `(255,255,255)` and HSV tuple: `(100,100,100)` or a hex string: `"ffffff"`.\
  Change format by using the mode keyword with either "rgb", "hsv" or "hex"

   ```python
   hsv = colorpicker.getColor(mode="hsv")
   rgb = colorpicker.getColor(mode="rgb")
   hex = colorpicker.getColor(mode="hex")
   ```

* Use ColorPicker's `colorChanged` signal to update directly when the user changes the color:

  ```python
  colorpicker.colorChanged.connect(my_function)

  def my_function():
    print(colorpicker.getColor())
  ```

* For an example with a bigger application based on a main class, look at the `example.py` file.
