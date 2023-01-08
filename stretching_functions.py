'''Stretching functions for image stretcher, accessed through main.py'''

from PIL import Image
import numpy as np


def create_np_array(pil_image):
    '''converts a jpg to a numpy array'''
    return np.array(pil_image)


def create_index_list(multiplication_factor=13):
    '''
    Returns:
        list
    '''
    inverse_value_dict = {13: 1, 12: 1.25, 11: 1.5, 10: 1.75, 9: 2, 8: 2.25, 7: 2.5, 6: 2.75, 5: 3, 4: 3.25,
                          3: 3.5, 2: 3.75, 1: 4}

    pairs = [[1, 13], [2, 8], [3, 5], [5, 3], [8, 2], [13, 1], [21, 1], [34, 1], [55, 1], [89, 1],
             [144, 1], [233, 1], [377, 1], [610, 1], [987, 1]]

    for pair in pairs:
        pair[0] = pair[0] * 1
        pair[1] = int(pair[1] * inverse_value_dict[multiplication_factor])

    index_list = []
    for pair in pairs:
        for _ in range(pair[1]):
            index_list.append(pair[0])

    return index_list


def create_gradient(two_row_array, gradient_size):
    '''returns a gradient made from two rows of pixels'''
    image_width = two_row_array.shape[1]
    gradient_array = np.zeros((gradient_size+2, image_width, 3))
    gradient_array[0] += two_row_array[0]
    gradient_array[-1] += two_row_array[-1]
    difference_array = abs(gradient_array[0] - gradient_array[-1])

    for num in range(gradient_size):
        for row in range(image_width):
            for column in range(3):
                if gradient_array[0][row][column] >= gradient_array[-1][row][column]:
                    gradient_array[num+1][row][column] += (gradient_array[0][row][column] - (
                        (difference_array[row][column])/(gradient_size+1)*(num+1)))
                else:
                    gradient_array[num+1][row][column] += (gradient_array[0][row][column] + (
                        (difference_array[row][column])/(gradient_size+1)*(num+1)))
    return gradient_array


def build_new_image(index_list, source_image, starting_pixel):
    '''
    index_list : list
    source_image : numpy array
    '''
    starting_pixel = int(starting_pixel)
    index_value = starting_pixel
    index_list_value = 0

    new_image = np.zeros((source_image.shape))

    for num in range(starting_pixel):
        new_image[num] += source_image[num]

    height = new_image.shape[0]
    width = new_image.shape[1]

    for num in range(starting_pixel, height):
        two_row_array = np.zeros((2, width, 3))
        two_row_array[0] += source_image[num]
        two_row_array[1] += source_image[num+1]

        gradient_array = create_gradient(
            two_row_array, index_list[index_list_value])
        index_list_value += 1

        try:
            for number in range(gradient_array.shape[0] - 1):
                # for number in range(gradient_array.shape[0] - 1):
                new_image[index_value] += gradient_array[number]
                index_value += 1
        except IndexError:
            break

    int_array = new_image.astype(np.uint8)

    return Image.fromarray(int_array)
