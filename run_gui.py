from tkinter import ttk, filedialog, messagebox, StringVar, PhotoImage, Tk
from PIL import Image, ImageTk
from main import create_np_array, create_index_list, build_new_image


class Gui:
    def __init__(self, master):

        self.image_frame = ttk.Frame(master)
        self.image_frame.pack(side='left', anchor='nw')

        self.art = PhotoImage(file='intro_image.gif')
        self.art_label = ttk.Label(self.image_frame, image=self.art)
        self.art_label.grid(row=0, column=0)

        self.widget_frame = ttk.Frame(master)
        self.widget_frame.pack(side='right', anchor='ne', padx=10, pady=10)

        self.open_button = ttk.Button(self.widget_frame, text="Open", command=self.open_image)
        self.open_button.grid(row=0, column=1)

        self.save_button = ttk.Button(self.widget_frame, text="Save", command=self.save_image)
        self.save_button.grid(row=0, column=2, pady=4)

        ttk.Label(self.widget_frame, text='      Intensity').grid(row=1, column=1)
        self.intensity_value = StringVar()
        self.intensity_value.set("1")
        self.intensity_spinbox = ttk.Spinbox(self.widget_frame, from_=1, to=10, width=5,
                                             textvariable=self.intensity_value,
                                             command=self.stretch_image)
        self.intensity_spinbox.grid(row=1, column=2, pady=0)


        ttk.Label(self.widget_frame, text='           Rate').grid(row=2, column=1)
        self.rate_value = StringVar()
        self.rate_value.set("1")
        self.rate_spinbox = ttk.Spinbox(self.widget_frame, from_=1, to=50, width=5,
                                        textvariable=self.rate_value,
                                        command=self.stretch_image)
        self.rate_spinbox.grid(row=2, column=2)


        self.starting_point_slider = ttk.Scale(self.widget_frame, orient='vertical')
        self.starting_point_slider.grid(row=0, column=0, rowspan=3)

        self.unprocessed_jpg = None
        self.processed_image = None

    def stretch_image(self):
        try:
            img_array = create_np_array(self.unprocessed_jpg)
            index_list = create_index_list(img_array,
                                           int(self.intensity_value.get()),
                                           int(self.rate_value.get()))
            self.processed_image = build_new_image(index_list, img_array)
            self.art = ImageTk.PhotoImage(self.processed_image)
            self.art_label = ttk.Label(self.image_frame, image=self.art)
            self.art_label.grid(row=0, column=0)
        except AttributeError:
            # exception handling for trying to change variables before opening initial image
            messagebox.showerror("Error", "Please open an image file before stretching")
            self.intensity_value.set("1")
            self.rate_value.set("1")

    def open_image(self):
        filename = filedialog.askopenfilename()

        try: #checking for non-jpg files
            jpg_image = Image.open(filename)
            if jpg_image.format != 'JPEG':
                jpg_image = jpg_image.convert('RGB')
        except Exception as ex:
            print(ex)
            messagebox.showerror("Error", "Image files only please!")

        self.unprocessed_jpg = jpg_image
        self.stretch_image()

    def save_image(self):
        save_filename = filedialog.asksaveasfilename(defaultextension='*.jpg')
        self.processed_image.save(save_filename)


def main():
    root = Tk()
    Gui(root)
    root.mainloop()


if __name__ == '__main__':
    main()