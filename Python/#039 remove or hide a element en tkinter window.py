from tkinter import *

window = Tk()
window.title('testTitle')
window.geometry('920x720+100+100')
window.resizable(False,False)
window['bg'] = '#aaa'
window.iconbitmap()
def hide():
    myTxt.pack_forget()
    bnt.pack_forget()

myTxt = Label(text='some string')
myTxt.pack()
bnt = Button(text='remove txt',height=1,width=20,bg='#454545',activebackground='blue',activeforeground='green',bd=5,command=hide)
bnt.pack()
window.mainloop()