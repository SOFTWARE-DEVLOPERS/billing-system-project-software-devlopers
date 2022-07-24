from email import message
from logging import exception
from tkinter import *

from mysqlx import Statement
from tkcalendar import Calendar, DateEntry
from PIL import Image, ImageTk


from tkinter import messagebox

import sqlite3 
import regisdb














special_ch= ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*',  '-', '_', '+', '=',  '[', ']', '|', '\\', '/', ':', ';', '"', "'", '<', '>', ',', '.', '?']


global entry21
global entry22
global entry51
global entry52
global entry53
global entry54
global entry55
global entry56






    


    

    

  





def login():
    username=entry21.get()
    password=entry22.get()
    
    #exception handling


    try:


        if (username=="" and password==''):
           messagebox.showinfo('error','Enter your username and password')
        
    


        elif(username!='' and  password==''):
           messagebox.showinfo('','Enter your password')
           entry22.delete(0,END)

        elif(username==''  and password!=''):
           messagebox.showinfo('','Enter your username')
           entry21.delete(0,END)
        else:
         with sqlite3.connect('regis.db') as db:
            c=db.cursor()
            find_user=('select * from regis where Username=? and Confirm_password=?')
            c.execute(find_user,(username,password))
            result=c.fetchall()
            if result:
        
               messagebox.showinfo('','logged in successfully')
               
           
            
              
        
           
            else:
               messagebox.showerror('','Incorrect Username and Password ')
               entry21.delete(0,END)
               entry22.delete(0,END)
    except exception as ep:
        messagebox.showerror('error',ep)





    


    

    

    
    

        
            









     




def toggle():
    if show_pass.get() == 1:
        entry22.config(show= '')
    else:
        entry22.config(show= '*')

def toggle1():
    if show_pass1.get() == 1:
        entry7.config(show= '')
    else:
        entry7.config(show= '*')

def toggle2():
    if show_pass2.get() == 1:
        entry50.config(show= '')
    else:
        entry50.config(show= '*')
               
            
    
   

def register():
    entry51=entry3.get()
    entry52=entry4.get()
    entry53=cal.get()
    entry54=entry6.get()
    entry55=entry7.get()
    entry56=entry50.get()

    

#exception handling

        
    try:
             
            if entry51=='' or entry52=='' or entry53=='' or entry54=='' or entry55==''or entry56=='':
                messagebox.showinfo(" ", 'Fill all the credentials')

           
                    


            elif(len(entry51))>35:
                messagebox.showinfo(" ",'Enter a valid first name')

            

            elif(len(entry52))>35:
                messagebox.showinfo(" "',Enter a valid last name')

           
           
            elif len(entry54)>20:
                messagebox.showinfo(" ",'Too long username')

           


            
            elif not any(ch in special_ch for ch in entry55):
                messagebox.showinfo (" ",'Atleast one symbolic character is required in password!')
                
           
            
            elif len(entry55) < 8 or len(entry55)>15:
                messagebox.showinfo (" ",'Password must be minimum of 8 characters and maximum of 15 characters!')


            elif(entry55)!=entry56:
                messagebox.showerror(" ","Password doesn't matched!!")


            else:
                db=sqlite3.connect('regis.db')
                cr=db.cursor()
                cr.execute(
                "select * from 'regis' WHERE Username='" +entry54+"'")
                r=cr.fetchone()
                if r!=None:
                    messagebox.showerror(" ",'Username already existed')
                else:
                    regisdb.insert(entry51,entry52,entry53,entry54,entry55,entry56)
                    messagebox.showinfo('SUCCESS','Registration Success')
                db.commit()


               
                 
           

            
    except Exception as ep:
        messagebox.showerror('error', ep)

    


#creating a main window
window = Tk()
window.title('LOGIN')

window.resizable(FALSE,False)
window.geometry('1000x670+230+50')


#for signup 
def create():
    global editor
    editor = Toplevel(window)
    global entry3
    global entry4
    global cal
    global entry6
    global entry7
    global entry50
    

    editor.title('SIGN UP')
    editor.geometry("700x600+400+70")
    editor.resizable(FALSE,False)
    ag = PhotoImage(file="C:\\Users\\ittra\\OneDrive\\Desktop\\photos for tkinter\\screen3.png")
    my_label1 = Label(editor, image=ag)


    frame1 = Frame(editor, bg='white').place(x=260, y=100, width=250, height=400)
    label2 = Label(editor, text='SIGN UP', font=20, fg='blue', bg='white').place(x=340, y=110)
    label3 = Label(editor, text='First name', fg='black', bg='white')
    label3.place(x=292, y=140)
    signup_btn = PhotoImage(file="C:\\Users\\ittra\\OneDrive\\Desktop\\photos for tkinter\\signup4.png")
    label10=PhotoImage(file="C:\\Users\\ittra\\OneDrive\\Desktop\\photos for tkinter\\entry.png")
    hi=Label(editor,image=label10,bg='white').place(x=290,y=156)
    label11=PhotoImage(file="C:\\Users\\ittra\\OneDrive\\Desktop\\photos for tkinter\\entry.png")
    hii=Label(editor,image=label11,bg='white').place(x=290,y=205)
    label12=PhotoImage(file="C:\\Users\\ittra\\OneDrive\\Desktop\\photos for tkinter\\entry.png")
    hiii=Label(editor,image=label12,bg='white').place(x=290,y=255)
    label13=PhotoImage(file="C:\\Users\\ittra\\OneDrive\\Desktop\\photos for tkinter\\entry.png")
    hiiii=Label(editor,image=label13,bg='white').place(x=290,y=305)
    label14=PhotoImage(file="C:\\Users\\ittra\\OneDrive\\Desktop\\photos for tkinter\\entry.png")
    hope=Label(editor,image=label14,bg='white').place(x=290,y=355)
    

    imgg = Button(editor, image=signup_btn,command=register, borderwidth=0).place(x=320, y=440)
    entry3 = Entry(editor, fg='black', bg='white')
    entry3.place(x=300, y=160)
    label4 = Label(editor, text='Last name', fg='black', bg='white').place(x=292, y=184)
    entry4 = Entry(editor, fg='black', bg='white')
    entry4.place(x=300, y=210)
    label5 = Label(editor, text='Date of birth', fg='black', bg='white').place(x=292, y=235)
    cal = DateEntry(editor,width=17,bd=2,  background= "grey", foreground= "white")
    cal.place(x=300,y=260)
    
    label6 = Label(editor, text='Create your username', fg='black', bg='white').place(x=292, y=285)
    entry6 = Entry(editor, fg='black', bg='white')
    entry6.place(x=300, y=310)
    label = Label(editor, text='Enter Password', fg='black', bg='white').place(x=292, y=335)
    entry7 = Entry(editor, fg='black', bg='white', show='*')
    entry7.place(x=300, y=360)
    
    
    label114=PhotoImage(file="C:\\Users\\ittra\\OneDrive\\Desktop\\photos for tkinter\\entry.png")
    hopeeee=Label(editor,image=label114,bg='white').place(x=290,y=405)
    label50 = Label(editor, text='Confirm Password', fg='black', bg='white').place(x=292, y=385)
    entry50 = Entry(editor,fg='black', bg='white', show='*')
    entry50.place(x=300, y=410)
    global show_pass1

    global show_pass2
    
    show_pass1=IntVar()
    show_pass2=IntVar()
    
 
    
    checkbutton1 = Checkbutton (editor,bg='white',variable=show_pass1,command=toggle1)
    lebeelll1=Label(editor,text='show',bg='white')
    lebeelll1.place(x=465,y=355)
    checkbutton1.place(x=437,y=355)
    checkbutton2 = Checkbutton (editor,bg='white',variable=show_pass2,command=toggle2)
    lebeelll2=Label(editor,text='show',bg='white')
    lebeelll2.place(x=465,y=410)
    checkbutton2.place(x=437,y=405)
    

    my_label1.pack()
    editor.mainloop()




 
 



    
#for login page

bg = PhotoImage(file="C:\\Users\\ittra\\OneDrive\\Desktop\\photos for tkinter\\screen2.png")
my_label = Label(window, image=bg)
frame = Frame(window, bg='white').place(x=350, y=100, width=300, height=500)
image1 = Image.open(r"C:\Users\ittra\OneDrive\Desktop\photos for tkinter\user4.png")
photoimage1 = ImageTk.PhotoImage(image1)
labelimg1 = Label(image=photoimage1, bg='white', fg='white', borderwidth=0).place(x=460, y=105)
label = Label(window, text='GET STARTED', font=(20), fg='blue', bg='white').place(x=440, y=170)
label1 = Label(window, text='Username', bg='white').place(x=457, y=215)
label8=PhotoImage(file="C:\\Users\\ittra\\OneDrive\\Desktop\\photos for tkinter\\entry1.png")
label=Label(window,image=label8,bg='white').place(x=451,y=235)
label9=PhotoImage(file="C:\\Users\\ittra\\OneDrive\\Desktop\\photos for tkinter\\entry1.png")
label=Label(window,image=label8,bg='white').place(x=451,y=280)

entry21 = Entry(window, fg='black', bg='white')
entry21.place(x=460, y=240)
label2 = Label(window, text='Password', bg='white').place(x=458, y=262)
entry22 = Entry(window, fg='black', bg='white', show='*')
entry22.place(x=460, y=285)





image2= Image.open(r"C:\\Users\\ittra\\OneDrive\\Desktop\\photos for tkinter\\men2.png")
photoimage2 = ImageTk.PhotoImage(image2)
labelimg2 = Label(image=photoimage2, bg='white', fg='white', borderwidth=0).place(x=420, y=238)
image3 = Image.open(r"C:\\Users\\ittra\\OneDrive\\Desktop\\photos for tkinter\\lock1.png")
photoimage3 = ImageTk.PhotoImage(image3)
labelimg3 = Label(image=photoimage3, bg='white', fg='white', borderwidth=0).place(x=420, y=283)
login_btn = PhotoImage(file="C:\\Users\\ittra\\OneDrive\\Desktop\\photos for tkinter\\button6.png") 
img = Button(window, image=login_btn,command=login,borderwidth=0).place(x=470, y=345)

label3 = Label(window, text="Don't have a account?", fg='black', bg='white').place(x=425, y=390)
button2 = Button(window, text='Sign up here', fg='blue', bg='white', borderwidth=0, command=create).place(x=560, y=390)
show_pass= IntVar()





checkbutton = Checkbutton (window,bg='white',variable=show_pass,command=toggle)
lebeelll=Label(window,text='show password',bg='white')
lebeelll.place(x=500,y=312)
checkbutton.place(x=470,y=310)




my_label.pack()


window.mainloop()


#creating a  database

import sqlite3
conn=sqlite3.connect("regis.db")
conn.execute("create table if not exists regis(First_name text,Last_name text,Date_of_birth text ,Username text , Enter_password text, Confirm_Password text)")



def insert(First_name ,Last_name ,Date_of_birth  ,Username  , Enter_password , Confirm_Password):

    query="insert into regis(First_name ,Last_name ,Date_of_birth  ,Username  , Enter_password , Confirm_Password) values(?,?,?,?,?,?)"
    conn.execute(query,(First_name ,Last_name ,Date_of_birth  ,Username  , Enter_password , Confirm_Password))
    conn.commit()

conn.commit()
conn.close()



#for Billing dashboard

from tkinter import*
from tkinter import messagebox

root=Tk()
root.geometry ("1000x500")
root. title ("Bill Management")
root. resizable(False,False)

def Reset():
    entry_Noddles.delete(0, END)
    entry_Biscuits.delete(0, END)
    entry_Bread.delete(0, END)
    entry_Eggs.delete(0, END)
    entry_Chips.delete(0, END)
    entry_Chocolate.delete(0, END)
    entry_Milk.delete(0, END)

def Total():
    try:a1=int (Noddles.get())
    except: a1=0
    try:a2=int (Biscuits.get())
    except: a2=0
    try: a3=int (Eggs.get())
    except: a3=0
    try: a4=int (Chips.get ())
    except: a4=0
    try: a5=int (Chocolate.get())
    except: a5=0
    try:a6=int(Bread.get())
    except:a6=0
    try:a7=int(Milk.get())
    except:a7=0
    


    p1 = 20 * a1
    p2 = 10 * a2
    p3 = 15 * a3
    p4 = 30 * a4
    p5 = 50 * a5
    p6 = 35 * a6
    p7 = 80 * a7


    total = Label(f2, font=('aria', 20, 'bold'), text="Total", width=16, fg="lightyellow", bg="black")
    total.place(x=0, y=50)
    entry_total = Entry(f2, font=('aria', 20, 'bold'), textvariable=Total_bill, bd = 6, width = 15, bg = "lightgreen")
    entry_total.place(x=20, y=100)
    totalcost= p1+p2+p3+p4+p5+p6+p7
    string_bill="Rs.",str('%.2f'%totalcost)
    Total_bill.set(string_bill)

#Heading
Label(text="BILL MANAGEMENT", bg="black", fg="white", font= ("calibri", 33) , width="300", height="2"). pack()

#MENU CARD
f=Frame (root, bg="lightyellow", highlightbackground="black",highlightthickness=1, width=300, height=370)
f.place(x=10,y=118)
Label (f, text="Items", font= ("Gabriola", 40, "bold"), fg="black", bg="lightyellow") .place(x=80,y=0)
Label(f, font=("Lucida" ,15, 'bold'),text="Noddles. ......Rs.20 perPiece",fg="black",bg="lightyellow").place(x=10,y=80)
Label(f, font=("Lucida" ,15, 'bold'),text="Biscuit. ......Rs.10 perPiece",fg="black",bg="lightyellow").place(x=10,y=110)
Label(f, font=("Lucida" ,15, 'bold'),text="Egg. ......Rs.15 perPiece",fg="black",bg="lightyellow").place(x=10,y=140)
Label(f, font=("Lucida" ,15, 'bold'),text="Chips . ......Rs.30 perPiece",fg="black",bg="lightyellow").place(x=10,y=170)
Label(f, font=("Lucida" ,15, 'bold'),text="Chocolate. ......Rs.50 perPiece",fg="black",bg="lightyellow").place(x=10,y=200)
Label(f, font=("Lucida" ,15, 'bold'),text="Bread . ......Rs.35 perPiece",fg="black",bg="lightyellow").place(x=10,y=230)
Label(f, font=("Lucida" ,15, 'bold'),text="Milk. .....Rs.80 perLitre",fg="black",bg="lightyellow").place(x=10,y=260)

#ENTRY WORK
f1=Frame (root, bd=5, height=370, width=300, relief=RAISED)
f1.pack()
Noddles=StringVar()
Biscuits=StringVar()
Eggs=StringVar()
Chips=StringVar()
Chocolate=StringVar()
Bread=StringVar()
Milk=StringVar()
Total_bill=StringVar()

f2=Frame(root, bg="lightyellow", highlightbackground="black" ,highlightthickness=1,width=300, height=370)
f2. place(x=690,y=118)
Bill=Label(f2, text="Bill", font= ('calibri',20,'bold'),bg="lightgreen")
Bill.place(x=120,y=10)

#Label
label_Noddles=Label(f1, font=("aria", 20, 'bold'), text= "Noodles", width=12, fg="BlACK").grid(row=1,column=0)
label_Biscuits=Label(f1, font=("aria", 20, 'bold'), text= "Biscuit", width=12, fg="BlACK").grid(row=2,column=0)
label_Eggs=Label(f1, font=("aria", 20, 'bold'), text= "Eggs", width=12, fg="BlACK").grid(row=3,column=0)
label_Chips=Label(f1, font=("aria", 20, 'bold'), text= "Chips", width=12, fg="BlACK").grid(row=4,column=0)
label_Chocolate=Label(f1, font=("aria", 20, 'bold'), text= "Chocolate", width=12, fg="BlACK").grid(row=5,column=0)
label_Bread=Label(f1, font=("aria", 20, 'bold'), text= "Bread", width=12, fg="BlACK").grid(row=6,column=0)
label_Milk=Label(f1, font=("aria", 20, 'bold'), text= "Milk", width=12, fg="BlACK").grid(row=7,column=0)


#Entry
entry_Noddles=Entry(f1, font=("aria",20, 'bold'), textvariable=Noddles, bd=6,width=8,bg="silver")
entry_Noddles.grid(row=1,column=1)
entry_Biscuits=Entry(f1, font=("aria",20, 'bold'), textvariable=Biscuits, bd=6,width=8,bg="silver")
entry_Biscuits.grid(row=2,column=1)
entry_Eggs=Entry(f1, font=("aria",20, 'bold'), textvariable=Eggs, bd=6,width=8,bg="silver")
entry_Eggs.grid(row=3,column=1)
entry_Chips=Entry(f1, font=("aria",20, 'bold'), textvariable=Chips, bd=6,width=8,bg="silver")
entry_Chips.grid(row=4,column=1)
entry_Chocolate=Entry(f1, font=("aria",20, 'bold'), textvariable=Chocolate, bd=6,width=8,bg="silver")
entry_Chocolate.grid(row=5,column=1)
entry_Bread=Entry(f1, font=("aria",20, 'bold'), textvariable=Bread, bd=6,width=8,bg="silver")
entry_Bread.grid(row=6,column=1)
entry_Milk=Entry(f1, font=("aria",20, 'bold'), textvariable=Milk, bd=6,width=8,bg="silver")
entry_Milk.grid(row=7,column=1)

#button

btn_reset=Button (f1,bd=5, fg="black",bg="lightblue",font=("ariel",16, 'bold'), width=10, text="Reset",command=Reset)
btn_reset.grid(row=8, column=0)

btn_total=Button(f1,bd=5, fg="black", bg="lightblue", font=("ariel", 16, 'bold' ), width=10, text="Total", command=Total)
btn_total.grid(row=8,column=1)


root.mainloop()
