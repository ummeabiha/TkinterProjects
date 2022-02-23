from tkinter import *
import math

m=Tk()
m.geometry('350x450')
m.title('Calculator')
m.resizable('False','False')

frame1=Frame(m,bg="hot pink")
frame1.place(width=350,height=450)

frame2=Frame(frame1,bg="Papaya whip")
frame2.place(x=25,y=25,width=300,height=400)

num1_l=Label(frame2,text="Enter Num1:",bg="lemon chiffon",fg="black",width=15)
num1_l.place(relx=0.02,rely=0.05)

num2_l=Label(frame2,text="Enter Num2:",bg="lemon chiffon",fg="black",width=15)
num2_l.place(relx=0.02,rely=0.11)

result_l=Label(frame2,text="",bg="Papaya Whip",fg="black",width=15)
result_l.place(relx=0.01,rely=0.17)

result_e=Label(frame2,text="",bg="Papaya Whip",fg="Purple",font=("bold"),width=21,height=1)
result_e.place(relx=0.41,rely=0.17)

num1_e=Entry(frame2,width=25,bg="White",fg="Black")
num1_e.place(relx=0.44,rely=0.05)

num2_e=Entry(frame2,width=25,bg="White",fg="Black")
num2_e.place(relx=0.44,rely=0.11)

# FUNCTIONS

def sum():
    n1=int(num1_e.get())
    n2=int(num2_e.get())
    add=n1+n2
    result_l.config(text="Addition")
    result_e.config(text=add)

def subtract():
    n1=int(num1_e.get())
    n2=int(num2_e.get())
    diff=n1-n2
    result_l.config(text="Difference")
    result_e.config(text=diff)

def multiply():
    n1=int(num1_e.get())
    n2=int(num2_e.get())
    mult=n1*n2
    result_l.config(text="Multiplication")
    result_e.config(text=mult)

def divide():
    n1=int(num1_e.get())
    n2=int(num2_e.get())
    if n2>0:
      div=n1/n2
      result_l.config(text="Division")
      result_e.config(text=div)
    elif n2==0:
        result_e.config(text="Division not possible")

def factorial():
    fact=1
    x=int(num1_e.get())
    for i in range(1,x+1):
        fact=fact*i
    result_l.config(text="Factorial")
    result_e.config(text=fact)

def sine():
    sin=math.sin(int(num1_e.get()))
    result_l.config(text="Sin")
    result_e.config(text=sin)

def cosine():
    cos=math.cos(int(num1_e.get()))
    result_l.config(text="Cos")
    result_e.config(text=cos)

def tangent():
    tan=math.tan(int(num1_e.get()))
    result_l.config(text="Tan")
    result_e.config(text=tan)

def sq_root():
    root=math.sqrt(int(num1_e.get()))
    result_l.config(text="Square root")
    result_e.config(text=root)

def square():
    num1=int(num1_e.get())
    sq=int(num1*num1)
    result_l.config(text="Square")
    result_e.config(text=sq)

def power():
    num1 = num1_e.get()
    num2= num2_e.get()
    power = int(num1)**int(num2)
    result_l.config(text="Power")
    result_e.config(text=power)

def log():
    log=math.log10(int(num1_e.get()))
    result_l.config(text="Log")
    result_e.config(text=log)

#BUTTONS

sum_btn=Button(frame2,text="+",width=12,height=1,bg='alice blue',fg="Black",command=sum)
sum_btn.place(relx=0.08,rely=0.28)

sub_btn=Button(frame2,text="-",width=12,height=1,bg='alice blue',fg="Black",command=subtract)
sub_btn.place(relx=0.08,rely=0.38)

mul_btn=Button(frame2,text="*",width=12,height=1,bg='alice blue',fg="Black",command=multiply)
mul_btn.place(relx=0.08,rely=0.48)

div_btn=Button(frame2,text="/",width=12,height=1,bg='alice blue',fg="Black",command=divide)
div_btn.place(relx=0.08,rely=0.58)

fac_btn=Button(frame2,text="Factorial",width=12,height=1,bg='alice blue',fg="Black",command=factorial)
fac_btn.place(relx=0.08,rely=0.68)

sin_btn=Button(frame2,text="Sin",width=12,height=1,bg='alice blue',fg="Black",command=sine)
sin_btn.place(relx=0.55,rely=0.28)

cos_btn=Button(frame2,text="Cos",width=12,height=1,bg='alice blue',fg="Black",command=cosine)
cos_btn.place(relx=0.55,rely=0.38)

tan_btn=Button(frame2,text="Tan",width=12,height=1,bg='alice blue',fg="Black",command=tangent)
tan_btn.place(relx=0.55,rely=0.48)

sq_root=Button(frame2,text="Square root",width=12,height=1,bg='alice blue',fg="Black",command=sq_root)
sq_root.place(relx=0.55,rely=0.58)

sq_btn=Button(frame2,text="Square",width=12,height=1,bg='alice blue',fg="Black",command=square)
sq_btn.place(relx=0.55,rely=0.68)

power_btn=Button(frame2,text="Power",width=12,height=1,bg='alice blue',fg="Black",command=power)
power_btn.place(relx=0.32,rely=0.78)


m.mainloop()
