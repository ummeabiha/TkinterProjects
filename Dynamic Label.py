from tkinter import*
m=Tk()

def table():
    tno = int(e.get())
    trange = int(e1.get())
    for i in range(1, trange + 1):
        z = (tno, "*", i, "=", tno * i)
        Label(m,text=z,bg="red",fg="white",width=20,font=("Aerial",16)).grid(row=5+i,column=1,pady=10)


l=Label(m,width=20,text="Enter num1",bg="pink",pady=20)
l.grid(row=0,column=0)

l1=Label(m,width=20,text="Enter num2",bg="pink",pady=20)
l1.grid(row=1,column=0)

e=Entry(m,width=20)
e.grid(row=0,column=1)

e1=Entry(m,width=20)
e1.grid(row=1,column=1)

btn=Button(m,text="Table generate",width=12,height=1,command=table)
btn.grid(row=9,column=1)

m.mainloop()
