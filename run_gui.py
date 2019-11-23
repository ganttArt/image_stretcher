import datetime
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk


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

        self.save_button = ttk.Button(self.widget_frame, text="Save")
        self.save_button.grid(row=0, column=2)

        intensity_value = StringVar()
        intensity_value.set("1")
        self.intensity_spinbox = ttk.Spinbox(self.widget_frame, from_=1, to=10,
                                             textvariable=intensity_value)
        self.intensity_spinbox.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
        # spinbox alternative
        # self.starting_point_slider = ttk.Scale(self.widget_frame, orient=HORIZONTAL)


        # # functionality to add later
        # self.starting_point_slider = ttk.Scale(self.widget_frame, orient=VERTICAL)
        # self.starting_point_slider.grid(row=0, column=0, rowspan=3)

    def open_image(self):
        filename = filedialog.askopenfilename()

        try: #checking for non-jpg files
            jpg_image = Image.open(filename)
            if jpg_image.format != 'JPEG':
                jpg_image = jpg_image.convert('RGB')
        except Exception as ex:
            print(ex)
            messagebox.showerror("Error", "Image files only please!")

        self.art = ImageTk.PhotoImage(jpg_image)
        self.art_label = ttk.Label(self.image_frame, image=self.art)
        self.art_label.grid(row=0, column=0)

    def stretch_image(self, preprocessed_image):
        pass


    def save_image(self, processed_image):
        #consider doing this last
        pass
        # save_filename = filedialog.asksaveasfilename()

        # now = datetime.datetime.now()
        # processed_image.save(f'ps{now.year}{now.month}{now.day}_'+
        #                      f'{now.hour}{now.minute}{now.second}.jpg')


def main():
    root = Tk()
    gui = Gui(root)
    root.mainloop()

if __name__ == '__main__':
    main()
