from tkinter import *
from mysqlx import Statement
from tkcalendar import Calendar, DateEntry
from PIL import Image, ImageTk


from tkinter import messagebox

# import sqlite3 
# import regisdb








special_ch= ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*',  '-', '_', '+', '=',  '[', ']', '|', '\\', '/', ':', ';', '"', "'", '<', '>', ',', '.', '?']


global entry21
global entry22



def login():
    username=entry21.get()
    password=entry22.get()
    


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
        #    hi=Tk()
        #    hi.resizable(FALSE,False)
        #    hi.geometry('1200x670+230+50')
        #    label=Label(hi,text='k xa nigga').grid(row=1,column=1)

        #    hi.mainloop()
           messagebox.showinfo('',"Success")


           
        else:
            messagebox.showerror('','Incorrect Username and Password ')
            entry21.delete(0,END)
            entry22.delete(0,END)
    

        
            
        



               
    
   

def register():
    entry51=entry3.get()
    entry52=entry4.get()
    entry53=cal.get()
    entry54=entry6.get()
    entry55=entry7.get()
    entry56=entry50.get()



        
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


                # entry51.delete(0,END)
                # entry52.delete(0,END)
                # entry53.delete(0,END)
                # entry54.delete(0,END)
                # entry55.delete(0,END)
                # entry56.delete(0,END)
                 
           

            
    except Exception as ep:
        messagebox.showerror('error', ep)

    



window = Tk()
window.title('LOGIN')

window.resizable(FALSE,False)
window.geometry('1000x670+230+50')
