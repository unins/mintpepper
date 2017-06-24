import sys
from tkinter import *

def identify():
    head = "Cannot confirm"
    cntx = "Soldier is out of Artillery shell"
    msg = messagebox.showinfo(head, cntx)



tk = Tk()
canvas = Canvas(tk, width=640, height=500, bd=3, highlightthickness=0)
tk.title("Error")
tk.resizable(1,1)
tk.wm_attributes("-topmost",1)

id = canvas.create_oval(10,10,40,40,fill='red')
canvas.move(id,450,300)

points = [110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 60, 100, 90, 110]
poly = canvas.create_polygon(100, 140, points , fill='yellow', outline='black', width='3')
canvas.move(poly, 450,300)

btn = Button(tk, text="Fire", command=identify)
btn.place (x = 200, y = 10)
btn.pack()

canvas.pack()
mainloop()
