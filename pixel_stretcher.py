'''
    Incremental Pixel Stretcher
'''
import datetime
from PIL import Image
import numpy as np

FILENAME = '5.fb.20190424.jpg'
# FILENAME = '14h15w.png'

def create_np_array(file):
    img = Image.open(file, 'r')
    return np.array(img)


def create_index_list(np_array):
    index_list = []
    for num in range(len(np_array)):
        for _ in range(num+1):
            index_list.append(num)
    return index_list


def build_new_image(index_list, source_image):
    new_image = np.zeros((source_image.shape), dtype=np.uint8)

    for num in range(new_image.shape[0]):
        new_image[num] += source_image[index_list[num]]

    return Image.fromarray(new_image)


def save_file(pil_image):
    now = datetime.datetime.now()
    pil_image.save(f'ps{now.year}{now.month}{now.day}_'+
                   f'{now.hour}{now.minute}{now.second}.png')


if __name__ == '__main__':
    IMG_ARRAY = create_np_array(FILENAME)
    INDEX_LIST = create_index_list(IMG_ARRAY)
    # print(INDEX_LIST)
    NEW_IMG = build_new_image(INDEX_LIST, IMG_ARRAY)
    save_file(NEW_IMG)