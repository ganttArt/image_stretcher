import datetime
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
from main import create_np_array, create_index_list, create_gradient, build_new_image


class Gui:
    def __init__(self, master):

        self.image_frame = ttk.Frame(master)
        self.image_frame.pack(side=LEFT, anchor='nw')

        self.art = PhotoImage(file = 'intro_image.gif')
        self.art_label = ttk.Label(self.image_frame, image=self.art)
        self.art_label.grid(row=0, column=0)

        self.widget_frame = ttk.Frame(master)
        self.widget_frame.pack(side=RIGHT, anchor='ne', padx=10, pady=10)

        self.open_button = ttk.Button(self.widget_frame, text="Open", command=self.open_image)
        self.open_button.grid(row=0, column=1)

        self.save_button = ttk.Button(self.widget_frame, text="Save", command=self.save_image)
        self.save_button.grid(row=0, column=2)

        self.intensity_value = StringVar()
        self.intensity_value.set("1")
        self.intensity_spinbox = ttk.Spinbox(self.widget_frame, from_=1, to=10,
                                             textvariable=self.intensity_value, command=self.stretch_image)
        self.intensity_spinbox.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

        # spinbox alternative
        # self.starting_point_slider = ttk.Scale(self.widget_frame, orient=HORIZONTAL)


        # # functionality to add later
        # self.starting_point_slider = ttk.Scale(self.widget_frame, orient=VERTICAL)
        # self.starting_point_slider.grid(row=0, column=0, rowspan=3)

    def stretch_image(self):        
        try:
            IMG_ARRAY = create_np_array(self.unprocessed_jpg)
            print(self.intensity_value.get())
            INDEX_LIST = create_index_list(IMG_ARRAY, int(self.intensity_value.get()))
            STRETCHED_IMAGE = build_new_image(INDEX_LIST, IMG_ARRAY)
            self.art = ImageTk.PhotoImage(STRETCHED_IMAGE)
            self.art_label = ttk.Label(self.image_frame, image=self.art)
            self.art_label.grid(row=0, column=0)
        except AttributeError:
            messagebox.showerror("Error", "Image files only please!")
            self.intensity_value.set("1")



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
        # stretched_image = self.stretch_image()

        # self.art = ImageTk.PhotoImage(stretched_image)
        # self.art_label = ttk.Label(self.image_frame, image=self.art)
        # self.art_label.grid(row=0, column=0)
        
    def save_image(self):
        pass
        save_filename = filedialog.asksaveasfilename()
        print(save_filename)
        # now = datetime.datetime.now()
        # processed_image.save(f'ps{now.year}{now.month}{now.day}_'+
        #                      f'{now.hour}{now.minute}{now.second}.jpg')


def main():
    root = Tk()
    gui = Gui(root)
    root.mainloop()

if __name__ == '__main__':
    main()
