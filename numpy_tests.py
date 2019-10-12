'''numpy tests'''

from PIL import Image
import numpy as np

FILENAME = '2h_580w.jpg'

img = Image.open(FILENAME, 'r')

print(img.size[0])
