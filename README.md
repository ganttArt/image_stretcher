# Image Stretcher

Python script that incrementally stretches an image in any direction, starting at any pixel of your choice.

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

- `. venv/bin/activate`
- Move desired image into image_stretcher directory
- Update variables on [main.py](main.py) to include your image and desired settings (starting point, direction, stretch intensity)
- run `python main.py`
