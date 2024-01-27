from datetime import datetime
import mysql.connector as mycon
db=mycon.connect(host="localhost",user="root",password="ani*2004",database="parking_management")
cur=db.cursor()


def entry():
 insert_stmt=("insert into user values(%s,%s,%s,%s,NULL)")
 global rno
 rno=int(input("enter rollno:"))

 vno=int(input("enetr vehicle no"))
 global sno
 sno=int(input("enter spot no"))
 now = datetime.now()
 dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
 t=dt_string
 data=(rno,sno,vno,t)
 cur.execute(insert_stmt,data)
 modifier()
 rolladder()
 db.commit()
 

def checkspot():
    cur.execute("select spot_no from spotter where availability='available'") 
    result=cur.fetchall()
    for x in result:
        print(x)
def modifier():
  upt=("update spotter set availability='occupied' where spot_no=%s")
  spot=[sno]
  cur.execute(upt,spot)
def rolladder():
    upt=("update spotter set rollno=%s where spot_no=%s")
    s=(rno,sno)
    cur.execute(upt,s)

def exit():
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    et=dt_string
    roll=int(input("enter roll no:" ))
    t=[et,roll]
    upt=("update user set exit_time=%s where rollno=%s")
    cur.execute(upt,t)
    r=[roll]
    upd=("update spotter set availability='available',rollno=0 where rollno=%s")
    cur.execute(upd,r)
    db.commit()
checkspot()
while input(" y- to add another data \n n- to close\n")=='y':
 
   
 op=int(input("\n 1.entry\n2.exit\n"))
 if op==1:
    entry()
 elif op==2:
    exit()
 else:
    print("enter 1 or 2")



