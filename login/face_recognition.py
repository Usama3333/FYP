from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np




class face_recognition:
    def __init__(self,face_recognition_root):
        self.face_recognition_root = face_recognition_root
        self.face_recognition_root.geometry("800x600+300+80")
        self.face_recognition_root.title("Train Model")
        
        
        
if __name__ == "__main__":
    homeroot=Tk()
    obj =face_recognition(homeroot)
    homeroot.mainloop()