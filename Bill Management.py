from tkinter import *

root=Tk()
root.geometry("1000x500")
root.title("Bill Management")
root.resizable(False,False)

def Total():
    
    try:a1=int(Dosa.get())   
    except: a1=0

    try:a2=int(Cookies.get())
    except: a2=0

    try:a3=int(Coffee.get())
    except: a3=0

    try:a4=int(Tea.get())
    except: a4=0

    try:a5=int(Juice.get())
    except: a5=0

    try:a6=int(Pancakes.get())
    except: a6=0

    try:a7=int(Eggs.get())
    except: a7=0

    #define Cost of each item per quantity

    c1=60*a1
    c2=30*a2
    c3=7*a3
    c4=100*a4
    c5=20*a5
    c6=15*a6
    c7=7*a7

    lbl_total=Label(f2,text="Total",font=("aria 20 bold"),width=16,fg="lightyellow",bg="black")
    lbl_total.place(x=0,y=50)

    entry_total=Entry(f2,font=("aria 20 bold"),textvariable=Total_bill,bd=6,width=15,bg="lightgreen")
    entry_total.place(x=20,y=100)

    totalcost=c1+c2+c3+c4+c5+c6+c7
    string_bill="Rs.",str('%.2f' %totalcost)
    Total_bill.set(string_bill)

def Reset():
    entry_dosa.delete(0,END)
    entry_cookies.delete(0,END)
    entry_coffee.delete(0,END)
    entry_tea.delete(0,END)
    entry_juice.delete(0,END)
    entry_pancakes.delete(0,END)
    entry_eggs.delete(0,END)

img_icon=PhotoImage(file="billlogo.png")
root.iconphoto(False,img_icon)


Label(root,text="Shivam Mini Hotel Bill Management",bg="black",fg="white",font=("calibri",33),height="2").pack(fill="both")

#Menu Card

f=Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)

Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="lightgreen").place(x=80,y=0)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Dosa..........Rs.60/plate",fg="black",bg="lightgreen").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Cookies.......Rs.30/plate",fg="black",bg="lightgreen").place(x=10,y=110)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Tea...........Rs.7/cup",fg="black",bg="lightgreen").place(x=10,y=140)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Coffee........Rs.100/Cup",fg="black",bg="lightgreen").place(x=10,y=170)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Juice.........Rs.20/glass",fg="black",bg="lightgreen").place(x=10,y=200)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Pancakes......Rs.15/pack",fg="black",bg="lightgreen").place(x=10,y=230)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Eggs..........Rs.7/piece",fg="black",bg="lightgreen").place(x=10,y=260)


#Bill
f2=Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)

Bill=Label(f2,text="Bill",font=("calibri 20"),bg="lightyellow")
Bill.place(x=120,y=10)
#Entry Work

f1=Frame(root,bd=5,height=370,width=300,relief=GROOVE)
f1.pack()

Dosa=StringVar()
Cookies=StringVar()
Tea=StringVar()
Coffee=StringVar()
Juice=StringVar()
Pancakes=StringVar()
Eggs=StringVar()
Total_bill=StringVar()


#Label

lbl_Dosa=Label(f1,font=("aria 20 bold"),text="Dosa",width=12,fg="blue")
lbl_Dosa.grid(row=1,column=0)

lbl_Cookies=Label(f1,font=("aria 20 bold"),text="Cookies",width=12,fg="blue")
lbl_Cookies.grid(row=2,column=0)

lbl_Tea=Label(f1,font=("aria 20 bold"),text="Tea",width=12,fg="blue")
lbl_Tea.grid(row=3,column=0)

lbl_Coffee=Label(f1,font=("aria 20 bold"),text="Coffee",width=12,fg="blue")
lbl_Coffee.grid(row=4,column=0)

lbl_Juice=Label(f1,font=("aria 20 bold"),text="Juice",width=12,fg="blue")
lbl_Juice.grid(row=5,column=0)

lbl_Pancakes=Label(f1,font=("aria 20 bold"),text="Pancakes",width=12,fg="blue")
lbl_Pancakes.grid(row=6,column=0)

lbl_Eggs=Label(f1,font=("aria 20 bold"),text="Eggs",width=12,fg="blue")
lbl_Eggs.grid(row=7,column=0)



#Entry

entry_dosa=Entry(f1,font=("aria 20 bold"),textvariable=Dosa,bd=6,width=8,bg="lightpink",justify="center")
entry_dosa.grid(row=1,column=1)

entry_cookies=Entry(f1,font=("aria 20 bold"),textvariable=Cookies,bd=6,width=8,bg="lightpink",justify="center")
entry_cookies.grid(row=2,column=1)

entry_tea=Entry(f1,font=("aria 20 bold"),textvariable=Coffee,bd=6,width=8,bg="lightpink",justify="center")
entry_tea.grid(row=3,column=1)

entry_coffee=Entry(f1,font=("aria 20 bold"),textvariable=Tea,bd=6,width=8,bg="lightpink",justify="center")
entry_coffee.grid(row=4,column=1)

entry_juice=Entry(f1,font=("aria 20 bold"),textvariable=Juice,bd=6,width=8,bg="lightpink",justify="center")
entry_juice.grid(row=5,column=1)

entry_pancakes=Entry(f1,font=("aria 20 bold"),textvariable=Pancakes,bd=6,width=8,bg="lightpink",justify="center")
entry_pancakes.grid(row=6,column=1)

entry_eggs=Entry(f1,font=("aria 20 bold"),textvariable=Eggs,bd=6,width=8,bg="lightpink",justify="center")
entry_eggs.grid(row=7,column=1)


#Buttons

btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("arial 16 bold"),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,bd=5,fg="black",bg="lightblue",font=("arial 16 bold"),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)
root.mainloop()
