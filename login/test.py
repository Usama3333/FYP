from asyncore import write
from importlib.resources import contents
from multiprocessing import Value
from operator import delitem
from re import A
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog



if __name__ == "__main__":

#     mydata=[]   
# a = 0
    fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL Files","*.*")))
    print(str(fln))
    print("--------------------")
    print("/n")
# with open(fln) as myfile:
#     csvread=csv.reader(myfile,delimiter=",")
#     for i in csvread:
#         mydata.append(i)
#         a+=1
#         # print("Attrattion No : "+ str(a))
#         # print(i)
       
#     print(mydata[1][0])
file=open(str(fln),'r')
reader=csv.reader(file)
L=[]
uroll=int(input('Enter the Roll No of Student whose section you want to update : '))
found=False
# row=1
for row in reader:
    if len(row)!=0:
        if row[0]==str(uroll):
            found=True
            section=input('Enter the Section You want to replace : ')
            row[3]=section
        L.append(row)
file.close()

if found==False:
    print("Record for the selected Roll num wasnot Found !!")
else:
    file=open(str(fln),'w+',newline='')
    write=csv.writer(file)
    write.writerows(L)
    file.seek(1)
    Reader=csv.reader(file)
    for row in Reader:
        print (row)
    file.close()