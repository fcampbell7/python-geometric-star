'''
Using TK inter this program iteratively generates a cool geometric star shape
'''

from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("1000x1000")

canvas = Canvas(root, width=800, height=800)
canvas.pack()

canvasMid = 790//2

canvas.create_line(canvasMid,10,canvasMid,790,fill="black",width=3)
canvas.create_line(10,canvasMid,790,canvasMid, fill="black",width=3)

#segment 1
step = 5
x1 = canvasMid
y1 = step
x2 = canvasMid + step
y2 = canvasMid

iterations = (790/2)//step

i=1
while i <= iterations:
    canvas.create_line(x1,y1,x2,y2,fill="blue",width=2)
    y1 += step
    x2 += step
    i+=1

    
#segment 2
step = 5
x1 = canvasMid - step
y1 = canvasMid
x2 = canvasMid
y2 = 790

iterations = (790/2)//step

i=1
while i <= iterations:
    canvas.create_line(x1,y1,x2,y2,fill="yellow",width=2)
    x1 -= step
    y2 -= step
    i+=1


#segment 3
step = 5
x1 = step
y1 = canvasMid
x2 = canvasMid
y2 = canvasMid + step

iterations = (790/2)//step

i=1
while i <= iterations:
    canvas.create_line(x1,y1,x2,y2,fill="green",width=2)
    x1 += step
    y2 -= step
    i+=1


#segment 4
step = 5
x1 = canvasMid + step
y1 = canvasMid
x2 = canvasMid
y2 = 790

iterations = (790/2)//step

i=1
while i <= iterations:
    canvas.create_line(x1,y1,x2,y2,fill="red",width=2)
    x1 += step
    y2 -= step
    i+=1
    
root.mainloop()
