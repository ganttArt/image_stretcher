from stretching_functions import create_np_array, create_index_list, build_new_image

def downward_stretch(image, intensity, start):
    img_array = create_np_array(image)
    index_list = create_index_list(intensity)
    processed_image = build_new_image(
        index_list, img_array, start)
    return processed_image


def upward_stretch(image, intensity, start):
    unprocessed_jpg = image.rotate(180)
    img_array = create_np_array(unprocessed_jpg)
    index_list = create_index_list(intensity)
    processed_image = build_new_image(
        index_list, img_array, start)
    processed_image = processed_image.rotate(180)
    return processed_image


def right_stretch(image, intensity, start):
    unprocessed_jpg = image.rotate(270, expand=True)
    img_array = create_np_array(unprocessed_jpg)
    index_list = create_index_list(intensity)
    processed_image = build_new_image(
        index_list, img_array, start)
    processed_image = processed_image.rotate(90, expand=True)
    return processed_image



def left_stretch(image, intensity, start):
    unprocessed_jpg = image.rotate(90, expand=True)
    img_array = create_np_array(unprocessed_jpg)
    index_list = create_index_list(intensity)
    processed_image = build_new_image(
        index_list, img_array, start)
    processed_image = processed_image.rotate(270, expand=True)
    return processed_image
