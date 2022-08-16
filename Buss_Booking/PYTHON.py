from tkinter import *
from tkinter import messagebox
import sqlite3
import splash

root = Tk()
root.geometry('950x900')

Label(root,text="BUS BOOKING SERVICE",font=("large",35),bg="dark blue",fg="white",activebackground="lawn green",width=100).pack()


img = PhotoImage(file="bus1.png")
label=Label(root,image=img)
label.place(x=100,y=100)

con = sqlite3.connect('my_db')
cur= con.cursor()
cur.execute("CREATE Table IF NOT EXISTS bus(OPERATOR text ,BUS_TYPE text,_FROM text,_TO text,DATE text,DEP_TIME text,ARR_TIME text,FARE INTEGER,SEATS INTEGER)")
con.commit()


def first():
    r=Tk()
     
    r.geometry('950x900')
    r.configure(bg='#ADD8E6')

    Label(r,text="BUS OPERATOR DETAILS FILLING",font=("large",20),bg="dark blue",fg="white",activebackground="light blue",width=100).pack()
    lb1=Label(r,text="FULL NAME",font="large").place(x=300,y=100)
    e1=Entry(r).place(x=450,y=100)
    
    lb2=Label(r,text="CONTACT NUMBER",font="large").place(x=250,y=150)
    e2=Entry(r).place(x=450,y=150)
    
    lb3=Label(r,text="ADDRESS",font="large").place(x=300,y=200)

    e3=Entry(r).place(x=450,y=200)
    def second():
        
         l1= Label(r,text="OPERATOR",font="large").place(x=300,y=300)
         a=Entry(r)
         a.place(x=450,y=300)
         l2=Label(r,text="BUS TYPE",font="large").place(x=300,y=350)
         b=Entry(r)
         b.place(x=450,y=350)
         l3=Label(r,text="FROM",font="large").place(x=300,y=400)
         c=Entry(r)
         c.place(x=450,y=400)

         l4=Label(r,text="TO",font="large").place(x=300,y=450)
         d=Entry(r)
         d.place(x=450,y=450)
         l5=Label(r,text="DATE",font="large").place(x=300,y=500)
         e=Entry(r)
         e.place(x=450,y=500)
         l6=Label(r,text="DEP_TIME",font="large").place(x=300,y=550)
         f=Entry(r)
         f.place(x=450,y=550)
         l7=Label(r,text="ARR_TIME",font="large").place(x=300,y=600)
         g=Entry(r)
         g.place(x=450,y=600)
         l8=Label(r,text="FARE",font="large").place(x=300,y=650)
         h=Entry(r)
         h.place(x=450,y=650)
         l9=Label(r,text="SEATS",font="large").place(x=300,y=700)
         i=Entry(r)
         i.place(x=450,y=700)
         def third():
             
             con= sqlite3.connect('my_db')
             cur = con.cursor()
             values = (a.get(), b.get(), c.get(), d.get(), e.get(), f.get(), g.get(), h.get(), i.get())
             cur.execute("""INSERT INTO bus(OPERATOR,BUS_TYPE,_FROM,_TO ,DATE,DEP_TIME ,ARR_TIME ,FARE ,SEATS)
                          VALUES(?,?,?,?,?,?,?,?,?)""", values)
             con.commit()
             row = cur.fetchall()
             print(row)
             con.close()
             

             
             messagebox.showinfo("DATA", "DATA SAVED")
             r.destroy()
         btnb=Button(r, text="SAVE",bg="blue",activebackground="lawn green",font=("bold",15),height=1,width=10,command=third).place(x=300,y=750)
    Button(r,text="ADD DETAILS",command=second,font="bolt",width=30,height=1,borderwidth=8,relief=SUNKEN,activebackground="light blue",bg="light grey").place(x=300,y=250)
    r.mainloop()





def fourth():
    s=Tk()
    Label(s,text="SEARCH BUS",font=("large",30),bg="dark blue",fg="white",width=100).pack()
    s.geometry('900x950')
    
    llb1=Label(s,text="BUS TYPE",font="large").place(x=300,y=350)
    k=StringVar(s)

    choice=['AC','NON-AC','SLEEPER','NON SLEEPER']
    OptionMenu(s,k,*choice).place(x=450,y=350)
    llb2=Label(s,text="FROM",font="large").place(x=300,y=400)
    w1=Entry(s)
    w1.place(x=450,y=400)
    llb3=Label(s,text="TO",font="large").place(x=300,y=450)
    w2=Entry(s)
    w2.place(x=450,y=450)
    llb4=Label(s,text="DATE",font="large").place(x=300,y=500)
    w3=Entry(s)
    w3.place(x=450,y=500)


    def fifth():
       
        Label(q,text="OPERATOR  ",font="large",bg="light blue").grid(row=0,column=0)
        Label(q,text="BUS TYPE  ",font="large",bg="white").grid(row=0,column=1)
        Label(q,text="FROM  ",font="large",bg="light blue").grid(row=0,column=2)
        Label(q,text="TO  ",font="large",bg="white").grid(row=0,column=3)
        Label(q,text="DATE  ",font="large",bg="light blue").grid(row=0,column=4)
        Label(q,text="DEP_TIME  ",font="large",bg="white").grid(row=0,column=5)
        Label(q,text="ARR_TIME  ",font="large",bg="light blue").grid(row=0,column=6)
        Label(q,text="FARE  ",font="large",bg="white").grid(row=0,column=7)
        Label(q,text="SEATS  ",font="large",bg="ligh blue").grid(row=0,column=8)
        Label(q,text="SELECT  ",font="large",bg="white").grid(row=0,column=9)



        
        r1=w1.get()
        r2=w2.get()
        r3=w3.get()
        if r1==' ' or r2==' ' or r3==' ' or r1==r2:
            tkMessageBox.showerror("error")
        else:
            con=sqlite3.connect('my_db')
            cur=con.cursor()
            cur.execute("SELECT * FROM bus WHERE _FROM= ? AND _TO = ?  ",(r1,r2))
            con.commit()
            label=cur.fetchall()
            c=0
            v=IntVar()
            d=1
            

            for i in label:
                c=c+1
                j=0
               
                for k in i:
                    x1=Label(q,text=k)
                    x1.grid(row=c,column=j)
                    j=j+1
            
                p=Radiobutton(q,variable=v,value=d)
                p.grid(row=c,column=j)
                d=d+1
                print(v.get())
                


            Button(q,text="book",bg="red",activebackground="light blue").grid(row=c+1,column=j)
            con.close()
            
        q.mainloop()
            





    
 
    b1=Button(s, text="HOME",bg="dark blue",font="bolt",width=25,height=1,borderwidth=8,relief=SUNKEN,activebackground="light blue",command=s.destroy).place(x=200,y=550)
    b2=Button(s, text="SEARCH",command=fifth,bg="dark blue",font="bolt",borderwidth=8,relief=SUNKEN,width=25,height=1,activebackground="light blue").place(x=500,y=550)
    s.mainloop()

btn=Button(root,text="SEARCH BUS",command=fourth,font="bolt",width=30,height=1,borderwidth=8,relief=SUNKEN,activebackground="light blue")
btn.place(x=280,y=500)
btn.pack(side=LEFT,padx=103)




btn=Button(root,text="ADD BUS",command=first,font="bolt",width=30,height=1,relief=SUNKEN,borderwidth=8,activebackground="light blue")
btn.place(x=280,y=400)
btn.pack(side=LEFT)
          
root.mainloop() 
