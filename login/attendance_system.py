from distutils import command
from fileinput import close
from importlib.resources import contents
from multiprocessing import Value
from operator import delitem
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

fln=""
mydata=[]

class attendance_system:
    def __init__(self,attendanceroot):
        self.attendanceroot = attendanceroot
        self.attendanceroot.geometry("1530x790+0+0")
        self.attendanceroot.title("Attendance System")
           
            #------------------------ variables -----------------------------
        self.std_rollno = StringVar()
        self.std_name = StringVar()
        self.std_dep = StringVar()
        self.std_att = StringVar()
        self.date = StringVar()
        self.time = StringVar()
        self.std_sec = StringVar()
        self.std_sem = StringVar()
        
        bgimg = Image.open(r".\login\images\plain-white-background.jpg")
        self.bg = ImageTk.PhotoImage(bgimg)
        lbl_bg=Label(self.attendanceroot,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        img = Image.open(r".\login\images\superior-university-logo.jpg") 
        # img = Image.open(r"E:\FYP\images\superior-university-logo.jpg")
        img= img.resize((150,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.attendanceroot,image=self.photoimg)
        f_lbl.place(x=600,y=0,width=150,height=150)
        
        main_frame=Frame(self.attendanceroot,bd=2,bg="#a43a8e",border=2)
        main_frame.place(x=0,y=125,width=1400,height=600) 
        
        #Left Frame
        left_label=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),bg="white")
        left_label.place(x=10,y=10,width=660,height=580)
        std = Image.open(r".\login\images\student_detail.png")
        std= std.resize((100,100),Image.ANTIALIAS)
        self.stdimg=ImageTk.PhotoImage(std)
        std_lbl=Label(left_label,image=self.stdimg,bg="white")
        std_lbl.place(x=300,y=0,width=100,height=100)
        
        
        # Student Information
        
        information_label=LabelFrame(left_label,bd=2,relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"),bg="white")
        information_label.place(x=5,y=150,width=650,height=265)
        
        department_label=Label(information_label,text="Department:",font=("times new roman",12,"bold"),bg="white")
        department_label.grid(row=2,column=0,padx=10,sticky=W)
        
        dep_entry=ttk.Entry(information_label,width=20,font=("times new roman",13),textvariable=self.std_dep)
        dep_entry.grid(row=2,column=1,padx=5,pady=10,sticky=W)
        
        date_label=Label(information_label,text="Date:",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=1,column=2,padx=5,sticky=W)
        
        date_entry=ttk.Entry(information_label,width=20,font=("times new roman",13),textvariable=self.date)
        date_entry.grid(row=1,column=3,padx=5,pady=10,sticky=W)
        
        std_name_label=Label(information_label,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        std_name_label.grid(row=1,column=0,padx=5,sticky=W)
        
        std_name_entry=ttk.Entry(information_label,width=20,font=("times new roman",13),textvariable=self.std_name)
        std_name_entry.grid(row=1,column=1,padx=5,pady=10,sticky=W)
        
        time_label=Label(information_label,text="Time:",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=2,padx=5,sticky=W)
        
        time_entry=ttk.Entry(information_label,width=20,font=("times new roman",13),textvariable=self.time)
        time_entry.grid(row=2,column=3,padx=5,pady=10,sticky=W)
        
        std_rollno_label=Label(information_label,text="Student Roll#",font=("times new roman",12,"bold"),bg="white")
        std_rollno_label.grid(row=0,column=0,padx=5,sticky=W)
        
        std_rollno_entry=ttk.Entry(information_label,width=20,font=("times new roman",13),textvariable=self.std_rollno)
        std_rollno_entry.grid(row=0,column=1,padx=5,pady=10)
        
        std_sem_label=Label(information_label,text="Semester",font=("times new roman",12,"bold"),bg="white")
        std_sem_label.grid(row=3,column=0,padx=5,sticky=W)
        
        std_sem_entry=ttk.Entry(information_label,width=20,font=("times new roman",13),textvariable=self.std_sem)
        std_sem_entry.grid(row=3,column=1,padx=5,pady=10)
        
        std_sec_label=Label(information_label,text="Section",font=("times new roman",12,"bold"),bg="white")
        std_sec_label.grid(row=3,column=2,padx=5,sticky=W)
        
        std_sec_entry=ttk.Entry(information_label,width=20,font=("times new roman",13),textvariable=self.std_sec)
        std_sec_entry.grid(row=3,column=3,padx=5,pady=10)
        
        attendance_label=Label(information_label,text="Attendance:",font=("times new roman",12,"bold"),bg="white")
        attendance_label.grid(row=0,column=2,padx=5,sticky=W)
        
        attendance_combo=ttk.Combobox(information_label,font=("times new roman",12),width=20,textvariable=self.std_att,state="readonly")
        attendance_combo["values"]=("Select Attendance","Present","Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row=0,column=3,padx=5,pady=10)
        
        
        #---------------------------------------------- Button Frame --------------------------------------------
        
        Button_frame=Frame(information_label,bd=2,relief=RIDGE,bg="white")
        Button_frame.place(x=2,y=200,width=640,height=40)
        
        import_csv_btn=Button(Button_frame,width=13,text="Import CSV",command=self.importcsv,font=("times new roman", 15, "bold"), borderwidth=1, fg="#a43a8e",
        bg="white", activeforeground="white", activebackground="#a43a8e",cursor="hand2")
        import_csv_btn.grid(row=0,column=0)
        
        export_csv_btn=Button(Button_frame,width=13,text="Export CSV",command=self.exportcsv,font=("times new roman", 15, "bold"), borderwidth=1, fg="#a43a8e",
        bg="white", activeforeground="white", activebackground="#a43a8e",cursor="hand2")
        export_csv_btn.grid(row=0,column=1)
        
        update_btn=Button(Button_frame,width=13,text="Update",command=self.update,font=("times new roman", 15, "bold"), borderwidth=1, fg="#a43a8e",
        bg="white", activeforeground="white", activebackground="#a43a8e",cursor="hand2")
        update_btn.grid(row=0,column=2)
        
        reset_btn=Button(Button_frame,width=13,text="Reset",command=self.reset,font=("times new roman", 15, "bold"), borderwidth=1, fg="#a43a8e",
        bg="white", activeforeground="white", activebackground="#a43a8e",cursor="hand2")
        reset_btn.grid(row=0,column=3)
        
        
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
        
        # ----------------- Table Frame ---------------------
        
        table_frame=Frame(right_label,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=125,width=650,height=430)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.attendance_table=ttk.Treeview(table_frame,column=("rollno","name","dep","sec","sem","time","date","att"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)
        
        self.attendance_table.heading("rollno",text="Student Roll#")
        self.attendance_table.heading("name",text="Student Name")
        self.attendance_table.heading("dep",text="Department")
        self.attendance_table.heading("sec",text="Section")
        self.attendance_table.heading("sem",text="Semester")
        self.attendance_table.heading("time",text="Time")
        self.attendance_table.heading("date",text="Date")
        self.attendance_table.heading("att",text="Attendance")
        self.attendance_table["show"]="headings"

        self.attendance_table.column("rollno",width=100)
        self.attendance_table.column("name",width=100)
        self.attendance_table.column("dep",width=100)
        self.attendance_table.column("sec",width=100)
        self.attendance_table.column("sem",width=100)
        self.attendance_table.column("time",width=100)
        self.attendance_table.column("date",width=100)
        self.attendance_table.column("att",width=100)
        self.attendance_table.pack(fill=BOTH,expand=1)
        self.attendance_table.bind("<ButtonRelease>",self.get_cursor)
        
        #-------------------------------- Fetching Data -----------------------------------
        
    def fetchdata(self,rows):
            self.attendance_table.delete(*self.attendance_table.get_children())
            for i in rows:
                self.attendance_table.insert("",END,value=i)
                
    def importcsv(self):
        global mydata,fln
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL Files","*.*")),parent=self.attendanceroot)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)
            
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found To Export",parent=self.attendanceroot)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL Files","*.*")),parent=self.attendanceroot)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data is exported Successfully!",parent=self.attendanceroot)
        except Exception as ex:
            messagebox.showerror("Error",f"Due To : {str(ex)}",parent=self.attendanceroot)
        
        
    def get_cursor(self,event=""):
        cursor_row=self.attendance_table.focus()
        content=self.attendance_table.item(cursor_row)
        row=content['values']
        self.std_rollno.set(row[0])
        self.std_name.set(row[1])
        self.std_dep.set(row[2])
        self.std_sec.set(row[3])
        self.std_sem.set(row[4])
        self.time.set(row[5])
        self.date.set(row[6])
        self.std_att.set(row[7])
        
    def reset(self):
        self.std_rollno.set("")
        self.std_name.set("")
        self.std_dep.set("")
        self.std_sec.set("")
        self.std_sem.set("")
        self.time.set("")
        self.date.set("")
        self.std_att.set("")
        
    def update(self):
        yesno=messagebox.askyesno("Update Data","Are you Sure You Want To Update Data?",parent=self.attendanceroot)
        if yesno>0:
            List_Update=[]
            file=open(str(fln),'r')
            reader=csv.reader(file)
            for row in reader:
                if len(row)!=0:
                    # if row[0]!=self.std_rollno:
                    #     messagebox.showerror("Error","You Cannot Change Students Roll Number Edit any other Field please !",parent=self.attendanceroot)
                    if row[0]==self.std_rollno.get():
                        row[1]=self.std_name.get()
                        row[2]=self.std_dep.get()
                        row[3]=self.std_sec.get()
                        row[4]=self.std_sem.get()
                        row[5]=self.time.get()
                        row[6]=self.date.get()
                        row[7]=self.std_att.get()
                        List_Update.append(row)
                    else:
                        List_Update.append(row)
                else:
                    List_Update.append(row)
            # print(List_Update)
            file.close()
            file=open(str(fln),'w+',newline='')
            write=csv.writer(file)
            write.writerows(List_Update)
            file.seek(0)
            mydata.clear()
            with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetchdata(mydata)
            messagebox.showinfo("Success","Your Data Is Updated Successfully",parent=self.attendanceroot)
            file.close()
        else:
            return


if __name__ == "__main__":
    homeroot=Tk()
    obj =attendance_system(homeroot)
    homeroot.mainloop()