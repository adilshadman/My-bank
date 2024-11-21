from tkinter import *
import time
from tkinter import messagebox
import sqlite3
try:
    conobj=sqlite3.connect(database="bank.sqlite")
    curobj=conobj.cursor()
    curobj.execute("""create table acn(acn_acno integer primary key autoincrement,
    acn_name text,acn_pass text,acn_email text,acn_mob text,acn_bal float,
    acn_opendate text)""")
    print("table created")

except:
    print("table already exists or something went wrong")
    conobj.close()





win=Tk()
win.configure(bg="grey")
win.title("Project by Shadman")
win.state("zoomed")
win.resizable(width="False",height="False")
lb1_title=Label(win,text="Banking Automation",font=("arial",50,"bold","underline"),
                bg="grey")
lb1_title.pack()
date=time.strftime("%d-%m-%Y")
lb1_date=Label(win,text=date,font=("arial",20,"bold"),
                bg="grey")
lb1_date.place(relx=.85,rely=.1)

def main_screen():
    frm=Frame(win)
    frm.configure(bg="brown")
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)


    def newuser():
        frm.destroy()
        newuser_screen()

    def forgotten():
        frm.destroy()
        forgotten_screen()

    def login():
        global acn
        acn=e_acn.get()
        pwd=e_pass.get()
        if len(acn)==0 or len(pwd)==0:
            messagebox.showwarning("validation","Empty Fields are not allowed")

            
        else:
            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            curobj.execute("""select * from acn where acn_acno=?
            and acn_pass=?""",(acn,pwd))
            tup=curobj.fetchone()
            conobj.close()
            if tup==None:
                messagebox.showerror("Login","Invalid ACN/PASS")
            else:
                frm.destroy()
                welcome_screen()

    def reset():
         e_acn.delete(0,'end')
         e_pass.delete(0,'end')
         e_acn.focus()



       

    lb1_acn=Label(frm,text="ACN",font=("arial",20,"bold"),
                bg="brown")
    lb1_acn.place(relx=.3,rely=.1)
    
    lb1_pass=Label(frm,text="PASS",font=("arial",20,"bold"),
                bg="brown")
    lb1_pass.place(relx=.3,rely=.2)

    e_acn=Entry(frm,font=("arial",20,"bold"),bd=4,bg="grey")
    e_acn.focus()
    e_acn.place(relx=.4,rely=.1)

    e_pass=Entry(frm,font=("arial",20,"bold"),bd=4,bg="grey",show="*")
    e_pass.place(relx=.4,rely=.2)

    btn_login=Button(frm,command=login,text="login",font=("arial",15,"bold"),bd=4,bg="brown")
    btn_login.place(relx=.45,rely=.34)
    btn_reset=Button(frm,command=reset,text="reset",font=("arial",15,"bold"),bd=4,bg="brown")
    btn_reset.place(relx=.53,rely=.34)

    btn_newuser=Button(frm,command=newuser,text="Create new account",font=("arial",15,"bold"),bd=4,bg="brown")
    btn_newuser.place(relx=.44,rely=.55)

    btn_fpass=Button(frm,command=forgotten,text="forgotten password?",font=("arial",10,"bold"),
                     bd=4,bg="brown")
    btn_fpass.place(relx=.46,rely=.45)

    def newuser_screen():
        frm=Frame(win)
        frm.configure(bg="brown")
        frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
        def reset():
          e_name.delete(0,'end')
          e_pass.delete(0,'end')
          e_email.delete(0,'end')
          e_mob.delete(0,'end')
          e_name.focus()
        def newacn():
            name=e_name.get()
            pwd=e_pass.get()
            email=e_email.get()
            mob=e_mob.get()
            bal=0
            date=time.strftime('%d-%m-%Y')
            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            curobj.execute('''insert into acn(acn_name,acn_pass,acn_email,
            acn_mob,acn_bal,acn_opendate)
            values(?,?,?,?,?,?)''',(name,pwd,email,mob,bal,date))
            conobj.commit()
            conobj.close()

           

            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            curobj.execute('select max(acn_acno) from acn')
            tup=curobj.fetchone()
            conobj.close()

            messagebox.showinfo("New Account",f"Account Created,ACN:{tup[0]}")
            
            


        

        lb1_name=Label(frm,text="Name",font=("arial",20,"bold"),
                bg="brown")
        lb1_name.place(relx=.3,rely=.1)

        e_name=Entry(frm,font=("arial",20,"bold"),bd=4,bg="grey")
        e_name.focus()
        e_name.place(relx=.4,rely=.1)

        lb1_pass=Label(frm,text="Pass",font=("arial",20,"bold"),
                bg="brown")
        lb1_pass.place(relx=.3,rely=.2)

        e_pass=Entry(frm,font=("arial",20,"bold"),bd=4,bg="grey",show="*")
        e_pass.place(relx=.4,rely=.2)

        lb1_email=Label(frm,text="Email",font=("arial",20,"bold"),
                bg="brown")
        lb1_email.place(relx=.3,rely=.3)

        e_email=Entry(frm,font=("arial",20,"bold"),bd=4,bg="grey")
        e_email.place(relx=.4,rely=.3)

        
        lb1_mob=Label(frm,text="Mob",font=("arial",20,"bold"),
                bg="brown")
        lb1_mob.place(relx=.3,rely=.4)

        e_mob=Entry(frm,font=("arial",20,"bold"),bd=4,bg="grey")
        e_mob.place(relx=.4,rely=.4)

        btn_submit=Button(frm,command=newacn,text="Submit",font=("arial",12,"bold"),
                     bd=4,bg="brown")
        btn_submit.place(relx=.44,rely=.52)

        btn_reset=Button(frm,command=reset,text="reset",font=("arial",12,"bold"),bd=4,bg="brown")
        btn_reset.place(relx=.53,rely=.52)


        def back():
            frm.destroy()
            main_screen()

        btn_back=Button(frm,command=back,text="back",font=("arial",10,"bold"),bd=4,bg="brown")
        btn_back.place(relx=0,rely=0)

    def forgotten_screen():
        frm=Frame(win)
        frm.configure(bg="brown")
        frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)

        def reset():
          e_acn.delete(0,'end')
          e_email.delete(0,'end')
          e_mob.delete(0,'end')
          e_acn.focus()

        
        def back():
            frm.destroy()
            main_screen()

        def forgot():
            email=e_email.get()
            acn=e_acn.get()
            mob=e_mob.get()


            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            curobj.execute("""select acn_pass from acn where
                           acn_acno=? and acn_mob=? and acn_email=?""",
                           (acn,mob,email))
            
            tup=curobj.fetchone()
            conobj.close()
            if tup==None:
                messagebox.showerror("Password","Invalid details!")
            else:
                messagebox.showinfo("Password",tup[0])
            frm.destroy()
            main_screen()


        btn_back=Button(frm,command=back,text="back",font=("arial",10,"bold"),bd=4,bg="brown")
        btn_back.place(relx=0,rely=0)


        lb1_acn=Label(frm,text="ACN",font=("arial",20,"bold"),
                bg="brown")
        lb1_acn.place(relx=.3,rely=.1)

        e_acn=Entry(frm,font=("arial",20,"bold"),bd=4,bg="grey")
        e_acn.focus()
        e_acn.place(relx=.4,rely=.1)

        lb1_email=Label(frm,text="Email",font=("arial",20,"bold"),
                bg="brown")
        lb1_email.place(relx=.3,rely=.2)

        e_email=Entry(frm,font=("arial",20,"bold"),bd=4,bg="grey")
        
        e_email.place(relx=.4,rely=.2)

        lb1_mob=Label(frm,text="Mob",font=("arial",20,"bold"),
                bg="brown")
        lb1_mob.place(relx=.3,rely=.3)

        e_mob=Entry(frm,font=("arial",20,"bold"),bd=4,bg="grey")
    
        e_mob.place(relx=.4,rely=.3)

        btn_submit=Button(frm,command=forgot,text="Submit",font=("arial",12,"bold"),
                     bd=4,bg="brown")
        btn_submit.place(relx=.45,rely=.45)

        btn_reset=Button(frm,command=reset,text="reset",font=("arial",12,"bold"),bd=4,bg="brown")
        btn_reset.place(relx=.53,rely=.45)


    def welcome_screen():
        frm=Frame(win)
        frm.configure(bg="brown")
        frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)

        conobj=sqlite3.connect(database="bank.sqlite")
        curobj=conobj.cursor()
        curobj.execute("""select * from acn where
        acn_acno=?""",(acn,))
        tup=curobj.fetchone()
        conobj.close()
        
        def logout():
            frm.destroy()
            main_screen()
        def details():
            ifrm=Frame(frm,highlightbackground="black",highlightthickness=5)
            ifrm.configure(bg="white")
            ifrm.place(relx=.18,rely=.15,relwidth=.73,relheight=.63)

            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            curobj.execute("""select * from acn where
            acn_acno=?""",(acn,))
            tup=curobj.fetchone()
            conobj.close()

            lb1_wel=Label(ifrm,text="This is details screen",font=("arial",20,"bold","underline"),
                bg="white",fg="purple")
            lb1_wel.pack()

            lb1_acn=Label(ifrm,text=f"Account no={tup[0]}",font=("arial",20,"bold","underline"),
                bg="white")
            lb1_acn.place(relx=.3,rely=.2)

            lb1_bal=Label(ifrm,text=f"Your acn bal={tup[5]}",font=("arial",20,"bold","underline"),
                bg="white",)
            lb1_bal.place(relx=.3,rely=.3)

            lb1_date=Label(ifrm,text=f"Opendate={tup[6]}",font=("arial",20,"bold","underline"),
                bg="white",)
            lb1_date.place(relx=.3,rely=.4)

        def deposit():
            ifrm=Frame(frm,highlightbackground="black",highlightthickness=5)
            ifrm.configure(bg="white")
            ifrm.place(relx=.18,rely=.15,relwidth=.73,relheight=.63)
            def depacn():
                
                conobj=sqlite3.connect(database="bank.sqlite")
                curobj=conobj.cursor()
                amt=float(e_acn.get())
                curobj.execute("""update acn set acn_bal=acn_bal+?
                where acn_acno=?""",(amt,acn))
                conobj.commit()
                conobj.close()
                messagebox.showinfo("deposit",f"{amt} deposited")
                

            def reset():
                e_acn.delete(0,"end")
                e_acn.focus()
          

            lb1_wel=Label(ifrm,text="This is deposit screen",font=("arial",20,"bold","underline"),
                bg="white",fg="purple")
            lb1_wel.pack()

            lb1_amt=Label(ifrm,text="Amount",font=("arial",20,"bold"),
                bg="white")
            lb1_amt.place(relx=.2,rely=.3)

            e_acn=Entry(ifrm,font=("arial",20,"bold"),bd=4,bg="grey")
            e_acn.focus()
            e_acn.place(relx=.35,rely=.3)

            btn_submit=Button(ifrm,command=depacn,text="Submit",font=("arial",12,"bold"),
                     bd=4,bg="brown")
            btn_submit.place(relx=.43,rely=.48)

            btn_reset=Button(frm,command=reset,text="reset",font=("arial",12,"bold"),bd=4,bg="brown")
            btn_reset.place(relx=.57,rely=.454)


        def withdraw():
            ifrm=Frame(frm,highlightbackground="black",highlightthickness=5)
            ifrm.configure(bg="white")
            ifrm.place(relx=.18,rely=.15,relwidth=.73,relheight=.63)

            def withacn():
                conobj=sqlite3.connect(database="bank.sqlite")
                curobj=conobj.cursor()
                amt=float(e_acn.get())
                curobj.execute("""update acn set acn_bal=acn_bal-?
                where acn_acno=?""",(amt,acn))
                conobj.commit()
                conobj.close()
                messagebox.showinfo("withdraw",f"{amt} withdrawn")

            
            def reset():
                e_acn.delete(0,"end")
                e_acn.focus()
          


            lb1_wel=Label(ifrm,text="This is withdraw screen",font=("arial",20,"bold","underline"),
                bg="white",fg="purple")
            lb1_wel.pack()

            lb1_amt=Label(ifrm,text="Amount",font=("arial",20,"bold"),
                bg="white")
            lb1_amt.place(relx=.2,rely=.3)

            e_acn=Entry(ifrm,font=("arial",20,"bold"),bd=4,bg="grey")
            e_acn.focus()
            e_acn.place(relx=.35,rely=.3)

            btn_submit=Button(ifrm,command=withacn,text="Submit",font=("arial",12,"bold"),
                     bd=4,bg="brown")
            btn_submit.place(relx=.43,rely=.48)

            btn_reset=Button(frm,command=reset,text="reset",font=("arial",12,"bold"),bd=4,bg="brown")
            btn_reset.place(relx=.57,rely=.454)

        def update():
            ifrm=Frame(frm,highlightbackground="black",highlightthickness=5)
            ifrm.configure(bg="white")
            ifrm.place(relx=.18,rely=.15,relwidth=.73,relheight=.63)

            def updateacn():
                name=e_name.get()
                pwd=e_pass.get()
                email=e_email.get()
                mob=e_mob.get()

                conobj=sqlite3.connect(database="bank.sqlite")
                curobj=conobj.cursor()
                curobj.execute("""update acn set acn_name=?,
                acn_pass=?,acn_email=?,acn_mob=? where acn_acno=?""",
                               (name,pwd,email,mob,acn))
                conobj.commit()
                conobj.close()
                messagebox.showinfo("Update","Profile Updated")
                frm.destroy()
                welcome_screen()
                

            lb1_wel=Label(ifrm,text="This is update screen",font=("arial",20,"bold","underline"),
                bg="white",fg="purple")
            lb1_wel.pack()

            lb1_name=Label(ifrm,text="Name",font=("arial",20,"bold"),
                bg="white")
            lb1_name.place(relx=.1,rely=.2)

            e_name=Entry(ifrm,font=("arial",20,"bold"),bd=4,bg="grey")
            e_name.place(relx=.1,rely=.3)

            lb1_pass=Label(ifrm,text="Pass",font=("arial",20,"bold"),
                bg="white")
            lb1_pass.place(relx=.5,rely=.2)

            e_pass=Entry(ifrm,font=("arial",20,"bold"),bd=4,bg="grey")
            e_pass.place(relx=.5,rely=.3)

            lb1_email=Label(ifrm,text="Email",font=("arial",20,"bold"),
                bg="white")
            lb1_email.place(relx=.1,rely=.5)

            e_email=Entry(ifrm,font=("arial",20,"bold"),bd=4,bg="grey")
            e_email.place(relx=.1,rely=.6)

            lb1_mob=Label(ifrm,text="Mob",font=("arial",20,"bold"),
                bg="white")
            lb1_mob.place(relx=.5,rely=.5)

            e_mob=Entry(ifrm,font=("arial",20,"bold"),bd=4,bg="grey")
            e_mob.place(relx=.5,rely=.6)

            
            btn_update=Button(ifrm,command=updateacn,text="Update",font=("arial",12,"bold"),bd=4,bg="brown")
            btn_update.place(relx=0.7,rely=0.8)

            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            curobj.execute("""select * from acn where
            acn_acno=?""",(acn,))
            tup=curobj.fetchone()
            conobj.close()

            e_name.insert(0,tup[1])
            e_pass.insert(0,tup[2])
            e_email.insert(0,tup[3])
            e_mob.insert(0,tup[4])
            e_name.focus()









        btn_logout=Button(frm,command=logout,text="Logout",font=("arial",10,"bold"),bd=4,bg="brown")
        btn_logout.place(relx=0.95,rely=0)

        lb1_wel=Label(frm,text=f"Welcome,{tup[1]}",font=("arial",20,"bold"),
                bg="brown")
        lb1_wel.place(relx=0,rely=0)

        
        btn_check=Button(frm,command=details,text="Check details",font=("arial",12,"bold"),bd=4,bg="brown")
        btn_check.place(relx=0,rely=.15)

        btn_deposit=Button(frm,command=deposit,text="Deposit Amt",font=("arial",12,"bold"),bd=4,bg="brown")
        btn_deposit.place(relx=0,rely=.30)

        btn_withdraw=Button(frm,command=withdraw,text="Withdraw Amt",font=("arial",12,"bold"),bd=4,bg="brown")
        btn_withdraw.place(relx=0,rely=.45)

        btn_update=Button(frm,command=update,text="Update details",font=("arial",12,"bold"),bd=4,bg="brown")
        btn_update.place(relx=0,rely=.60)







    

        

    

    
main_screen()










win.mainloop()
