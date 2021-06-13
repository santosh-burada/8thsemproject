from tkinter import *
import os
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import cv2
import pickle
import face_recognition


class Train:

    def __init__(self,rootwindow):
        self.rootwindow = rootwindow
        self.rootwindow.geometry("500x500+0+0")
        self.rootwindow.title("Training")
        img = Image.open(r"Images\TraindataImage.jpg")
        img = img.resize((500, 500))
        self.photoimg = ImageTk.PhotoImage(img)
        background_image = Label(self.rootwindow, image=self.photoimg)
        background_image.place(x=0, y=0)

        upload_pic = Button(background_image,command=self.TrainingData, text="Train data",
                            font=("times new roman", 12, "bold"),
                            bg="green", fg="white",
                            cursor="hand2", width=25)
        upload_pic.place(x=130, y=250)
    def TrainingData(self):

        messagebox.showinfo("JOB","Training...",parent=self.rootwindow)
        os.chdir(r"InputData")
        images = []
        imgNames = []
        # Now we have to go through every photo in multiple folders
        for root, dirs, files in os.walk(".", topdown=False):

            for name in files:
                imgNames.append(name.split("_")[0])
                images.append(cv2.imread(os.path.join(root, name)))
        print(imgNames, "Imagnmaes")

        # This function is used to collect the features and face location of particular image.
        def features(images):
            featuresOfImages = []
            c = 0
            print("Face Locations of Loaded Images")
            for img in images:
                imgs = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                if len(face_recognition.face_locations(imgs))>0:
                    print(face_recognition.face_locations(imgs)[0])
                try:
                    featuresOfImg = face_recognition.face_encodings(imgs, model='cnn')[0]
                except IndexError as e:
                    print("Some Faces are not detected by dlib")
                    # sys.exit(1)
                featuresOfImages.append(featuresOfImg)
            messagebox.showinfo("JOB", "Training...", parent=self.rootwindow)
            return featuresOfImages

        featuresOfTrainingImages = features(
            images)  # In this featuresOfTrainingImages list we will have the features of all
        # loaded images
        print(type(featuresOfTrainingImages))
        print("Features are collected...", len(featuresOfTrainingImages))
        os.chdir(r"TrainData")
        with open("featuresOfTrainingImages.txt", "wb") as fp:  # Pickling
            pickle.dump(featuresOfTrainingImages, fp)
        with open("images.txt", "wb") as fp:  # Pickling
            pickle.dump(images, fp)
        with open("imgNames.txt", "wb") as fp:  # Pickling
            pickle.dump(imgNames, fp)

        messagebox.showinfo("Training","Training is completed")


if __name__ == "__main__":


    root = Tk()
    obj = Train(root)
    root.mainloop()
