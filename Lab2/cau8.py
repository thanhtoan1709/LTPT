from tabnanny import check
from textwrap import wrap
import tkinter as tk
from tkinter import Variable, ttk
from tkinter import scrolledtext
from turtle import width
from numpy import number
from sympy import rad
win = tk.Tk()
#title
win.title("Python Gui")
#label
ttk.Label(win,text="Enter A name").grid(column=0,row=0)
ttk.Label(win,text="Choose a number").grid(column=1,row=0)
#def
def click_me():
    action.configure(text="Hello "+ name.get() +" " +number.get())
#button
action = ttk.Button(win,text="click me !!!", command=click_me)
action.grid(column=3,row=1)

#VARIABLE
name = tk.StringVar()
name_ent = ttk.Entry(win,width=12,textvariable=name)
name_ent.grid(column=0,row=1)
number = tk.StringVar()
number_chose = ttk.Combobox(win,width=12,textvariable=number)
number_chose.grid(column=1,row=1)
number_chose['values']= (1,2,4,6,42)
number_chose.current(0)
#variable disable - check
varDis = tk.IntVar()
check1 = tk.Checkbutton(win,text="Disable",variable=varDis,state='disable')
check1.grid(column=0,row=2)
check1.select()
varUn = tk.IntVar()
check2 = tk.Checkbutton(win,text="Unchecked",variable=varUn)
check2.deselect()
check2.grid(column=1,row=2)
varEn = tk.IntVar()
check3 = tk.Checkbutton(win,text="Enable",variable=varEn)
check3.select()
check3.grid(column=2,row=2)
#Scroll
scW = 30
scH = 3
scr = scrolledtext.ScrolledText(win,width=scW,height=scH,wrap=tk.WORD)
scr.grid(column=0)
#variable COLOR
radVar = tk.IntVar()
#Def color
def radCall():
    Sel=radVar.get()
    if Sel == 1: win.configure(background=COLOR1)
    elif Sel == 2: win.configure(background=COLOR2)
    elif Sel == 3: win.configure(background=COLOR3)
COLOR1= "red"
COLOR2= "Blue"
COLOR3 = "YELLOW"
rad1 = tk.Radiobutton(win,text=COLOR1,variable=radVar,value=1,command=radCall)
rad2 = tk.Radiobutton(win,text=COLOR2,variable=radVar,value=2,command=radCall)
rad3 = tk.Radiobutton(win,text=COLOR3,variable=radVar,value=3,command=radCall)
#hello
rad1.grid(column=0,row=5,sticky=tk.W,columnspan=3)
rad2.grid(column=1,row=5,sticky=tk.W,columnspan=3)
rad3.grid(column=2,row=5,sticky=tk.W,columnspan=3)
#labelframe
buttons_frame = ttk.LabelFrame(win,text='')
buttons_frame.grid(column=0,row=7,padx=10,pady=20)
#ttk frame
ttk.Label(buttons_frame,text="Label1").grid(column=0,row=0,sticky=tk.W)
ttk.Label(buttons_frame,text="Label2").grid(column=1,row=0,sticky=tk.W)
ttk.Label(buttons_frame,text="Label3").grid(column=2,row=0,sticky=tk.W)
for child in buttons_frame.winfo_children():
    child.grid_configure(padx=8 ,pady=4)
name_ent.focus()
#end
win.mainloop()