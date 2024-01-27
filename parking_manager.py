import tkinter,customtkinter
from tkinter import *
from datetime import datetime
import mysql.connector as mycon
db=mycon.connect(host="localhost",user="root",password="test123",database="parking_management")
cur=db.cursor()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def entry():
 insert_stmt=("insert into user values(%s,%s,%s,%s,NULL)")
 global rno
 rno=int(rne.get())

 vno=int(vne.get())
 global sno
 sno=int(spne.get())
 now = datetime.now()
 dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
 t=dt_string
 data=(rno,sno,vno,t)
 cur.execute(insert_stmt,data)
 modifier()
 rolladder()
 db.commit()
 rne.delete(0, customtkinter.END)
 vne.delete(0, customtkinter.END)
 spne.delete(0, customtkinter.END)
 
def checkspot():
    cur.execute("select spot_no from spotter where availability='available'") 
    result=cur.fetchall()
    
    
def modifier():
  upt=("update spotter set availability='occupied' where spot_no=%s")
  spot=[sno]
  cur.execute(upt,spot)
def rolladder():
    upt=("update spotter set rno=%s where spot_no=%s")
    s=(rno,sno)
    cur.execute(upt,s)

def exit():
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    et=dt_string
    roll=int(erne.get())
    t=[et,roll]
    upt=("update user set exit_time=%s where rno=%s")
    cur.execute(upt,t)
    r=[roll]
    upd=("update spotter set availability='available',rno=0 where rno=%s")
    cur.execute(upd,r)
    db.commit()
    erne.delete(0, customtkinter.END)
checkspot()


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
app= customtkinter.CTk()
app.geometry("568x400")

#appearance
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#ui elements

l1=customtkinter.CTkLabel(app,text="Parkingmanager",font=('calibre',30, 'bold'))
l1.pack()
entl=customtkinter.CTkLabel(app,text="ENTRY",font=('calibre',16, 'bold'))
entl.place(x=60,y=55)



rnl=customtkinter.CTkLabel(app,text="roll_no")
rnl.place(x=20,y=85)
rne=customtkinter.CTkEntry(app)
rne.place(x=80,y=85)

vnl=customtkinter.CTkLabel(app,text="veh_no")
vnl.place(x=20,y=115)
vne=customtkinter.CTkEntry(app)
vne.place(x=80,y=115)

spnl=customtkinter.CTkLabel(app,text="spot_no")
spnl.place(x=20,y=145)
spne=customtkinter.CTkEntry(app)
spne.place(x=80,y=145)

b1=customtkinter.CTkButton(app,text="Submit",command=entry)
b1.place(x=55,y=180)

exl=customtkinter.CTkLabel(app,text="EXIT",font=('calibre',16, 'bold'))
exl.place(x=60,y=230)

ernl=customtkinter.CTkLabel(app,text="roll_no")
ernl.place(x=20,y=255)
erne=customtkinter.CTkEntry(app)
erne.place(x=80,y=255)

b1=customtkinter.CTkButton(app,text="Submit",command=exit)
b1.place(x=55,y=295)


#app frame



#run app 
app.mainloop()