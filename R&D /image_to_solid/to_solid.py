'''gradient to solid color from average of last pixel rows'''

from PIL import Image
import numpy as np

FILENAME = 'cropped.jpg'


def create_np_array(file):
    '''converts a jpg to a numpy array'''
    img = Image.open(file, 'r')
    return np.array(img)


def find_average(np_array):
    '''
        returns list with rgb averages for the last row
        [int, int, int]
    '''
    # can probably find a more elegant way to write this one using np sums
    red_value = 0
    green_value = 0
    blue_value = 0

    for pixel in np_array[-1]:
        red_value += pixel[0]
        green_value += pixel[1]
        blue_value += pixel[2]

    red_value = int(red_value / np_array.shape[1])
    green_value = int(green_value / np_array.shape[1])
    blue_value = int(blue_value / np_array.shape[1])

    return [red_value, green_value, blue_value]



def build_image(averages, np_array):
    new_image = np.zeros(((np_array.shape[0] * 3),
                           np_array.shape[1],
                           3))
    

    # fill new image with original image
    # for num in range(np_array.shape[0]):
    #     new_image[num] += np_array[num]



    # create gradient
    gradient_length = np_array.shape[0]
    image_width = np_array.shape[1]

    gradient_array = np.zeros((gradient_length + 2, image_width, 3))

    gradient_array[0] += np_array[-1]
    for pixel in gradient_array[-1]:
        pixel += averages

    diff_array = abs(gradient_array[0]-gradient_array[-1])

    for num in range(gradient_length):
        for row in range(image_width):
            for column in range(3):
                if gradient_array[0][row][column] >= gradient_array[-1][row][column]:
                    gradient_array[num+1][row][column] += (gradient_array[0][row][column] - ((diff_array[row][column])/(gradient_length+1)*(num+1)))                
                else:
                    gradient_array[num+1][row][column] += (gradient_array[0][row][column] + ((diff_array[row][column])/(gradient_length+1)*(num+1)))

    #create solid color row
    solid_color_row = np.zeros((1, image_width, 3))
    for num in range(image_width):
        solid_color_row[0][num] += averages


    # fill in new image with old image, gradients, and solid color
    for num in range(gradient_length):
        new_image[num] += np_array[num]

    for num in range(gradient_length + 1):
    # for num in range(gradient_length + 1, gradient_length * 2)
        new_image[num + gradient_length] += gradient_array[num]

    for num in range(gradient_length * 2 + 1, gradient_length * 3):
        new_image[num] += solid_color_row[0]


    int_array = new_image.astype(np.uint8)

    return Image.fromarray(int_array)

def main():
    IMG_ARRAY = create_np_array(FILENAME)
    AVERAGES = find_average(IMG_ARRAY)
    NEW_IMG = build_image(AVERAGES, IMG_ARRAY)
    NEW_IMG.show()





if __name__ == '__main__':
    main()


'''future, instead of averages try going to the most saturated pixel color in the last row, or choose a random ''' 
