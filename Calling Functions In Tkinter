from tkinter import*
m=Tk()
def sum():
    n1=int(e.get())
    n2=int(e1.get())
    add=n1+n2
    lb.config(text="Addition")
    lb1.config(text=add)
def subtract():
    n1=int(e.get())
    n2=int(e1.get())
    diff=n1-n2
    lb.config(text="Difference")
    lb1.config(text=diff)
def multiply():
    n1=int(e.get())
    n2=int(e1.get())
    mult=n1*n2
    lb.config(text="Multiplication")
    lb1.config(text=mult)
def divide():
    n1=int(e.get())
    n2=int(e1.get())
    div=n1/n2
    lb.config(text="Division")
    lb1.config(text=div)

def factorial():
    fact=1
    x=int(e.get())
    for i in range(1,x+1):
        fact=fact*i
    lb1.config(text="The Factorial is"+str(fact),font=("Arial",20))

# Dynamic Label
def table():
    tno=int(e.get())
    trange=int(e1.get())
    for i in range(1,trange+1):
        z=(tno,"*",i,"=",tno*i)
        lb1.config(text=z)

l=Label(m,width=20,text="Enter num1",bg="pink",pady=20)
l.grid(row=0,column=0)

e=Entry(m,width=20)
e.grid(row=0,column=1)

l1=Label(m,width=20,text="Enter num2",bg="pink",pady=20)
l1.grid(row=1,column=0)

e1=Entry(m,width=20)
e1.grid(row=1,column=1)

lb=Label(m,width=20,text="",bg="Grey")
lb.grid(row=2,column=0)

lb1=Label(m,width=20,text="",bg="pink")
lb1.grid(row=2,column=1)

btn=Button(m,text="Add",width=12,height=1,command=sum)
btn.grid(row=4,column=1)
btn=Button(m,text="Subtract",width=12,height=1,command=subtract)
btn.grid(row=5,column=1)
btn=Button(m,text="Multiply",width=12,height=1,command=multiply)
btn.grid(row=6,column=1)
btn=Button(m,text="Divide",width=12,height=1,command=divide)
btn.grid(row=7,column=1)
btn=Button(m,text="Factorial",width=12,height=1,command=factorial)
btn.grid(row=8,column=1)
btn=Button(m,text="Table generate",width=12,height=1,command=table)
btn.grid(row=9,column=1)

m.mainloop()
