from atexit import register
from cgitb import text
from pydoc import plain
from tkinter import*
from tkinter import*
from tkinter import ttk
from tkinter import font
from tokenize import String
from turtle import heading, width
from PIL import Image,ImageTk
from tkinter import messagebox
import main



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #varaible
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()



        #bg image
        self.bg1=ImageTk.PhotoImage(file="D:/photopix/p9.jpg")

        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=100,y=150,height=510,width=490)

        #main frame
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=150,width=800,height=510)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="dark green")
        register_lbl.place(x=40,y=40)

        #label and entry

        #row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)

        #row 2
        contact=Label(frame,text="Contact Number",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)

        #row 3
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","your birth name","your pet name","your email id")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new romann",15))
        self.txt_security.place(x=370,y=270,width=250)

        #row 4
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #checkbutton
        self.var_check=IntVar
        self.checkbtn=checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree the terms & condition",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)

        #button
        img=Image.open("D:/aa/login1.png")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,borderwidth=0,cursor="hand2",font=("times new roman",12,"bold"))
        b1.place(x=10,y=420,width=300)
        
      
       

        img1=Image.open("D:/aa/rr.png")
        img1=img1.resize((250,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=330,y=420,width=200)

        #function decelaration
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","all fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password and confirm password must be same")
        #elif self.var_check.get()==0:
            #messagebox.showerror("Error","please agree our terms and condition")
        else:
            messagebox.showinfo("Sucess","Welcome")
            
            obj=main.Bill_App(root)






if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()