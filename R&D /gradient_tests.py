'''gradient testing'''

from PIL import Image
import numpy as np
import datetime

FILENAME = '10w6h.jpg'
gradient_length = 15

img = Image.open(FILENAME, 'r')
image_width = img.size[0]


np_array = np.array(img)

# new_image = np.zeros((10, 10, 3), dtype=np.uint8)
new_image = np.zeros((gradient_length+2, image_width, 3))

new_image[0] += np_array[0]
new_image[-1] += np_array[-1]

diff_array = abs(new_image[0]-new_image[-1])

for num in range(gradient_length):
    for row in range(image_width):
        for column in range(3):
            if new_image[0][row][column] >= new_image[-1][row][column]:
                new_image[num+1][row][column] += (new_image[0][row][column] - ((diff_array[row][column])/(gradient_length+1)*(num+1)))                
            else:
                new_image[num+1][row][column] += (new_image[0][row][column] + ((diff_array[row][column])/(gradient_length+1)*(num+1)))


#convert np array to integers
even_newer = new_image.astype(np.uint8)


pil_image = Image.fromarray(even_newer)
pil_image.show()
# now = datetime.datetime.now()
# pil_image.save(f'ps{now.year}{now.month}{now.day}_'+
#                f'{now.hour}{now.minute}{now.second}.jpg')


