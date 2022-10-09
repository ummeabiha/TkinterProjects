import pyodbc
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
m=Tk()
var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()

def display():
  con = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                      r'DBQ=C:\Users\USER\Desktop\Database.accdb;')
  cur1 = con.cursor()
  cur1.execute('select * from Employee')
  data = cur1.fetchall()
  print("Name","\t","Address")
  if (len(data) != 0):
      for i in data:
          print(i)

      for i in data:
        print(i.get['Name'])
  con.close()

def insert():
 con = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                      r'DBQ=C:\Users\USER\Desktop\Database.accdb;')
 cur1=con.cursor()
 cur1.execute(f"INSERT INTO Employee(emp no,emp name,address,deptid) VALUES('{var1.get()}','{var2.get()}','{var3.get()}','{var4.get()}')")
 con.commit()
 messagebox.showinfo("Insert", "One record has been added")
 display()
 con.close()
def delete():
 con=pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                    r'DBQ=C:\Users\USER\Desktop\Database.accdb;')
 cur1=con.cursor()
 cur1.execute(f"DELETE FROM Employee WHERE emp no={var1.get()}")
 con.commit()
 messagebox.showinfo("Delete","One record has been deleted")
 display()
 con.close()

# FRAMES
l1=Label(m,bg="gold",fg="red",text="Employee Management System",font=("Times New Roman",45),bd=10)
l1.pack(side=TOP,fill=X)
f1=Frame(m,bg="light blue")
f1.place(x=10,y=100,width=450,height=650)
f2=Frame(m,bg="pink")
img1=PhotoImage(file=r'C:\Users\USER\Desktop\ned.png')
img2=img1.subsample(2,2)

# LABEL
l=Label(f1,image=img2).grid(row=0,column=0,padx=50,pady=10,columnspan=2)
l1=Label(f1,bg="gold",fg="red",text="empno",font=("bold"),width=15,bd=15).grid(row=1,column=0,padx=50,pady=10)
l2=Label(f1,bg="gold",fg="red",text="Name",font=("bold"),width=15,bd=15).grid(row=2,column=0,padx=50,pady=10)
l3=Label(f1,bg="gold",fg="red",text="Address",font=("bold"),width=15,bd=15).grid(row=3,column=0,padx=50,pady=10)
l4=Label(f1,bg="gold",fg="red",text="Deptid",font=("bold"),width=15,bd=15).grid(row=4,column=0,padx=50,pady=10)

# ENTRY
e1=Entry(f1,bg="red",fg="white",textvariable=var1,width=15,bd=10).grid(row=1,column=1)
e2=Entry(f1,bg="red",fg="white",textvariable=var2,width=15,bd=10).grid(row=2,column=1)
e3=Entry(f1,bg="red",fg="white",textvariable=var3,width=15,bd=10).grid(row=3,column=1)
e4=Entry(f1,bg="red",fg="white",textvariable=var4,width=15,bd=10).grid(row=4,column=1)

# BUTTONS
b1=Button(f1,text="Display",bg="blue",fg="white",font=("bold"),width=15,bd=10,command=display).grid(row=5,column=0)
b2=Button(f1,text="Insert",bg="blue",fg="white",font=("bold"),width=15,bd=10,command=insert).grid(row=6,column=0)
b3=Button(f1,text="Delete",bg="blue",fg="white",font=("bold"),width=15,bd=10,command=delete).grid(row=7,column=0)
b4=Button(f1,text="Update",bg="blue",fg="white",font=("bold"),width=15,bd=10).grid(row=8,column=0)

f2.place(x=450,y=100,width=900,height=700)

stable=ttk.Treeview(f2,height=900,columns=("emp no","emp name","address","deptid"))


stable.pack()
m.mainloop()
