from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI . title('โปรแกรมสุ่มเลขหวย')
GUI.geometry('500x400')

L1 = Label(GUI,text='กดปุ่มเพื่อสุ่มตัวเลข',font=('Angsana New',30),fg='blue')
L1.place(x=150,y=20)

def Button2():
    text = '456321'
    messagebox.showinfo('เลขที่ออก',text)

FB1 = Frame(GUI)
FB1.place(x=50,y=150)
B2 = ttk.Button(FB1,text='รางวัลที่1',command=Button2)
B2.pack(ipadx=20,ipady=20)

def Button3():
    text = '865'
    messagebox.showinfo('เลขที่ออก',text)

FB1 = Frame(GUI)
FB1.place(x=200,y=150)
B2 = ttk.Button(FB1,text='เลขท้าย 3 ตัว',command=Button3)
B2.pack(ipadx=20,ipady=20)

def Button4():
    text = '10'
    messagebox.showinfo('เลขที่ออก',text)

FB1 = Frame(GUI)
FB1.place(x=350,y=150)
B2 = ttk.Button(FB1,text='เลขท้าย 2 ตัว',command=Button4)
B2.pack(ipadx=20,ipady=20)


GUI.mainloop()
