import sys
from tkinter import *

def helloCallBack():
    # POP-UP messagebox option in Button function
    head = "HEAD : Hello Python 3.6 World"
    cntx = "CONTEXT : This is Practice for Message Box \n \
        You will never be satisfied with this \n \
        This is a only a example"
    msg = messagebox.showinfo(head, cntx)   # POP-UP Message function

def tkInterSHOW():
    tk = Tk()
    canvas = Canvas(tk, width=640, height=500, bd=3, highlightthickness=0)
    tk.title("HELLO tkinter WORLD~!!(640 x 500) -ver.1.00")# Header
    tk.resizable(0,0)                   # resize's not allowed (=0)
    tk.wm_attributes("-topmost",1)      # Always on top

    id = canvas.create_oval(10,10,40,40,fill='red')    # make Ball.object
    canvas.move(id,450,300)     	  		           # move to canvas_center

    points = [110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 60, 100, 90, 110]
    poly = canvas.create_polygon(100, 140, points , fill='yellow', outline='black', width='3')
    canvas.move(poly, 450,300) # draw POLY: see this = https://goo.gl/x1qck2


    aaa = PhotoImage(file='./data/nom.png')       # Vari. should be after Tk()
    canvas.create_image(120,200, image=aaa, anchor='nw')    # aaa can't be changed as Direct use

    '''
    bbb = PhotoImage(file='./data/Felix_munch.png')# Vari. should be after Tk()
    ccc = PhotoImage(file='./data/Felix_dizzy.png')# Vari. should be after Tk()
    canvas.create_image(0,0, image=bbb, anchor='nw')    # aaa can't be changed as Direct use
    canvas.create_image(350,50, image=ccc, anchor='nw')    # aaa can't be changed as Direct use
    '''

    B = Button(tk, text=" Comm'n man, take it easy! ", command = helloCallBack )   # TK_window Button(Text)
    B.place (x = 200, y = 10)

    canvas.pack()                       # Draw Window
    mainloop()                       # Keep screen turn on. -- makeing a loop. '''

tkInterSHOW()
