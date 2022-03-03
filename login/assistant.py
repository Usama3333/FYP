from cgitb import text
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Assistant:
    
    def __init__(self,assistantroot):
        self.enter_var=StringVar()
        self.q1= "How to use application ?"
        self.q2= "How to mark attendance ?"
        self.q3= "How to add student's details ?"
        self.q4= "How to train model for marking attendance ?"
        self.q5= "How to manually mark attendance ?"
        self.q6= "How to contact support ?"
        self.assistantroot = assistantroot
        self.assistantroot.geometry("730x620+0+0")
        self.assistantroot.title("Assistant")
        self.assistantroot.bind('<Return>',self.enter_func)
        
        main_frame=Frame(self.assistantroot,bd=4,bg="#a43a8e",width=800)
        main_frame.pack()
        
        img_chat=Image.open(r".\login\images\chatbot.png")
        img_chat=img_chat.resize((100,100),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_chat)
        
        Title_Lable=Label(main_frame,relief=RAISED,anchor='nw',width=800,compound=LEFT,image=self.photoimg,text='Assistant',font=('times new roman',30,'bold'),fg="#a43a8e",bg='white')
        Title_Lable.pack(side=TOP)
        
        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=5,relief=RAISED,font=('arial',12),yscrollcommand=self.scroll_y.set )
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()
        
        self.text.insert(END,'\n\n'+"""Assistant: Hi How Can I Help You ?
        You Can Type Any Of The Following Number:
        1) %s
        2) %s
        3) %s
        4) %s
        5) %s
        6) %s
        """ % (self.q1,self.q2,self.q3,self.q4,self.q5,self.q6))
        
        btn_frame=Frame(self.assistantroot,bd=4,bg="white",width=2000)
        btn_frame.pack()
        
        Label_1=Label(btn_frame,text="Type Here:",font=('times new roman',18,'bold'),fg="#a43a8e",bg='white')
        Label_1.grid(row=0,column=0,padx=5,sticky=W)
        
        
        self.entry=ttk.Entry(btn_frame,textvariable=self.enter_var,width=40,font=('times new roman',15))
        self.entry.grid(row=0,column=1,padx=5,sticky=W)
        
        self.send=Button(btn_frame,text="SEND",font=('arial',15,'bold'),command=self.send,width=8,bg="#a43a8e", fg="white")
        self.send.grid(row=0,column=2,padx=5,sticky=W)
        
        Label_2=Label(btn_frame,text="",font=('times new roman',18,'bold'),fg="#a43a8e",bg='white')
        Label_2.grid(row=1,column=0,padx=5,sticky=W)
        
        self.clear=Button(btn_frame,text="CLEAR CHAT",font=('arial',15,'bold'),command=self.clear,width=10,bg="#a43a8e", fg="white")
        self.clear.grid(row=2,column=0,padx=5,sticky= W)
        
        self.Exit=Button(btn_frame,text="EXIT",font=('arial',15,'bold'),command=self.exit,width=8,bg="#a43a8e", fg="white")
        self.Exit.grid(row=2,column=2,padx=5,sticky= W)
        
        self.msg=''
        self.Label_3=Label(btn_frame,text=self.msg,font=('times new roman',18,'bold'),fg="#a43a8e",bg='white')
        self.Label_3.grid(row=2,column=1,padx=5,sticky=W)
        
        
    def enter_func(self,event):
        self.send.invoke()
        
    def clear(self):
        self.text.delete('1.0',END)
        self.enter_var.set('')
        self.text.insert(END,'\n\n'+"""Assistant: Hi How Can I Help You ?
        You Can Type Any Of The Following Number:
        1) %s
        2) %s
        3) %s
        4) %s
        5) %s
        6) %s
        """ % (self.q1,self.q2,self.q3,self.q4,self.q5,self.q6)) 
        
    def exit(self):
        self.assistantroot.destroy()
        
    # def checking_text(self,text):
    #     sc1,sc2,sc3,sc4,sc5,sc6=0,0,0,0,0,0
    #     questions=[self.q1,self.q2,self.q3,self.q4,self.q5,self.q6]
    #     for index in questions:
    #         if index=="How to use application ?":
    #             for i in text:
    #                 j=0
    #                 if i==index[j]:
    #                     sc1+=1
                        
            
        
    def send(self):
        entered_text=self.entry.get()
        entered_text=entered_text.lower()
        send='\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)
        
        if(entered_text==''):
            self.msg='Please Type Something'
            self.Label_3.config(text=self.msg,fg='red')
        else:
            self.msg=''
            self.Label_3.config(text=self.msg,fg='red')
            
            if(entered_text=='hello'):
                self.text.insert(END,'\n\n'+'Assistant: HI !')
            elif(entered_text=="1" or entered_text=="how to use application ?"):
                self.text.insert(END,'\n\n'+"""Assistant:
                You can perform different things by pressing differenet buttons,
                the interface is easy to understand! if you still find it difficult
                then take a help from senior or contact the support!!
                """)
            elif(entered_text=="2" or entered_text=="how to mark attendance ?"):
                self.text.insert(END,'\n\n'+"""Assistant:
                you can mark by facial recognition as well as manually
                
                1) For marking attendanace by facal recognition click onto
                " Mark Attendance " button and the apllication will mark
                your attendance. but don't forget to select the file for marking attendace.
                
                2) For marking attendance manually click onto the attendance button,
                but manual attendace only allows you to update the attendance already
                marked by facial recognition!
                """)
            elif(entered_text=="3" or entered_text=="how to add student's details ?"):
                self.text.insert(END,'\n\n'+"""Assistant:
                You can add or remove students details by clicking onto the student details 
                button the appearing window will have all the optional data and buttons 
                needed for adding or removing a student.
                NOTE: Keep in mind! for facail recognition photo samples of a student are 
                compulsory.
                """)
            elif(entered_text=="4" or entered_text=="how to train model for marking attendance ?"):
                self.text.insert(END,'\n\n'+"""Assistant:
                By simply clicking onto the train model button one can train a model for
                every student's facial recognition attendance marking.
                NOTE: if model is not being trained after clicking the button then
                contact the support please.
                """)
            elif(entered_text=="5" or entered_text=="how to manually mark attendance ?"):
                self.text.insert(END,'\n\n'+"""Assistant:
                You can't mark attendance manually but you can modify it or export it to
                somewhere else by clicking onto the "Attendance" button.
                NOTE: If you want to mark manual attendance then you can do that on
                the .csv file of the attendace by opening it in operating system's
                directory.
                """)
            elif(entered_text=="6" or entered_text=="how to contact support ?"):
                self.text.insert(END,'\n\n'+"""Assistant:
                You Can find all the information about the support by clicking onto the
                "Support" button. 
                """)
            else:
                self.text.insert(END,'\n\n'+"""Assistant:
                Sorry either you have typed wrong number or your question is irrelevant
                I can only answer queations related to the application,if your question is
                related to the application and I cannot get it so you can try above given 
                questions, answers to those questions might help you.
                NOTE: If you're query isn't cleared after using the above given questions' 
                answers then please contact the support for further clarification.
                """)
        self.enter_var.set('')
        
        


        
if __name__ == "__main__":
    root=Tk()
    obj=Assistant(root)
    root.mainloop()