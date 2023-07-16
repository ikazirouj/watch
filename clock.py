##youtubeからコードを引用
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from time import strftime

##define the main window
root = tk.Tk()
##define the name of main window
root.title("時計だよ")
#specify the window size
root.geometry("850x150")
#change the main window coloer
root.configure(bg="white")
chacha = Image.open("chacha.png")
chacha=chacha.resize((150, 150))
chacha = ImageTk.PhotoImage(chacha)

class flont:
    def clock():
        global label
        label = Label(root, font=("gTerminal", 100), bg="white", fg="black")
        label.pack(side="left")
    
    def time():
        ##Conver data structure to "str" and assign to "clock"
        clock = strftime("%p %H:%M:%S")
        ##I don't konw! 
        label.config(text=clock)
        ##start function every 1000 ms
        label.after(1000, flont.time)

    def icon():
        canvas = tk.Canvas(root, bg="white", height=200, width=200, highlightthickness=0)
        canvas.pack(side="left")    
        canvas.create_image(80, 80, image=chacha)

flont.clock()
flont.time()
flont.icon()

root.mainloop()