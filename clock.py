#youtubeからコードを引用
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from time import strftime

#メイン画面の定義
root = tk.Tk()
#メイン画面の名前
root.title("時計だよ")
#メイン画面の色とサイズを指定
root.geometry("850x180")
root.configure(bg="white")
#ちゃちゃの画像を読み込み
chacha = Image.open("chacha.png")
chacha=chacha.resize((150, 150))
chacha = ImageTk.PhotoImage(chacha)

#アプリ起動時に使用するクラス
class flont:
    #時計の表示
    def clock():
        global label
        label = Label(root, font=("gTerminal", 100), bg="white", fg="black")
        label.pack(side="left")

    #時計機能
    def time():
        ##時刻データをstr型で取得
        clock = strftime("%p %H:%M:%S")
        ##I don't konw! 
        label.config(text=clock)
        ##1000msごとに機能させる
        label.after(1000, flont.time)

    #アイコン表示
    def icon():
        canvas = tk.Canvas(root, bg="white", height=200, width=200, highlightthickness=0)
        canvas.pack(side="left")    
        canvas.create_image(80, 80, image=chacha)

    def btu_press():
        print("わんわん！")

    def btn_oyatu():
        print("ｷｬｯｷｬ")

    def btu():
        bt_b = tk.Button(text="おてて", command=flont.btu_press)
        bt_o = tk.Button(text="おやつ", command=flont.btn_oyatu)
        bt_b.place(x=500, y=160)
        bt_o.place(x=400, y= 160)


#execution (e.g. program)
flont.btu()
flont.clock()
flont.time()
flont.icon()
root.mainloop()