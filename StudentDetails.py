from tkinter import *
import os

from PIL import Image, ImageTk
from tkinter import ttk, messagebox, filedialog
import mysql.connector
import cv2


class Student:
    def __init__(self, rootwindow):
        # Database Variables
        self.var_dep = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_stdId = StringVar()
        self.var_std_name = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.rootwindow = rootwindow
        self.rootwindow.geometry("1530x790+0+0")
        self.rootwindow.title("Student-Details")
        # os.chdir("/usr/app/")
        # BackGround Details
        img = Image.open("Images\studentdetails.jpg")
        img = img.resize((1530, 710))
        self.photoimg = ImageTk.PhotoImage(img)
        background_image = Label(self.rootwindow, image=self.photoimg)
        background_image.place(x=0, y=0)

        # Titile

        title = Label(background_image, text="Student Details", font=("times new roman", 30, "bold"), bg="white",
                      fg="green")
        title.place(x=0, y=0, width=1530, height=45)

        # Frame
        Main_Frame = Frame(background_image, bd=2, bg="#00FA9A")
        Main_Frame.place(x=30, y=70, width=1300, height=600)

        # Left Frame
        Left_frame = LabelFrame(Main_Frame, bd=2, relief=RIDGE, bg="white", text="Student Details",
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=25, width=763, height=550)

        # Image in Student Details Frame
        img1 = Image.open("Images/StudentFormImage.png")
        img1 = img1.resize((150, 150))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        left_Lable = Label(Left_frame, image=self.photoimg1)
        left_Lable.place(x=325, y=0)

        # current Course Details
        current_Course = LabelFrame(Main_Frame, bd=2, relief=RIDGE, bg="white", text="Current Course Info",
                                    font=("times new roman", 12, "bold"))
        current_Course.place(x=20, y=200, width=750, height=150)

        # Department label
        dept_label = Label(current_Course, text="Department : ", font=("times new roman", 12, "bold"), bg="white")
        dept_label.grid(row=0, column=0, padx=10, sticky=W)

        # combo Box for Department
        dept_combo = ttk.Combobox(current_Course, textvariable=self.var_dep, font=("times new roman", 12, "bold"),
                                  width=20, state="readonly")
        dept_combo["values"] = ("Select Department", "Computer Science", "Information Technology", "Mechanical")
        dept_combo.current(0)
        dept_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Year label
        year_label = Label(current_Course, text="Batch : ", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=0, column=8, padx=10, sticky=W)

        # combo Box for Year
        year_label = ttk.Combobox(current_Course, textvariable=self.var_year, font=("times new roman", 12, "bold"),
                                  width=20, state="readonly")
        year_label["values"] = ("Select Batch", "2017-2021", "2018-2022", "2019-2023")
        year_label.current(0)
        year_label.grid(row=0, column=9, padx=2, pady=10, sticky=W)

        # Semester label
        Semester_label = Label(current_Course, text="Semester : ", font=("times new roman", 12, "bold"), bg="white")
        Semester_label.grid(row=1, column=0, padx=10, sticky=W)

        # combo Box for Year
        Semester_label = ttk.Combobox(current_Course, textvariable=self.var_semester,
                                      font=("times new roman", 12, "bold"), width=20, state="readonly")
        Semester_label["values"] = (
            "Select Semester", "1st Semester", "2nd Semester", "3rd Semester", "4th Semester", "5th Semester",
            "6th Semester", "7th Semester", "8th Semester")
        Semester_label.current(0)
        Semester_label.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Student Personal Details
        Personal_Details = LabelFrame(Main_Frame, bd=2, relief=RIDGE, bg="white", text="Personal Info",
                                      font=("times new roman", 12, "bold"))
        Personal_Details.place(x=20, y=360, width=750, height=200)

        # StudentId
        StudentID = Label(Personal_Details, text="StudentID : ", font=("times new roman", 12, "bold"), bg="white")
        StudentID.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        StudentID_entry = ttk.Entry(Personal_Details, textvariable=self.var_stdId, font=("times new roman", 12, "bold"),
                                    width=15)
        StudentID_entry.grid(row=0, column=1, padx=2, pady=10)

        # StudentId
        Gender = Label(Personal_Details, text="Gender : ", font=("times new roman", 12, "bold"), bg="white")
        Gender.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        Gender_label = ttk.Combobox(Personal_Details, textvariable=self.var_gender,
                                    font=("times new roman", 12, "bold"), width=15, state="readonly")
        Gender_label["values"] = (
            "Select Gender", "Male", "Female", "Others")
        Gender_label.current(0)
        Gender_label.grid(row=1, column=1, padx=2, pady=10)

        # Email
        EmailID = Label(Personal_Details, text="EmailId : ", font=("times new roman", 12, "bold"), bg="white")
        EmailID.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        EmailID_entry = ttk.Entry(Personal_Details, textvariable=self.var_email, font=("times new roman", 12, "bold"),
                                  width=15)
        EmailID_entry.grid(row=2, column=1, padx=2, pady=10)

        # Name

        Name = Label(Personal_Details, text="Name : ", font=("times new roman", 12, "bold"), bg="white")
        Name.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        Name_entry = ttk.Entry(Personal_Details, textvariable=self.var_std_name, font=("times new roman", 12, "bold"),
                               width=15)
        Name_entry.grid(row=0, column=4, padx=2, pady=10)

        # Address

        Address = Label(Personal_Details, text="Address : ", font=("times new roman", 12, "bold"), bg="white")
        Address.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        Address_entry = ttk.Entry(Personal_Details, textvariable=self.var_address, font=("times new roman", 12, "bold"),
                                  width=15)
        Address_entry.grid(row=1, column=4, padx=2, pady=10)

        # Phone Number

        Phone_Number = Label(Personal_Details, text="PhoneNo : ", font=("times new roman", 12, "bold"), bg="white")
        Phone_Number.grid(row=2, column=3, padx=10, pady=10, sticky=W)

        Phone_Number = ttk.Entry(Personal_Details, textvariable=self.var_phone, font=("times new roman", 12, "bold"),
                                 width=15)
        Phone_Number.grid(row=2, column=4, padx=2, pady=10)

        # Teacher Name

        Teacher_name = Label(Personal_Details, text="Mentor Name : ", font=("times new roman", 12, "bold"), bg="white")
        Teacher_name.grid(row=0, column=6, padx=10, pady=10, sticky=W)

        Teacher_name = ttk.Entry(Personal_Details, textvariable=self.var_teacher, font=("times new roman", 12, "bold"),
                                 width=15)
        Teacher_name.grid(row=0, column=7, padx=2, pady=10)

        upload_pic = Button(Personal_Details, command=self.Capture_Photos, text="Upload Photos [Min 3 photos]",
                            font=("times new roman", 12, "bold"),
                            bg="green", fg="white",
                            cursor="hand2", width=25)
        upload_pic.place(x=500, y=50)

        upload_raw_pic = Button(Personal_Details, command=self.Get_raw_photos, text="Upload Raw Photos [Min 3 photos]",
                                font=("times new roman", 12, "bold"),
                                bg="green", fg="white",
                                cursor="hand2", width=25)
        upload_raw_pic.place(x=500, y=90)

        save_button = Button(Personal_Details, text="Save", command=self.Insert_Details,
                             font=("times new roman", 12, "bold"), bg="blue", fg="white", cursor="hand2", width=15)
        save_button.place(x=13, y=135)

        update_button = Button(Personal_Details, text="Update", command=self.update_data,
                               font=("times new roman", 12, "bold"), bg="blue",
                               fg="white",
                               cursor="hand2", width=15)
        update_button.place(x=160, y=135)

        delete_button = Button(Personal_Details, text="Delete", command=self.Delete_data,
                               font=("times new roman", 12, "bold"), bg="blue",
                               fg="white",
                               cursor="hand2", width=15)
        delete_button.place(x=307, y=135)

        UpdatePhoto_button = Button(Personal_Details, text="Update Photo", font=("times new roman", 12, "bold"),
                                    bg="blue",
                                    fg="white",
                                    cursor="hand2", width=15)
        UpdatePhoto_button.place(x=455, y=135)

        #####################################################################################
        # Search Frame
        # Right Frame
        Right_frame = LabelFrame(Main_Frame, bd=2, relief=RIDGE, bg="white", text="Search Details",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=775, y=25, width=510, height=550)
        # Image in Student Details Frame
        Search_image = Image.open("Images/SearchImage.png")
        Search_image = Search_image.resize((400, 150))
        self.Search_image = ImageTk.PhotoImage(Search_image)
        left_Lable = Label(Right_frame, image=self.Search_image)
        left_Lable.place(x=35, y=0)

        # SearchFrame = LabelFrame(Right_frame, bd=2, relief=RIDGE, bg="white", text="Search Details",
        #                          font=("times new roman", 12, "bold"))
        # SearchFrame.place(x=0, y=155, width=500, height=60)
        #
        # Seach_lable = Label(SearchFrame, text="Search By : ", font=("times new roman", 10, "bold"), bg="white",
        #                     fg="dark green")
        # Seach_lable.grid(row=0, column=0, padx=5, pady=3, sticky=W)
        #
        # Search_label = ttk.Combobox(SearchFrame, font=("times new roman", 10, "bold"), width=10, state="readonly")
        # Search_label["values"] = (
        #     "Select key", "StudentId", "PhoneNo")
        # Search_label.current(0)
        # Search_label.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        #
        # # Entry
        # Search_entry = ttk.Entry(SearchFrame, font=("times new roman", 10, "bold"), width=11)
        # Search_entry.grid(row=0, column=2, padx=2, pady=10)
        #
        # # buttons
        # Search_btn = Button(SearchFrame, text="Search", font=("times new roman", 10, "bold"), bg="blue",
        #                     fg="white",
        #                     cursor="hand2", width=10)
        # Search_btn.grid(row=0, column=3, padx=5)
        #
        # Search_all = Button(SearchFrame, text="Show-All", font=("times new roman", 10, "bold"), bg="blue",
        #                     fg="white",
        #                     cursor="hand2", width=10)
        # Search_all.grid(row=0, column=4, padx=5)

        # table frame to show search details
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=0, y=220, width=500, height=300)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, column=(
            "dep", "year", "sem", "id", "name", "email", "phone", "address", "teacher", "photo"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus ")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        # this fetch to show tha data always
        self.fetch_data()
        # to show the data which is selected in the student web table

        self.student_table.bind("<ButtonRelease>", self.get_Cursor)

    def Insert_Details(self):
        if self.var_dep.get() == "Select Department" or self.var_year.get() == "Select Batch" or self.var_semester.get() == "Select Semester" or self.var_gender.get() == "Select Gender" or self.var_teacher.get() == "" or self.var_phone.get() == "" or self.var_stdId.get() == "" or self.var_address.get() == "" or self.var_std_name.get() == "":
            messagebox.showerror("Error", "Please fill all Details", parent=self.rootwindow)
        else:
            try:
                connect = mysql.connector.connect(host="localhost", username="root", password="root",
                                                  database="facerec")
                cursor = connect.cursor()
                cursor.execute("insert into studetails values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_stdId.get(),
                    self.var_std_name.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get()

                ))
                connect.commit()
                # this fetch is to show the data immediately after the insert
                self.fetch_data()
                connect.close()
                messagebox.showinfo("success", " Details Submitted ", parent=self.rootwindow)
            except EXCEPTION as e:
                messagebox.showerror("Error", f"Due to {str(e)}")

    def fetch_data(self):
        connect = mysql.connector.connect(host="localhost", username="root", password="root", database="facerec")
        cursor = connect.cursor()
        cursor.execute("select * from studetails")
        data = cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            connect.commit()
        connect.close()

    # cursor for the web student table....this is not a database cursor.
    def get_Cursor(self, event=""):
        web_cursor = self.student_table.focus()
        # get the data from the student web table
        data = self.student_table.item(web_cursor)
        data = data["values"]

        self.var_dep.set(data[0])
        self.var_year.set(data[1])
        self.var_semester.set(data[2])
        self.var_stdId.set(data[3])
        self.var_std_name.set(data[4])
        self.var_gender.set(data[5])
        self.var_email.set(data[6])
        self.var_phone.set(data[7])
        self.var_address.set(data[8])
        self.var_teacher.set(data[9])

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_year.get() == "Select Batch" or self.var_semester.get() == "Select Semester" or self.var_gender.get() == "Select Gender" or self.var_teacher.get() == "" or self.var_phone.get() == "" or self.var_stdId.get() == "" or self.var_address.get() == "" or self.var_std_name.get() == "":
            messagebox.showerror("Error", "Please fill all Details", parent=self.rootwindow)
        else:
            try:
                Update = messagebox.askyesno("update", "Do you want to Update the details", parent=self.rootwindow)
                if Update > 0:
                    connect = mysql.connector.connect(host="localhost", username="root", password="root",
                                                      database="facerec")
                    cursor = connect.cursor()
                    cursor.execute(
                        "update studetails set Dep=%s,Year=%s,Semester=%s,Name=%s,Gender=%s,Email=%s,PhoneNo=%s,Address=%s,Teacher=%s where StudentId=%s",
                        (
                            self.var_dep.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_gender.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_stdId.get()
                        ))
                    connect.commit()
                    # this fetch is to show the data immediately after the insert
                    self.fetch_data()
                    connect.close()
                    messagebox.showinfo("success", " Details Updated ", parent=self.rootwindow)
                else:
                    return

            except EXCEPTION as e:
                messagebox.showerror("Error", f"Due to {str(e)}", parent=self.rootwindow)

    def Delete_data(self):
        if self.var_stdId.get() == "":
            messagebox.showerror("Error", "Please Provide Student Id", parent=self.rootwindow)
        else:
            try:
                delete = messagebox.askyesno("Delete",
                                             f"Do yo want to delete student-Id :{self.var_stdId.get()} details",
                                             parent=self.rootwindow)
                if delete > 0:
                    connect = mysql.connector.connect(host="localhost", username="root", password="root",
                                                      database="facerec")
                    cursor = connect.cursor()
                    cursor.execute("delete from studetails where StudentId=%s", (self.var_stdId.get(),))
                    connect.commit()
                    # this fetch is to show the data immediately after the insert
                    self.fetch_data()
                    connect.close()
                    messagebox.showinfo("success", " Details Deleted ", parent=self.rootwindow)
                else:
                    return


            except EXCEPTION as e:
                messagebox.showerror("Error", f"Due to {str(e)}", parent=self.rootwindow)

    def Capture_Photos(self):
        os.environ['OPENCV_VIDEOIO_PRIORITY_MSMF'] = '0'
        messagebox.showinfo("Instructions", "Click Space Bar to take Picture and ESC to close", parent=self.rootwindow)
        try:
            if self.var_stdId.get() == "":
                messagebox.showinfo("Error", "Please provide Student Id", parent=self.rootwindow)
                return

            directory = str(self.var_stdId.get())
            parent_dir = "InputData"
            path = os.path.join(parent_dir, directory)
            os.mkdir(path)
            directory = r"InputData/" + str(self.var_stdId.get())

            face_classifer = cv2.CascadeClassifier("DataSetsPre/haarcascade_frontalface_default.xml")
            os.chdir(directory)

            def Crop(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifer.detectMultiScale(gray, 1.3, 5)

                for (x, y, w, h) in faces:
                    facecrop = img[y:y + h, x:x + w]
                    return facecrop

            cap = cv2.VideoCapture(0)
            counter = 0
            while True:

                ret, frame = cap.read()
                cv2.imshow("frame", frame)
                k = cv2.waitKey(30) & 0xFF
                if Crop(frame) is not None:
                    counter += 1
                    face = cv2.resize(Crop(frame), (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                    if k == 27:
                        break
                    elif k == ord('c'):

                        filepath = str(self.var_stdId.get()) + "_" + str(counter) + ".jpeg"
                        cv2.imwrite(filepath, face)
                        cv2.imshow("Cropped Face", face)
                else:
                    print("cascade")
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "photos captured", parent=self.rootwindow)
        except Exception as i:
            messagebox.showinfo("Error", f"Due to {str(i)} ", parent=self.rootwindow)

    def Get_raw_photos(self):
        if self.var_stdId.get() == "":
            messagebox.showinfo("Error", "Please provide Student Id", parent=self.rootwindow)
            return
        delete = messagebox.askyesno("User Option",
                                     "Use this option only when there is low intensity of light",
                                     parent=self.rootwindow)
        if delete > 0:
            files = filedialog.askopenfilenames(initialdir=r"C:\Users\santosh\OneDrive\Pictures\Camera Roll",
                                                title="Select "
                                                      "Files",
                                                filetypes=(("png", "*.png"), ("jpeg", "*.jpeg"), ("jpg", "*.jpg")),
                                                parent=self.rootwindow)
            directory = str(self.var_stdId.get())
            parent_dir = "InputData"
            path = os.path.join(parent_dir, directory)
            os.mkdir(path)
            for i in range(len(files)):
                img = cv2.imread(files[i])
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                cv2.imwrite(r"InputData/" + str(self.var_stdId.get()) + "/" + str(self.var_stdId.get()) + "_" + str(
                    i) + ".jpeg",
                            img)
        else:
            return


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
