import pyodbc
from tkinter import*

m=Tk()
m.config(background="peachpuff")
m.title("City Hospital")
m.state('zoomed')

def dentist():
    dentist_f=Frame(m,bg="peachpuff")
    dentist_f.place(x=450,y=100,width=900,height=700)

    con = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                         r'DBQ=C:\Users\USER\Desktop\Hospital.accdb;')
    cur = con.cursor()
    cur.execute('select * from Dentist')
    data = cur.fetchall()
    no=len(data)
    for i in data:
        dentist_l = Label(dentist_f, text="DENTIST", font=("Times New Roman", 25, "bold"), bg="peachpuff")
        dentist_l.grid(row=0, column=2, padx=50, pady=30)
        dr_l=Label(dentist_f,text="Doctor",font=("Arial 15"),bg="peachpuff")
        dr_l.grid(row=1, column=2, padx=50, pady=30)
        time_l = Label(dentist_f, text="Timings", font=("Arial 15"),bg="peachpuff")
        time_l.grid(row=1, column=3, padx=50, pady=30)
        dentist_label=Label(dentist_f,text=i[0],font=("Arial 15"),bg="peachpuff")
        dentist_label.grid(row=no,column=2,padx=50,pady=30)
        timings_label=Label(dentist_f,text=i[1],font=("Arial 15"),bg="peachpuff")
        timings_label.grid(row=no,column=3)
        no=no+2
    con.close()

def eye():
    eye_f = Frame(m, bg="peachpuff")
    eye_f.place(x=450, y=100, width=900, height=700)

    con = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                         r'DBQ=C:\Users\USER\Desktop\Hospital.accdb;')
    cur = con.cursor()
    cur.execute('select * from Eye')
    record = cur.fetchall()
    no=len(record)
    for i in record:
        eye_l = Label(eye_f, text="EYE", font=("Times New Roman", 25, "bold"), bg="peachpuff")
        eye_l.grid(row=0, column=2, padx=50, pady=30)
        dr_l=Label(eye_f,text="Doctor",font=("Arial 15"),bg="peachpuff")
        dr_l.grid(row=1, column=2, padx=50, pady=30)
        time_l = Label(eye_f, text="Timings", font=("Arial 15"),bg="peachpuff")
        time_l.grid(row=1, column=3, padx=50, pady=30)
        eye_label=Label(eye_f,text=i[0],font=("Arial 15"),bg="peachpuff")
        eye_label.grid(row=no,column=2,padx=50,pady=30)
        timings_label=Label(eye_f,text=i[1],font=("Arial 15"),bg="peachpuff")
        timings_label.grid(row=no,column=3)
        no=no+2

    con.close()


def heart():
    heart_f = Frame(m, bg="peachpuff")
    heart_f.place(x=450, y=100, width=900, height=700)

    con = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                         r'DBQ=C:\Users\USER\Desktop\Hospital.accdb;')
    cur = con.cursor()
    cur.execute('select * from Heart')
    db = cur.fetchall()
    no=len(db)
    for i in db:
        heart_l=Label(heart_f,text="HEART",font=("Times New Roman", 25,"bold"),bg="peachpuff")
        heart_l.grid(row=0, column=2, padx=50, pady=30)
        dr_l=Label(heart_f,text="Doctors",font=("Arial 15"),bg="peachpuff")
        dr_l.grid(row=1, column=2, padx=50, pady=30)
        time_l = Label(heart_f, text="Timings", font=("Arial 15"),bg="peachpuff")
        time_l.grid(row=1, column=3, padx=50, pady=30)
        heart_label=Label(heart_f,text=i[0],font=("Arial 15"),bg="peachpuff")
        heart_label.grid(row=no,column=2,padx=50,pady=30)
        timings_label=Label(heart_f,text=i[1],font=("Arial 15"),bg="peachpuff")
        timings_label.grid(row=no,column=3)
        no=no+2
    con.close()


def kidney():
    kidney_f = Frame(m, bg="peachpuff")
    kidney_f.place(x=450, y=100, width=900, height=700)

    con = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                         r'DBQ=C:\Users\USER\Desktop\Hospital.accdb;')
    cur = con.cursor()
    cur.execute('select * from Kidney')
    de = cur.fetchall()
    no=len(de)
    for i in de:
        kidney_l=Label(kidney_f,text="KIDNEY",font=("Times New Roman", 25,"bold"),bg="peachpuff")
        kidney_l.grid(row=0, column=2, padx=50, pady=30)
        name_l=Label(kidney_f,text="Doctors",font=("Arial 15"),bg="peachpuff")
        name_l.grid(row=1, column=2, padx=50, pady=30)
        time_l = Label(kidney_f, text="Timings", font=("Arial 15"),bg="peachpuff")
        time_l.grid(row=1, column=3, padx=50, pady=30)
        doctor_label=Label(kidney_f,text=i[0],font=("Arial 15"),bg="peachpuff")
        doctor_label.grid(row=no,column=2,padx=50,pady=30)
        timings_label=Label(kidney_f,text=i[1],font=("Arial 15"),bg="peachpuff")
        timings_label.grid(row=no,column=3)
        no=no+2
    con.close()


l1=Label(m,bg="Indian red",fg="White",text="CITY HOSPITAL",font=("Times New Roman",45),bd=10)
l1.pack(side=TOP,fill=X)
f1=Frame(m,bg="light blue")
f1.place(x=10,y=100,width=450,height=650)

img=PhotoImage(file=r"C:\Users\USER\Desktop\hospital.png")
img_s=img.subsample(3,3)
img_l=Label(f1,image=img_s)
img_l.grid(row=0,column=0,padx=50,pady=10,columnspan=2)

l2=Label(f1,bg="lavender blush",fg="sandy brown",text="FIELDS",font=("Times New Roman",15,"bold"),width=12,bd=15)
l2.grid(row=1,column=0,padx=40,pady=10)
b1=Button(f1,text="Dentist",bg="purple",fg="white",font=("bold"),width=15,bd=10,command=dentist).grid(row=5,column=0)
b2=Button(f1,text="Eye",bg="purple",fg="white",font=("bold"),width=15,bd=10,command=eye).grid(row=6,column=0)
b3=Button(f1,text="Heart",bg="purple",fg="white",font=("bold"),width=15,bd=10,command=heart).grid(row=7,column=0)
b4=Button(f1,text="Kidney",bg="purple",fg="white",font=("bold"),width=15,bd=10,command=kidney).grid(row=8,column=0)


m.mainloop()
