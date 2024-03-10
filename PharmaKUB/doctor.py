from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import sys

    
#---------------------------------- HOSPITAL ----------------------------------------------



class Doctor:
    def __init__(self,root):

        # ---------------------- HEAD FRAME  --------------------------
        self.root=root
        self.root.title("Doctor PharmaKUB ") 
        self.root.geometry('1540x740+0+0')



        self.NameofTablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NoOftablets = StringVar()
        self.Lot = StringVar()
        self.issuedate = StringVar()
        self.Expdate = StringVar()
        self.DailyDose = StringVar()
        self.txtFind = StringVar()
        self.condition = StringVar()
        # ---------------------- TOPTITLE FRAME -------------------------

        toptitle = Label(self.root,bd=15,relief=RIDGE,text="+ Doctor ",fg="#fd6236",bg="white",font=("kanit",45,"bold"))
        toptitle.pack(side=TOP , fill = BOTH)

        # ---------------------- INPUT FARME ------------------------

        InputFrame  = Frame(self.root,bd=15,relief = RIDGE)
        InputFrame.place(x=0,y=90,width=1440,height=315)

        # ---------------------- INPUT LEFT ------------------------
        

        InputframeLeft = LabelFrame(InputFrame,bd=10,relief=RIDGE,padx=10,font=("kanit",14,"bold"),text="รายละเอียดยารักษา")
        InputframeLeft.place(x=5,y=1,width=950,height=280)



        lblNameTablet = Label(InputframeLeft,text="ชื่อประเภทยา :",font=("kanit",18,"bold"),padx=2)
        lblNameTablet.grid(row = 0 ,column=0,sticky=W)

        comNametablet = ttk.Combobox(InputframeLeft,textvariable=self.NameofTablets,font=("kanit",16,"bold"),width=25)

        comNametablet["values"]=("ประเภทยา","Moderna","Pfizer","Thai Vaccine","Astrazeneca","Sinovac","Sinopharm")
        comNametablet.current(0)
        comNametablet.grid(row = 0 ,column=1)



        lblref = Label(InputframeLeft,font=("kanit",18,"bold"),text="เลขอ้างอิง :",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref = Entry(InputframeLeft,font=("kanit",16,"bold"),textvariable=self.ref,width=28)
        txtref.grid(row=1,column=1)

        lblDose = Label(InputframeLeft,font=("kanit",18,"bold"),text="เลขโดส :",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose = Entry(InputframeLeft,font=("kanit",16,"bold"),textvariable=self.Dose,width=28)
        txtDose.grid(row=2,column=1)

        lblNoOftablets = Label(InputframeLeft,font=("kanit",18,"bold"),text="หมายเลขที่ยา :",padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets = Entry(InputframeLeft,font=("kanit",16,"bold"),textvariable=self.NoOftablets,width=28)
        txtNoOftablets.grid(row=3,column=1)




        lblLot = Label(InputframeLeft,font=("kanit",18,"bold"),text="ล็อตที่ :",padx=5,pady=6)
        lblLot.grid(row=0,column=2,sticky=W,ipady= 10)
        txtLot = Entry(InputframeLeft,font=("kanit",16,"bold"),textvariable=self.Lot,width=30)
        txtLot.grid(row=0,column=3)

        lblissuedate = Label(InputframeLeft,font=("kanit",18,"bold"),text="วันที่ออก :",padx=2,pady=6)
        lblissuedate.grid(row=1,column=2,sticky=W,ipady= 10)
        txtissuedate = Entry(InputframeLeft,font=("kanit",16,"bold"),textvariable=self.issuedate,width=30)
        txtissuedate.grid(row=1,column=3)

        lblExpdate = Label(InputframeLeft,font=("kanit",18,"bold"),text="วันหมดอายุ :",padx=2,pady=6)
        lblExpdate.grid(row=2,column=2,sticky=W,ipady= 10)
        txtExpdate = Entry(InputframeLeft,font=("kanit",16,"bold"),textvariable=self.Expdate,width=30)
        txtExpdate.grid(row=2,column=3)

        lblDailyDose = Label(InputframeLeft,font=("kanit",18,"bold"),text="ปริมาณ/วัน :",padx=2,pady=4)
        lblDailyDose.grid(row=3,column=2,sticky=W,ipady= 10)
        txtDailyDose = Entry(InputframeLeft,font=("kanit",16,"bold"),textvariable=self.DailyDose,width=30)
        txtDailyDose.grid(row=3,column=3)



        # ---------------------- INPUT RIGHT ----------------------


        InputframeRight = LabelFrame(InputFrame,bd=10,relief=RIDGE,padx=10,font=("kanit",14,"bold"),text="ค้นหาเลขที่อ้างอิงยา")
        InputframeRight.place(x=960,y=1,width=445,height=280)


        lblcondition = Label(InputframeRight,font=("kanit",15,"bold"),text="เลขที่ผู้ป่วย :")
        lblcondition.grid(row=0,column=0,sticky=W,ipady = 25 ,ipadx=4)
        txtcondition = Entry(InputframeRight,font=("kanit",15,"bold"),textvariable=self.condition,width=21,state='disable',disabledbackground='#929292',disabledforeground='black')
        txtcondition.grid(row=0,column=1)


        lblFind = Label(InputframeRight,font=("kanit",15,"bold"),text="ตรวจสอบ ( Ref.No ) :")
        lblFind.grid(row=1,column=0,sticky=W,ipady = 25 ,ipadx=4)
        txtFind = Entry(InputframeRight,font=("kanit",15,"bold"),textvariable=self.txtFind,width=21)
        txtFind.grid(row=1,column=1)

        btnfind = Button(InputframeRight ,font=("kanit",17,"bold"),text="ค้นหา",fg="black",width=15,height=2 ,command=self.CheckID)
        btnfind.grid(row = 4 , sticky=N , columnspan= 3 , pady=10)



        # ----------------------- BUTTON FRAME -----------------------


        Buttonframe = Frame(self.root,bd=15,relief=RIDGE)
        Buttonframe.place(x=1,y=410,width=1440,height=105)

        btnInsertdata = Button(Buttonframe,text="Insert Data",bg="black",fg="green",font=("kanit",15,"bold"),width=29,height=3,pady = 6,command=self.InsertData)
        btnInsertdata.grid(row=0,column= 0)

        btnUpdate = Button(Buttonframe,text="Update",bg="black",fg="blue",font=("kanit",15,"bold"),width=29,height=3,padx=0,pady = 6,command=self.iUpdate)
        btnUpdate.grid(row=0,column= 1)

        btnClear = Button(Buttonframe,text="Clear",bg="black",fg="red",font=("kanit",15,"bold"),width=29,height=3,padx=0,pady = 6,command=self.iClear)
        btnClear.grid(row=0,column= 2)

        btnDelete = Button(Buttonframe,text="Exit",bg="black",fg="red",font=("kanit",15,"bold"),width=29,height=3,padx=0,pady = 6,command=self.iExit)
        btnDelete.grid(row=0,column= 3)


        # --------------------- DETAIL FRAME -----------------------

        Detailsframe = Frame(self.root,bd=15,relief=RIDGE)
        Detailsframe.place(x=1,y=515,width=1440,height=385)

        # ----------------------------- DETAIL --------------------------


        scroll_x = ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.Hospital_table = ttk.Treeview(Detailsframe,columns=("PatientID","NameofTablets","ref","Dose","NoOftablets","Lot","issuedate","Expdate","Dailydose"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x = ttk.Scrollbar(command=self.Hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.Hospital_table.yview)

        self.Hospital_table.heading("PatientID",text="เลขประจำตัวผู้ป่วย")
        self.Hospital_table.heading("NameofTablets",text="ชื่อประเภทยา")
        self.Hospital_table.heading("ref",text="เลขอ้างอิง :")
        self.Hospital_table.heading("Dose",text="เลขโดส")
        self.Hospital_table.heading("NoOftablets",text="หมายเลขที่ยา")
        self.Hospital_table.heading("Lot",text="ล็อตที่")
        self.Hospital_table.heading("issuedate",text="วันที่ออก")
        self.Hospital_table.heading("Expdate",text="วันหมดอายุ")
        self.Hospital_table.heading("Dailydose",text="ปริมาณ/วัน")

        self.Hospital_table["show"]="headings"


        self.Hospital_table.column("PatientID",width=95)
        self.Hospital_table.column("NameofTablets",width=95)
        self.Hospital_table.column("ref",width=95)
        self.Hospital_table.column("Dose",width=95)
        self.Hospital_table.column("NoOftablets",width=95)
        self.Hospital_table.column("Lot",width=95)
        self.Hospital_table.column("issuedate",width=95)
        self.Hospital_table.column("Expdate",width=95)
        self.Hospital_table.column("Dailydose",width=95)

        self.Hospital_table.pack(fill=BOTH,expand=1)
        self.Hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fatch_data()


    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="0628082548Jai",database="hospital")
        my_cursor=conn.cursor()
        my_cursor.execute("select PatientID,NameofTablets,Reference_No,dose,NumberofTablets,Lot,issuedate,expdate,dailydose from hospital order by Reference_No ")
        rows = my_cursor.fetchall()
        if len(rows) != 0 :
            self.Hospital_table.delete(*self.Hospital_table.get_children())
            for i in (rows):
                self.Hospital_table.insert("",END,values = i )
            conn.commit()
        conn.close()



    def get_cursor(self,event=""):
        cursor_row = self.Hospital_table.focus()
        content = self.Hospital_table.item(cursor_row)
        row = content["values"]
        self.condition.set(row[0])
        self.NameofTablets.set(row[1])
        self.ref.set(row[2])
        self.Dose.set(row[3])
        self.NoOftablets.set(row[4])
        self.Lot.set(row[5])
        self.issuedate.set(row[6])
        self.Expdate.set(row[7])
        self.DailyDose.set(row[8])


    def iExit(self):
        iExit = messagebox.askyesno("คำเตือน","ต้องการออกจากโปรแกรม หรือไม่")
        if iExit > 0 :
            self.root.destroy()
            sys.exit()       

    def iClear(self):
        self.NameofTablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NoOftablets.set("")
        self.Lot.set("")
        self.issuedate.set("")
        self.Expdate.set("")
        self.DailyDose.set("")
        self.condition.set("")


        self.txtFind.set("")

    def iUpdate(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="0628082548Jai",database="hospital")
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital set NameofTablets = %s  , dose = %s , NumberofTablets = %s , Lot = %s , issuedate = %s , expdate = %s , dailydose = %s , Reference_No = %s where PatientID = %s " , (
  
                                                                                                    self.NameofTablets.get(),
                                                                                                    self.Dose.get(), 
                                                                                                    self.NoOftablets.get(),
                                                                                                    self.Lot.get(),
                                                                                                    self.issuedate.get(),
                                                                                                    self.Expdate.get(),
                                                                                                    self.DailyDose.get(),
                                                                                                    self.ref.get(),
                                                                                                    
                                                                                                    

                                                                                                    # Condition where ....
                                                                                                    self.condition.get()
                                                                                                    

                                                                                                    ))    
        conn.commit()  
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Success","ดำเนินการสำเร็จ \nอัปเดตข้อมูลแล้ว !!!")


    def CheckID(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="0628082548Jai",database="hospital") 
        my_cursor=conn.cursor()
        admin_table = 'hospital.hospital'
        query = f"select Reference_No from {admin_table} where Reference_No = (%s) " 
        value = self.txtFind.get()
        my_cursor.execute(query,(value,))
        ID_result  = my_cursor.fetchall()

        conn.commit()
        conn.close()

        if  len(ID_result) > 0 :
            messagebox.showinfo(title="ตรวจสอบสำเร็จ", message="เลขที่อ้างอิงอยู่ในระบบ !!!")

            """  self.window.withdraw()
            self.newWindow = Toplevel(self.window)
            self.newWindow.protocol("WM_DELETE_WINDOW", self.on_closing) """

        else:
            messagebox.showerror(title="ผิดพลาด", message="ไม่พบเลขที่อ้างอิง !!\n กรุณาเพิ่มข้อมูล ")





    def InsertData(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="0628082548Jai",database="hospital") 
        my_cursor=conn.cursor()
        admin_table = 'hospital.hospital'
        query = f"select Reference_No from {admin_table} where Reference_No = (%s) " 
        value = self.ref.get()
        my_cursor.execute(query,(value,))
        ID_result = my_cursor.fetchall()

        conn.commit()
        conn.close()

        if  len(ID_result) > 0 :

            messagebox.showerror("Error","กรอกข้อมูลไม่สำเร็จ !!! \nเลขที่อ้างอิงถูกใช้ไปแล้ว")

        elif self.ref.get()=="":

            messagebox.showerror("Error","กรอกข้อมูลไม่สำเร็จ !!! \nโปรดใส่เลขที่อ้างอิง")

        elif self.NoOftablets.get()=="" :

            messagebox.showerror("Error","กรอกข้อมูลไม่สำเร็จ !!! \nโปรดใส่เลขที่ยา")

        else :
            conn=mysql.connector.connect(host="localhost",username="root",password="0628082548Jai",database="hospital")
            my_cursor=conn.cursor()
            my_cursor.execute("update hospital set NameofTablets = %s , Reference_No = %s , dose = %s , NumberofTablets = %s , Lot = %s , issuedate = %s , expdate = %s , dailydose = %s where PatientID = %s  " , (
  
                                                                                                    self.NameofTablets.get(),
                                                                                                    self.ref.get(),
                                                                                                    self.Dose.get(), 
                                                                                                    self.NoOftablets.get(),
                                                                                                    self.Lot.get(),
                                                                                                    self.issuedate.get(),
                                                                                                    self.Expdate.get(),
                                                                                                    self.DailyDose.get(),
                                                                                                    

                                                                                                    # Condition where ....
                                                                                                    self.condition.get()
                                                                                                    

                                                                                                    ))   
           

            conn.commit()  
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Success","ดำเนินการสำเร็จ \nข้อมูลถูกบันทึกแล้ว !!!") 



        


























if __name__ == "__main__":

    root=Tk()
    ob=Doctor(root)
    root.mainloop()













































































#----------------------Update-----------------------

""" def iUpdate(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="0628082548Jai",database="hospital")
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital set NameofTablets = %s , dose = %s , NumberofTablets = %s , Lot = %s , issuedate = %s , expdate = %s , dailydose = %s , storage = %s , nhsnumber = %s , patientName = %s , DOB = %s , patientAddress = %s     where  Reference_No = %s " , (

                                                                                                    self.NameofTablets.get(),
                                                                                                    self.Dose.get(),
                                                                                                    self.NoOftablets.get(),
                                                                                                    self.Lot.get(),
                                                                                                    self.issuedate.get(),
                                                                                                    self.Expdate.get(),
                                                                                                    self.DailyDose.get(),  
                                                                                                    self.Storage.get(),      
                                                                                                    self.NHSNumber.get(),
                                                                                                    self.PatientName.get(), 
                                                                                                    self.DateofBirth.get(),
                                                                                                    self.PatienAddress.get(),

                                                                                                    # Condition where ....
                                                                                                    self.ref.get()

                                                                                                    ))
        
        conn.commit()  
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Success","ดำเนินการสำเร็จ \nอัปเดตข้อมูลแล้ว !!!")  """



#-----------------------Insert into Database----------------------------

""" def iPrescriptionData(self):
        if self.NameofTablets.get()=="" or self.ref.get()=="" :
            messagebox.showerror("Error","กรอกข้อมูลไม่สำเร็จ!!! \n โปรดใส่ข้อมูล")
        else :
            conn=mysql.connector.connect(host="localhost",username="root",password="0628082548Jai",database="hospital")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.NameofTablets.get(),
                                                                                                    self.ref.get(),
                                                                                                    self.Dose.get(),
                                                                                                    self.NoOftablets.get(),
                                                                                                    self.Lot.get(),
                                                                                                    self.issuedate.get(),
                                                                                                    self.Expdate.get(),
                                                                                                    self.DailyDose.get(),  
                                                                                                    self.NameofTablets.get(),      
                                                                                                    self.NHSNumber.get(),
                                                                                                    self.PatientName.get(), 
                                                                                                    self.DateofBirth.get(),
                                                                                                    self.PatienAddress.get()
                                                                                                     ))
            


            conn.commit()  
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Success","ดำเนินการสำเร็จ \nข้อมูลถูกบันทึกแล้ว !!!")  """


#----------------------- button -----------------



""" btnPrescriptionData = Button(Buttonframe,text="Prescription Data",bg="black",fg="black",font=("kanit",15,"bold"),width=18,height=2,padx=0,pady = 6)
        btnPrescriptionData.grid(row=0,column= 1)
        
        btnUpdate = Button(Buttonframe,text="Update",bg="black",fg="black",font=("kanit",15,"bold"),width=18,height=2,padx=0,pady = 6)
        btnUpdate.grid(row=0,column=2) """



#--------------------- combobox -------------


""" comNametablet = ttk.Combobox(InputframeLeft,textvariable=self.NameofTablets,font=("kanit",12,"bold"),width=30)

        comNametablet["values"]=("ประเภทยา","Moderna","Pfizer","Thai Vaccine","Astrazeneca","Sinovac","Sinopharm")
        comNametablet.current(0)
        comNametablet.grid(row = 0 ,column=1) """