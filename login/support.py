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
from tkinter import filedialog


class Support:
    
    mark_check=None
    def __init__(self,supportroot):
        self.supportroot = supportroot
        self.supportroot.geometry("1530x790+0+0")
        self.supportroot.title("face Recognition Attendance System Support")
        
        bgimg = Image.open(r".\login\images\plain-white-background.jpg")
        self.bg = ImageTk.PhotoImage(bgimg)
        lbl_bg=Label(self.supportroot,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        img = Image.open(r".\login\images\superior-university-logo.jpg")
        img= img.resize((200,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.supportroot,image=self.photoimg)
        f_lbl.place(x=580,y=0,width=200,height=200)
        
        Title_lbl=Label(self.supportroot,text="FACIAL RECOGNITION ATTENDANCE SYSTEM SUPPORT",font=("times new roman",15,"bold"),bg="white",fg="#a43a8e")
        Title_lbl.place(x=420,y=200)
        
        developer_details_lbl=Label(self.supportroot,text="DELVEOPER DETAILS:",font=("times new roman",15,"bold"),bg="white",fg="#a43a8e")
        developer_details_lbl.place(x=0,y=300)
        
        details_text_lbl=Label(self.supportroot,text="In case of problem contact the following team.",font=("times new roman",12),bg="white",fg="#a43a8e")
        details_text_lbl.place(x=0,y=328)
        
        names_Title_lbl=Label(self.supportroot,text="NAMES:",font=("times new roman",13,"bold"),bg="white",fg="#a43a8e")
        names_Title_lbl.place(x=0,y=360)
        
        names_lbl=Label(self.supportroot,text="Muhammad Usama\nRazi Nasir\nHamid Munawar",font=("times new roman",12),bg="white",fg="#a43a8e")
        names_lbl.place(x=0,y=390)
        
        Contact_Title_lbl=Label(self.supportroot,text="Emails:",font=("times new roman",13,"bold"),bg="white",fg="#a43a8e")
        Contact_Title_lbl.place(x=0,y=480)
        
        emails_lbl=Label(self.supportroot,text="BSEM-F18-105@superior.edu.pk\nBSEM-F18-114@superior.edu.pk\nBSEM-F18-100@superior.edu.pk",font=("times new roman",12),bg="white",fg="#a43a8e")
        emails_lbl.place(x=0,y=510)
        
        
        
if __name__ == "__main__":
    supportroot=Tk()
    obj =Support(supportroot)
    supportroot.mainloop()