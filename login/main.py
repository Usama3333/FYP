from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
from home import Face_Recognition_System


def main():
    window=Tk()
    app=login_window(window)
    window.mainloop()



class login_window:
    def __init__(self,loginhomeroot):
        
        self.var_user = StringVar()
        self.var_pass = StringVar()
        
        self.loginhomeroot = loginhomeroot
        self.loginhomeroot.title("Login")
        self.loginhomeroot.geometry("1550x800+0+0")
        # img = Image.open(r".\images\plain-white-background.jpg")
        img = Image.open(r".\login\images\plain-white-background.jpg")
        self.bg = ImageTk.PhotoImage(img)
        lbl_bg=Label(self.loginhomeroot,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        # Purple Frame
        # "#dfcced"
        frame = Frame(self.loginhomeroot,bg="#a43a8e")
        frame.place(x=500,y=150,width=340,height=500)

        # Logo on Frame
        img1=Image.open(r".\login\images\superior-university-logo.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="white",borderwidth=1)
        lblimg1.place(x=620,y=170,width=100,height=100)

        #Label Below the University Icon
        login=Label(frame,text="Login",font=("times new roman",20,"bold"),fg="white",bg="#a43a8e")
        login.place(x=133,y=120)

        # Email Field
        username=lbl=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="white",bg="#a43a8e")
        username.place(x=70,y=160)
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"),textvariable=self.var_user)
        self.txtuser.place(x=40,y=190,width=270)

        # Password Field
        password = lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="#a43a8e")
        password.place(x=70, y=230)
        self.txtpass = ttk.Entry(frame,show="*", font=("times new roman",15, "bold"),textvariable=self.var_pass)
        self.txtpass.place(x=40, y=260, width=270)

        # Icons
        email_icon = Image.open(r".\login\images\email.png")
        email_icon = email_icon.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(email_icon)
        lblimg2 = Label(image=self.photoimage2, bg="#a43a8e", borderwidth=1)
        lblimg2.place(x=540, y=310, width=25, height=25)

        password_icon = Image.open(r".\login\images\password.png")
        password_icon = password_icon.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(password_icon)
        lblimg3 = Label(image=self.photoimage3, bg="#a43a8e", borderwidth=1)
        lblimg3.place(x=540, y=380, width=25, height=25)

        # Login Buttons
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman", 15, "bold"),bd=1 ,relief=RIDGE,fg="#a43a8e",bg="white",activeforeground="white",activebackground="#9e8cab")
        loginbtn.place(x=110,y=305,width=120,height=35)

        # Registration Button

        register_icon = Image.open(r".\login\images\registration.png")
        register_icon = register_icon.resize((25, 25), Image.ANTIALIAS)
        self.photoimage4 = ImageTk.PhotoImage(register_icon)
        lblimg4 = Label(frame,image=self.photoimage4, bg="#a43a8e", borderwidth=1)
        lblimg4.place(x=15, y=345, width=25, height=25)

        registerbtn = Button(frame, text="Register", command=self.register_window,font=("times new roman", 13, "bold"), borderwidth=0, fg="white",
                          bg="#a43a8e", activeforeground="white", activebackground="#a43a8e")
        registerbtn.place(x=42, y=345, width=70)

        # Forgot Password

        forgot_icon = Image.open(r".\login\images\forgot_password.png")
        forgot_icon = forgot_icon.resize((25, 25), Image.ANTIALIAS)
        self.photoimage5 = ImageTk.PhotoImage(forgot_icon)
        lblimg5 = Label(frame, image=self.photoimage5, bg="#a43a8e", borderwidth=1)
        lblimg5.place(x=13, y=373, width=25, height=25)

        forgotbtn = Button(frame, text="Forgot Password",command=self.forgot_password_window, font=("times new roman", 13, "bold"), borderwidth=0, fg="white",
                             bg="#a43a8e", activeforeground="white", activebackground="#a43a8e")
        forgotbtn.place(x=42, y=373, width=130)
        
    def register_window(self):
        self.new_window=Toplevel(self.loginhomeroot)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "Username or Password is empty")
        elif self.txtuser.get() == "usama" and self.txtpass.get() == "12345":
            messagebox.showinfo("Success", "WELCOME TO THE HOME PAGE :)")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="usama12345",database="user")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
            self.txtuser.get(),
            self.txtpass.get()
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Email or Password!")
            else:
                opne_main=messagebox.askyesno("Access Verification!","Access is only allowed to the admins, Are you a admin?")
                if opne_main>0:
                    self.new_window=Toplevel()
                    self.app=Face_Recognition_System(self.new_window)
                    self.var_pass.set("")
                    self.var_user.set("")
                else:
                    if not opne_main:
                        return
            conn.commit()
            conn.close()
            
# --------------------------Reset Password Function ------------------------------

    def rest_password(self):
        if self.question_entry1.get()=="select":
            messagebox.showerror("Error","Select Security Question",parent=self.loginhomeroot2)
        elif self.answer_entry1.get()=="":
            messagebox.showerror("Error","Please Enter The Answer",parent=self.loginhomeroot2)
        elif self.new_password_entry.get()=="":
            messagebox.showerror("Error","Please Enter The New Password",parent=self.loginhomeroot2)
        else:
            conn=mysql.connector.connect(host="localhost",user="homeroot",password="usama12345",database="user")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.question_entry1.get(),self.answer_entry1.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Your Answer was not correct, Please Give a Correct Answer!",parent=self.loginhomeroot2)
            else:
                query=("update register set password=%s where email=%s")
                value1=(self.new_password_entry.get(),self.txtuser.get())
                my_cursor.execute(query,value1)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password Has Changed Successfully, Please Login With Your New Password",parent=self.loginhomeroot2)
                self.loginhomeroot2.destroy()
            
# -------------------------- Forgot Password Window -------------------------------
    
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter a Email to Reset Password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="usama12345",database="user")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error"," Your Entered Email Is Not Valid, Please Enter a Valid Email")
            else:
                conn.close()
                self.loginhomeroot2=Toplevel()
                self.loginhomeroot2.title("Forget Password")
                self.loginhomeroot2.geometry("340x450+610+170")
                
                img = Image.open(r".\login\images\plain-white-background.jpg")
                self.bg = ImageTk.PhotoImage(img)
                lbl=Label(self.loginhomeroot2,image=self.bg)
                lbl.place(x=0,y=0,relwidth=1)
                
                logo_icon = Image.open(r".\login\images\superior-university-logo.jpg")
                logo_icon = logo_icon.resize((100, 100), Image.ANTIALIAS)
                self.logoimage1 = ImageTk.PhotoImage(logo_icon)
                limg1 = Label(self.loginhomeroot2,image=self.logoimage1, bg="white", borderwidth=1)
                limg1.place(x=120, y=10, width=100, height=80)
                
                question=Label(self.loginhomeroot2,text="Select Security Question",font=("times new roman",15),bg="white",fg="#a43a8e")
                question.place(x=50,y=100)

                self.question_entry1=ttk.Combobox(self.loginhomeroot2,font=("times new roman",15),state="readonly")
                self.question_entry1["values"]=("select","your favourit pet name","your best friends name","your favourit cousin")
                self.question_entry1.place(x=50,y=130,width=250)
                self.question_entry1.current(0)

                answer=Label(self.loginhomeroot2,text="Security Answer",font=("times new roman",15),bg="white",fg="#a43a8e")
                answer.place(x=50,y=170)

                self.answer_entry1=ttk.Entry(self.loginhomeroot2,font=("times new roman",15))
                self.answer_entry1.place(x=50,y=200,width=250)
                
                new_password=Label(self.loginhomeroot2,text="Enter New Password",font=("times new roman",15),bg="white",fg="#a43a8e")
                new_password.place(x=50,y=230)

                self.new_password_entry=ttk.Entry(self.loginhomeroot2,show="*",font=("times new roman",15))
                self.new_password_entry.place(x=50,y=260,width=250)
                
                reset_icon = Image.open(r".\login\images\reset_password.png")
                reset_icon = reset_icon.resize((25, 25), Image.ANTIALIAS)
                self.photoimage2 = ImageTk.PhotoImage(reset_icon)
                lblimg2 = Label(self.loginhomeroot2,image=self.photoimage2, bg="white", borderwidth=1)
                lblimg2.place(x=40, y=292, width=60, height=60)
                
                loginbtn = Button(self.loginhomeroot2, text="Change Password",command=self.rest_password, font=("times new roman", 15, "bold"), borderwidth=1, fg="#a43a8e",
                bg="white", activeforeground="#a43a8e", activebackground="#dfcced")
                loginbtn.place(x=90, y=300,height=40)
            

            
class Register:
    def __init__(self,registerhomeroot):
        self.registerhomeroot = registerhomeroot
        self.registerhomeroot.title("Registration")
        self.registerhomeroot.geometry("1800x800+0+0")


        #---------- Variables -------------
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_password=StringVar()
        self.var_confirmpassword=StringVar()
        self.var_check= Variable()

        # -------- Back Ground Image ---------

        self.bg=ImageTk.PhotoImage(file=r".\login\images\plain-white-background.jpg")
        bg_lbl=Label(self.registerhomeroot,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        # --------- Left Side Icon ----------
        self.logo=ImageTk.PhotoImage(file=r".\login\images\superior-university-logo.jpg")
        logo_lbl=Label(self.registerhomeroot,image=self.logo)
        logo_lbl.place(x=50,y=100,width=500,height=500)

        #------------- Frame For Fields -----------
        frame=Frame(self.registerhomeroot,bg="white")
        frame.place(x=550,y=100,width=800,height=500)

        register_lbl=Label(frame,text="Registeration Form",font=("times new roman",20,"bold"),fg="#a43a8e",bg="white")
        register_lbl.place(x=250,y=20)

        # ------------- Labels and Entries ------------
        fname=Label(frame,text="First Name",font=("times new roman",15),bg="white",fg="#a43a8e")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        self.fname_entry.place(x=50,y=130,width=250)


        Lname=Label(frame,text="Last Name",font=("times new roman",15),bg="white",fg="#a43a8e")
        Lname.place(x=370,y=100)

        self.Lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.Lname_entry.place(x=370,y=130,width=250)


        contact=Label(frame,text="Contact #",font=("times new roman",15),bg="white",fg="#a43a8e")
        contact.place(x=50,y=170)

        self.contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.contact_entry.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15),bg="white",fg="#a43a8e")
        email.place(x=370,y=170)

        self.email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.email_entry.place(x=370,y=200,width=250)

        question=Label(frame,text="Select Security Question",font=("times new roman",15),bg="white",fg="#a43a8e")
        question.place(x=50,y=250)

        self.question_entry=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15),state="readonly")
        self.question_entry["values"]=("select","your favourit pet name","your best friends name","your favourit cousin")
        self.question_entry.place(x=50,y=280,width=250)
        self.question_entry.current(0)

        answer=Label(frame,text="Security Answer",font=("times new roman",15),bg="white",fg="#a43a8e")
        answer.place(x=370,y=250)

        self.answer_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.answer_entry.place(x=370,y=280,width=250)

        password=Label(frame,text="Password",font=("times new roman",15),bg="white",fg="#a43a8e")
        password.place(x=50,y=320)

        self.password_entry=ttk.Entry(frame,textvariable=self.var_password,show="*",font=("times new roman",15))
        self.password_entry.place(x=50,y=350,width=250)

        confirm_password=Label(frame,text="Confirm Password",font=("times new roman",15),bg="white",fg="#a43a8e")
        confirm_password.place(x=370,y=320)

        self.confirm_password_entry=ttk.Entry(frame,textvariable=self.var_confirmpassword,show="*",font=("times new roman",15))
        self.confirm_password_entry.place(x=370,y=350,width=250)

        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms And Condition",font=("times new roman",12),onvalue=1,offvalue=0,bg="white",fg="#a43a8e")
        checkbtn.place(x=50,y=390)

        register_icon = Image.open(r".\login\images\register.png")
        register_icon = register_icon.resize((60, 60), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(register_icon)
        lblimg1 = Label(frame,image=self.photoimage1, bg="white", borderwidth=1)
        lblimg1.place(x=50, y=440, width=60, height=60)

        registerbtn = Button(frame, text="Register",command=self.register_data, font=("times new roman", 15, "bold"), borderwidth=1, fg="#a43a8e",
                          bg="white", activeforeground="#a43a8e", activebackground="#dfcced")
        registerbtn.place(x=120, y=440,height=60)

        login_icon = Image.open(r".\login\images\login.png")
        login_icon = login_icon.resize((60, 60), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(login_icon)
        lblimg2 = Label(frame,image=self.photoimage2, bg="white", borderwidth=1)
        lblimg2.place(x=370, y=440, width=60, height=60)

        loginbtn = Button(frame, text="Login Now",command=self.return_login ,font=("times new roman", 15, "bold"), borderwidth=1, fg="#a43a8e",
                          bg="white", activeforeground="#a43a8e", activebackground="#dfcced")
        loginbtn.place(x=435, y=440,height=60)

    # --------------------- Function Decleration ----------------------------
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="select":
            messagebox.showerror("Error","Required First Name , Email and Security Question",parent=self.registerhomeroot)
        elif self.var_password.get()!=self.var_confirmpassword.get():
            messagebox.showerror("Error","Password Must Be Same",parent=self.registerhomeroot)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree To The Terms And Condition",parent=self.registerhomeroot)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="usama12345",database="user")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already Exist!",parent=self.registerhomeroot)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
            self.var_fname.get(),
            self.var_lname.get(),
            self.var_contact.get(),
            self.var_email.get(),
            self.var_securityQ.get(),
            self.var_securityA.get(),
            self.var_password.get()
            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","User Registered Successfully!",parent=self.registerhomeroot)
    
    def return_login(self):
        self.registerhomeroot.destroy()
        





if __name__ == "__main__":
    main()