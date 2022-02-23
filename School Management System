import pyodbc
from tkinter import*

m=Tk()
m.config(background="lemon chiffon")

def maths():
    math_f=Frame(m,bg="lemon chiffon")
    math_f.place(x=450,y=100,width=900,height=700)

    con = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                         r'DBQ=C:\Users\USER\Desktop\School.accdb;')
    cur = con.cursor()
    cur.execute('select * from Maths')
    data = cur.fetchall()
    no=len(data)
    for i in data:
        math_l = Label(math_f, text="MATHS", font=("Times New Roman", 25, "bold"), bg="lemon chiffon")
        math_l.grid(row=0, column=2, padx=50, pady=30)
        teacher_l=Label(math_f,text="Teachers",font=("Arial 15"),bg="lemon chiffon")
        teacher_l.grid(row=1, column=2, padx=50, pady=30)
        time_l = Label(math_f, text="Timings", font=("Arial 15"),bg="lemon chiffon")
        time_l.grid(row=1, column=3, padx=50, pady=30)
        math_label=Label(math_f,text=i[0],font=("Arial 15"),bg="lemon chiffon")
        math_label.grid(row=no,column=2,padx=50,pady=30)
        timings_label=Label(math_f,text=i[1],font=("Arial 15"),bg="lemon chiffon")
        timings_label.grid(row=no,column=3)
        no=no+2
    con.close()

def phy():
    phy_f = Frame(m, bg="lemon chiffon")
    phy_f.place(x=450, y=100, width=900, height=700)

    con = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                         r'DBQ=C:\Users\USER\Desktop\School.accdb;')
    cur = con.cursor()
    cur.execute('select * from Phy')
    record = cur.fetchall()
    no=len(record)
    for i in record:
        phy_l = Label(phy_f, text="PHYSICS", font=("Times New Roman", 25, "bold"), bg="lemon chiffon")
        phy_l.grid(row=0, column=2, padx=50, pady=30)
        teacher_l=Label(phy_f,text="Teachers",font=("Arial 15"),bg="lemon chiffon")
        teacher_l.grid(row=1, column=2, padx=50, pady=30)
        time_l = Label(phy_f, text="Timings", font=("Arial 15"),bg="lemon chiffon")
        time_l.grid(row=1, column=3, padx=50, pady=30)
        phy_label=Label(phy_f,text=i[0],font=("Arial 15"),bg="lemon chiffon")
        phy_label.grid(row=no,column=2,padx=50,pady=30)
        timings_label=Label(phy_f,text=i[1],font=("Arial 15"),bg="lemon chiffon")
        timings_label.grid(row=no,column=3)
        no=no+2

    con.close()


def chem():
    chem_f = Frame(m, bg="lemon chiffon")
    chem_f.place(x=450, y=100, width=900, height=700)

    con = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                         r'DBQ=C:\Users\USER\Desktop\School.accdb;')
    cur = con.cursor()
    cur.execute('select * from Chem')
    db = cur.fetchall()
    no=len(db)
    for i in db:
        chem_l=Label(chem_f,text="CHEMISTRY",font=("Times New Roman", 25,"bold"),bg="lemon chiffon")
        chem_l.grid(row=0, column=2, padx=50, pady=30)
        teacher_l=Label(chem_f,text="Teachers",font=("Arial 15"),bg="lemon chiffon")
        teacher_l.grid(row=1, column=2, padx=50, pady=30)
        time_l = Label(chem_f, text="Timings", font=("Arial 15"),bg="lemon chiffon")
        time_l.grid(row=1, column=3, padx=50, pady=30)
        chem_label=Label(chem_f,text=i[0],font=("Arial 15"),bg="lemon chiffon")
        chem_label.grid(row=no,column=2,padx=50,pady=30)
        timings_label=Label(chem_f,text=i[1],font=("Arial 15"),bg="lemon chiffon")
        timings_label.grid(row=no,column=3)
        no=no+2
    con.close()


def comp():
    comp_f = Frame(m, bg="lemon chiffon")
    comp_f.place(x=450, y=100, width=900, height=700)

    con = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                         r'DBQ=C:\Users\USER\Desktop\School.accdb;')
    cur = con.cursor()
    cur.execute('select * from Comp')
    de = cur.fetchall()
    no=len(de)
    for i in de:
        comp_l=Label(comp_f,text="COMPUTER",font=("Times New Roman", 25,"bold"),bg="lemon chiffon")
        comp_l.grid(row=0, column=2, padx=50, pady=30)
        name_l=Label(comp_f,text="Teachers",font=("Arial 15"),bg="lemon chiffon")
        name_l.grid(row=1, column=2, padx=50, pady=30)
        time_l = Label(comp_f, text="Timings", font=("Arial 15"),bg="lemon chiffon")
        time_l.grid(row=1, column=3, padx=50, pady=30)
        comp_label=Label(comp_f,text=i[0],font=("Arial 15"),bg="lemon chiffon")
        comp_label.grid(row=no,column=2,padx=50,pady=30)
        timings_label=Label(comp_f,text=i[1],font=("Arial 15"),bg="lemon chiffon")
        timings_label.grid(row=no,column=3)
        no=no+2
    con.close()


l1=Label(m,bg="salmon",fg="White",text="THE SMART SCHOOL",font=("Times New Roman",45),bd=10)
l1.pack(side=TOP,fill=X)
f1=Frame(m,bg="peach puff")
f1.place(x=10,y=100,width=450,height=650)

img=PhotoImage(file=r"C:\Users\USER\Desktop\school.png")
img_s=img.subsample(1,1)
img_l=Label(f1,image=img_s)
img_l.grid(row=0,column=0,padx=50,pady=10,columnspan=2)

l2=Label(f1,bg="lavender blush",fg="sandy brown",text="FACULTY",font=("Times New Roman",15,"bold"),width=12,bd=15)
l2.grid(row=1,column=0,padx=40,pady=10)
b1=Button(f1,text="Maths",bg="gainsboro",fg="black",font=("bold"),width=15,bd=10,command=maths).grid(row=5,column=0)
b2=Button(f1,text="Physics",bg="gainsboro",fg="black",font=("bold"),width=15,bd=10,command=phy).grid(row=6,column=0)
b3=Button(f1,text="Chemistry",bg="gainsboro",fg="black",font=("bold"),width=15,bd=10,command=chem).grid(row=7,column=0)
b4=Button(f1,text="Computer",bg="gainsboro",fg="black",font=("bold"),width=15,bd=10,command=comp).grid(row=8,column=0)


m.mainloop()
