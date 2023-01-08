# Image Stretcher

![App](/Assets/ImageStretcherApp.jpeg)

Application built using Python, PIL, NumPy and Tkinter (GUI).
Incrementally stretches an image in any cardinal direction, starting at any pixel of your choice.

Requirements: Python3, Pillow, Numpy, Tkinter

To operate the stretcher: Choose your direction, move the slider to the desired stretch-starting place, and press the Stretch! button.
Alternatively, you can just push the random button these choices will be made for you.

## Examples

![Example - Waterfall](/Assets/Waterfall_Stretch.jpg)
![Example - Face Stretch](/Assets/Face_Stretch.png)

## Setup

```bash
git clone https://github.com/ganttArt/image_stretcher.git
cd image_stretcher
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

## Run

Start:

```bash
. venv/bin/activate
python main.py
```

Stop:

```bash
deactivate
```
