from PIL import Image, ImageTk
import tkinter as tk

IMAGE_PATH = 'dicee.png'
WIDTH, HEIGTH = 200, 200

root = tk.Tk()
root.geometry('{}x{}'.format(WIDTH, HEIGTH ))

canvas = tk.Canvas(root, width=WIDTH, height=HEIGTH)
canvas.pack()

img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGTH), Image.ANTIALIAS))
canvas.background = img  # Keep a reference in case this code is put in a function.
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

# Put a tkinter widget on the canvas.
button = tk.Button(root, text="Start")
button_window = canvas.create_window(10, 10, anchor=tk.NW, window=button)

root.mainloop()
