from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import sys



class Staff:
    def __init__(self,root):

        self.txtPatientID = StringVar()
        self.NHSNumber = StringVar()
        self.Name = StringVar()
        self.BirthDate = StringVar()
        self.Address = StringVar()
        self.txtFind = StringVar()
        self.Bloodpreasure  = StringVar()


        # ---------------------- HEAD FRAME  -----------------------
        
        self.root=root
        self.root.title("Staff PharmaKUB ") 
        self.root.geometry('1540x740+0+0')

        # ---------------------- TOP TITLE -------------------------

        toptitle = Label(self.root,bd=15,relief=RIDGE,text="+ STAFF ",fg="#fd6236",bg="white",font=("kanit",45,"bold"))
        toptitle.pack(side=TOP,fill=BOTH)

        # ---------------------- INPUT FRAME ----------------------

        Inputframe = Frame(self.root,bd=15,relief=RIDGE)
        Inputframe.place(x=0,y=90,width=1440,height=315)

        # ------------------ INPUT LEFT --------------------

        InputframeLeft = LabelFrame(Inputframe,bd=10,relief=RIDGE,padx=10,font=("kanit",14,"bold"),text="ประว้ติส่วนตัว")
        InputframeLeft.place(x=5,y=1,width=950,height=280)

        lblPatientID = Label(InputframeLeft,font=("kanit",20,"bold"),text="เลขประจำตัวผู้ป่วย :")
        lblPatientID.grid(row=0,column=0,sticky=W,ipady = 5,ipadx=2)
        txtPatientID = Entry(InputframeLeft,font=("kanit",18,"bold"),textvariable=self.txtPatientID,width=24)
        txtPatientID.grid(row=0,column=1)

        lblNHSNumber= Label(InputframeLeft,font=("kanit",20,"bold"),text="ระบบดูแลสุขภาพ :")
        lblNHSNumber.grid(row=1,column=0,sticky=W,ipady = 5,ipadx=2)
        txtNHSNumber = Entry(InputframeLeft,font=("kanit",18,"bold"),textvariable=self.NHSNumber,width=24)
        txtNHSNumber.grid(row=1,column=1)

        lblName= Label(InputframeLeft,font=("kanit",20,"bold"),text="ชื่อ :")
        lblName.grid(row=2,column=0,sticky=W,ipady = 5,ipadx=2)
        txtName = Entry(InputframeLeft,font=("kanit",18,"bold"),textvariable=self.Name,width=24)
        txtName.grid(row=2,column=1)

        lblBirthDate= Label(InputframeLeft,font=("kanit",20,"bold"),text="วัน/เดือน/ปี เกิด :")
        lblBirthDate.grid(row=3,column=0,sticky=W,ipady = 5,ipadx=2)
        txtBirthDate = Entry(InputframeLeft,font=("kanit",18,"bold"),textvariable=self.BirthDate,width=24)
        txtBirthDate.grid(row=3,column=1)

        lblAddress= Label(InputframeLeft,font=("kanit",20,"bold"),text="ที่อยู่ :")
        lblAddress.grid(row=4,column=0,sticky=W,ipady = 5,ipadx=2)
        txtAddress = Entry(InputframeLeft,font=("kanit",18,"bold"),textvariable=self.Address,width=24)
        txtAddress.grid(row=4,column=1)

        lblBloodpreasure = Label(InputframeLeft,font=("kanit",20,"bold"),text="ความดันเลือด ( mmHg ) :")
        lblBloodpreasure.grid(row=5,column=0,sticky=W,ipady = 5,ipadx=2)
        txtBloodpresure = Entry(InputframeLeft,font=("kanit",18,"bold"),textvariable=self.Bloodpreasure,width=24)
        txtBloodpresure.grid(row=5,column=1)

        # ------------------- INPUT RIGHT --------------------

        InputframeRight = LabelFrame(Inputframe,bd=10,relief=RIDGE,padx=10,font=("kanit",14,"bold"),text="ค้นหาข้อมูลส่วนบุคคล")
        InputframeRight.place(x=960,y=1,width=445,height=280)

        lblFind = Label(InputframeRight,font=("kanit",15,"bold"),text="ตรวจสอบ (ID) :")
        lblFind.grid(row=0,column=0,sticky=W,ipady = 65 ,ipadx=4)
        txtFind = Entry(InputframeRight,font=("kanit",15,"bold"),textvariable=self.txtFind,width=26)
        txtFind.grid(row=0,column=1)

        btnfind = Button(InputframeRight ,font=("kanit",17,"bold"),text="ค้นหา",fg="black",width=15,height=2 , command = self.CheckID)
        btnfind.grid(row = 3 , sticky=N , columnspan= 3)











        # ----------------------- BUTTON FRAME -----------------------

        Buttonframe = Frame(self.root,bd=15,relief=RIDGE)
        Buttonframe.place(x=1,y=410,width=1440,height=105)

        btnInsertdata = Button(Buttonframe,text="Insert Data",bg="black",fg="green",font=("kanit",15,"bold"),width=29,height=3,pady = 6 , command = self.InsertData)
        btnInsertdata.grid(row=0,column= 0)

        btnUpdate = Button(Buttonframe,text="Update",bg="black",fg="blue",font=("kanit",15,"bold"),width=29,height=3,padx=0,pady = 6 , command= self.iUpdate)
        btnUpdate.grid(row=0,column= 1)

        btnClear = Button(Buttonframe,text="Clear",bg="black",fg="red",font=("kanit",15,"bold"),width=29,height=3,padx=0,pady = 6 ,command = self.iClear)
        btnClear.grid(row=0,column= 2)

        btnDelete = Button(Buttonframe,text="Exit",bg="black",fg="red",font=("kanit",15,"bold"),width=29,height=3,padx=0,pady = 6,command = self.iExit)
        btnDelete.grid(row=0,column= 3)

        

        # --------------------- DETAIL FRAME -----------------------

        Detailsframe = Frame(self.root,bd=15,relief=RIDGE)
        Detailsframe.place(x=1,y=515,width=1440,height=385)

    # ----------------------------- DETAIL --------------------------


        scroll_x = ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.Hospital_table = ttk.Treeview(Detailsframe,columns=("PatientID","NHSNumber","Name","BirthDate","Address","BloodPreasure"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x = ttk.Scrollbar(command=self.Hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.Hospital_table.yview)

        self.Hospital_table.heading("PatientID",text="เลขที่ผู้ป่วย")
        self.Hospital_table.heading("NHSNumber",text="ระบบดูแลสุขภาพ")
        self.Hospital_table.heading("Name",text="ชื่อ")
        self.Hospital_table.heading("BirthDate",text="วัน/เดิอน/ปีเกิด")
        self.Hospital_table.heading("Address",text="ที่อยู่")
        self.Hospital_table.heading("BloodPreasure",text="ความดันเลือด")

        self.Hospital_table["show"]="headings"

        self.Hospital_table.column("PatientID",width=100)
        self.Hospital_table.column("NHSNumber",width=100)
        self.Hospital_table.column("Name",width=100)
        self.Hospital_table.column("BirthDate",width=100)
        self.Hospital_table.column("Address",width=100)
        self.Hospital_table.column("BloodPreasure",width=100)

        self.Hospital_table.pack(fill=BOTH,expand=1)
        self.Hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fatch_data()


# ---------------------------- FUNCTION ---------------------------------




    def InsertData(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="0628082548Jai",database="hospital") 
        my_cursor=conn.cursor()
        admin_table = 'hospital.hospital'
        query = f"select patientID from {admin_table} where patientID = (%s) " 
        value = self.txtPatientID.get()
        my_cursor.execute(query,(value,))
        ID_result = my_cursor.fetchall()

        conn.commit()
        conn.close()

        if  len(ID_result) > 0 :

            messagebox.showerror("Error","กรอกข้อมูลไม่สำเร็จ !!! \nหมายเลขผู้ป่วยถูกใช้ไปแล้ว")

        elif self.txtPatientID.get()=="" or self.Name.get()=="" :

            messagebox.showerror("Error","กรอกข้อมูลไม่สำเร็จ !!! \nโปรดใส่ข้อมูล")

        else :
            conn=mysql.connector.connect(host="localhost",username="root",password="0628082548Jai",database="hospital")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital(PatientID,nhsnumber,patientName,DOB,patientAddress,BloodPS) values(%s,%s,%s,%s,%s,%s)",(                                                                  
                                                                                    self.txtPatientID.get(),      
                                                                                    self.NHSNumber.get(),
                                                                                    self.Name.get(), 
                                                                                    self.BirthDate.get(),
                                                                                    self.Address.get(),
                                                                                    self.Bloodpreasure.get()
                                                                                                     ))

            conn.commit()  
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Success","ดำเนินการสำเร็จ \nข้อมูลถูกบันทึกแล้ว !!!") 


    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="0628082548Jai",database="hospital")
        my_cursor=conn.cursor()
        my_cursor.execute("select PatientID,nhsnumber,patientName,DOB,patientAddress,BloodPS from hospital order by PatientID ")
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
        self.txtPatientID.set(row[0])  
        self.NHSNumber.set(row[1])
        self.Name.set(row[2]) 
        self.BirthDate.set(row[3])
        self.Address.set(row[4])
        self.Bloodpreasure.set(row[5])

    def iExit(self):
        iExit = messagebox.askyesno("คำเตือน","ต้องการออกจากโปรแกรม หรือไม่")
        if iExit > 0 :
            self.root.destroy()
            sys.exit()       

    def iClear(self):
        self.txtPatientID.set("")
        self.NHSNumber.set("")
        self.Name.set("")
        self.BirthDate.set("")
        self.Address.set("")
        self.Bloodpreasure.set("")


        self.txtFind.set("")

    
    def iUpdate(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="0628082548Jai",database="hospital")
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital set NHSNumber = %s , PatientName = %s , DOB = %s , PatientAddress = %s , BloodPS = %s where  PatientID = %s " , (
  
                                                                                                    self.NHSNumber.get(),
                                                                                                    self.Name.get(),      
                                                                                                    self.BirthDate.get(), 
                                                                                                    self.Address.get(),
                                                                                                    self.Bloodpreasure.get(),

                                                                                                    # Condition where ....
                                                                                                    self.txtPatientID.get()

                                                                                                    ))    
        conn.commit()  
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Success","ดำเนินการสำเร็จ \nอัปเดตข้อมูลแล้ว !!!")

    
    def CheckID(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="0628082548Jai",database="hospital") 
        my_cursor=conn.cursor()
        admin_table = 'hospital.hospital'
        query = f"select nhsnumber from {admin_table} where patientID = (%s) " 
        value = self.txtFind.get()
        my_cursor.execute(query,(value,))
        ID_result  = my_cursor.fetchall()

        conn.commit()
        conn.close()

        if  len(ID_result) > 0 :
            messagebox.showinfo(title="ตรวจสอบสำเร็จ", message="ข้อมูลผู้ป่วยอยู่ในระบบ !!!")

            """  self.window.withdraw()
            self.newWindow = Toplevel(self.window)
            self.newWindow.protocol("WM_DELETE_WINDOW", self.on_closing) """

        else:
            messagebox.showerror(title="ผิดพลาด", message="ไม่พบเลขที่ผู้ป่วย !!\n กรุณาเพิ่มข้อมูล ")




















if __name__ == "__main__":

    root=Tk()
    ob=Staff(root)
    root.mainloop()
