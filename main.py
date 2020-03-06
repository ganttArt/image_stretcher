import random
from tkinter import ttk, filedialog, messagebox, StringVar, Tk
from PIL import Image, ImageTk
from stretching_functions import create_np_array, create_index_list, build_new_image

class Gui:
    def __init__(self, master):

        self.image_frame = ttk.Frame(master)
        self.image_frame.pack(side='left', anchor='nw', padx=8, pady=8)

        self.screen_height = master.winfo_screenheight()
        self.screen_width = master.winfo_screenwidth()

        self.unprocessed_jpg = Image.open('Intro_Image_from_fb20190306.jpg')
        self.art = ImageTk.PhotoImage(self.unprocessed_jpg)
        self.art_label = ttk.Label(self.image_frame, image=self.art)
        self.art_label.grid(row=0, column=0)

        self.vertical_index_list = list(range(0, self.unprocessed_jpg.size[1]))
        self.horizontal_index_list = list(range(0, self.unprocessed_jpg.size[0]))

        self.horizontal_slider = ttk.Scale(self.image_frame, orient='horizontal',
                                           from_=1, to=int(self.art.width()),
                                           length=int(self.art.width()))
        self.horizontal_slider.grid(row=1, column=0)
        self.horizontal_slider.set(220)

        self.vertical_slider = ttk.Scale(self.image_frame, orient='vertical',
                                         from_=1, to=int(self.art.height()),
                                         length=int(self.art.height()))
        self.vertical_slider.grid(row=0, column=1)
        self.vertical_slider.set(235)

        self.widget_frame = ttk.Frame(master)
        self.widget_frame.pack(anchor='nw', padx=8, pady=8)

        self.open_button = ttk.Button(self.widget_frame, text="Open", command=self.open_image)
        self.open_button.grid(row=0, column=1)

        self.save_button = ttk.Button(self.widget_frame, text="Save", command=self.save_image)
        self.save_button.grid(row=0, column=2, pady=4)

        ttk.Label(self.widget_frame, text='      Intensity').grid(row=1, column=1)
        self.intensity_value = StringVar()
        self.intensity_value.set("13")
        self.intensity_spinbox = ttk.Spinbox(self.widget_frame, from_=1, to=13, width=5,
                                             textvariable=self.intensity_value)
        self.intensity_spinbox.grid(row=1, column=2, pady=0)


        self.orientation = StringVar()
        self.up_rb = ttk.Radiobutton(self.widget_frame, variable=self.orientation,
                                     value="up", text='Up    ', command=self.upward_stretch)
        self.up_rb.grid(row=2, column=1, sticky='e')

        self.down_rb = ttk.Radiobutton(self.widget_frame, variable=self.orientation,
                                       value="down", text='Down', command=self.downward_stretch)
        self.down_rb.grid(row=3, column=1, sticky='e')

        self.left_rb = ttk.Radiobutton(self.widget_frame, variable=self.orientation,
                                       value="left", text='Left', command=self.left_stretch)
        self.left_rb.grid(row=2, column=2, sticky='w')

        self.right_rb = ttk.Radiobutton(self.widget_frame, variable=self.orientation,
                                        value="right", text='Right', command=self.right_stretch)
        self.right_rb.grid(row=3, column=2, sticky='w')
        self.orientation.set('right')


        self.random_button = ttk.Button(self.widget_frame, text='Random',
                                        command=self.random_stretch)
        self.random_button.grid(row=4, column=1, columnspan=2)


        self.stretch_button = ttk.Button(self.widget_frame, text="Stretch!",
                                         command=self.update_stretch
                                         )
        self.stretch_button.grid(row=5, column=1, columnspan=2)


        self.processed_image = None
        self.right_stretch()

    def display_image(self):
        self.art = ImageTk.PhotoImage(self.processed_image)
        self.art_label = ttk.Label(self.image_frame, image=self.art)
        self.art_label.grid(row=0, column=0)

    def update_stretch(self):
        direction = self.orientation.get()
        direction_dict = {'up': self.upward_stretch, 'down': self.downward_stretch,
                          'left': self.left_stretch, 'right': self.right_stretch}
        direction_dict[direction]()

    def downward_stretch(self):
        img_array = create_np_array(self.unprocessed_jpg)
        index_list = create_index_list(int(self.intensity_value.get()))
        self.processed_image = build_new_image(index_list, img_array, self.vertical_slider.get())
        self.display_image()


    def upward_stretch(self):
        self.unprocessed_jpg = self.unprocessed_jpg.rotate(180)
        img_array = create_np_array(self.unprocessed_jpg)
        index_list = create_index_list(int(self.intensity_value.get()))
        starting_pixel = self.vertical_index_list[int(self.vertical_slider.get())* -1]
        self.processed_image = build_new_image(index_list, img_array, starting_pixel)
        self.processed_image = self.processed_image.rotate(180)
        self.display_image()
        self.unprocessed_jpg = self.unprocessed_jpg.rotate(180)

    def right_stretch(self):
        self.unprocessed_jpg = self.unprocessed_jpg.rotate(270, expand=True)
        img_array = create_np_array(self.unprocessed_jpg)
        index_list = create_index_list(int(self.intensity_value.get()))
        self.processed_image = build_new_image(index_list, img_array, self.horizontal_slider.get())
        self.processed_image = self.processed_image.rotate(90, expand=True)
        self.display_image()
        self.unprocessed_jpg = self.unprocessed_jpg.rotate(90, expand=True)

    def left_stretch(self):
        self.unprocessed_jpg = self.unprocessed_jpg.rotate(90, expand=True)
        # self.unprocessed_jpg.show()
        img_array = create_np_array(self.unprocessed_jpg)
        index_list = create_index_list(int(self.intensity_value.get()))
        starting_pixel = self.horizontal_index_list[int(self.horizontal_slider.get()) * -1]
        self.processed_image = build_new_image(index_list, img_array, starting_pixel)
        self.processed_image = self.processed_image.rotate(270, expand=True)
        self.display_image()
        self.unprocessed_jpg = self.unprocessed_jpg.rotate(270, expand=True)

    def open_image(self):
        filename = filedialog.askopenfilename()

        try: #checking for non-jpg files
            jpg_image = Image.open(filename)
            if jpg_image.format != 'JPEG':
                jpg_image = jpg_image.convert('RGB')
        except Exception:
            messagebox.showerror("Error", "File type not compatible!")
            raise

        # image resizing for large images
        max_height = self.screen_height - 100
        max_width = self.screen_width - 230
        img_height = jpg_image.size[1]
        if img_height > max_height:
            height_percent = max_height / img_height
            new_width = int(jpg_image.size[0] * height_percent)
            if new_width > max_width:
                width_percentage = max_width / new_width
                new_height = int(new_width * width_percentage)
                jpg_image = jpg_image.resize((max_width, new_height), Image.LANCZOS)
            else:
                jpg_image = jpg_image.resize((new_width, max_height), Image.LANCZOS)

        # solves problem of empty space in frame for different shaped images
        for widget in self.image_frame.winfo_children():
            widget.destroy()

        self.unprocessed_jpg = jpg_image
        self.vertical_slider = ttk.Scale(self.image_frame, orient='vertical',
                                         from_=1, to=self.unprocessed_jpg.size[1],
                                         length=self.unprocessed_jpg.size[1])
        self.vertical_slider.grid(row=0, column=1)
        self.vertical_slider.set(100)

        self.horizontal_slider = ttk.Scale(self.image_frame, orient='horizontal',
                                           from_=1, to=self.unprocessed_jpg.size[0],
                                           length=self.unprocessed_jpg.size[0])
        self.horizontal_slider.grid(row=1, column=0)
        self.horizontal_slider.set(100)
        self.orientation.set('down')

        self.vertical_index_list = list(range(0, self.unprocessed_jpg.size[1]))
        self.horizontal_index_list = list(range(0, self.unprocessed_jpg.size[0]))

        self.downward_stretch()

    def save_image(self):
        '''asks user for a directory to save image to'''
        orientation = self.orientation.get()
        if orientation in ('up', 'down'):
            filename = '/IIS_intensity{}_starting{}'.format(self.intensity_value.get(),
                                                            int(self.vertical_slider.get()))
            directory = filedialog.askdirectory()
            self.processed_image.save(directory + filename + '.jpg')
        else:
            filename = '/IIS_intensity{}_starting{}'.format(self.intensity_value.get(),
                                                            int(self.horizontal_slider.get()))
            directory = filedialog.askdirectory()
            self.processed_image.save(directory + filename + '.jpg')

        # # old approach using 'save_as'
        # save_filename = filedialog.asksaveasfilename(defaultextension='*.jpg')
        # self.processed_image.save(save_filename)

    def random_stretch(self):
        direction = random.choice(['up', 'down', 'left', 'right'])

        if direction == 'up':
            self.vertical_slider.set(random.randint(80, self.unprocessed_jpg.size[1]))
        elif direction == 'down':
            self.vertical_slider.set(random.randint(1, self.unprocessed_jpg.size[1]-80))
        elif direction == 'left':
            self.horizontal_slider.set(random.randint(80, self.unprocessed_jpg.size[0]))
        else:
            self.horizontal_slider.set(random.randint(1, self.unprocessed_jpg.size[0]-80))

        self.intensity_value.set(random.randint(6, 13))
        self.orientation.set(direction)
        self.update_stretch()


def main():
    root = Tk()
    Gui(root)
    root.mainloop()


if __name__ == '__main__':
    main()
