#HAHA JUST LITTLE COMMENT


from tkinter import *
import math
root=Tk()
c = Canvas(width=1100, height=600, bg='gray4')
c.focus_set()
c.pack()
obj1_x=400 
c.create_line(0,400,1200,400,width=6,fill="deep pink")
rect = c.create_rectangle(0, 0, 1201, 396, fill='#3E1133')
text=c.create_text(50, 190, font="Purisa 20",text="My first demo! pavcoder",fill="red")
c.create_line(100,400,-150,500,width=6,fill="deep pink")
c.create_line(200,400,-10,500,width=6,fill="deep pink")
c.create_line(300,400,0,600,width=6,fill="deep pink")
c.create_line(400,400,200,600,width=6,fill="deep pink")
c.create_line(500,400,400,600,width=6,fill="deep pink")
c.create_line(600,400,700,600,width=6,fill="deep pink")
c.create_line(700,400,900,600,width=6,fill="deep pink")
c.create_line(800,400,1100,600,width=6,fill="deep pink")
c.create_line(900,400,1110,500,width=6,fill="deep pink")
c.create_line(1000,400,1250,500,width=6,fill="deep pink")
#circle=c.create_oval(10, 10, 60, 60, outline="#3EEA33", fill="#3EEA33", width=2)
obj1=c.create_line(0,obj1_x+150,1100,obj1_x+150,width=6,fill="deep pink")
obj2=c.create_line(0,obj1_x+100,1100,obj1_x+100,width=6,fill="deep pink")
obj3=c.create_line(0,obj1_x+50,1100,obj1_x+50,width=6,fill="deep pink")
obj4=c.create_line(0,obj1_x,1100,obj1_x,width=6,fill="deep pink")

def redraw_obj1():
	c.after(50,redraw_obj1)
	c.move(obj1,0,5)
	if c.coords(obj1)[1]>=600:
		c.coords(obj1,0,400,1200,400)
	c.update()
def redraw_obj2():
	c.after(50,redraw_obj2)
	c.move(obj2,0,5)
	if c.coords(obj2)[1]>=600:
		c.coords(obj2,0,400,1200,400)
	c.update()
def redraw_obj3():
	c.after(50,redraw_obj3)
	c.move(obj3,0,5)
	if c.coords(obj3)[1]>=600:
		c.coords(obj3,0,400,1200,400)
	c.update()
def redraw_obj4():
	c.after(50,redraw_obj4)
	c.move(obj4,0,5)
	if c.coords(obj4)[1]>=600:
		c.coords(obj4,0,400,1200,400)
	c.update()
def redraw_text():
	c.after(5,redraw_text)
	c.move(text,2,math.sin(c.coords(text)[0]))
	if (c.coords(text)[0]==970 or c.coords(text)[1]==950):
		c.coords(text,50, 190)
	c.update()	
def motion_circle():
	c.after(40,motion_circle)
	c.move(circle,0,5)
	c.move(circle,5,0)
	if c.coords(circle)[1]==100:
		c.coords(circle,10, 10, 60, 60)
	c.update()
redraw_obj1()
redraw_obj2()
redraw_obj3()
redraw_obj4()
redraw_text()
#motion_circle()
root.mainloop()
