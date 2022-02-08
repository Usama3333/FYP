import glob,os
from tabnanny import check
from tkinter import messagebox



def delete_data():
    Directory='login/img_data'
    os.chdir(Directory)
    files=glob.glob('*.jpg')
    check=0
    for filename in files:
        img_id=1
        for x in range(1, 101):
            student_name="student_105_Software Engineering_C_"+str(img_id)+".jpg"
            if filename == student_name:
                print("--------------- Deleting File: "+filename+"-------------------")
                print("--------------- Student Name: "+student_name+"-------------------")
                os.unlink(filename)
                check+=1
                break
            else:
                print("--------------- Else Deleting File: "+filename+"-------------------")
                print("--------------- Else Student Name: "+student_name+"-------------------")
                img_id+=1
                print("img id is:"+str(img_id))
    print("Check is :"+str(check)+" at the end of loop")
                
                
                
                
                
            
if __name__ == "__main__":
    obj =delete_data()