from tkinter import *

from PIL import Image, ImageTk


class Devs:
    def __init__(self, rootwindow):
        self.rootwindow = rootwindow
        self.rootwindow.geometry("1530x790+0+0")
        self.rootwindow.title("Developers")
        img = Image.open("Images\devsback.png")
        img = img.resize((1530, 710))
        self.photoimg = ImageTk.PhotoImage(img)
        background_image = Label(self.rootwindow, image=self.photoimg)
        background_image.place(x=0, y=0)


        SantoshBurada = Image.open("Images\Devs\Santosh.JPG")
        SantoshBurada = SantoshBurada.resize((230, 250))
        self.Dev1 = ImageTk.PhotoImage(SantoshBurada)
        SantoshBurada = Label(background_image, image=self.Dev1)
        SantoshBurada.place(x=600, y=240)

        Monica = Image.open(
            "Images\Devs\Monica.jpeg")
        MonicaImage = Monica.resize((220, 220))
        self.Monica = ImageTk.PhotoImage(MonicaImage)

        MonicaImage = Label(background_image, image=self.Monica,)
        MonicaImage.place(x=1000, y=100)


if __name__ == "__main__":
    root = Tk()
    obj = Devs(root)
    root.mainloop()
