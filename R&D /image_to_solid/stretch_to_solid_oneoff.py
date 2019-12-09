'''
    Taking the average of all of the pixels in the image,
    Fading to that color while stretching
'''
from PIL import Image
import numpy as np

FILENAME = 'cropped.jpg'

def create_np_array(file):
    '''converts a jpg to a numpy array'''
    img = Image.open(file, 'r')
    return np.array(img)

def find_average_for_all_pixels(np_array):
    '''
        returns list with rgb averages for all pixels
        [int, int, int]
    '''
    red_value = 0
    green_value = 0
    blue_value = 0

    for row in np_array:
        for pixel in row:
            red_value += pixel[0]
            green_value += pixel[1]
            blue_value += pixel[2]

    total_pixels = np_array.shape[1] * np_array.shape[0]

    red_value = int(red_value / total_pixels)
    green_value = int(green_value / total_pixels)
    blue_value = int(blue_value / total_pixels)

    return [red_value, green_value, blue_value]


def build_image(averages, np_array):


def main():
    IMG_ARRAY = create_np_array(FILENAME)
    AVERAGES = find_average_for_all_pixels(IMG_ARRAY)
    print(AVERAGES)
    # NEW_IMG = build_image(AVERAGES, IMG_ARRAY)
    # NEW_IMG.show()

if __name__ == '__main__':
    main()
