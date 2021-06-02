# Rasmil Misc Tools Python Libraty

## Libraries

### rasmil.xfce

class Xfconf : Library to access Xfce conf

### rasmil.widgets
contains custom gtk3 widgets

class CircularProgressBar : an Circular ProgressBar widget with 2 lines of text in the center with customizable fonts

![alt text][progress]

[progress]: docs/circular.png "Circular ProgressBar"

### rasmil.materials

Contains Google Material Design color palettes

https://material.io/design/color/the-color-system.html#tools-for-picking-colors


**USAGE:**

`MATERIAL.<ColorName>.Shade<ShadeValue>`

Methods                       | Description
----------------------------- | ------------------------------------------------------
`MATERIAL.colors`             | Gives a list of available color names
`MATERIAL.<ColorName>.shades` | Returns a list of available shades for a give color

**test.py**
```python
from rasmil.material import MATERIAL

print(MATERIAL.colors)
print(MATERIAL.Teal.shades)
print(MATERIAL.Green.Shade100)
```

**Output**
```bash
python3 test.py

['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
['Shade50', 'Shade100', 'Shade200', 'Shade300', 'Shade400', 'Shade500', 'Shade600', 'Shade700', 'Shade800', 'Shade900', 'ShadeA100', 'ShadeA200', 'ShadeA400', 'ShadeA700']
#C8E6C9

```
