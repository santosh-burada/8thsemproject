import mysql.connector

# def getdata(key='17341A1207'):
#
#     connect = mysql.connector.connect(host="localhost", username="root", password="root",
#                                       database="facerec")
#     cursor = connect.cursor()
#     cursor.execute("select Name,Dep,Year from studetails where StudentId=%s", (key,))
#     identiyed = cursor.fetchone()
#
#     return identiyed
# print(getdata())

import os
#
ROOT_DI = os.path.dirname(os.path.abspath(__file__))
# print(ROOT_DI)
# img = (ROOT_DI+"\Images\Traindata.jpg")
# print(img)
lv =os.path.sep.join([ROOT_DI+ '\face_detector', "deploy.prototxt"])
print(type(lv))

