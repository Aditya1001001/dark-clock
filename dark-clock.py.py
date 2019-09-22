import sys
from  tkinter import *
import time 

def times():
	current_time=time.strftime("%H:%M:%S") 
	clock.config(text=current_time)
	clock.after(200,times)


root=Tk()
root.title("Dark clock")
root.geometry("400x250")
root.configure(background='#181818')
clock=Label(root,font=("times",50,"bold"),bg="#181818",fg="#ffffff")
clock.grid(row=2,column=2,pady=25,padx=75)
times()

digi=Label(root,text="Digital clock",font="times 24 bold",bg="#181818",fg="#ffffff")
digi.grid(row=0,column=2)

nota=Label(root,text="Hours     Minutes     Seconds",font="times 15 bold",bg="#181818",fg="#ffffff")
nota.grid(row=3,column=2)

root.mainloop()