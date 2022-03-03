from tkinter import*
from tkinter import ttk
from tkinter.tix import CheckList
from PIL import Image,ImageTk
from cv2 import VideoCapture
from student import Student
import os
import cv2
import numpy as np
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
from train import Train
from attendance_system import attendance_system
from support import Support
from tkinter import filedialog
from assistant import Assistant

fln=""
class Face_Recognition_System:
    
    mark_check=None
    def __init__(self,homeroot):
        self.homeroot = homeroot
        self.homeroot.geometry("1530x790+0+0")
        self.homeroot.title("face Recognition Attendance System")
        
        bgimg = Image.open(r".\login\images\plain-white-background.jpg")
        self.bg = ImageTk.PhotoImage(bgimg)
        lbl_bg=Label(self.homeroot,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        img = Image.open(r".\login\images\superior-university-logo.jpg")
        img= img.resize((200,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.homeroot,image=self.photoimg)
        f_lbl.place(x=580,y=0,width=200,height=200)
        
        Title_lbl=Label(self.homeroot,text="FACIAL RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",15,"bold"),bg="white",fg="#a43a8e")
        Title_lbl.place(x=460,y=200)
        
        #---------------------------------- Icon Buttons --------------------------------
        
        #---------------------------------- Student Detail Button ----------------------------------
        img1=Image.open(r".\login\images\student_detail.png")
        img1=img1.resize((150,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        b1=Button(self.homeroot, image=self.photoimg1,command=self.student_details,cursor="hand2",border=0,bg="white",activebackground="#a43a8e")
        b1.place(x=130,y=270,width=150,height=150)
        
        stud_detail_label=Label(self.homeroot,text="Student Details",border=1,font=("times new roman",15),bg="white",fg="#a43a8e")
        stud_detail_label.place(x=130,y=430)
        
        #---------------------------------- Train Model Button ----------------------------------
        img2=Image.open(r".\login\images\train_model.png")
        img2=img2.resize((150,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        b2=Button(self.homeroot, image=self.photoimg2,command=self.train_model,cursor="hand2",border=0,bg="white",activebackground="#a43a8e")
        b2.place(x=130,y=500,width=150,height=150)
        
        model_train_label=Label(self.homeroot,text="Train Model",border=1,font=("times new roman",15),bg="white",fg="#a43a8e")
        model_train_label.place(x=150,y=665)
        
         #---------------------------------- Mark Attendance Button ----------------------------------
        img3=Image.open(r".\login\images\mark_attendance.png")
        img3=img3.resize((150,150),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        b3=Button(self.homeroot, image=self.photoimg3,command=self.face_recognition,cursor="hand2",border=0,bg="white",activebackground="#a43a8e")
        b3.place(x=580,y=260,width=150,height=150)
        
        Mark_Attendance_label=Label(self.homeroot,text="Mark Attendance",border=1,font=("times new roman",15),bg="white",fg="#a43a8e")
        Mark_Attendance_label.place(x=580,y=420)
        
        #---------------------------------- Attendance Button ----------------------------------
        img4=Image.open(r".\login\images\attendance.png")
        img4=img4.resize((150,150),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b4=Button(self.homeroot, image=self.photoimg4,command=self.attendance,cursor="hand2",border=0,bg="white",activebackground="#a43a8e")
        b4.place(x=580,y=500,width=150,height=150)
        
        Attendance_label=Label(self.homeroot,text="Attendance",border=1,font=("times new roman",15),bg="white",fg="#a43a8e")
        Attendance_label.place(x=605,y=660)
        
        #---------------------------------- Support Button ----------------------------------
        img5=Image.open(r".\login\images\support.png")
        img5=img5.resize((150,150),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b5=Button(self.homeroot, image=self.photoimg5,command=self.support,cursor="hand2",border=0,bg="white",activebackground="#a43a8e")
        b5.place(x=1010,y=260,width=150,height=150)
        
        support_label=Label(self.homeroot,text="Support",border=1,font=("times new roman",15),bg="white",fg="#a43a8e")
        support_label.place(x=1050,y=420)
        
        #---------------------------------- Exit Button ----------------------------------
        img6=Image.open(r".\login\images\exit.png")
        img6=img6.resize((150,150),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b6=Button(self.homeroot, image=self.photoimg6,command=self.exit,cursor="hand2",border=0,bg="white",activebackground="#a43a8e")
        b6.place(x=1010,y=500,width=150,height=150)
        
        exit_label=Label(self.homeroot,text="Exit",border=1,font=("times new roman",15),bg="white",fg="#a43a8e")
        exit_label.place(x=1050,y=660)
    
        #---------------------------------- Assistant Button ----------------------------------
        img7=Image.open(r".\login\images\chatbot.png")
        img7=img7.resize((70,70),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b7=Button(self.homeroot, image=self.photoimg7,command=self.Assistant,cursor="hand2",border="0",bg="#bc5cb4",activebackground="#a43a8e")
        b7.place(x=1278,y=660,width=70,height=70)
        
        assistant_label=Label(self.homeroot,text="Assistant",border=1,font=("Agency FB",15,"bold"),bg="white",fg="#a43a8e")
        assistant_label.place(x=1283,y=625)
        
        
        #---------------------------------- Date Button ----------------------------------
        img8=Image.open(r".\login\images\calendar.png")
        img8=img8.resize((70,70),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b8=Button(self.homeroot, image=self.photoimg8,command=self.select_date,cursor="hand2",border="0",bg="#bc5cb4",activebackground="#a43a8e")
        b8.place(x=10,y=660,width=70,height=70)
        
        assistant_label=Label(self.homeroot,text="Attendance File",border=1,font=("Agency FB",15,"bold"),bg="white",fg="#a43a8e")
        assistant_label.place(x=5,y=625)

        
    # ------------------------------ Button Functions --------------------------------------------
    
    def select_date(self):
        global fln
        yesno=messagebox.askyesno("Mark Attendance","You Want to Mark Attendance in a Existing File?",parent=self.homeroot)
        if yesno>0:
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL Files","*.*")),parent=self.homeroot)
        else:
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL Files","*.*")),parent=self.homeroot)
            file= open(str(fln),"w")
            file.close()
    
    def student_details(self):
        self.new_window=Toplevel(self.homeroot)
        self.app=Student(self.new_window) 
        
    def support(self):
        self.new_window=Toplevel(self.homeroot)
        self.app=Support(self.new_window) 
        
    def Assistant(self):
        self.new_window=Toplevel(self.homeroot)
        self.app=Assistant(self.new_window) 
        
        
    def train_model(self):
        try:
            
            data_dir=("login/img_data")
            path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
            
            faces=[]
            ids=[]
            
            for image in path:
                img=Image.open(image).convert('L') #Gray Scale Image
                imageNp=np.array(img,'uint8')
                id=int(os.path.split(image)[1].split('_')[1]) #list comprehancing
                
                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training",imageNp)
                cv2.waitKey(1)==13
            ids=np.array(ids)
            #--------------------------- Train The Classifier and Save --------------------------------
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces,ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Training Dataset Completed!!")
        except Exception as ex:
            messagebox.showerror("Error",f"Due To : {str(ex)}",parent=self.homeroot)
    
    def face_recognition(self):


        def draw_boundary(img,classifier,scalefactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scalefactor,minNeighbors)
            
            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost",username="root",password="usama12345",database="user")
                my_cursor=conn.cursor()
                
                my_cursor.execute("select std_name from student where std_rollnum="+str(id))
                std_name=my_cursor.fetchone()
                std_name="+".join(std_name)
                
                my_cursor.execute("select std_rollnum from student where std_rollnum="+str(id))
                std_rollno=my_cursor.fetchone()
                std_rollno="+".join(std_rollno)
                
                my_cursor.execute("select std_department from student where std_rollnum="+str(id))
                std_dep=my_cursor.fetchone()
                std_dep="+".join(std_dep)
                
                my_cursor.execute("select std_section from student where std_rollnum="+str(id))
                std_sec=my_cursor.fetchone()
                std_sec="+".join(std_sec)
                
                my_cursor.execute("select std_semester from student where std_rollnum="+str(id))
                std_sem=my_cursor.fetchone()
                std_sem="+".join(std_sem)
                
                
                if confidence>77:
                    cv2.putText(img,f"Roll:{std_rollno}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Name:{std_name}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Department:{std_dep}",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Section:{std_sec}",(x,y-15),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    if fln!="":
                        self.mark_attendance(std_rollno,std_name,std_dep,std_sec,std_sem)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-25),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord=[x,y,w,h]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        faceCascade=cv2.CascadeClassifier(r".\login\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(1)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To FaceRecognition",img)
            
            if cv2.waitKey(1)==13:
                if fln!="":
                    if self.mark_check == True :
                        messagebox.showinfo("Success","The Attendance is Marked Successfully")
                        self.mark_check=False
                        break
                    else:
                        messagebox.showerror("Error","The Attendance is Already Marked !")
                        self.mark_check=False
                        break
                else:
                    messagebox.showerror("File Not Found","No File Was Found To Mark Attendance Please Select A File From Select File Button ",parent=self.homeroot)
                    break
                # break
        video_cap.release()
        cv2.destroyAllWindows()
        
    def mark_attendance(self,rollno,name,dep,sec,sem):
        
        
        # "attendance/attendance.csv"
        with open(str(fln),"r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            
            if((rollno not in name_list) and (name not in name_list) and (dep not in name_list) and (sec not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{rollno},{name},{dep},{sec},{sem},{dtString},{d1},Present")
                self.mark_check=True
            
            
    def attendance(self):
        self.new_window=Toplevel(self.homeroot)
        self.app=attendance_system(self.new_window)   
            
    def exit(self):
        self.homeroot.destroy()






if __name__ == "__main__":
    homeroot=Tk()
    obj =Face_Recognition_System(homeroot)
    homeroot.mainloop()