import datetime
from tkinter import *
import os
from PIL import Image, ImageTk

from datetime import datetime
import mysql.connector
import cv2
import pickle
import face_recognition
import numpy as np
import mysql.connector
os.environ['OPENCV_VIDEOIO_PRIORITY_MSMF'] = '0'

class Facerec:

    def __init__(self, rootwindow):
        self.rootwindow = rootwindow
        self.rootwindow.geometry("500x500+0+0")
        self.rootwindow.title("FaceRecognition")
        img = Image.open(r"Images/TraindataImage.jpg")
        img = img.resize((500, 500))
        self.photoimg = ImageTk.PhotoImage(img)
        background_image = Label(self.rootwindow, image=self.photoimg)
        background_image.place(x=0, y=0)

        upload_pic = Button(background_image, command=self.FaceRecognition, text="Face Recognition",
                            font=("times new roman", 12, "bold"),
                            bg="green", fg="white",
                            cursor="hand2", width=25)
        upload_pic.place(x=130, y=250)

    def ObjectDetectP1(self):
        global WidthHeightTarget, cap, classNames, net
        WidthHeightTarget = 320
        cap = cv2.VideoCapture(0)
        classesFile = "Yolo-Obj/coco.names"
        classNames = []
        with open(classesFile, 'rt') as f:
            classNames = f.read().rstrip('\n').split('\n')
        modelConfiguration = "Yolo-Obj/320/yolov3-320.cfg"
        modelWeights = "Yolo-Obj/320/yolov3.weights"
        net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    def ObjectDetectionP2(self,img,c):
        blob = cv2.dnn.blobFromImage(img, 1 / 255, (WidthHeightTarget, WidthHeightTarget), [0, 0, 0], 1, crop=False)
        net.setInput(blob)
        layersNames = net.getLayerNames()
        outputNames = [(layersNames[i[0] - 1]) for i in net.getUnconnectedOutLayers()]
        outputs = net.forward(outputNames)
        return self.findObjects(outputs, img,c)

    def findObjects(self,outputs, img,c):
        hT, wT, cT = img.shape
        bbox = []
        classIds = []
        confs = []
        for output in outputs:
            for detection in output:
                scores = detection[5:]
                classId = np.argmax(scores)
                confidence = scores[classId]
                # higher the confidence value means it identifies correctly.
                if confidence > 0.6:
                    w, h = int(detection[2] * wT), int(detection[3] * hT)
                    x, y = int((detection[0] * wT) - w / 2), int((detection[1] * hT) - h / 2)
                    bbox.append([x, y, w, h])
                    classIds.append(classId)
                    confs.append(float(confidence))
        # According to my testings greater the nms_threshold more overlap bounding boxes appear
        # which is good to detect the mobile phones if they overlap with faces.
        indices = cv2.dnn.NMSBoxes(bbox, confs, 0.6, nms_threshold=0.6)

        for i in indices:
            # print(i,"i")
            i = i[0]
            if (classNames[classIds[i]]) == "cell phone":
                # cv2.imwrite("E:\PycharmProjects\/attendence\FraudFraud.png" + str(c) + ".png", img)
                return (classNames[classIds[i]])

    def attendence(self, name, depart, Yr, id,OPEN):
        with open(OPEN, "r+", newline="\n") as file:
            filedata = file.readlines()
            Ids_lst = []
            for data in filedata:
                candidate_details = data.split(",")
                Ids_lst.append(candidate_details[0])
            if id not in Ids_lst:
                t = datetime.now()
                d = t.strftime("%d/%m/%Y")
                dstr = t.strftime("%H:%M:%S")
                file.writelines(f"\n{id},{name},{depart},{Yr},{dstr},{d},present")

    def FaceRecognition(self):
        cap = cv2.VideoCapture(0)
        face_classifer = cv2.CascadeClassifier(r"DataSetsPre/haarcascade_frontalface_default.xml")
        self.ObjectDetectP1()
        c = 0
        attendance = []
        while True:
            success, img = cap.read()
            c+=1
            fraud=self.ObjectDetectionP2(img,c)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_classifer.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
            k = cv2.waitKey(1)
            if k % 256 == 27:
                break
            c += 1
            imgInput = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgInput = cv2.cvtColor(imgInput, cv2.COLOR_BGR2RGB)

            try:

                faceLocation = face_recognition.face_locations(imgInput)
                if len(faceLocation) > 0:

                    inputFeatures = face_recognition.face_encodings(imgInput, faceLocation, model='cnn')
                    # Here we wil have the input face features
                    with open("TrainData/featuresOfTrainingImages.txt", "rb") as fp:  # Unpickling
                        featuresOfTrainingImages = pickle.load(fp)
                    with open("TrainData/imgNames.txt", "rb") as fp:
                        imgNames = pickle.load(fp)
                    with open("TrainData/images.txt", "rb") as fp:
                        images = pickle.load(fp)
                    # matching the input feature with the loaded images features.

                    for encodeInput, (x, y, w, h) in zip(inputFeatures, faceLocation):

                        faceDistance = face_recognition.face_distance(featuresOfTrainingImages, encodeInput)

                        index = np.argmin(faceDistance)
                        print(index,type(index))
                        print(imgNames[index],type(imgNames[index]))

                        connect = mysql.connector.connect(host="localhost", username="root", password="root",
                                                          database="facerec")
                        cursor = connect.cursor()
                        cursor.execute("select Name,Dep,Year from studetails where StudentId=%s", (imgNames[index],))
                        identiyed = cursor.fetchone()

                        if fraud :
                            self.attendence(identiyed[0], identiyed[1], identiyed[2], imgNames[index],"FRAUD.csv")
                            cv2.imwrite("FRAUD/FraudFraud.png" + str(c) + ".png", img)
                        else:
                            self.attendence(identiyed[0], identiyed[1], identiyed[2], imgNames[index], "Attendance.csv")
                        cv2.putText(img, f"Name:{identiyed[0]}", (x, y - 70), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                                    (255, 0, 0), 2)
                        cv2.putText(img, f"Department:{identiyed[1]}", (x, y - 45), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                                    (0, 255, 0), 2)
                        cv2.putText(img, f"Year:{identiyed[2]}", (x, y - 20), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                                    (0, 0, 255), 2)
                        cv2.putText(img, f"RollNo:{imgNames[index]}", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                                    (0, 255, 0), 2)


            except Exception as e:
                print(f" {e}")
            cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
            cv2.imshow("Image", img)


        cap.release()
        cv2.destroyAllWindows()
        # print(attendance)


if __name__ == "__main__":
    root = Tk()
    obj = Facerec(root)
    root.mainloop()
