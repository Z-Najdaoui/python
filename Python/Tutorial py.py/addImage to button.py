#Import tkinter library
from tkinter import *
from PIL import Image,ImageTk
#Create an instance of Tkinter frame or window
win= Tk()
#Set the geometry of tkinter frame
win.geometry("750x250")
#Define a function to close the window
def close_win():
   win.destroy()
#Load the image
image = Image.open('dicee.png')
#Resize the Image
image = image.resize((50,50), Image.ANTIALIAS)
#Convert the image to PhotoImage
img= ImageTk.PhotoImage(image)
#Create a Label
Label(win, text="Click the below button to close the window",font=('Aerial 15 bold')).pack(pady=20)
#Create a label with the image
button= Button(win, text="Click Me",font= ('Helvetica 15 bold'),image=img, compound= LEFT, command=close_win)
button.pack()
win.mainloop()