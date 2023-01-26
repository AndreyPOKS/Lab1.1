import tkinter as tk

from Skelet import MainClass

def get_Entry():
    value1 = number.get()
    value2 = number2.get()
    trel = MainClass(int(value1), int(value2))
    trel.Pir()
    trel.Ugol()
    trel.Krug()
    lbl = trel.Krug()
    lbl1 = trel.Ugol()
    print(lbl1[1])
    x = 50
    y = 50

    x2 = x + int(value1) * 10
    y2 = y + int(value1) * 10
    x3 = x + int(value2) * 10

    y3 = y
    lbl2 = tk.Label(win, text=lbl1[0])
    lbl3 = tk.Label(win, text=lbl1[1])
    lbl4 = tk.Label(win, text=lbl1[2])
    lbl5 = tk.Label(win, text=lbl)

    lbl2.grid(row=0, column=1, sticky="S")
    lbl3.grid(row=0, column=2, sticky="S")
    lbl4.grid(row=0, column=3, sticky="S")
    lbl5.grid(row=0, column=4, sticky="S")
    canvas = tk.Canvas(win, height=500, width=500, bg="#ccf9ff")
    canvas.grid(row=0, column=0,)
    canvas.create_line(x, y, x2, y2, width=3)
    canvas.create_line(x, y, x3, y3, width=3)
    canvas.create_line(x2, y2, x3, y3, width=3)





win = tk.Tk()

win.config(bg="white")
win.title("Рисуем треугольник")
win.geometry("1000x500")
genii = tk.PhotoImage(file="Genius.png")
label1 = tk.Label(win, image=genii)
label1.place(x=270, y=0, relwidth=1, relheight=1)
win.resizable(False, False)
canvas = tk.Canvas(win, height=500, width=500, bg="#ccf9ff")
canvas.grid(row=0, column=0)
number = tk.Entry(win,)
number2 = tk.Entry(win,)
number2.grid(row=0, column=2, sticky="N")
number.grid(row=0, column=1, sticky="N")

bkt1 = tk.Button(win, text="Создать", command=get_Entry,)
bkt1.grid(row=0, column=3, sticky="N")






win.mainloop()
