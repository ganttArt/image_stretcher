'''
main.py
functions to use with gui
'''

from PIL import Image
import numpy as np


def create_np_array(pil_image):
    '''converts a jpg to a numpy array'''
    return np.array(pil_image)


def create_index_list(np_array, multiplication_factor=1, rate_value=1):
    '''
    Returns:
        list
    '''    
    #fibonacci style
    pairs = [[1,13], [2,8], [3,5], [5,3], [8,2], [13,1], [21,1], [34,1], [55,1], [89,1], [144,1], [233,1], [377,1]]
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
    index_value = 1
    
    new_image = np.zeros((source_image.shape))
    new_image[0] += source_image[0]

    for num in range(1, new_image.shape[0]):
        two_row_array = np.zeros((2, new_image.shape[1], 3))
        two_row_array[0] += source_image[num]
        two_row_array[1] += source_image[num+1]
        gradient_array = create_gradient(two_row_array, index_list[num])
        try:
            for number in range(gradient_array.shape[0] - 1):
                new_image[index_value] += gradient_array[number]
                index_value += 1
        except IndexError as e:
            # print(e)
            break

    int_array = new_image.astype(np.uint8)

    return Image.fromarray(int_array)