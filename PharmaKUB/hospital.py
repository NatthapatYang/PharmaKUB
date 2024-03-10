from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import sys

    
#---------------------------------- HOSPITAL ----------------------------------------------



class Hospital:
    def __init__(self,root):

        # ---------------------- HEAD FRAME  --------------------------
        self.root=root
        self.root.title("Pharmacist PharmaKUB ") 
        self.root.geometry('1540x740+0+0')
        


        self.NameofTablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NoOftablets = StringVar()
        self.Lot = StringVar()
        self.issuedate = StringVar()
        self.Expdate = StringVar()
        self.DailyDose = StringVar()
        self.SideEffect = StringVar()
        self.Furtherinfo = StringVar()
        self.BloodPressure = StringVar()
        self.Storage = StringVar()
        self.Medicine = StringVar()
        self.PatientID = StringVar()
        self.NHSNumber = StringVar()
        self.PatientName = StringVar()
        self.DateofBirth = StringVar()
        self.PatienAddress = StringVar()
    

        lbltitle = Label(self.root,bd=20,relief=RIDGE,text="+ PHARMACIST ",fg="#fd6236",bg="white",font=("kanit",45,"bold"))
        lbltitle.pack(side=TOP,fill=BOTH)

        # ---------------------- DATA FRAME LEFT , RIGHT  --------------------------
        Dataframe = Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=100,width=1440,height=390)

        DataframeLeft = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("kanit",14,"bold"),text="ข้อมูลการใช้คนไข้")
        DataframeLeft.place(x=5,y=1,width=950,height=340)

        DataframeRight = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("kanit",14,"bold"),text="ใบสั่งยา")
        DataframeRight.place(x=960,y=1,width=435,height=340)

        # ---------------------- BUTTON FRAME --------------------------

        Buttonframe = Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=1,y=490,width=1440,height=100)

        # ---------------------- DETAIL FRAME --------------------------

        Detailsframe = Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=1,y=590,width=1440,height=310) #อันเก่า height = 150

    #------------------------- END DATA FRAME -----------------------
        
        lblNameTablet = Label(DataframeLeft,text="ชื่อประเภทยา :",font=("kanit",15,"bold"),padx=2)
        lblNameTablet.grid(row = 0 ,column=0,sticky=W)
        txtNameTablet = Entry(DataframeLeft,font=("kanit",13,"bold"),textvariable=self.NameofTablets,width=30 ,state='disable',disabledbackground='#929292',disabledforeground='black')
        txtNameTablet.grid(row=0,column=1)

        lblref = Label(DataframeLeft,font=("kanit",15,"bold"),text="เลขอ้างอิง :",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref = Entry(DataframeLeft,font=("kanit",13,"bold"),textvariable=self.ref,width=30,state='disable',disabledbackground='#929292',disabledforeground='black')
        txtref.grid(row=1,column=1)

        lblDose = Label(DataframeLeft,font=("kanit",15,"bold"),text="เลขโดส :",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose = Entry(DataframeLeft,font=("kanit",13,"bold"),textvariable=self.Dose,width=30,state='disable',disabledbackground='#929292',disabledforeground='black')
        txtDose.grid(row=2,column=1)

        lblNoOftablets = Label(DataframeLeft,font=("kanit",15,"bold"),text="หมายเลขที่ยา :",padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets = Entry(DataframeLeft,font=("kanit",13,"bold"),textvariable=self.NoOftablets,width=30,state='disable',disabledbackground='#929292',disabledforeground='black')
        txtNoOftablets.grid(row=3,column=1)

        lblLot = Label(DataframeLeft,font=("kanit",15,"bold"),text="ล็อตที่ :",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot = Entry(DataframeLeft,font=("kanit",13,"bold"),textvariable=self.Lot,width=30,state='disable',disabledbackground='#929292',disabledforeground='black')
        txtLot.grid(row=4,column=1)

        lblissuedate = Label(DataframeLeft,font=("kanit",15,"bold"),text="วันที่ออก :",padx=2,pady=6)
        lblissuedate.grid(row=5,column=0,sticky=W)
        txtissuedate = Entry(DataframeLeft,font=("kanit",13,"bold"),textvariable=self.issuedate,width=30,state='disable',disabledbackground='#929292',disabledforeground='black')
        txtissuedate.grid(row=5,column=1)

        lblExpdate = Label(DataframeLeft,font=("kanit",15,"bold"),text="วันหมดอายุ :",padx=2,pady=6)
        lblExpdate.grid(row=6,column=0,sticky=W)
        txtExpdate = Entry(DataframeLeft,font=("kanit",13,"bold"),textvariable=self.Expdate,width=30,state='disable',disabledbackground='#929292',disabledforeground='black')
        txtExpdate.grid(row=6,column=1)

        lblDailyDose = Label(DataframeLeft,font=("kanit",15,"bold"),text="ปริมาณ/วัน :",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose = Entry(DataframeLeft,font=("kanit",13,"bold"),textvariable=self.DailyDose,width=30,state='disable',disabledbackground='#929292',disabledforeground='black')
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect = Label(DataframeLeft,font=("kanit",15,"bold"),text="ผลข้างเคียง :",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect = Entry(DataframeLeft,font=("kanit",13,"bold"),textvariable=self.SideEffect,width=30)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherinfo = Label(DataframeLeft,font=("kanit",15,"bold"),text="เพิ่มเติม :",padx=2)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo = Entry(DataframeLeft,font=("kanit",13,"bold"),textvariable=self.Furtherinfo,width=34)
        txtFurtherinfo.grid(row=0,column=3)

        lblBloodPressure = Label(DataframeLeft,font=("kanit",15,"bold"),text="ความดันเลือด ( mmHg ) :",padx=2)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure = Entry(DataframeLeft,font=("kanit",13,"bold"),textvariable=self.BloodPressure,width=34,state='disable',disabledbackground='#929292',disabledforeground='black')
        txtBloodPressure.grid(row=1,column=3)

        lblStorage = Label(DataframeLeft,font=("kanit",15,"bold"),text="คำแนะนำในการเก็บ :",padx=2)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage = Entry(DataframeLeft,font=("kanit",13,"bold"),textvariable=self.Storage,width=34 )
        txtStorage.grid(row=2,column=3)
        
        lblMedicine = Label(DataframeLeft,font=("kanit",15,"bold"),text="การให้ยา :",padx=2)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine = Entry(DataframeLeft,font=("kanit",13,"bold"),textvariable=self.Medicine,width=34)
        txtMedicine.grid(row=3,column=3)

        lblPatientID = Label(DataframeLeft,font=("kanit",15,"bold"),text="เลขประจำตัวผู้ป่วย :",padx=2)
        lblPatientID.grid(row=4,column=2,sticky=W)
        txtPatientID = Entry(DataframeLeft,font=("kanit",13,"bold"),textvariable=self.PatientID,width=34,state='disable',disabledbackground='#929292',disabledforeground='black')
        txtPatientID.grid(row=4,column=3)

        lblNHSNumber = Label(DataframeLeft,font=("kanit",15,"bold"),text="ระบบดูแลสุขภาพ :",padx=2)
        lblNHSNumber.grid(row=5,column=2,sticky=W)
        txtNHSNumber = Entry(DataframeLeft,font=("kanit",13,"bold"),textvariable=self.NHSNumber,width=34,state='disable',disabledbackground='#929292',disabledforeground='black')
        txtNHSNumber.grid(row=5,column=3)

        lblPatientName = Label(DataframeLeft,font=("kanit",15,"bold"),text="ชื่อ :",padx=2)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName = Entry(DataframeLeft,font=("kanit",13,"bold"),textvariable=self.PatientName,width=34,state='disable',disabledbackground='#929292',disabledforeground='black')
        txtPatientName.grid(row=6,column=3)

        lblDateofBirth = Label(DataframeLeft,font=("kanit",15,"bold"),text="วัน/เดิอน/ปี เกิด :",padx=2)
        lblDateofBirth.grid(row=7,column=2,sticky=W)
        txtDateofBirth = Entry(DataframeLeft,font=("kanit",13,"bold"),textvariable=self.DateofBirth,width=34,state='disable',disabledbackground='#929292',disabledforeground='black')
        txtDateofBirth.grid(row=7,column=3)

        lblPatienAddress = Label(DataframeLeft,font=("kanit",15,"bold"),text="ที่อยู่ :",padx=2)
        lblPatienAddress.grid(row=8,column=2,sticky=W)
        txtPatienAddress = Entry(DataframeLeft,font=("kanit",13,"bold"),textvariable=self.PatienAddress,width=34,state='disable',disabledbackground='#929292',disabledforeground='black')
        txtPatienAddress.grid(row=8,column=3)

    # -------------------------------- DATA FRAME RIGHT INTERIOR -------------------------------------
        
        self.txtPrescription = Text(DataframeRight,font=("kanit",15,"bold"),width=36,height=15,padx=0,pady = 6)
        self.txtPrescription.grid(row=0,column=0)

    # -------------------------------- BUTTON FRAME ---------------------------------------------
        
        btnPrescription = Button(Buttonframe,text="Prescription",bg="black",fg="black",font=("kanit",15,"bold"),width=29,height=2,padx=0,pady = 6,command=self.iPrescription)
        btnPrescription.grid(row=0,column= 0)

        btnDelete = Button(Buttonframe,text="Delete",bg="black",fg="black",font=("kanit",15,"bold"),width=29,height=2,padx=0,pady = 6,command=self.idelete)
        btnDelete.grid(row=0,column= 1)

        btnClear = Button(Buttonframe,text="Clear",bg="black",fg="black",font=("kanit",15,"bold"),width=29,height=2,padx=0,pady = 6,command=self.iClear)
        btnClear.grid(row=0,column= 2)

        btnExit = Button(Buttonframe,text="Exit",bg="black",fg="black",font=("kanit",15,"bold"),width=28,height=2,padx=0,pady = 6,command=self.iExit)
        btnExit.grid(row=0,column= 3)


#-----------------------------------------------  DATA BASE TABLE   -----------------------------------------------------
        
        #--------------------------------------- SCROLLBAR ------------------------------------

        scroll_x = ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.Hospital_table = ttk.Treeview(Detailsframe,columns=("nameofTablets","ref","dose","nooftablets","lot","issuedate"
                                                                 ,"expdate","dailydose","PatientID","nhsnumber","patientname","dateofB","address","BloodPS"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x = ttk.Scrollbar(command=self.Hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.Hospital_table.yview)

        self.Hospital_table.heading("nameofTablets",text="ชื่อประเภทยา")
        self.Hospital_table.heading("ref",text="เลขอ้างอิง :")
        self.Hospital_table.heading("dose",text="เลขโดส")
        self.Hospital_table.heading("nooftablets",text="หมายเลขที่ยา")
        self.Hospital_table.heading("lot",text="ล็อตที่")
        self.Hospital_table.heading("issuedate",text="วันที่ออก")
        self.Hospital_table.heading("expdate",text="วันหมดอายุ")
        self.Hospital_table.heading("dailydose",text="ปริมาณ/วัน")
        self.Hospital_table.heading("PatientID",text="การเก็บรักษา")
        self.Hospital_table.heading("nhsnumber",text="ระบบดูลสุขภาพ")
        self.Hospital_table.heading("patientname",text="ชื่อ")
        self.Hospital_table.heading("dateofB",text="วันเกิด")
        self.Hospital_table.heading("address",text="ที่อยู่")
        self.Hospital_table.heading("BloodPS",text="ความดัน")

        self.Hospital_table["show"]="headings"

        self.Hospital_table.column("nameofTablets",width=95)
        self.Hospital_table.column("ref",width=95)
        self.Hospital_table.column("dose",width=95)
        self.Hospital_table.column("nooftablets",width=95)
        self.Hospital_table.column("lot",width=95)
        self.Hospital_table.column("issuedate",width=95)
        self.Hospital_table.column("expdate",width=95)
        self.Hospital_table.column("dailydose",width=95)
        self.Hospital_table.column("PatientID",width=95)
        self.Hospital_table.column("nhsnumber",width=95)
        self.Hospital_table.column("patientname",width=95)
        self.Hospital_table.column("dateofB",width=95)
        self.Hospital_table.column("address",width=95)
        self.Hospital_table.column("BloodPS",width=95)

        self.Hospital_table.pack(fill=BOTH,expand=1)
        self.Hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fatch_data()

    # ----------------------------- Function ----------------------------------------
        


    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="0628082548Jai",database="hospital")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital order by Reference_no ")
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
        self.NameofTablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NoOftablets.set(row[3])
        self.Lot.set(row[4])
        self.issuedate.set(row[5])
        self.Expdate.set(row[6])
        self.DailyDose.set(row[7])
        self.PatientID.set(row[8])  
        self.NHSNumber.set(row[9])
        self.PatientName.set(row[10]) 
        self.DateofBirth.set(row[11])
        self.PatienAddress.set(row[12])
        self.BloodPressure.set(row[13])


    def iPrescription(self):
        self.txtPrescription.insert(END,"ชื่อประเภทยา : \t\t\t" + self.NameofTablets.get() + "\n")
        self.txtPrescription.insert(END,"เลขอ้างอิง : \t\t\t" + self.ref.get() + "\n")
        self.txtPrescription.insert(END,"หมายเลขที่ยา : \t\t\t" + self.NoOftablets.get() + "\n")
        self.txtPrescription.insert(END,"ล็อตที่ : \t\t\t" + self.Lot.get() + "\n")
        self.txtPrescription.insert(END,"วันที่ออก : \t\t\t" + self.issuedate.get() + "\n")
        self.txtPrescription.insert(END,"วันหมดอายุ : \t\t\t" + self.Expdate.get() + "\n")

        self.txtPrescription.insert(END,"ปริมาณ/วัน : \t\t\t" + self.DailyDose.get() + "\n")
        self.txtPrescription.insert(END,"ผลข้างเคียง : \t\t\t" + self.SideEffect.get() + "\n")
        self.txtPrescription.insert(END,"เพิ่มเติม : \t\t\t" + self.Furtherinfo.get() + "\n")
        self.txtPrescription.insert(END,"ความดันเลือด ( mmHg ) : \t\t\t" + self.BloodPressure.get() + "\n")
        self.txtPrescription.insert(END,"คำแนะนำในการเก็บ : \t\t\t" + self.Storage.get() + "\n")
        self.txtPrescription.insert(END,"การให้ยา : \t\t\t" + self.Medicine.get() + "\n")

        self.txtPrescription.insert(END,"เลขประจำตัวผู้ป่วย : \t\t\t" + self.PatientID.get() + "\n")
        self.txtPrescription.insert(END,"ระบบดูแลสุขภาพ : \t\t\t" + self.NHSNumber.get() + "\n")
        self.txtPrescription.insert(END,"ชื่อ : \t\t\t" + self.PatientName.get() + "\n")
        self.txtPrescription.insert(END,"วัน/เดือน/ปี เกิด : \t\t\t" + self.DateofBirth.get() + "\n")
        self.txtPrescription.insert(END,"ที่อยู่ : \t\t\t" + self.PatienAddress.get() + "\n")

    def idelete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="0628082548Jai",database="hospital")
        my_cursor=conn.cursor()
        query = "delete from hospital where Reference_No =%s"
        value = (self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("Delete","ลบประวัติสำเร็จ !!!")




    def iClear(self):
        self.NameofTablets.set("")
        self.ref.set("")                                                                                            
        self.Dose.set("")                                                                                                 
        self.NoOftablets.set("")
        self.Lot.set("")
        self.issuedate.set("")
        self.Expdate.set("")
        self.DailyDose.set("")
        self.SideEffect.set("")
        self.Furtherinfo.set("")
        self.BloodPressure.set("")
        self.Storage.set("")    
        self.Medicine.set("")
        self.PatientID.set("")
        self.NHSNumber.set("")
        self.PatientName.set("")
        self.DateofBirth.set("")
        self.PatienAddress.set("")



        self.txtPrescription.delete("1.0",END)

    def iExit(self):
        iExit = messagebox.askyesno("คำเตือน","ต้องการออกจากโปรแกรม หรือไม่")
        if iExit > 0 :
            self.root.destroy()
            sys.exit()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     




if __name__ == "__main__":

    root=Tk()
    ob=Hospital(root)
    root.mainloop()











