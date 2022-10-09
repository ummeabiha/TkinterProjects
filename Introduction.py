from tkinter import *

# Main Window: (To execute our program in GUI-Tkinter)
m=Tk()

# Defining Labels:
l1=Label(m,text="ID",bg="Pink",fg="Light Yellow",pady=10,padx=5,width=5,height=2)
l1.grid(row=0,column=0)   #(grid: use to define the position)(grid should be defined on next line to avoid any errors)

l2=Label(m,text="Name",bg="Pink",fg="Light Yellow",pady=10,padx=5,width=5,height=2)
l2.grid(row=1,column=0)

l3=Label(m,text="Depart",bg="Pink",fg="Light Yellow",pady=10,padx=5,width=5,height=2)
l3.grid(row=2,column=0)

l4=Label(m,text="Address",bg="Pink",fg="Light Yellow",pady=10,padx=5,width=5,height=2)
l4.grid(row=3,column=0)

# Entry Boxes (to take input from user):
e1=Entry(m,bg="gold", fg="black")
e1.grid(row=0,column=1,pady=10,padx=5)

e2=Entry(m,bg="gold",fg="black")
e2.grid(row=1,column=1,pady=10,padx=5)

e3=Entry(m,bg="gold",fg="black")
e3.grid(row=2,column=1,pady=10,padx=5)

e4=Entry(m,bg="gold",fg="black")
e4.grid(row=3,column=1,pady=10,padx=5)

# List box:
l5=Label(m,bg="gold",fg="black",text="Program",pady=10,padx=5,width=5,height=2)
l5.grid(row=4,column=0)

lb=Listbox(m)
lb.insert(0,"BESE")
lb.insert(0,"BECE")
lb.insert(0,"BSCS")
lb.insert(0,"BEEE")
lb.grid(row=6,column=1)

# Buttons:
b1=Button(m,bg="orange",fg="purple",text="Submit",width=10,height=2,)
b1.grid(row=7,column=1)

m.mainloop() #(to stop our loop after executing our program, if we will not use it our program will run forever)
