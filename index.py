import tkinter
import customtkinter as ctk
from mysql import connector
from tkinter.ttk import Treeview

mydb = connector.connect(
  host="localhost",
  user="root",
  password="vin123"
)
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.geometry("900x700")
app.title("Password Encryption")

mycur = mydb.cursor()
mycur.execute('use mini_project')


def loginfrontend():
    def loginbackend():
        uname = user_entry.get()
        upass = user_pass.get()
        mycur.execute('select * from login_signin1 where email="'+uname+'" and pass="'+upass+'";')
        for dt in mycur.fetchall():
            if (uname == dt[3] and upass == dt[4]):
                selection()
                global emailid
                emailid=uname
            else:
                loginfrontend()
    cleanning()
    sublabel = ctk.CTkLabel(master=frame,text='Login Page',font=("Arial",30),bg_color="White",width=300)
    sublabel.pack(pady=12,padx=10)
    user_entry= ctk.CTkEntry(master=frame,placeholder_text="Username",font=("Arial",20),width=400)
    user_entry.pack(pady=12,padx=10)
    user_pass= ctk.CTkEntry(master=frame,placeholder_text="Password",font=("Arial",20),width=400,show="*")
    user_pass.pack(pady=12,padx=10)
    button = ctk.CTkButton(master=frame,text='Login',command=loginbackend)
    button.pack(pady=12,padx=10)
    checkbox = ctk.CTkCheckBox(master=frame,text='Remember Me')
    checkbox.pack(pady=12,padx=10)
    signbtn=ctk.CTkButton(master=frame,text="Sign in",command=signinfrontend)
    signbtn.pack(pady=12,padx=10)

def cleanning():
    for widget in frame.winfo_children():
        widget.destroy()

def signinfrontend():
    def signinbackend():
        ufname=entFName.get()
        ulname=entLName.get()
        uphone=entphone.get()
        uemail=entemail.get()
        upass=entpass.get()
        mycur.execute("insert into login_signin1 values ('"+ufname+"','"+ulname+"',"+uphone+",'"+uemail+"','"+upass+"');")
        mydb.commit()
        loginfrontend()
    cleanning()
    sublabel = ctk.CTkLabel(master=frame, text='Login Page', font=("Arial", 30), fg_color="blue", width=500)
    sublabel.pack(pady=12, padx=10)
    entFName = ctk.CTkEntry(master=frame, placeholder_text="First Name", font=("Arial", 20), width=400)
    entFName.pack(pady=12, padx=10)
    entLName = ctk.CTkEntry(master=frame, placeholder_text="Last Name", font=("Arial", 20), width=400)
    entLName.pack(pady=12, padx=10)
    entphone = ctk.CTkEntry(master=frame, placeholder_text="Phone", font=("Arial", 20), width=400)
    entphone.pack(pady=12, padx=10)
    entemail = ctk.CTkEntry(master=frame, placeholder_text="Email", font=("Arial", 20), width=400)
    entemail.pack(pady=12, padx=10)
    entpass = ctk.CTkEntry(master=frame, placeholder_text="Password", font=("Arial", 20), width=400, show="*")
    entpass.pack(pady=12, padx=10)
    entconfpass = ctk.CTkEntry(master=frame, placeholder_text="Confirm Password", font=("Arial", 20), width=400,show="*")
    entconfpass.pack(pady=12, padx=10)
    submitbtn = ctk.CTkButton(master=frame, text='Submit',command=signinbackend)
    submitbtn.pack(pady=12, padx=10)
    resetbtn = ctk.CTkButton(master=frame, text='Reset')
    resetbtn.pack(pady=12, padx=10)

def selection():
    cleanning()
    btnwesbite = ctk.CTkButton(frame, text="Wesbite", font=("airal", 35,"bold"), fg_color="Black", width=180,height=50,command=website)
    btnwesbite.place(x=200, y=300)
    btncard = ctk.CTkButton(frame, text="Card", font=("airal", 35,"bold"), fg_color="Black", width=180,height=50,command=card)
    btncard.place(x=500, y=300)

def website():
    cleanning()
    def username_password():
        def enter_details():
            web = entweb.get()
            uname = entuname.get()
            upass = entpass.get()
            result = ""
            mycur.execute('select * from main_pass1 where email="' + emailid + '" ;')
            for dt in mycur.fetchall():
                s=int(dt[2])
            for i in range(len(upass)):
                char = upass[i]
                result += chr((ord(char) + s - 65) + 65)
            mycur.execute("insert into userpass2(email,sitename,username,passw) values ('" + emailid + "','"+web+"','" + uname + "','" + result + "');")
            mydb.commit()
            entweb.delete(0,tkinter.END)
            entuname.delete(0,tkinter.END)
            entpass.delete(0,tkinter.END)
        for widget in subframe2.winfo_children():
            widget.destroy()
        lblemail = ctk.CTkLabel(master=subframe2, text="Enter your Website or app name", font=("Arial", 30), width=450)
        lblemail.grid(row=0, column=0, padx=30, pady=30)
        entweb = ctk.CTkEntry(master=subframe2, font=("Arial", 30), width=450, placeholder_text_color="red")
        entweb.grid(row=0, column=1, padx=30, pady=30)
        lbluname = ctk.CTkLabel(master=subframe2, text="Enter Your Username ", font=("Arial", 30), width=450)
        lbluname.grid(row=1, column=0, padx=30, pady=30)
        entuname = ctk.CTkEntry(master=subframe2, font=("Arial", 30), width=450)
        entuname.grid(row=1, column=1, padx=30, pady=30)
        lblpass = ctk.CTkLabel(master=subframe2, text="Enter Password", font=("Arial", 30), width=450)
        lblpass.grid(row=2, column=0, padx=30, pady=30)
        entpass = ctk.CTkEntry(master=subframe2, font=("Arial", 30), width=450, show="*")
        entpass.grid(row=2, column=1, padx=30, pady=30)
        tbnsubmit = ctk.CTkButton(master=subframe2, text="Submit", font=("Arial", 35), width=100, fg_color="green",
                                  hover_color="black", height=20,command=enter_details)
        tbnsubmit.grid(row=3, column=1, padx=30, pady=40)
    def show():
        for widget in subframe2.winfo_children():
            widget.destroy()
        def checking():
            upass=entpass.get()
            mycur.execute('select * from main_pass1 where email="' + emailid + '" and Pincode="' + upass + '";')
            for dt in mycur.fetchall():
                if (emailid == dt[0] and upass == dt[2]):
                    converting()
                else:
                    show()
        def converting():
            for dt1 in tree1.get_children():
                tree1.delete(dt1)
            mycur.execute('select * from main_pass1 where email="' + emailid + '" ;')
            for dt in mycur.fetchall():
                s = int(dt[2])
            mycur.execute("Select * from userpass2 where email='" + emailid + "';")
            for dt in mycur.fetchall():
                decry = ""
                if (dt[1] != None):
                    for ddt in dt[3]:
                        for i in range(len(ddt)):
                            char = ddt[i]
                            decry += chr((ord(char) - s + 65) - 65)
                    tree1.insert("", 'end', text=dt[0], values=(dt[0], dt[1], dt[2], decry,))
        tree1 = Treeview(subframe2, height=10, selectmode='browse',)
        tree1.grid(row=0, column=0,columnspan=2)
        tree1['columns'] = ("1", "2", "3", "4")
        tree1['show'] = 'headings'
        tree1.column("1", width=300, anchor='c')
        tree1.column("2", width=300, anchor='c')
        tree1.column("3", width=300, anchor='c')
        tree1.column("4", width=300, anchor='c')
        tree1.heading("1", text='Email')
        tree1.heading("2", text='Site Name')
        tree1.heading("3", text='Username')
        tree1.heading("4", text='Password')
        mycur.execute("Select * from userpass2 where email='"+emailid+"';")
        for dt in mycur.fetchall():
            if(dt[1]!=None):
                tree1.insert("", 'end', text=dt[0], values=(dt[0], dt[1], dt[2], dt[3],))
        lblpassword = ctk.CTkLabel(master=subframe2, text="Enter Your pin to decrypt the passowrd", font=("Arial", 30),width=400)
        lblpassword.grid(row=1, column=0, padx=30, pady=50)
        entpass = ctk.CTkEntry(master=subframe2, font=("Arial", 30), width=100, placeholder_text_color="red",show="*")
        entpass.grid(row=1, column=1, padx=30, pady=50)
        btnconvert=ctk.CTkButton(subframe2,text="Convert",font=("Arial", 35), width=200, fg_color="green",hover_color="black",command=checking)
        btnconvert.grid(row=2,column=0,padx=300,pady=20)
    def passpin():
        def pinpass():
            passw=entpass.get()
            pincode=entpin.get()
            mycur.execute("insert into main_pass1 values ('" + emailid + "','" + passw + "'," + pincode + ");")
            mydb.commit()
            entpass.configure(state=tkinter.DISABLED)
            entpin.configure(state=tkinter.DISABLED)

        for widget in subframe2.winfo_children():
            widget.destroy()
        lblpassword = ctk.CTkLabel(master=subframe2, text="Set your password for decryption", font=("Arial", 30), width=450)
        lblpassword.grid(row=0, column=0, padx=30, pady=50)
        entpass = ctk.CTkEntry(master=subframe2, font=("Arial", 30), width=450, placeholder_text_color="red")
        entpass.grid(row=0, column=1, padx=30, pady=50)
        lblpin = ctk.CTkLabel(master=subframe2, text="Enter your encrypt number ", font=("Arial", 30), width=450)
        lblpin.grid(row=1, column=0, padx=30, pady=50)
        entpin = ctk.CTkEntry(master=subframe2, font=("Arial", 30), width=450)
        entpin.grid(row=1, column=1, padx=30, pady=50)
        tbnsubmit = ctk.CTkButton(master=subframe2, text="Submit", font=("Arial", 35), width=100, fg_color="green",
                                  hover_color="black", height=20,command=pinpass)
        tbnsubmit.grid(row=3, column=1, padx=30, pady=60)

    btnwesbite = ctk.CTkButton(frame, text="Wesbite", font=("airal", 35, "bold"), fg_color="Black", width=180,
                               height=50, hover_color="white", command=website)
    btnwesbite.grid(row=0, column=0, padx=30, pady=60)
    btncard = ctk.CTkButton(frame, text="Card", font=("airal", 35, "bold"), fg_color="Black", width=180, height=50,
                            hover_color="white",command=card)
    btncard.grid(row=0, column=1, padx=30, pady=60)
    subframe1 = ctk.CTkFrame(master=frame, width=400, height=600)
    subframe1.place(x=20, y=130)
    btnshow = ctk.CTkButton(master=subframe1, text="Show", width=350, font=("Arial", 30),command=show)
    btnshow.grid(row=0, column=0, pady=30, padx=10)
    btnenter = ctk.CTkButton(master=subframe1, text="Username Password", width=350, font=("Arial", 30),command=username_password)
    btnenter.grid(row=1, column=0, pady=30, padx=10)
    btnpin = ctk.CTkButton(master=subframe1, text="Password and pin", width=350, font=("Arial", 30),command=passpin)
    btnpin.grid(row=2, column=0, pady=30, padx=10)
    btnquit = ctk.CTkButton(master=subframe1, text="Quit", width=350, font=("Arial", 30),command=loginfrontend)
    btnquit.grid(row=3, column=0, pady=30, padx=10)
    subframe2 = ctk.CTkFrame(master=frame, width=1000, height=400)
    subframe2.place(x=400, y=130)
def card():
    cleanning()
    def username_password():
        def enter_details():
            uname = entuname.get()
            upass = entpass.get()
            result = ""
            mycur.execute('select * from main_pass1 where email="' + emailid + '" ;')
            for dt in mycur.fetchall():
                s = int(dt[2])
            for i in range(len(upass)):
                char = upass[i]
                result += chr((ord(char) + s - 65) + 65)
            print(result)
            mycur.execute("insert into userpass2(email,credit_debit,pin) values ('" + emailid + "'," + uname + ",'" + result + "');")
            mydb.commit()

        for widget in subframe2.winfo_children():
            widget.destroy()
        lbluname = ctk.CTkLabel(master=subframe2, text="Enter Your Card Number ", font=("Arial", 30), width=450)
        lbluname.grid(row=1, column=0, padx=30, pady=30)
        entuname = ctk.CTkEntry(master=subframe2, font=("Arial", 30), width=450)
        entuname.grid(row=1, column=1, padx=30, pady=30)
        lblpass = ctk.CTkLabel(master=subframe2, text="Enter pin", font=("Arial", 30), width=450)
        lblpass.grid(row=2, column=0, padx=30, pady=30)
        entpass = ctk.CTkEntry(master=subframe2, font=("Arial", 30), width=450, show="*")
        entpass.grid(row=2, column=1, padx=30, pady=30)
        tbnsubmit = ctk.CTkButton(master=subframe2, text="Submit", font=("Arial", 35), width=100, fg_color="green",hover_color="black", height=20,command=enter_details)
        tbnsubmit.grid(row=3, column=1, padx=30, pady=40)
    def show():
        for widget in subframe2.winfo_children():
            widget.destroy()
        def checking():
            upass=entpass.get()
            mycur.execute('select * from main_pass1 where email="' + emailid + '" and Pincode="' + upass + '";')
            for dt in mycur.fetchall():
                if (emailid == dt[0] and upass == dt[1]):
                    converting()
                else:
                    show()
        def converting():
            for dt1 in tree1.get_children():
                tree1.delete(dt1)
            mycur.execute('select * from main_pass1 where email="' + emailid + '" ;')
            for dt in mycur.fetchall():
                s = int(dt[2])
            mycur.execute("Select * from userpass2 where email='" + emailid + "';")
            for dt in mycur.fetchall():
                decry = ""
                if (dt[4] != None):
                    for ddt in dt[5]:
                        for i in range(len(ddt)):
                            char = ddt[i]
                            decry += chr((ord(char) - s + 65) - 65)
                    tree1.insert("", 'end', text=dt[0], values=(dt[0], dt[4],decry,))
        tree1 = Treeview(subframe2, height=18, selectmode='browse', )
        tree1.grid(row=0, column=0,columnspan=2)
        tree1['columns'] = ("1", "2", "3")
        tree1['show'] = 'headings'
        tree1.column("1", width=350, anchor='c')
        tree1.column("2", width=350, anchor='c')
        tree1.column("3", width=350, anchor='c')
        tree1.heading("1", text='Email')
        tree1.heading("2", text='Card Number')
        tree1.heading("3", text='Pin')
        mycur.execute("Select * from userpass2 where email='" + emailid + "';")
        for dt in mycur.fetchall():
            if(dt[4]==None):
                break
            tree1.insert("", 'end', text=dt[0], values=(dt[0], dt[4], dt[5],))
        lblpassword = ctk.CTkLabel(master=subframe2, text="Enter Your pin to decrypt the passowrd", font=("Arial", 30),
                                   width=400)
        lblpassword.grid(row=1, column=0, padx=30, pady=50)
        entpass = ctk.CTkEntry(master=subframe2, font=("Arial", 30), width=100, placeholder_text_color="red", show="*")
        entpass.grid(row=1, column=1, padx=30, pady=50)
        btnconvert = ctk.CTkButton(subframe2, text="Convert", font=("Arial", 35), width=200, fg_color="green",
                                   hover_color="black", command=checking)
        btnconvert.grid(row=2, column=0, padx=300, pady=20)
    def passpin():
        for widget in subframe2.winfo_children():
            widget.destroy()
        lblpassword = ctk.CTkLabel(master=subframe2, text="Set your password for decryption", font=("Arial", 30), width=450)
        lblpassword.grid(row=0, column=0, padx=30, pady=50)
        entpass = ctk.CTkEntry(master=subframe2, font=("Arial", 30), width=450, placeholder_text_color="red",state=tkinter.DISABLED)
        entpass.grid(row=0, column=1, padx=30, pady=50)
        lblpin = ctk.CTkLabel(master=subframe2, text="Enter your encrypt number ", font=("Arial", 30), width=450)
        lblpin.grid(row=1, column=0, padx=30, pady=50)
        entpin = ctk.CTkEntry(master=subframe2, font=("Arial", 30), width=450,state=tkinter.DISABLED)
        entpin.grid(row=1, column=1, padx=30, pady=50)

        tbnsubmit = ctk.CTkButton(master=subframe2, text="Submit", font=("Arial", 35), width=100, fg_color="green",
                                  hover_color="black", height=20,command=website)
        tbnsubmit.grid(row=3, column=1, padx=30, pady=60)

    btnwesbite = ctk.CTkButton(frame, text="Wesbite", font=("airal", 35, "bold"), fg_color="Black", width=180,
                               height=50, hover_color="white", command=website)
    btnwesbite.grid(row=0, column=0, padx=30, pady=60)
    btncard = ctk.CTkButton(frame, text="Card", font=("airal", 35, "bold"), fg_color="Black", width=180, height=50,
                            hover_color="white",command=card)
    btncard.grid(row=0, column=1, padx=30, pady=60)
    subframe1 = ctk.CTkFrame(master=frame, width=400, height=600)
    subframe1.place(x=20, y=130)
    btnshow = ctk.CTkButton(master=subframe1, text="Show", width=350, font=("Arial", 30),command=show)
    btnshow.grid(row=0, column=0, pady=30, padx=10)
    btnenter = ctk.CTkButton(master=subframe1, text="Card No and pin", width=350, font=("Arial", 30),command=username_password)
    btnenter.grid(row=1, column=0, pady=30, padx=10)
    btnpin = ctk.CTkButton(master=subframe1, text="Password and pin", width=350, font=("Arial", 30),command=passpin)
    btnpin.grid(row=2, column=0, pady=30, padx=10)
    btnquit = ctk.CTkButton(master=subframe1, text="Quit", width=350, font=("Arial", 30),command=loginfrontend)
    btnquit.grid(row=3, column=0, pady=30, padx=10)
    subframe2 = ctk.CTkFrame(master=frame, width=1000, height=400)
    subframe2.place(x=400, y=130)
label = ctk.CTkLabel(app,text="Password Security")
label.pack(pady=20)
frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=20, fill='both', expand=True)
loginfrontend()
app.mainloop()
