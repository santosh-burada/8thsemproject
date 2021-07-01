import mysql.connector

def getdata(key='17341A1207'):

    connect = mysql.connector.connect(host="localhost", username="root", password="root",
                                      database="facerec")
    cursor = connect.cursor()
    cursor.execute("select Name,Dep,Year from studetails where StudentId=%s", (key,))
    identiyed = cursor.fetchone()

    return identiyed
print(getdata())

