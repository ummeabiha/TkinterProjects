def clock():
    text=time.strftime("%H:%M:%S")
    clock_label.config(text=text)
    clock_label.after(100,clock)

clock_label=Label(m,font=("ds-digital",20,"bold"),bg="White",fg="gold")
clock_label.grid(row=0,column=1)
clock()
