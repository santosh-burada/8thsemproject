from tkinter import *

from PIL import Image, ImageTk

from StudentDetails import Student

from TrainData import Train

from Facerec import Facerec
import os

class FaceRecognition:

    def __init__(self, rootwindow):
        # rootwindow -->root
        self.rootwindow = rootwindow
        self.rootwindow.geometry("1530x790+0+0")
        self.rootwindow.title("ComputerVision")
        # os.chdir("/usr/app/")
        # Background Image
        img = Image.open("Images/backgroundImage.jpg")
        img = img.resize((1530, 710))
        self.photoimg = ImageTk.PhotoImage(img)
        background_image = Label(self.rootwindow, image=self.photoimg)
        background_image.place(x=0, y=0)

        # Title On Background Image
        title = Label(background_image, text="Face Recognition", font=("times new roman", 30, "bold"), bg="white",
                      fg="green")
        title.place(x=0, y=0, width=1530, height=45)

        # Student Details Button On Background Image
        student = Image.open("Images/studnetDetailsImage.png")
        student = student.resize((220, 220))
        self.studentDetailsImage = ImageTk.PhotoImage(student)

        StudentButton = Button(background_image, image=self.studentDetailsImage, command=self.student_details,
                               cursor="hand2")
        StudentButton.place(x=200, y=100)

        # Training Button
        TrainDataimg = Image.open("Images/attendeceExportImage.jpg")
        TrainDataimg = TrainDataimg.resize((220, 220))
        self.Traindata = ImageTk.PhotoImage(TrainDataimg)

        TrainDatabutton = Button(background_image, command=self.TrainDatabutton, image=self.Traindata, cursor="hand2")
        TrainDatabutton.place(x=200, y=400)

        # FaceRecognition attendance Button.
        FaceRecognitionImage = Image.open(
            "Images/FaceRecognitionImage.jpg")
        FaceRecognitionImage = FaceRecognitionImage.resize((220, 220))
        self.FaceRecognitionImage = ImageTk.PhotoImage(FaceRecognitionImage)

        FaceRecognitionImage = Button(background_image, command=self.Facerecbutton,image=self.FaceRecognitionImage, cursor="hand2")
        FaceRecognitionImage.place(x=1000, y=100)

        # # Images Gallery Button
        # ImagesButton = Image.open(
        #     "Images/photogallery.png")
        # ImagesButton = ImagesButton.resize((220, 220))
        # self.ImagesButton = ImageTk.PhotoImage(ImagesButton)
        #
        # ImagesButton = Button(background_image, image=self.ImagesButton, cursor="hand2")
        # ImagesButton.place(x=1000, y=400)

        # Computer Eye Image Just for show No functionality Provided.
        ComputerEye = Image.open("Images/Computer Eye.png")
        ComputerEye = ComputerEye.resize((220, 220))
        self.ComputerEye = ImageTk.PhotoImage(ComputerEye)
        ComputerEye = Label(background_image, image=self.ComputerEye)
        ComputerEye.place(x=600, y=250)

    # Button Functions
    def student_details(self):
        self.studentWindow = Toplevel(self.rootwindow)
        self.app = Student(self.studentWindow)

    def TrainDatabutton(self):
        self.trainWindow = Toplevel(self.rootwindow)
        self.app1 = Train(self.trainWindow)

    def Facerecbutton(self):
        self.faceWindow = Toplevel(self.rootwindow)
        self.app1 = Facerec(self.faceWindow)


if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()
