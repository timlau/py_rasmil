# Rasmil Misc Tools Python Libraty

## Libraries

### rasmil.xfce

Class Xfconf : Library to access Xfce conf


### rasmil.materials

Contains Google Material Design color palettes

**USAGE:**

MATERIAL.<ColorName>.Shade<ShadeValue>

MATERIAL.colors             : Gives a list of available color names

MATERIAL.<ColorName>.shades : Returns a list of available shades for a give color

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
