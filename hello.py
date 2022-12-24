from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import main

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x500+0+0")


        self.var_name=StringVar()
        self.var_pasw=StringVar()

       
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open("D:/aa/login.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=90,height=90)

        get_str=Label(frame,text="Login Here",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #label1
        username=lbl=Label(frame,text="User name",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,textvariable=self.var_name,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        #label2
        password=lbl=Label(frame,text="password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,textvariable=self.var_pasw,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #loginbutton
        loginbtn=Button(frame,text="Login",command=self.login_data,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activebackground="red",activeforeground="white")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #registerbutton
        registerbtn=Button(frame,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activebackground="black",activeforeground="white")
        registerbtn.place(x=15,y=350,width=160)

        #forgetbutton
        forgetbtn=Button(frame,text="Forget password",font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activebackground="black",activeforeground="white")
        forgetbtn.place(x=10,y=370,width=160)


    def login_data(self):
        if self.var_name.get()=="" or self.var_pasw.get()=="":
            messagebox.showerror("Error","all fields are required")
        elif self.var_pasw.get()=="":
            messagebox.showerror("Error","Please enter the password")

        else:
            messagebox.showinfo("Sucess","Welcome")

            

            obj=main.Bill_App(root)
            
            
        




if __name__=="__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()