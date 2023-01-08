from stretching_functions import create_np_array, create_index_list, build_new_image


DIRECTION_TO_DEGREES = {
    'left': 90,
    'right': 270,
    'up': 180,
    'down': 0
}


def stretch_image(image, intensity, starting_pixel, direction):
    rotated_image = image.rotate(
        DIRECTION_TO_DEGREES[direction],
        expand=True
    )
    img_array = create_np_array(rotated_image)
    index_list = create_index_list(intensity)
    processed_image = build_new_image(
        index_list, img_array, starting_pixel)
    processed_image = processed_image.rotate(
        360 - DIRECTION_TO_DEGREES[direction],
        expand=True
    )
    return processed_image
