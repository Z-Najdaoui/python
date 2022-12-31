from tkinter import *
window = Tk()
window.title('testTitle')
window.geometry('920x720+100+100')
window.resizable(False,False)
window['bg'] = '#aaa'
window.iconbitmap()
 
canvas_1_manage =Canvas(window, width = 12, height = 50)
canvas_1_manage.grid(row = 0, column = 0)
canvas_1_manage.create_text(6, 50, text = "Node", angle = 90, anchor = "w")
window.mainloop()
