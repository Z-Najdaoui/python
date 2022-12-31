from tkinter import *
def addone():
    lbl2['text']=str(int(lbl2['text'])+1)
def subone():
    lbl2['text']=str(int(lbl2['text'])-1)
window = Tk()
window.title('testTitle')
window.geometry('920x720+100+100')
window.resizable(False,False)
window['bg'] = '#aaa'
window.iconbitmap()
 

frm2 = Frame(width='460',height='720',bg='red')
frm2.place(x=460,y=0)
frm1 = Frame(width='460',height='720',bg='green')
frm1.place(x=0,y=0)


lbl1 = Label(frm2,text='Hello Mr \n Nsila',font=('Arial',30),bg='#0f0',fg='#00f')
lbl2 = Label(frm1,text='0',font=('Arial',60),bg='#0f0',fg='#00f')
# lbl1.pack()
lbl1.place(x=0,y=0)
lbl2.place(x=0,y=0)
# # lbl1.grid()
bnt1 = Button(frm1,text='Click me',height=1,width=20,bg='#454545',activebackground='blue',activeforeground='green',bd=5,command=addone,cursor='mouse')
bnt1.place(x=100,y=100)

bnt2 = Button(frm2,text='Click me',height=1,width=20,bg='#454545',activebackground='blue',activeforeground='green',bd=5,command=subone)
bnt2.place(x=100,y=100)

bnt3 = Button(frm2,text='exit',height=1,width=20,bg='#454545',activebackground='blue',activeforeground='green',bd=5,command=window.quit)
bnt3.place(x=100,y=200)

myInput = Entry(frm1,justify='center')
myInput.place(x=100,y=200)


window.mainloop()