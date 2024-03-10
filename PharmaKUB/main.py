import tkinter
from hospital import Hospital
from doctor import Doctor
from staff import Staff
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import os
import mysql.connector


class Log:
    def __init__(self,window):

        self.window = window
        self.window.title("PharmaKUB")
        self.window.geometry('800x650')
        self.window.configure(bg='#fd6236')

        self.username_entry = StringVar()
        self.password_entry = StringVar()
        self.position =StringVar()                      

        frame = Frame(self.window,bg='#fd6236')
        frame.place(x=170,y=90)

        username_label = Label(frame, text="Username", bg='#fd6236', fg="white", font=("kanit", 16))
        username_entry = Entry(frame, font=("kanit", 16),width=20,textvariable=self.username_entry)

        password_label = Label(frame, text="Password", bg='#fd6236', fg="white", font=("kanit", 16))
        password_entry = Entry(frame, show="*", font=("kanit", 16),width=20,textvariable=self.password_entry)

        position = Label(frame,text="ชื่อประเภทยา :",font=("kanit",15,"bold"))
        position = ttk.Combobox(frame,textvariable=self.position,font=("kanit",12,"bold"),width=20)

        position["values"]=("Position","Staff","Doctor","Pharmacist")
        position.current(0)


        login_label = Label(frame, text="PharmaKUB Sign in", bg='black', fg="white", font=("kanit", 30),width=25)
        login_button = Button(frame, text="เข้าสู่ระบบ", bg="black", fg="black", font=("kanit", 16),width=13, command=self.login)


        login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1, pady=20)
        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1, pady=20)
        position.grid(row = 4 ,column=1 , pady=20)
        login_button.grid(row=6, column=0, columnspan=2, pady=90)

    def on_closing(self): 
        self.window.destroy()

    def login(self):

        conn=mysql.connector.connect(host="localhost",username="root",password="0628082548Jai",database="hospital") 
        my_cursor=conn.cursor()
        admin_table = 'hospital.Admin'
        query = f"select username from {admin_table} where password = %s and username = %s and position = %s "
        value = self.password_entry.get() , self.username_entry.get() , self.position.get()
        my_cursor.execute(query,(value))
        username_result  = my_cursor.fetchall()

        conn.commit()
        conn.close()


        if  len(username_result) > 0 :

            if  self.position.get() == "Staff" :
                messagebox.showinfo(title="ดำเนินการสำเร็จ", message="เข้าสู่ระบบสำเร็จ !!")
                self.window.withdraw()
                self.newWindow = Toplevel(self.window)
                self.newWindow.protocol("WM_DELETE_WINDOW", self.on_closing)

                self.app = Staff(self.newWindow)

            elif self.position.get() == "Doctor" :
                
                messagebox.showinfo(title="ดำเนินการสำเร็จ", message="เข้าสู่ระบบสำเร็จ !!")
                self.window.withdraw()
                self.newWindow = Toplevel(self.window)
                self.newWindow.protocol("WM_DELETE_WINDOW", self.on_closing)

                self.app = Doctor(self.newWindow)

            elif self.position.get() == "Pharmacist" :
                
                messagebox.showinfo(title="ดำเนินการสำเร็จ", message="เข้าสู่ระบบสำเร็จ !!")
                self.window.withdraw()
                self.newWindow = Toplevel(self.window)
                self.newWindow.protocol("WM_DELETE_WINDOW", self.on_closing)

                self.app = Hospital(self.newWindow)

        else:
            messagebox.showerror(title="ผิดพลาด", message="ชื่อ-รหัสผ่านหรือตำแหน่งงาน\nไม่ถูกต้อง !!")


if __name__ == "__main__" :


    window=Tk()
    test = Log(window)
    window.mainloop()


    # username = "test"
    # password = "1234" 
    # position = "staff"


    # username = "test2"
    # password = "1234" 
    # position = "doctor"


    # username = "test3"
    # password = "1234" 
    # position = "phamacist"





    #(self.username_entry.get()==username and self.password_entry.get()==password):