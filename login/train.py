from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train:
    def __init__(self,trainroot):
        self.trainroot = trainroot
        self.trainroot.geometry("800x600+300+80")
        self.trainroot.title("Train Model")
        
        bgimg = Image.open(r".\login\images\plain-white-background.jpg")
        self.bg = ImageTk.PhotoImage(bgimg)
        lbl_bg=Label(self.trainroot,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        img = Image.open(r".\login\images\superior-university-logo.jpg")
        img= img.resize((200,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.trainroot,image=self.photoimg)
        f_lbl.place(x=310,y=0,width=200,height=200)
        
        Title_lbl=Label(self.trainroot,text="FACIAL RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",15,"bold"),bg="white",fg="#a43a8e")
        Title_lbl.place(x=190,y=200)
        
         #---------------------------------- Mark Attendance Button ----------------------------------
        img2=Image.open(r".\login\images\train_model.png")
        img2=img2.resize((150,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        b2=Button(self.trainroot, image=self.photoimg2,cursor="hand2",border=0,bg="white",command=self.train_model,activebackground="#a43a8e")
        b2.place(x=330,y=260,width=150,height=150)
        
        model_train_label=Label(self.trainroot,text="Train Model",border=1,font=("times new roman",15),bg="white",fg="#a43a8e")
        model_train_label.place(x=350,y=420)
    
    
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
            messagebox.showerror("Error",f"Due To : {str(ex)}",parent=self.trainroot)
        
        
        
        
if __name__ == "__main__":
    homeroot=Tk()
    obj =Train(homeroot)
    homeroot.mainloop()