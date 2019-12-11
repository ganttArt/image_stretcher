'''fibonacci_stretch.py'''

import datetime
import math
from PIL import Image
import numpy as np

FILENAME = '6.fb20190306.jpg'

def create_np_array(file):
    '''converts a jpg to a numpy array'''
    img = Image.open(file, 'r')
    return np.array(img)


def create_index_list(np_array):
    '''
    Returns:
        list
    '''
    multiplication_factor = 1
    rate_value = 1
    pairs = [[1,13], [2,8], [3,5], [5,3], [8,2], [13,1], [21,1], [34,1], [55,1], [89,1], [144,1], [233,1], [377,1]]
    
    if multiplication_factor > 1 or rate_value > 1:
        for pair in pairs:
            pair[0] = pair[0] * rate_value
            pair[1] = pair[1] * multiplication_factor

    index_list = []
    for pair in pairs:
            for _ in range(pair[1]):
                index_list.append(pair[0])

    return index_list


def create_gradient(two_row_array, gradient_size):
    image_width = two_row_array.shape[1]
    gradient_array = np.zeros((gradient_size+2, image_width, 3))
    gradient_array[0] += two_row_array[0]
    gradient_array[-1] += two_row_array[-1]
    difference_array = abs(gradient_array[0] - gradient_array[-1])

    for num in range(gradient_size):
        for row in range(image_width):
            for column in range(3):
                if gradient_array[0][row][column] >= gradient_array[-1][row][column]:
                    gradient_array[num+1][row][column] += (gradient_array[0][row][column] - ((difference_array[row][column])/(gradient_size+1)*(num+1)))
                else:
                    gradient_array[num+1][row][column] += (gradient_array[0][row][column] + ((difference_array[row][column])/(gradient_size+1)*(num+1)))
    return gradient_array


def build_new_image(index_list, source_image):
    '''
    index_list : list
    source_image : numpy array
    '''
    starting_pixel = 200
    index_value = starting_pixel
    index_list_value = 0
    
    new_image = np.zeros((source_image.shape))

    for num in range(starting_pixel):
        new_image[num] += source_image[num]
    # new_image[0] += source_image[0]

    image_height = new_image.shape[0]
    image_width = new_image.shape[1]

    for num in range(starting_pixel, image_height):
    # for num in range(1, image_height):
        two_row_array = np.zeros((2, image_width, 3))
        two_row_array[0] += source_image[num]
        two_row_array[1] += source_image[num+1]
        
        # gradient_array = create_gradient(two_row_array, index_list[num])
        gradient_array = create_gradient(two_row_array, index_list[index_list_value])
        index_list_value += 1
        
        try:
            for number in range(gradient_array.shape[0] - 1):
            # for number in range(gradient_array.shape[0] - 1):
                new_image[index_value] += gradient_array[number]
                index_value += 1
        except IndexError as e:
            # print(e)
            break

    int_array = new_image.astype(np.uint8)

    return Image.fromarray(int_array)

def save_file(pil_image):
    now = datetime.datetime.now()
    pil_image.save(f'ps{now.year}{now.month}{now.day}_'+
                   f'{now.hour}{now.minute}{now.second}.jpg')

if __name__ == '__main__':
    IMG_ARRAY = create_np_array(FILENAME)
    INDEX_LIST = create_index_list(IMG_ARRAY)
    NEW_IMG = build_new_image(INDEX_LIST, IMG_ARRAY)
    # NEW_IMG.show()
    save_file(NEW_IMG)

