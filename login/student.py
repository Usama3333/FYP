from cgitb import text
from email import message
from importlib.resources import contents
from logging import exception, root
from msilib.schema import Directory
from multiprocessing.sharedctypes import Value
from sqlite3 import Cursor
from tabnanny import check
from tkinter import*
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from tkinter.tix import ButtonBox
from turtle import bgcolor, update
from unittest import result
from webbrowser import BackgroundBrowser
from PIL import Image,ImageTk
from cv2 import CascadeClassifier
import mysql.connector
import cv2
import os,glob

class Student:
    def __init__(self,studentroot):
        self.studentroot = studentroot
        self.studentroot.geometry("1530x790+0+0")
        self.studentroot.title("Student System")
        
        #------------------------ variables -----------------------------
        self.var_dep = StringVar()
        self.var_year = StringVar()
        self.var_section = StringVar()
        self.var_semester = StringVar()
        self.var_rollnum = StringVar()
        self.var_name = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address  = StringVar()      
        self.var_search_by = StringVar()
        self.var_search_entry = StringVar()
        bgimg = Image.open(r".\login\images\plain-white-background.jpg")
        self.bg = ImageTk.PhotoImage(bgimg)
        lbl_bg=Label(self.studentroot,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        img = Image.open(r".\login\images\superior-university-logo.jpg") 
        # img = Image.open(r"E:\FYP\images\superior-university-logo.jpg")
        img= img.resize((150,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.studentroot,image=self.photoimg)
        f_lbl.place(x=600,y=0,width=150,height=150)
        
        main_frame=Frame(self.studentroot,bd=2,bg="#a43a8e",border=2)
        main_frame.place(x=0,y=125,width=1400,height=600) 
        
        #Left Frame
        left_label=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),bg="white")
        left_label.place(x=10,y=10,width=660,height=580)
        std = Image.open(r".\login\images\student_detail.png")
        # std = Image.open(r"E:\FYP\images\student_detail.png")
        std= std.resize((100,100),Image.ANTIALIAS)
        self.stdimg=ImageTk.PhotoImage(std)
        std_lbl=Label(left_label,image=self.stdimg,bg="white")
        std_lbl.place(x=300,y=0,width=100,height=100)
        
        current_label=LabelFrame(left_label,bd=2,relief=RIDGE,text="Current Course",font=("times new roman",12,"bold"),bg="white")
        current_label.place(x=5,y=100,width=650,height=120)
        
        dep_label=Label(current_label,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)
        
        dep_combo=ttk.Combobox(current_label,font=("times new roman",12,"bold"),textvariable=self.var_dep,state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","Information Technology","Software Engineering")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)
        
        section_label=Label(current_label,text="Section",font=("times new roman",12,"bold"),bg="white")
        section_label.grid(row=0,column=2,padx=10)
        
        section_combo=ttk.Combobox(current_label,font=("times new roman",12,"bold"),textvariable=self.var_section,state="readonly")
        section_combo["values"]=("Select Section","A","B","C","D")
        section_combo.current(0)
        section_combo.grid(row=0,column=3,padx=2,pady=10)
        
        Year_label=Label(current_label,text="Year",font=("times new roman",12,"bold"),bg="white")
        Year_label.grid(row=1,column=0,padx=10)
        
        year_combo=ttk.Combobox(current_label,font=("times new roman",12,"bold"),textvariable=self.var_year,state="readonly")
        year_combo["values"]=("Select Year","2018-2022","2019-2023","2020-2024","2021-2025")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10)
        
        Semester_label=Label(current_label,text="Semester",font=("times new roman",12,"bold"),bg="white")
        Semester_label.grid(row=1,column=2,padx=10)
        
        semester_combo=ttk.Combobox(current_label,font=("times new roman",12,"bold"),textvariable=self.var_semester,state="readonly")
        semester_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10)
        
        
        # Student Information
        
        information_label=LabelFrame(left_label,bd=2,relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"),bg="white")
        information_label.place(x=5,y=220,width=650,height=337)
        
        Std_rollno_label=Label(information_label,text="Student Roll#:",font=("times new roman",12,"bold"),bg="white")
        Std_rollno_label.grid(row=0,column=0,padx=5,sticky=W)
        
        std_rollno_entry=ttk.Entry(information_label,width=20,font=("times new roman",13),textvariable=self.var_rollnum)
        std_rollno_entry.grid(row=0,column=1,padx=5,pady=10,sticky=W)
        
        stdname_label=Label(information_label,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        stdname_label.grid(row=0,column=2,padx=10,sticky=W)
        
        stdname_entry=ttk.Entry(information_label,width=20,font=("times new roman",13),textvariable=self.var_name)
        stdname_entry.grid(row=0,column=3,padx=5,pady=10,sticky=W)
        
        stdgender_label=Label(information_label,text="Student Gender:",font=("times new roman",12,"bold"),bg="white")
        stdgender_label.grid(row=1,column=0,padx=5,sticky=W)
        
        gender_combo=ttk.Combobox(information_label,font=("times new roman",12),textvariable=self.var_gender,state="readonly")
        gender_combo["values"]=("Select Gender","male","female")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=1,padx=5,pady=10)
        
        # stdgender_entry=ttk.Entry(information_label,width=20,font=("times new roman",13))
        # stdgender_entry.grid(row=1,column=1,padx=5,pady=10,sticky=W)
        
        stddob_label=Label(information_label,text="Student DOB:",font=("times new roman",12,"bold"),bg="white")
        stddob_label.grid(row=1,column=2,padx=5,sticky=W)
        
        stddob_entry=ttk.Entry(information_label,width=20,font=("times new roman",13),textvariable=self.var_dob)
        stddob_entry.grid(row=1,column=3,padx=5,pady=10,sticky=W)
        
        stdemail_label=Label(information_label,text="Student Email:",font=("times new roman",12,"bold"),bg="white")
        stdemail_label.grid(row=2,column=0,padx=5,sticky=W)
        
        stdemail_entry=ttk.Entry(information_label,width=20,font=("times new roman",13),textvariable=self.var_email)
        stdemail_entry.grid(row=2,column=1,padx=5,pady=10,sticky=W)
        
        stdphone_label=Label(information_label,text="Student Phone#:",font=("times new roman",12,"bold"),bg="white")
        stdphone_label.grid(row=2,column=2,padx=5,sticky=W)
        
        stdphone_entry=ttk.Entry(information_label,width=20,font=("times new roman",13),textvariable=self.var_phone)
        stdphone_entry.grid(row=2,column=3,padx=5,pady=10,sticky=W)
        
        stdaddress_label=Label(information_label,text="Student Address:",font=("times new roman",12,"bold"),bg="white")
        stdaddress_label.grid(row=3,column=0,padx=5,sticky=W)
        
        stdaddress_entry=ttk.Entry(information_label,width=56,font=("times new roman",13),textvariable=self.var_address)
        stdaddress_entry.place(x=136,y=135)
        
        self.var_radiobtn1=StringVar()
        radiobtn1=ttk.Radiobutton(information_label,variable=self.var_radiobtn1,text="Take Photo Sample",value="yes")
        radiobtn1.grid(row=5,column=0)
        
        radiobtn2=ttk.Radiobutton(information_label,variable=self.var_radiobtn1,text="No Photo Sample",value="no")
        radiobtn2.grid(row=5,column=1)
        
        radiobtn3=ttk.Radiobutton(information_label,variable=self.var_radiobtn1,text="Taken Photo Sample",value="taken")
        radiobtn3.grid(row=5,column=2)
        
        
        #---------------------------------------------- Button Frame --------------------------------------------
        
        Button_frame=Frame(information_label,bd=2,relief=RIDGE,bg="white")
        Button_frame.place(x=2,y=200,width=640,height=40)
        
        save_btn=Button(Button_frame,width=13,text="Save",command=self.add_data,font=("times new roman", 15, "bold"), borderwidth=1, fg="#a43a8e",
        bg="white", activeforeground="white", activebackground="#a43a8e",cursor="hand2")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(Button_frame,width=13,text="Update",command=self.update_data,font=("times new roman", 15, "bold"), borderwidth=1, fg="#a43a8e",
        bg="white", activeforeground="white", activebackground="#a43a8e",cursor="hand2")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(Button_frame,width=13,text="Delete",command=self.delete_data,font=("times new roman", 15, "bold"), borderwidth=1, fg="#a43a8e",
        bg="white", activeforeground="white", activebackground="#a43a8e",cursor="hand2")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(Button_frame,width=13,text="Reset",command=self.reset_data,font=("times new roman", 15, "bold"), borderwidth=1, fg="#a43a8e",
        bg="white", activeforeground="white", activebackground="#a43a8e",cursor="hand2")
        reset_btn.grid(row=0,column=3)
        
        Button_frame1=Frame(information_label,bd=2,relief=RIDGE,bg="white")
        Button_frame1.place(x=0,y=240,width=640,height=44)
        
        take_photo_btn=Button(Button_frame1,width=27,text="Take Photo Samples",command=self.generate_dataset,font=("times new roman", 16, "bold"), borderwidth=1, fg="#a43a8e",
        bg="white", activeforeground="white", activebackground="#a43a8e",cursor="hand2")
        take_photo_btn.grid(row=0,column=1)
        
        delete_photo_btn=Button(Button_frame1,width=27,text="Delete Photo Samples",command=self.delete_dataset,font=("times new roman", 16, "bold"), borderwidth=1, fg="#a43a8e",
        bg="white", activeforeground="white", activebackground="#a43a8e",cursor="hand2")
        delete_photo_btn.grid(row=0,column=2)
        
        
        
        
        #Right Frame
        right_label=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details Display",font=("times new roman",12,"bold"),bg="white")
        right_label.place(x=690,y=10,width=660,height=580)
        
        std_info = Image.open(r".\login\images\information.png")
        std_info= std_info.resize((100,100),Image.ANTIALIAS)
        self.std_info_img=ImageTk.PhotoImage(std_info)
        std_info_lbl=Label(right_label,image=self.std_info_img,bg="white")
        std_info_lbl.place(x=300,y=0,width=100,height=100)
        
        std_search_label=LabelFrame(right_label,bd=2,relief=RIDGE,text="Search Information",font=("times new roman",12,"bold"),bg="white")
        std_search_label.place(x=5,y=100,width=650,height=457)
        
        serch_label=Label(std_search_label,text="Search By:",font=("times new roman",12,"bold"),bg="white",fg="black")
        serch_label.grid(row=0,column=0,padx=10,pady=5,sticky=W) 
        
        search_combo=ttk.Combobox(std_search_label,font=("times new roman",12,"bold"),textvariable=self.var_search_by,state="readonly")
        search_combo["values"]=("Search by:","Roll#","Email")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10)
        
        search_entry=ttk.Entry(std_search_label,width=15,font=("times new roman",13),textvariable=self.var_search_entry)
        search_entry.grid(row=0,column=2,padx=5,pady=10,sticky=W)
        
        search_btn=Button(std_search_label,width=8,text="Search",command=self.search_by,font=("times new roman", 12, "bold"), borderwidth=1, fg="#a43a8e",
        bg="white", activeforeground="white", activebackground="#a43a8e",cursor="hand2")
        search_btn.grid(row=0,column=3,padx=5)
        
        show_all_btn=Button(std_search_label,width=8,text="Show All",command=self.fetch_data,font=("times new roman", 12, "bold"), borderwidth=1, fg="#a43a8e",
        bg="white", activeforeground="white", activebackground="#a43a8e",cursor="hand2")
        show_all_btn.grid(row=0,column=4,padx=5)
        
        # ----------------- Table Frame ---------------------
        
        table_frame=Frame(right_label,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=650,height=350)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("roll","name","gen","dob","email","cell","add","dep","year","sec","sem","photosamples"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("roll",text="Roll#")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("gen",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("cell",text="cell#")
        self.student_table.heading("add",text="Address")
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sec",text="Section")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("photosamples",text="photosamples")
        self.student_table["show"]="headings"
        self.student_table.column("roll",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("gen",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("cell",width=100)
        self.student_table.column("add",width=100)
        self.student_table.column("dep",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sec",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("photosamples",width=100)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    # -------------------------- Add Data -----------------------------
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_year.get()=="Select Year" or self.var_section.get()=="Select Section" or self.var_semester.get()=="Select Semester":
            messagebox.showerror("Error","All Fields are Required in Current Corse!",parent=self.studentroot)
        elif self.var_rollnum.get()=="" or self.var_name.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error","All Fields are Required!",parent=self.studentroot)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="usama12345",database="user")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_rollnum.get(),
                self.var_name.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_dep.get(),
                self.var_year.get(),
                self.var_section.get(),
                self.var_semester.get(),
                self.var_radiobtn1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Information Inserted successfully",parent=self.studentroot)
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.studentroot)
    
    #------------------------------- Displaying Data ---------------------------------
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="usama12345",database="user")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    #---------------------------------Search By Function -----------------------------------
    
    def search_by(self):
        
        try:
            if self.var_search_by.get()=="Roll#":
                conn=mysql.connector.connect(host="localhost",username="root",password="usama12345",database="user")
                my_cursor=conn.cursor()
                query=("select * from student where std_rollnum=%s")
                value=(self.var_search_entry.get(),)
                my_cursor.execute(query,value)
                data = my_cursor.fetchall()
                
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            elif self.var_search_by.get()=="Email":
                conn=mysql.connector.connect(host="localhost",username="root",password="usama12345",database="user")
                my_cursor=conn.cursor()
                query=("select * from student where std_email=%s")
                value=(self.var_search_entry.get(),)
                my_cursor.execute(query,value)
                data = my_cursor.fetchall()
                
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            else:
                messagebox.showerror("Error","Please Select a Searching Key!",parent=self.studentroot)
        except Exception as es:
            messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.studentroot)
    
    #---------------------------------------- get cusor --------------------------------
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[7])
        self.var_section.set(data[9])
        self.var_year.set(data[8])
        self.var_semester.set(data[10])
        self.var_rollnum.set(data[0])
        self.var_name.set(data[1])
        self.var_gender.set(data[2])
        self.var_dob.set(data[3])
        self.var_email.set(data[4])
        self.var_phone.set(data[5])
        self.var_address.set(data[6])
        self.var_radiobtn1.set(data[11])
        
    #------------------------------- Update Function -------------------------
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_year.get()=="Select Year" or self.var_section.get()=="Select Section" or self.var_semester.get()=="Select Semester":
            messagebox.showerror("Error","All Fields are Required in Current Corse!",parent=self.studentroot)
        elif self.var_rollnum.get()=="" or self.var_name.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error","All Fields are Required!",parent=self.studentroot)
        else:
            try:
                update = messagebox.askyesno("Update","Do you want to update the data?",parent=self.studentroot)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="usama12345",database="user")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set std_rollnum=%s, std_name=%s, std_gender=%s, std_dob=%s, std_email=%s, std_phone=%s, std_address=%s, std_department=%s, std_year=%s, std_section=%s, std_semester=%s, photosample=%s where std_rollnum=%s",(
                    self.var_rollnum.get(),
                    self.var_name.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_dep.get(),
                    self.var_year.get(),
                    self.var_section.get(),
                    self.var_semester.get(),
                    self.var_radiobtn1.get(),
                    self.var_rollnum.get()
                    ))
                    messagebox.showinfo("Updated","The Data has been updated successfully!")
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                else:
                    if not update:
                        return
            except Exception as ex:
                messagebox.showerror("Error",f"Due To : {str(ex)}",parent=self.studentroot)
    
    #---------------------------- Delete Function -------------------------------
    def delete_data(self):
        if self.var_rollnum.get()=="":
            messagebox.showerror("Error","Enter a Student Roll No Please!",parent=self.studentroot)
        else:
            try:
                delete = messagebox.askyesno("Delete","Do you want to delete the following user?",parent=self.studentroot)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="usama12345",database="user")
                    my_cursor=conn.cursor()
                    query="delete from student where std_rollnum=%s"
                    val=(self.var_rollnum.get(),)
                    my_cursor.execute(query,val)
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()
                    messagebox.showinfo("Success","The User is deleted successfully!",parent=self.studentroot)
                else:
                    if not delete:
                        return
            except Exception as ex:
                messagebox.showerror("Error",f"Due To : {str(ex)}",parent=self.studentroot)
    
    #---------------------------------------------- Reset Function --------------------------------
    def reset_data(self):
        self.var_rollnum.set(""),
        self.var_name.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_dep.set("Select Department"),
        self.var_year.set("Select Year"),
        self.var_section.set("Select Section"),
        self.var_semester.set("Select Semester"),
        self.var_radiobtn1.set("")
        
    #------------------------------- Generate data set or  Take photo Sample ----------------------------
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_year.get()=="Select Year" or self.var_section.get()=="Select Section" or self.var_semester.get()=="Select Semester":
            messagebox.showerror("Error","All Fields are Required in Current Corse!",parent=self.studentroot)
        elif self.var_rollnum.get()=="" or self.var_name.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error","All Fields are Required!",parent=self.studentroot)
        elif self.var_radiobtn1.get()=="no":
            messagebox.showerror("Error","Please Check the Take Photo Sample!",parent=self.studentroot)
        elif self.var_radiobtn1.get()=="taken":
            messagebox.showerror("Error","Sample for the Student is Already taken!",parent=self.studentroot)
        else:
            try:
                self.var_radiobtn1.set("taken")
                conn=mysql.connector.connect(host="localhost",username="root",password="usama12345",database="user")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                
                for x in myresult:
                    my_cursor.execute("update student set std_rollnum=%s, std_name=%s, std_gender=%s, std_dob=%s, std_email=%s, std_phone=%s, std_address=%s, std_department=%s, std_year=%s, std_section=%s, std_semester=%s, photosample=%s where std_rollnum=%s",(
                    self.var_rollnum.get(),
                    self.var_name.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_dep.get(),
                    self.var_year.get(),
                    self.var_section.get(),
                    self.var_semester.get(),
                    self.var_radiobtn1.get(),
                    self.var_rollnum.get()
                ))
                #--------------------------------Load predefined data for frontal face from opencv ---------------------
                face_classifier=cv2.CascadeClassifier(r".\login\haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(1)    
                # cap=cv2.VideoCapture('http://192.168.18.33:8080/video')
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="login/img_data/student_"+str(self.var_rollnum.get())+"_"+str(self.var_dep.get())+"_"+str(self.var_section.get())+"_"+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Croped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Sample for the user added Successfully!",parent=self.studentroot)
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
        
            except Exception as ex:
                messagebox.showerror("Error",f"Due To : {str(ex)}",parent=self.studentroot)
    
    def delete_dataset(self):
        check=1
        try:
            # Directory='login/img_data'
            # os.chdir(Directory)
            os.chdir("login/img_data")
            files=glob.glob("*.jpg")
            # check=1
            for filename in files:
                img_id=1
                for x in range(1,101):
                    student_name="student_"+str(self.var_rollnum.get())+"_"+str(self.var_dep.get())+"_"+str(self.var_section.get())+"_"+str(img_id)+".jpg"
                    if filename == student_name:
                        os.unlink(filename)
                        check+=1
                        break
                    else:
                        img_id+=1
            # Directory=''
        except Exception as ex:
                messagebox.showerror("Error",f"Due To : {str(ex)}",parent=self.studentroot)
        if check == 1:
            messagebox.showerror("Error","Nothing was found to be deleted!",parent=self.studentroot)
        else:
                try:
                    self.var_radiobtn1.set("no")
                    conn=mysql.connector.connect(host="localhost",username="root",password="usama12345",database="user")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set std_rollnum=%s, std_name=%s, std_gender=%s, std_dob=%s, std_email=%s, std_phone=%s, std_address=%s, std_department=%s, std_year=%s, std_section=%s, std_semester=%s, photosample=%s where std_rollnum=%s",(
                    self.var_rollnum.get(),
                    self.var_name.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_dep.get(),
                    self.var_year.get(),
                    self.var_section.get(),
                    self.var_semester.get(),
                    self.var_radiobtn1.get(),
                    self.var_rollnum.get()
                    ))
                    messagebox.showinfo("Sample Set as Null","Sample for the Student is Empty Now please Add Sample for the Student and Train it!",parent=self.studentroot)
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()
                except Exception as ex:
                    messagebox.showerror("Error",f"Due To : {str(ex)}",parent=self.studentroot)         
    
    
    
               
        



if __name__ == "__main__":
    homeroot=Tk()
    obj =Student(homeroot)
    homeroot.mainloop()