from cProfile import label
from cgitb import text
from itertools import product
from re import L
import tempfile
from tkinter import *
from tkinter import ttk
from tkinter import font
from tokenize import String
from PIL import Image,ImageTk
import random,os
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x800+0+0")
        self.root.title("billing software")


        #==============varaible===============
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.total=StringVar()


        #product catogry list
        self.Category=["Select Option","Clothing","LifeStyle","Mobiles","Laptop"]
        
        #subcat clothing
        self.SubCatClothing=["Pant","T-Shirt","Shirt"]
        self.pant=["Levis","Mukti","Spykar"]
        self.price_levis=5000
        self.price_mukti=3000
        self.price_spykar=1700

        self.T_Shirt=['Polo','Roadstar','Jackson']
        self.price_polo=2000
        self.price_Roadstar=4000
        self.price_Jackson=6000

        self.Shirt=['Peter England','Louis Phillips','Park Avenu']
        self.price_Peter=2100
        self.price_Louis=2700
        self.price_park=1740

        #SubCatlife style
        self.SubCatLifeStyle=["Bath soap","Face Cream","Hair Oil"]
        self.Bath_soap=["Lifeboy","Lux","Santoor","Dove"]
        self.price_life=20
        self.price_lux=20
        self.price_santoor=20
        self.price_dove=30

        self.Face_cream=["FairLovely","Ponds","Olay","Garnier"]
        self.price_fair=50
        self.price_ponds=30
        self.price_olay=30
        self.price_garnier=40

        self.Hair_oil=["Parachute","Jashmin","Bajaj"]
        self.price_para=25
        self.price_jashmin=50
        self.price_bajaj=30

        #subcat mobiles
        self.SubCatMobiles=["Iphone","Samsung","Xiome","Realme","One+"]
        self.Iphone=["Iphone_X","Iphone_11","Iphone_12"]
        self.price_ix=40000
        self.price_i11=60000
        self.price_i12=850000

        self.Samsung=["Samsung M16","Samsung M12","Samsung M21"]
        self.price_sm16=16000
        self.price_sm12=12000
        self.price_sm21=18000

        self.Xiome=["Redme-11","Readme-12","ReadmePro"]
        self.price_r11=11000
        self.price_r12=12000
        self.price_rpro=9000

        self.RealMe=["RealMe 12","RealMe 13","RealMe Pro"]
        self.price_rel12=25000
        self.price_rel13=22000
        self.price_rel13=33000
        self.price_relpro=35000

        self.OnePlus=["OnePlus1","OnePlus2","OnePlus3"]
        self.price_one1=45000
        self.price_one12=60000
        self.price_one3=34800
        
        
        self.SubCatLaptops=["Dell","HP","Lenove","Avita"]
        self.Laptop=["I3","I4","I6"]
        self.price_i3=40000
        self.price_i4=60000
        self.price_i6=850000





        #self.SubCatLifeStyle=["Bath Soap","Creame","Hair Oil"]
        #self.SubCatMobiles=["Iphone","Samsung","Xiome","Realme","One+"]

        #image1
        img=Image.open("D:/software-bill/images/img/supermarket.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl__img=Label(self.root,image=self.photoimg)
        lbl__img.place(x=0,y=0,width=500,height=130)

        #image2
        img_1=Image.open("D:/software-bill/images/img/sm.jpg")
        img_1=img_1.resize((500,130),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        lbl__img_1=Label(self.root,image=self.photoimg_1)
        lbl__img_1.place(x=500,y=0,width=500,height=130)


         #image3
        img_2=Image.open("D:/software-bill/images/img/girl1.jpg")
        img_2=img_2.resize((500,130),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lbl__img_2=Label(self.root,image=self.photoimg_2)
        lbl__img_2.place(x=1000,y=0,width=520,height=130)

        #lbl_title=Label(self.root,text="BILLING SOFTWARE USING PYTHON",font=("times new roman",35,"bold"),bg="white",fg="red")
        #lbl_title.place(x=0,y=130,width=1530,height=45)

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=10,y=150,width=1530,height=620)

        #customer LabelFramw
        Cust_Frame=LabelFrame(Main_Frame,text="customer",font=("times in roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=310,height=140)

        self.lbl_mob=Label(Cust_Frame,text="Mobile no.",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phone,font=("times new roman",10,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1) 

        self.lblCustName=Label(Cust_Frame,text="customer name",font=("times new roman",12,"bold"),bg="white")
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.textCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("times new roman",10,"bold"),width=24)
        self.textCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2) 

        self.lblEmail=Label(Cust_Frame,text="Email id",font=("times new roman",12,"bold"),bg="white")
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.textEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("times new roman",10,"bold"),width=24)
        self.textEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2) 

        #Product LabelFrame

        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=330,y=5,width=620,height=140)
        

    
        self.lblCategory=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Select categories",bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=("arial",10,"bold"),width=24,state="readonly")
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.current(0)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

        
        
        #sub category
        self.lblSubCategory=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Sub categories",bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.ComboSubCategory=ttk.Combobox(Product_Frame,value=[""],font=("arial",10,"bold"),width=24,state="readonly")
        self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)
        
        
        #product name
        self.lblProduct=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Product Name",bd=4)
        self.lblProduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.product,font=("arial",10,"bold"),width=24,state="readonly")
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)
        
        #price
        self.lblPrice=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Price",bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.ComboPrice=ttk.Combobox(Product_Frame,textvariable=self.prices,state="readonly",font=('arial',10,'bold'),width=24)
        self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)
       
        #Qty
        self.lblQty=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Qty",bd=4)
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=("arial",10,"bold"),width=26)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)

        #middle frame
        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=150,width=900,height=340)

         #image2
        img12=Image.open("D:/software-bill/images/img/supermarket.jpg")
        img12=img12.resize((490,340),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        lbl__img12=Label(MiddleFrame,image=self.photoimg12)
        lbl__img12.place(x=0,y=0,width=490,height=340)

         #image3
        img_13=Image.open("D:/software-bill/images/img/good.jpg")
        img_13=img_13.resize((490,340),Image.ANTIALIAS)
        self.photoimg_13=ImageTk.PhotoImage(img_13)

        lbl__img_13=Label(MiddleFrame,image=self.photoimg_13)
        lbl__img_13.place(x=490,y=0,width=500,height=340)

        
        #search
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=950,y=15,width=600,height=40)

        self.lblBill=Label(Search_Frame,text="Bill Number",font=("arial",12,"bold"),fg="white",bg="red")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("arial",10,"bold"),width=24)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=("arial",10,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)





        #RightFrame bill areia
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Aria",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=940,y=47,width=440,height=380)


        scroll_x=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_x.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_x.pack(side=LEFT,fill=Y)
        scroll_x.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)


        #bill counter LabelFrame
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=430,width=1520,height=150)

         #sub total
        self.lblSubtotal=Label(Bottom_Frame,font=("arial",12,"bold"),bg="white",text="sub total",bd=2)
        self.lblSubtotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.EntrySubtotal=ttk.Entry(Bottom_Frame,font=("arial",10,"bold"),width=26)
        self.EntrySubtotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        #Gov tax
      #  self.lblGovTax=Label(Bottom_Frame,font=("arial",12,"bold"),bg="brown",text="Gov tax",bd=2)
       # self.lblGovTax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        #self.EntryGovTax=ttk.Entry(Bottom_Frame,font=("arial",10,"bold"),width=26)
        #self.EntryGovTax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        #total
        self.lblTotal=Label(Bottom_Frame,font=("arial",12,"bold"),bg="white",text="Total",bd=2)
        self.lblTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.EntryTotal=ttk.Entry(Bottom_Frame,font=("arial",10,"bold"),width=26)
        self.EntryTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #button frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,text="Add To Cart",height=2,font=("arial",10,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.Btngenerate_bill=Button(Btn_Frame,command=self.gen_bill,text="Generate Bill",height=2,font=("arial",10,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.Btngenerate_bill.grid(row=0,column=1)

        self.Btnsavebill=Button(Btn_Frame,command=self.save_bill,text="Save Bill",height=2,font=("arial",10,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.Btnsavebill.grid(row=0,column=2)

        self.Btnprint=Button(Btn_Frame,text="Print",height=2,font=("arial",10,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.Btnprint.grid(row=0,column=3)

        self.Btnclear=Button(Btn_Frame,command=self.clear,text="Clear",height=2,font=("arial",10,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.Btnclear.grid(row=0,column=4)

        self.Btnexit=Button(Btn_Frame,command=self.root.destroy,text="Exit",height=2,font=("arial",10,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.Btnexit.grid(row=0,column=5)
        
        self.welcome()

        self.l=[]
    #================function decelartion===============
    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please select the product name")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))


    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add To Cart")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n=========================================")
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            #self.textarea.insert(END,f"\n Tax Amount:\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n=========================================")

    def save_bill(self):
        op=messagebox.askyesno("Save bill","Do you want to save the bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            op=messagebox.showinfo("Save bill",f"bill No:{self.bill_no.get()} saved sucessfully")
            f1.close()


    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp(".txt")
        open(filename,"w").write(q)
        os.startfile(filename,"print")


    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split(".")[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=="no":
            messagebox.showerror("Error","Invalid bill number")

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_phone.set("")
        self.c_name.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.qty.set(0)
        self.prices.set(0)
        self.l=[0]
        self.sub_total.set("")
        self.total.set("")
        self.welcome()

   

    
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t Welcome To The Mini Mall")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phone.get()}")
        self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")

        self.textarea.insert(END,"\n==========================================")
        self.textarea.insert(END,f"\n Product\t\tQTY\t\tPrice")
        self.textarea.insert(END,"\n===========================================\n")
    
    
    
    def Categories(self,event=""):
        if self.Combo_Category.get()=="Clothing":
            self.ComboSubCategory.config(value=self.SubCatClothing)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="LifeStyle":
            self.ComboSubCategory.config(value=self.SubCatLifeStyle)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Mobiles":
            self.ComboSubCategory.config(value=self.SubCatMobiles)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Laptop":
            self.ComboSubCategory.config(value=self.SubCatLaptops)
            self.ComboSubCategory.current(0)

    def Product_add(self,event=""):
        if self.ComboSubCategory.get()=="Pant":
            self.ComboProduct.config(values=self.pant)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="T-Shirt":
            self.ComboProduct.config(values=self.T_Shirt)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Shirt":
            self.ComboProduct.config(values=self.Shirt)
            self.ComboProduct.current(0)

        #lifestyle
        if self.ComboSubCategory.get()=="Bath soap":
            self.ComboProduct.config(value=self.Bath_soap)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Face Cream ":
            self.ComboProduct.config(value=self.face_creams)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Hair Oil":
            self.ComboProduct.config(value=self.Hair_oil)
            self.ComboProduct.current(0)

        #mobiles
       
        if self.ComboSubCategory.get()=="Iphone":
            self.ComboProduct.config(value=self.Iphone)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Samsung":
            self.ComboProduct.config(value=self.Samsung)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Xiome":
            self.ComboProduct.config(value=self.Xiome)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="RealMe":
            self.ComboProduct.config(value=self.RealMe)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="OnePlus":
            self.ComboProduct.config(value=self.OnePlus)
            self.ComboProduct.current(0)

        #Laptop

        '''
        if self.ComboSubCategory.get()=="Dell":
            self.ComboProduct.config(value=self.Dell)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Hp":
            self.ComboProduct.config(value=self.Hp)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Xiome":
            self.ComboProduct.config(value=self.Xiome)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="RealMe":
            self.ComboProduct.config(value=self.RealMe)
            self.ComboProduct.current(0)
'''




    def price(self,event=""):
        #pant
        if self.ComboProduct.get()=="Levis":
            self.ComboPrice.config(value=self.price_levis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Mukti":
            self.ComboPrice.config(value=self.price_mukti)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Spykar":
            self.ComboPrice.config(value=self.price_spykar)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #T-shirt
        if self.ComboProduct.get()=="Polo":
            self.ComboPrice.config(value=self.price_polo)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Roadstar":
            self.ComboPrice.config(value=self.price_Roadstar)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Jackson":
            self.ComboPrice.config(value=self.price_Jackson)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Shirt
        if self.ComboProduct.get()=="Peter England":
            self.ComboPrice.config(value=self.price_Peter)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Louis Phillips":
            self.ComboPrice.config(value=self.price_Louis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Park Avenu":
            self.ComboPrice.config(value=self.price_park)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Lifestyle
        if self.ComboProduct.get()=="Lifeboy":
            self.ComboPrice.config(value=self.price_life)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Lux":
            self.ComboPrice.config(value=self.price_lux)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Santoor":
            self.ComboPrice.config(value=self.price_santoor)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Dove":
            self.ComboPrice.config(value=self.price_dove)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="FairLovely":
            self.ComboPrice.config(value=self.price_fair)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Ponds":
            self.ComboPrice.config(value=self.price_ponds)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Olay":
            self.ComboPrice.config(value=self.price_olay)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Parachute":
            self.ComboPrice.config(value=self.price_para)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Jashmin":
            self.ComboPrice.config(value=self.price_jashmin)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Bajaj":
            self.ComboPrice.config(value=self.price_bajaj)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Mobiles
        if self.ComboProduct.get()=="Iphone_X":
            self.ComboPrice.config(value=self.price_ix)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Iphone_11":
            self.ComboPrice.config(value=self.price_i11)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Iphone_12":
            self.ComboPrice.config(value=self.price_i12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Samsung M16":
            self.ComboPrice.config(value=self.price_sm16)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Samsung M12":
            self.ComboPrice.config(value=self.price_sm12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Samsung M21":
            self.ComboPrice.config(value=self.price_sm21)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Redme-11":
            self.ComboPrice.config(value=self.price_r11)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Readme-12":
            self.ComboPrice.config(value=self.price_r12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="ReadmePro":
            self.ComboPrice.config(value=self.price_rpro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="RealMe 12":
            self.ComboPrice.config(value=self.price_rel12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="RealMe 13":
            self.ComboPrice.config(value=self.price_rel13)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="RealMePro":
            self.ComboPrice.config(value=self.price_relpros)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="OnePlus1":
            self.ComboPrice.config(value=self.price_one1)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="OnePlus12":
            self.ComboPrice.config(value=self.price_one12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="OnePlus3":
            self.ComboPrice.config(value=self.price_one3)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="RealMePro":
            self.ComboPrice.config(value=self.price_relpros)
            self.ComboPrice.current(0)
            self.qty.set(1)













if __name__== '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()