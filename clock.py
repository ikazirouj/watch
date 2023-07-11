##youtubeからコードを引用
from tkinter import *
from time import strftime

##define the main window
root = Tk()
##define the name of main window
root.title("時計だよ")
#specify the window size
root.geometry("750x150")

root.configure(bg="white")

def time():
    ##Conver data structure to "str" and assign to "clock"
    clock = strftime("%p %H:%M:%S")
    ##I don't konw! 
    label.config(text=clock)
    ##start function every 1000 ms
    label.after(1000, time)

label = Label(root, font=("gTerminal", 100), bg="white", fg="black")
label.pack(anchor="center")
time()

root.mainloop()