from stretching_functions import create_np_array, create_index_list, build_new_image

def downward_stretch(image, intensity, start):
    img_array = create_np_array(image)
    index_list = create_index_list(intensity)
    processed_image = build_new_image(
        index_list, img_array, start)
    return processed_image


def upward_stretch(self):
    self.unprocessed_jpg = self.unprocessed_jpg.rotate(180)
    img_array = create_np_array(self.unprocessed_jpg)
    index_list = create_index_list(int(self.intensity_value.get()))
    starting_pixel = self.vertical_index_list[int(
        self.vertical_slider.get()) * -1]
    self.processed_image = build_new_image(
        index_list, img_array, starting_pixel)
    self.processed_image = self.processed_image.rotate(180)
    self.display_image()
    self.unprocessed_jpg = self.unprocessed_jpg.rotate(180)


def right_stretch(self):
    self.unprocessed_jpg = self.unprocessed_jpg.rotate(270, expand=True)
    img_array = create_np_array(self.unprocessed_jpg)
    index_list = create_index_list(int(self.intensity_value.get()))
    self.processed_image = build_new_image(
        index_list, img_array, self.horizontal_slider.get())
    self.processed_image = self.processed_image.rotate(90, expand=True)
    self.display_image()
    self.unprocessed_jpg = self.unprocessed_jpg.rotate(90, expand=True)


def left_stretch(self):
    self.unprocessed_jpg = self.unprocessed_jpg.rotate(90, expand=True)
    img_array = create_np_array(self.unprocessed_jpg)
    index_list = create_index_list(int(self.intensity_value.get()))
    starting_pixel = self.horizontal_index_list[int(
        self.horizontal_slider.get()) * -1]
    self.processed_image = build_new_image(
        index_list, img_array, starting_pixel)
    self.processed_image = self.processed_image.rotate(270, expand=True)
    self.display_image()
    self.unprocessed_jpg = self.unprocessed_jpg.rotate(270, expand=True)
