from tkinter import *
from PIL import ImageTk

root = Tk()
root.geometry("400x400")
root.wm_title("Photo")

root2 = Tk()
root2.geometry("400x400")
root2.wm_title("Photo")

photo = ImageTk.PhotoImage(file='photos/1.jpg')
labelphoto = Label(root, image = photo)
labelphoto.pack()






root.mainloop()
root2.mainloop()