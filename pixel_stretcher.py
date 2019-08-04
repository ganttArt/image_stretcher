'''Incremental Pixel Stretcher'''
import datetime
from PIL import Image
import numpy as np


filename = '5.fb.20190424.jpg'

img = Image.open(filename, 'r')
img_array = np.array(img)
new_image = np.zeros((img_array.shape), dtype=np.uint8)
index_array = []

for num in range(len(new_image)):
    for number in range(num+1):
        index_array.append(num)

for num in range(new_image.shape[0]):
    new_image[num] += img_array[index_array[num]]

im = Image.fromarray(new_image)


now = datetime.datetime.now()

im.save(f'ps{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}.png')














