from tabnanny import check
import tkinter as tk
from tkinter import Variable, ttk

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
#setting select
#setting row column
#end
win.mainloop()