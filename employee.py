from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
 
class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Employee Management System')
        lbl_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman',37,'bold'),fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=1530,height=50)
        #logo
        img_logo=Image.open('college_images/emp.png')
        img_logo=img_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=270,y=0,width=50,height=50)
        #Image Frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=160)

        #1st
        img_1=Image.open('college_images/emp5.jpg')
        img_1=img_1.resize((540,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img_1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=160)

        #img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        #img_frame.place(x=0,y=50,width=1530,height=160)

        #2nd

        img_2=Image.open('college_images/emp2.png')
        img_2=img_2.resize((540,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img_2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=540,y=0,width=540,height=160)

        #img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        #img_frame.place(x=0,y=50,width=1530,height=160)

        #3rd

        img_3=Image.open('college_images/nameofimage.jpg')
        img_3=img_3.resize((540,160),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img_3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=1000,y=0,width=540,height=160)

        #Main Frame

        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=220,width=1500,height=560)

        #upper Frame

        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information',font=('times new roman',15,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1480,height=270)

        #down Frame

        #down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information Table',font=('times new roman',15,'bold'),fg='red')
        #down_frame.place(x=10,y=280,width=1480,height=270)

         #Labels and Entry fields

        lbl_dep=Label(upper_frame,text='Department',font=('arial',11,'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(upper_frame,font=('arial',12,'bold'),width=18,state='readonly')
        combo_dep['value']=('Select Department','HR','Software Engineer','Manager')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #Name
        
        lbl_name=Label(upper_frame,font=('arial',12,'bold'),text='Name',bg='white')
        lbl_name.grid(row=0,column=2,sticky=W,padx=2,pady=7)
        txt_name=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_name.grid(row=0,column=3,padx=2,pady=7)
        
        #lbl designation
          
        lbl_Designation=Label(upper_frame,font=('arial',12,'bold'),text='Designation',bg='white')
        lbl_Designation.grid(row=1,column=0,sticky=W,padx=2,pady=7)
          
        txt_Designation=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_Designation.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        #email
        
        lbl_email=Label(upper_frame,font=('arial',12,'bold'),text='Email',bg='white')
        lbl_email.grid(row=1,column=2,sticky=W,padx=2,pady=7)
          
        txt_email=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_email.grid(row=1,column=3,sticky=W,padx=2,pady=7)

        #address

        lbl_address=Label(upper_frame,font=('arial',12,'bold'),text='Address',bg='white')
        lbl_address.grid(row=2,column=0,sticky=W,padx=2,pady=7)
          
        txt_address=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_address.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        # married

        lbl_married=Label(upper_frame,text='Married Status',font=('arial',11,'bold'),bg='white')
        lbl_married.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        combo_married=ttk.Combobox(upper_frame,font=('arial',12,'bold'),width=18,state='readonly')
        combo_married['value']=('Select','Married','Unmarried')
        combo_married.current(0)
        combo_married.grid(row=2,column=3,sticky=W,padx=2,pady=7)

        #dob

        lbl_dob=Label(upper_frame,font=('arial',12,'bold'),text='DOB',bg='white')
        lbl_dob.grid(row=3,column=0,sticky=W,padx=2,pady=7)
          
        txt_dob=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_dob.grid(row=3,column=1,sticky=W,padx=2,pady=7)

        #doj

        lbl_doj=Label(upper_frame,font=('arial',12,'bold'),text='DOJ',bg='white')
        lbl_doj.grid(row=3,column=2,sticky=W,padx=2,pady=7)
          
        txt_doj=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_doj.grid(row=3,column=3,sticky=W,padx=2,pady=7)
       
       # id proof
         
        ##lbl_ID=Label(upper_frame,text='ID Proof',font=('arial',11,'bold'),bg='white')
        ##lbl_ID.grid(row=4,column=0,padx=2,sticky=W)

        combo_ID=ttk.Combobox(upper_frame,font=('arial',12,'bold'),width=17,state='readonly')
        combo_ID['value']=('Select ID Proof','ADHAR CARD','DRIVING LICENSE','VOTER ID','PAN CARD','PASSPORT')
        combo_ID.current(0)
        combo_ID.grid(row=4,column=0,padx=2,pady=10,sticky=W)
        txt_ID=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_ID.grid(row=4,column=1,sticky=W,padx=2,pady=7)

       #gender
        
        lbl_GENDER=Label(upper_frame,text='Gender',font=('arial',11,'bold'),bg='white')
        lbl_GENDER.grid(row=4,column=2,padx=2,pady=7,sticky=W)

        combo_GENDER=ttk.Combobox(upper_frame,font=('arial',12,'bold'),width=18,state='readonly')
        combo_GENDER['value']=('Select','Male','Female')
        combo_GENDER.current(0)
        combo_GENDER.grid(row=4,column=3,padx=2,pady=7,sticky=W)
    
       #phone

        lbl_phone=Label(upper_frame,font=('arial',12,'bold'),text='Phone No.',bg='white')
        lbl_phone.grid(row=0,column=4,sticky=W,padx=2,pady=7)
          
        txt_phone=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_phone.grid(row=0,column=5,sticky=W,padx=2,pady=7)

       #country

        lbl_country=Label(upper_frame,font=('arial',12,'bold'),text='Country',bg='white')
        lbl_country.grid(row=1,column=4,sticky=W,padx=2,pady=7)
          
        txt_country=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_country.grid(row=1,column=5,sticky=W,padx=2,pady=7)

       #salary
       
        lbl_salary=Label(upper_frame,font=('arial',12,'bold'),text='Salary(CTC)',bg='white')
        lbl_salary.grid(row=2,column=4,sticky=W,padx=2,pady=7)
          
        txt_salary=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_salary.grid(row=2,column=5,sticky=W,padx=2,pady=7)


      #down Frame

        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information Table',font=('times new roman',15,'bold'),fg='red')
        down_frame.place(x=10,y=280,width=1480,height=270)

      # image

        img_emp=Image.open('college_images/employeedp.jpg')
        img_emp=img_emp.resize((200,220),Image.ANTIALIAS)
        self.photo4=ImageTk.PhotoImage(img_emp)

        self.img_emp=Label(upper_frame,image=self.photo4)
        self.img_emp.place(x=980,y=0,width=170,height=200)

    

       #button frame

        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1160,y=10,width=160,height=220)

        btn_add=Button(button_frame,text='SAVE',font=('arial',12,'bold'),width=14,fg='black',bg='light blue')
        btn_add.grid(row=0,column=0,padx=1,pady=5)

        btn_update=Button(button_frame,text='UPDATE',font=('arial',12,'bold'),width=14,fg='black',bg='light blue')
        btn_update.grid(row=1,column=0,padx=1,pady=5)

        btn_delete=Button(button_frame,text='DELETE',font=('arial',12,'bold'),width=14,fg='black',bg='light blue')
        btn_delete.grid(row=2,column=0,padx=1,pady=5)

        btn_reset=Button(button_frame,text='RESET',font=('arial',12,'bold'),width=14,fg='black',bg='light blue')
        btn_reset.grid(row=3,column=0,padx=1,pady=5)


       # search frame

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text='Search Employee Information',font=('times new roman',15,'bold'),fg='blue')
        search_frame.place(x=0,y=0,width=1470,height=60)

        lbl_search=Label(search_frame,font=('arial',12,'bold'),text='Search By',fg='black',bg='white')
        lbl_search.grid(row=0,column=0,sticky=W,padx=5)

    
       #search
         
        self.var_com_search=StringVar()
        combo_search=ttk.Combobox(search_frame,font=('arial',12,'bold'),width=18,state='readonly')
        combo_search['value']=('Select Option','Phone','ID Proof')
        combo_search.current(0)
        #combo_ID.grid(row=4,column=0,padx=2,pady=10,sticky=W)
        #txt_search=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        combo_search.grid(row=0,column=1,sticky=W,padx=5)

        txt_search=ttk.Entry(search_frame,width=22,font=('arial',11,'bold'))
        txt_search.grid(row=0,column=2,sticky=W,padx=5)

        btn_search=Button(search_frame,text='Search',font=('arial',11,'bold'),width=14,bg='light blue')
        btn_search.grid(row=0,column=3,padx=5)

        btn_showall=Button(search_frame,text='Show All',font=('arial',11,'bold'),width=14,bg='light blue')
        btn_showall.grid(row=0,column=4,padx=5)


        ########employee table######
        
           
        table_frame=Frame(down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=('dep','name','degi','email','married','dob','doj','idproof','gender','phone','country','salary',),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)
        
        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('degi',text='Designation')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('married',text='Married Status')
        self.employee_table.heading('dob',text='DOB')
        self.employee_table.heading('doj',text='DOJ')
        self.employee_table.heading('idproof',text='Id Proof')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('phone',text='Phone')
        self.employee_table.heading('country',text='Country')
        self.employee_table.heading('salary',text='Salary')

        self.employee_table['show']='headings'
        self.employee_table.column('dep',width=70)
        self.employee_table.column('name',width=70)
        self.employee_table.column('degi',width=70)
        self.employee_table.column('email',width=70)
        self.employee_table.column('married',width=70)
        self.employee_table.column('dob',width=70)
        self.employee_table.column('doj',width=70)
        self.employee_table.column('idproof',width=70)
        self.employee_table.column('gender',width=70)
        self.employee_table.column('phone',width=70)
        self.employee_table.column('country',width=70)
        self.employee_table.column('salary',width=70)

        self.employee_table.pack(fill=BOTH,expand=1)











if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()

    